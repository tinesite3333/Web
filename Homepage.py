from PIL import Image
import requests

import streamlit as st
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json

st.set_page_config(
    page_title="Multipage App",
    page_icon="wave"
)

st.title("Christine's Blog")


import streamlit as st

    # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20fcfjwiyb.json")
img_contact_form = Image.open("https://scontent.fcgy2-1.fna.fbcdn.net/v/t1.15752-9/364524585_269669775815085_2156670383389392228_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=8cd0a2&_nc_eui2=AeFHBriKpxDu1YCNxqFsuePkQIpbwMYpwcNAilvAxinBw4wQBFKyRhbo7lV6wJHPqUWqi1UEKt2u7Wa2SttzH9DV&_nc_ohc=be-IwEfcEykAX8iTx-W&_nc_ht=scontent.fcgy2-1.fna&oh=03_AdSyS99ta7j9jMIlw5NbVRHBHDZtCeYmQPnDfvNd04TyMg&oe=65973772")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with st.container():
    st.subheader("Hi, I am Christine J. Guerra :heart:")
    st.subheader("A BSCpE Student from Surigao del Norte State University")
    st.write(
        "I am  a friend that you can trust and at the same time you can lean on .")
    st.subheader("This is my socials feel free to visit them.")
    st.write(" ▶ Facebook: https://www.facebook.com/christine.guerra.560")
    st.write(" ▶ Instagram: Christine.guerra.560")
    st.write(" ▶Youtube: Christine Guerra")
    st.write(" ▶Email: christineguerra@82gmail.com")
    st.write(" ▶Contact Number: 09692090760")

    st.write("Good Vibes Only!!")







