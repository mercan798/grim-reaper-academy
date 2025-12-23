import pygame
import json
import os
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

pygame.mixer.init()


DATA_FILE = "data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    else:

        data = {
            "start_date": datetime.now().strftime("%Y-%m-%d"),
            "base_minutes": 1
        }
        save_data(data)
        return data

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

def calculate_today_minutes():
    data = load_data()
    start_date = datetime.strptime(data["start_date"], "%Y-%m-%d")
    today = datetime.now()
    
    days_passed = (today - start_date).days
    
    return data["base_minutes"] + days_passed

def breadfan():
    pygame.mixer.music.load("breadfan.mp3")
    pygame.mixer.music.play(start=52)

def stop_music():
    pygame.mixer.music.stop()
    
    
    
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chatBot(Konu=str, zaman=int) -> str:
    prompt = f"""Sen YKS'ye hazırlanan bir öğrenci için çalışan disiplinli bir ders koçusun.

Sana vereceğim:
- KONU
- SÜRE (dakika)

Görevin:
1) Bu süreyi AŞMADAN, dakikalara bölünmüş bir çalışma programı oluşturmak.
2) Konunun YKS’de çıkan KISA ve NET bilgisini vermek.
3) Gereksiz tarih, edebi süs, uzun açıklama YAPMAMAK.
4) Sadece sınavda işe yarayan bilgiyi yazmak.

Kurallar:
- Programı dakikalara böl (örn: 2 dk, 3 dk).
- Toplam süre verilen süreden fazla olmasın.
- Açıklamalar 1–2 cümleyi geçmesin.
- Motivasyon konuşması, sohbet, boş laf YOK.
- En sona 3 adet YKS tarzı mini soru ekle (cevapsız).

Format:
---
⏱️ {{SÜRE}} Dakikalık Çalışma Programı
📚 Konu: {{KONU}}

1) (x dk) …
2) (x dk) …
3) (x dk) …

🔎 Kısa Konu Özeti:
- …
- …
- …

📝 Mini Test:
1) …
2) …
3) …
---

Şimdi şu bilgilerle çalış:
KONU: {Konu}
SÜRE: {zaman} dakika"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Sen YKS ders koçusun."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content
  
