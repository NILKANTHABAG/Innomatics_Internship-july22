import streamlit as st
import pandas as pd
import numpy as np

from select import select
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns




def show_explore_page():
    st.title('Welcome to Explore Page')
    video_file = open('Video/diamond.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)




    