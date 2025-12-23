import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from BACKENDS import chatBot, calculate_today_minutes

with st.sidebar:
    lang = st.selectbox("Language", ["English", "Türkçe"], key="ai_lang")

def t(text_en, text_tr):
    return text_tr if lang == "Türkçe" else text_en

st.title(t("study plan generator", "çalışma planı oluşturucu"))


today_minutes = calculate_today_minutes()
st.warning(t(
    f"**suggested: {today_minutes} minutes**",
    f"**öneri: {today_minutes} dakika**"
))


col1, col2 = st.columns(2)

with col1:
    konu = st.text_input(t("topic:", "konu:"), 
                         placeholder=t("e.g., Ottoman Poetry, Mitosis", "Örn: Kaside, Mitoz"))

with col2:
    sure = st.number_input(t("time (min):", "süre (dk):"), 
                           min_value=1, 
                           max_value=120, 
                           value=today_minutes,
                           step=5)


if st.button(t("generate plan", "plan oluştur"), type="primary", use_container_width=True):
    if not konu:
        st.error(t(
            "enter a topic first",
            "önce konu gir"
        ))
    else:
        with st.spinner(t(
            f"generating plan for {konu}...",
            f"{konu} için plan oluşturuluyor..."
        )):
            try:
                response = chatBot(Konu=konu, zaman=sure)
                
                st.success(t(
                    "plan ready",
                    "plan hazır"
                ))
                
                st.markdown("---")
                st.markdown(response)
                st.markdown("---")
                
                st.download_button(
                    label=t("download", "indir"),
                    data=response,
                    file_name=f"{konu}_{sure}min.txt",
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(t(
                    f"error: {str(e)}",
                    f"hata: {str(e)}"
                ))
                
              
