import streamlit as st
import requests


st.set_page_config(page_title="Cat Fact Generator", page_icon="🐱")

st.title("Cat Fact Generator 🐱")
st.markdown("با هر کلیک یک فکت واقعی جالب درباره گربه ها ببین D:")


def translate_google(text):
    """ترجمه"""
    try:
        url = "https://translate.googleapis.com/translate_a/single"
        params = {
            'client': 'gtx',
            'sl': 'en',
            'tl': 'fa',
            'dt': 't',
            'q': text
        }
        response = requests.get(url, params=params, timeout=5)
        data = response.json()
        return data[0][0][0]
    except:
        return text + "(ترجمه نشد)"


def get_cat_fact():
    try:
        response = requests.get("https://catfact.ninja/fact")
        english_fact = response.json()["fact"]
        persian_fact = translate_google(english_fact)
        return english_fact, persian_fact
    except Exception as e:
        return None, f"خطا:{e}"


if st.button("گرفتن فکت جدید"):
    english, persian = get_cat_fact()
    if english:
        st.success("**فکت انگلیسی**")
        st.info(english)
        st.success("**ترجمه فارسی**")
        st.info(persian)
    else:
        st.error(persian)


if "initial_load" not in st.session_state:
    english, persian = get_cat_fact()
    if english:
        st.success("**فکت انگلیسی**")
        st.info(english)
        st.success("**ترجمه فارسی**")
        st.info(persian)
    st.session_state.initial_load = True


st.markdown("---")
st.caption("این برنامه از یک API رایگان استفاده میکنه به اسم Cat Fact")
