import streamlit as st

st.set_page_config(page_title= f"Russell Whealdon Data Science Portfolio",page_icon="🧑‍🚀",layout="wide")
st.markdown(f"<h1 style='text-align: center; color: cyan;'>Russell Whealdon Data Science Portfolio</h1>", unsafe_allow_html=True)

#Set background image for page
page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://source.unsplash.com/blue-sky-and-white-clouds-b8dA3eY5VrY");
background-size: cover;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
