import streamlit as st
import pandas as pd
import numpy as np
from select import select
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from pickle import load
clarity_encoder=load(open(r'C:\Users\smart\OneDrive\Desktop\Heroku Diamond App Deployment\Project\models\label_encoder_clarity.pkl','rb'))
color_encoder=load(open(r'C:\Users\smart\OneDrive\Desktop\Heroku Diamond App Deployment\Project\models\label_encoder_color.pkl','rb'))
cut_encoder=load(open(r'C:\Users\smart\OneDrive\Desktop\Heroku Diamond App Deployment\Project\models\label_encoder_cut.pkl','rb'))


def show_predict_page():

    st.title("Welcome To Diamond Price Prediction")
    st.image(r"Image\diamond.png")

    scaler=load(open('models/standard_scaler.pkl','rb'))

    dt_model=load(open(r'C:\Users\smart\OneDrive\Desktop\Heroku Diamond App Deployment\Project\models\decision_tree_model.pkl','rb'))

    clarity_encoder={'I1':1,'SI2':2,'SI1':3,'VS2':4,'VS1':5,'VVS2':6,'VVS1':7,'IF':8}
    color_encoder={'J':1,'I':2,'H':3,'G':4,'F':5,'E':6,'D':7}
    cut_encoder={'Fair':1,'Good':2,'Very Good':3,'Ideal': 4,'Premium':5}
    carat=st.text_input('Carat',placeholder='Enter value in mm (range 0.2-5.01)')
    depth=st.text_input('Depth',placeholder='Enter value in mm (range 43-79)')
    table=st.text_input('Table',placeholder='Enter value in mm (range 43-95)')
    x=st.text_input('X',placeholder='Enter value in mm (range 0-10.7)')
    y=st.text_input('Y',placeholder='Enter value in mm (range 0-58.9)')
    z=st.text_input('Z',placeholder='Enter value in mm (range 0-31.8)')

    
    clarity = st.selectbox(
        'How would you like to be contacted?',
        ('I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'))

    cut = st.selectbox(
        'How would be the cut of Diamond?',
        ('Fair', 'Good', 'Very Good', 'Ideal', 'Premium'))

    color = st.selectbox(
        'What should be the color of Diamond?',
        ('J', 'I', 'H', 'G', 'F', 'E', 'D'))

    

    btn_click=st.button("Predict")

    if btn_click==True:
        if carat and depth and table and x and y and z:
            
            
            query_point_num_transformed=scaler.transform([[float(carat),float(depth),float(table),float(x),float(y),float(z)]])
            query_point_cat=np.array([clarity_encoder[clarity],color_encoder[color],cut_encoder[cut]])#.reshape(1,-1)
            
            df=np.concatenate((query_point_cat,query_point_num_transformed.flatten()),axis=None)
            pred=dt_model.predict(df.reshape(1,-1)).item()
            st.success(pred)
            st.balloons()
        else:
            st.error('Enter the values properly')
            st.snow()
            

        