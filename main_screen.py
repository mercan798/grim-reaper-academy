import streamlit as st

st.set_page_config(
    page_title="Grim Reaper Academy",
    layout="wide"
)


st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-image: 
            linear-gradient(rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1)),
            url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 600"><path d="M0,400 Q300,200 600,300 T1200,400 L1200,600 L0,600 Z" fill="%23334455" opacity="0.3"/><path d="M0,450 Q300,350 600,400 T1200,480 L1200,600 L0,600 Z" fill="%23445566" opacity="0.4"/></svg>');
        background-size: cover;
        background-attachment: fixed;
    }
    
    .stApp::before {
        content: "⛰️ breathe deep, climb high ⛰️";
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        text-align: center;
        font-size: 10px;
        opacity: 0.3;
        color: #2c3e50;
        font-family: sans-serif;
        padding: 8px;
        z-index: 999;
        background: rgba(255,255,255,0.1);
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("Language")
    lang = st.selectbox("choose", ["English", "Türkçe"], key="lang_selector")


def t(text_en, text_tr):
    return text_tr if lang == "Türkçe" else text_en

st.title(t("Grim Reaper Academy", "Azrail Akademisi"))

st.markdown(t(
    """
procrastinated long enough?  
time to pay up:

- **timer** - counts down, gets worse daily  
- **ai helper** - generates study plans  
""",
    """
yeterince erteleme yaptın mı?  
ödeme zamanı:

- **zamanlayıcı** - geri sayım yapar, her gün daha uzun  
- **ai yardımcı** - çalışma planı yapar  
"""))
