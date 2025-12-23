import streamlit as st
import time
from datetime import datetime
import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from BACKENDS import load_data, save_data, calculate_today_minutes, breadfan, stop_music


with st.sidebar:
    lang = st.selectbox("Language", ["English", "Türkçe"], key="timer_lang")

def t(text_en, text_tr):
    return text_tr if lang == "Türkçe" else text_en

st.title(t("countdown timer", "geri sayım"))

today_minutes = calculate_today_minutes()

st.warning(t(f"**today: {today_minutes} minutes**", f"**bugün: {today_minutes} dakika**"))

manual_minutes = st.number_input(t("set minutes:", "dakika ayarla:"), 
                                  min_value=1, 
                                  value=today_minutes, 
                                  step=1)

if st.button(t("start countdown", "başlat"), type="primary"):
    dakika = int(manual_minutes)
    saniye = dakika * 60
    
   
    countdown_placeholder = st.empty()
    info_placeholder = st.empty()
    
    
    while saniye > 0:
        DK = saniye // 60
        SN = saniye % 60
        countdown_placeholder.markdown(t(
            f"## {DK}:{SN:02d}",
            f"## {DK}:{SN:02d}"
        ))
        time.sleep(1)
        saniye -= 1
    

    breadfan()
    
     
    countdown_placeholder.markdown(t(
        "## time's up\n### now get to work",
        "## süre doldu\n### çalışmaya başla"
    ))
    

    
    st.balloons()

if st.button(t("stop music", "müziği durdur"), type="secondary"):
    stop_music()
    st.success(t("music stopped", "müzik durdu"))

with st.sidebar:
    st.header(t("stats", "istatistikler"))
    
    data = load_data()
    start_date = datetime.strptime(data["start_date"], "%Y-%m-%d")
    days_passed = (datetime.now() - start_date).days
    
    st.metric(t("started", "başlangıç"), start_date.strftime("%d/%m/%Y"))
    st.metric(t("days passed", "geçen gün"), days_passed)
    st.metric(t("today (min)", "bugün (dk)"), today_minutes)
    
    st.markdown("---")
    if st.button(t("reset", "sıfırla")):
        data = {
            "start_date": datetime.now().strftime("%Y-%m-%d"),
            "base_minutes": 1
        }
        save_data(data)
        st.rerun()
