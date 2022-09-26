import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from home_page import show_home_page
import base64

@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


# img = get_img_as_base64("Image/diamond.png")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://wallpaperaccess.com/full/745867.jpg");
background-size: 180%;
background-position: cover;
background-repeat: repeat;
background-attachment: local;
}}
# [data-testid="stSidebar"] > div:first-child {{
# background-image: url("https://cdn.wallpapersafari.com/67/37/Hfn0Nd.jpg");
# background-position: center; 
# background-repeat: no-repeat;
# background-attachment: fixed;
# }}
# [data-testid="stHeader"] {{
# background: rgba(0,0,0,0);
# }}
# [data-testid="stToolbar"] {{
# right: 2rem;
# }}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


page = st.sidebar.selectbox("Main Menu", ("Home","Predict"))

if page == "Predict":
    show_predict_page()
elif page=="Home":
    show_home_page()