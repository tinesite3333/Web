from PIL import Image
import requests

import streamlit as st
from streamlit_lottie import st_lottie 

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.title("More information about myself.")
import streamlit as st

    # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images others/graduation.jpg")

# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.write("Good day everyone. Again my name is Christine J. Guerra. 18 years of existence. Born in October 12,2023. I live in Baranngay Bonifacio Surigao City.I graduated at Cabrera Altres National High School. My quote for today is 'Embrace the journey of self-discovery, for within your uniqueness lies the power to paint the world with your authentic colors.'")

import streamlit as st
from streamlit_lottie import st_lottie 

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.title("Chess")
import streamlit as st

    # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images others/chess.jpg")

# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.write("I do know how to play chess. But I couldn't consider it as my talent. I guess it is one of my hobbies.")
st.title("Photography")

import streamlit as st

    # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images others/camera.jpg")

# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

   # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images others/camera (2).jpg")

# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)
with text_column:

    st.write("Im very interested on capturing different scenarious of life. It gives me satisfactory whenever I captured a cery nice picture.")

st.title("Coffee")

import streamlit as st

    # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images others/coffee.gif")

# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:
    st.write("Coffee is my favorite thing in the morning. It give me energy and at the same time I can have quality time with myself.")

st.title("Cats")

import streamlit as st

    # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images others/cat.jpg")

# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

 # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images others/cat (2).jpg")

# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)
with text_column:
    st.write("My favorite pet and the most cutest among all is cats. What I like about them is they are friendly,soft and playful.Cats possess a unique charm that appeals to our emotions and instincts, making them irresistibly adorable to many people")

st.title("Editing")
import streamlit as st

    # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images others/editing.jpg")

# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:
    st.write("I'm passionate to do editing. Whether it is a video edit or pic edit. I can showcase my creativeness when I do editing. And it fives me fulfillment.")

st.title("Dancing")
import streamlit as st

    # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images others/folk dance.jpg")

# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:
    st.write("I love to dance, It brings the energetic me. The playful me that whats to dance between the rhythme and harmony of the music.Who wants to enjoy and bring the expressive me through dancing.")



