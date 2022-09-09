import streamlit as st
import numpy as np
import pandas as pd
from tkinter import Button

def app():
    # st.title('Find The Nearest Pub')

    st.write('This is `Find the nearest pub ` page of the multi-page app.')

    

    df = pd.read_csv('pub.csv')

    st.title("Nearest Pubs")
    st.header('Lets Enjoy The Party in Pub :wine_glass:')
    st.image("Gallery.png")
    df=pd.read_csv("pub.csv")
    location=df[["latitude","longitude"]]
    lat=st.number_input("Enter Your Latitude:")
    lon=st.number_input("Enter Your Longitude:")
    button=st.button("SHOW PUBS")

    new_location=np.array([lat,lon])
    distances = np.sqrt(np.sum((new_location - location)**2, axis = 1))
    n = 5
    min_indices = np.argpartition(distances,n-1)[:n]

    if button ==True:
        st.markdown("### Nearest Pubs Are")
        st.dataframe(df.iloc[min_indices])
        st.map(df.iloc[min_indices])