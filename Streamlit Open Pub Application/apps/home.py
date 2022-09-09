import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



def app():
    st.title('Welcome To The Home Page ')

    st.write("This multi-page app is using the streamlit-multiapps framework developed by `Nilkantha Bag.`")

    st.subheader("Let see some basic information and statistics about the dataset")


    df = pd.read_csv('finaldata.csv')
    st.dataframe(df)

    s_box= st.selectbox('',('Head','Tail',"Correlation",'Total Number of Pubs','Pub Near Me'))


    if s_box=='Total Number of Pubs':
        st.subheader(f'There  are  **{df.shape[0]}**  Pubs  in  your locality')

    
    elif s_box=='Head':
        st.markdown("Showing initial 5  data from the dataset")
        st.dataframe(df.head(5))

    elif s_box=='Tail':
        st.markdown("Showing last 5  data from the dataset")
        st.dataframe(df.tail(5))

    elif s_box=="Correlation":
        st.dataframe(df.corr())

    elif s_box=='Pub Near Me':
        st.subheader(f'Total no of pub near you is  {len(df.local_authority.unique())}')

   


    

    st.subheader('Click on `Describe` to see the Statistics information of the open _pub dataset')

    stat = st.button('Describe')

    if stat==True:
        st.dataframe(df.describe())
    else:
        st.text('')








    