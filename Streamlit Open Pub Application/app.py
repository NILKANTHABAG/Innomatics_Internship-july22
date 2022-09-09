from tkinter import CENTER
import streamlit as st
from multiapp import MultiApp
from apps import home, FindtheNearestpub, publocation # import your app modules here

import base64

st.title("WELCOME TO THE PUB FINDER APP")

st.image("PUB.jfif")




@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("blue.png")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://cdn.wallpapersafari.com/10/48/H9v73F.jpg");
background-size: 180%;
background-position: cover;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("https://cdn.wallpapersafari.com/67/37/Hfn0Nd.jpg");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

app = MultiApp()

st.title("NAVIGATION")


# Add all your application here
app.add_app("Home", home.app)
app.add_app("Pub Location", publocation.app)
app.add_app("Find The Nearest Pub", FindtheNearestpub.app)

# The main app 
app.run()

# https://cdn.wallpapersafari.com/10/48/H9v73F.jpg
# https://img.wallpapersafari.com/desktop/1366/768/13/2/hGKz4T.jpg

