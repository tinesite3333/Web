from PIL import Image
import requests

import streamlit as st

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
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20fcfjwiyb.json")
img_contact_form = Image.open("images/christine.jpg")
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







