import streamlit as st

st.set_page_config(page_title= f"Russell Whealdon Data Science Portfolio",page_icon="🧑‍🚀",layout="wide")
st.markdown(f"<h1 style='text-align: center; color: white;'>Russell Whealdon Data Science Portfolio</h1>", unsafe_allow_html=True)

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

st.markdown(f"<p style='text-align: center; color: white;'>Hi! I'm Russell Whealdon and this my Data Science portfolio that holds a wide range of interesting Analytics, Machine Learning, and AI related projects. I'm currently a Data Analyst working at an Ad Agency specializing in modeling and data infrastructure. In here you will also find projects from my Masters in Business Analytics program. I hope you find it interesting and would love to hear from you. Please reach out to me directly or connect on Linkedin. Cheers!</p>", unsafe_allow_html=True)

with st.container():
  st.markdown(f"<h2 style='text-align: center; color: white;'>Skills</h2>", unsafe_allow_html=True)
  col1, col2, col3, col4, col5, col6 = st.columns(6)
  with col1:
    st.write("")
  with col2:
    # HTML and CSS to center the image
st.markdown("""
    <style>
    .center-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 50%;
    }
    </style>
    <img src="images/icons8-python-48.png" class="center-image">
""", unsafe_allow_html=True)
    st.image("images/icons8-python-48.png")
  with col3:
    st.image("images/icons8-mysql-48.png")
  with col4:
    st.image("images/icons8-tableau-software-48.png")
  with col5:
    st.image("images/icons8-google-cloud-48.png")
  with col6:
    st.write("")
  
