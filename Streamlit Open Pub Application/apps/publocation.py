import streamlit as st
import numpy as np
import pandas as pd



def app():
    # st.title('Pub Location')
    # st.image("https://thumbs.dreamstime.com/b/gold-line-alcohol-beer-bar-location-icon-isolated-black-background-symbol-drinking-pub-club-vector-illustration-183544224.jpg")

    st.write('This is the `Publocation` page of the multi-page app.')

    
    df = pd.read_csv('pub.csv')

    st.subheader('Click on `Display Map` to see the Map')

    btn_map = st.button("Display Map ")

    if btn_map==True:
        st.map(df)


    st.subheader('Find Either by Locality or Postal code')


    local = df.local_authority.unique()
    
    option = st.selectbox('Locality',local)
    


    'You Selected : ' ,option


    btn_clk = st.button('Find now')
    if btn_clk==True:
        st.markdown(f'Displaying all the pubs near {option}') 
        res = df[df['local_authority']==option]
        res=res[['latitude','longitude']]
        st.map(res)



    post_code=df.postcode.unique()
    
    option2 = st.selectbox('Postal_code',post_code)

    'You Selected : ' ,option2

    btn_clk2 = st.button('Find now',key=2)
    if btn_clk2==True:
        st.markdown(f'Displaying all the pubs near {option2}') 
        res = df[df['postcode']==option2]
        res=res[['latitude','longitude']]
        st.map(res)
    


    












  
  
  
  
  
  
  
  
  
  
  
  
    # local = df.local_authority.unique()
    
    # option = st.selectbox('Locality',local)
    


    # 'You Selected : ' ,option

    # btn_clk = st.button('Find now')
    # if btn_clk==True:
    #     st.markdown(f'Displaying all the pubs near {option}') 
    #     res = df[df['local_authority']==option]
    #     res=res[['latitude','longitude']]
    #     st.map(res)
