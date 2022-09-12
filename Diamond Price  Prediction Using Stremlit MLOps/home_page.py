import streamlit as st
import pandas as pd
import numpy as np
import base64
from select import select
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

def show_home_page():
    st.title('Welcome to Diamond Price Prediction APP ')

    video_file = open('Video/diamond.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)


    st.subheader("Let see some basic information and statistics about the dataset")
    df = pd.read_csv("Data/diamonds.csv")
    st.dataframe(df)

    s_box= st.selectbox('',('Head','Tail',"carat",'cut',"color","clarity"))

    
    if s_box=='Head':
        st.markdown("Showing initial 5  data from the dataset")
        st.dataframe(df.head(5))

    elif s_box=='Tail':
        st.markdown("Showing last 5  data from the dataset")
        st.dataframe(df.tail(5))

    elif s_box=='carat':
        st.subheader(f"Range of Carat is {df.carat.min()} -{df.carat.max()}")

    elif s_box=='cut':
        st.subheader(f'Different cut are{df.cut.unique()}')
    
    elif s_box=='color':
        st.subheader(f'Different color are{df.color.unique()}')
    
    elif s_box=='clarity':
        st.subheader(f'Different clarity are{df.clarity.unique()}')


    st.subheader('Click on `Describe` to see the Statistics information of Diamond dataset')

    stat = st.button('Describe')

    if stat==True:
        st.dataframe(df.describe())
    else:
        st.text('')

    st.title('Exploratory Data Analysis')
    
    ######################################################################################################################
    # making sns plots in streamlit
    st.text('Different Boxplot ')
    fig = plt.figure(figsize=(15, 12))
    for i, col in enumerate(df.select_dtypes(exclude='object')):
        plt.subplot(4, 3, i+1)
        sns.boxplot(df[col])
        plt.tight_layout()

    st.write(fig)
    ########################################################################################################################

    # st.title('Bivariate Analysis')
    # "**Bivariate Analysis**"
    'Since the boxplot shows that most of the features have outliers thus median would be good choice for central tendency'

    '**Barchart shown below is controled with features in the sidebar**'
    opt = st.selectbox(label='Select any categorical feature', options=df.select_dtypes(include='object').columns)
    fig = px.bar(df.groupby(opt).median().price,labels={'value':'price'}, text_auto=True, title=f'Median price across {opt}').update_xaxes(categoryorder='total descending')
    st.write(fig)



    "* Fair cut diamonds has highest median price followed by premium cut followed by good cut."
    "* J colored diamonds has highest median price followed by I colored followed by H colored where as E colored diamonds have the least median price."
    "* SI2 clarity diamond has highest median price followed by I1 followed, by SI1 clarity followed  where as IF colored diamonds has least median price."
    '**Boxplot shown below is controled with features in the sidebar**'
    fig = px.box(df, x=opt, y='price', title=f'Boxplot: {opt} vs price')
    st.write(fig)
    '* Price has good variation across various clarity levels.'
    "* Price has good variation across various colors."

    opt2 = st.selectbox(label='Select any continuous feature', options=['carat', 'x'])
    fig = px.scatter(df, x=opt2, y='price', title=f'Scatterplot {opt2} vs price')
    st.write(fig)
    '* Carat has good correlation with price'
    '* X has good correlation with price'

    '**Correlation Heatmap**'
    #########################################################
    # fig = plt.figure(figsize=(15,10))
    # sns.heatmap(data, mask= np.triu(data,1), annot=True)
    # st.pyplot(fig)
    ############################################################
    st.header("Correlation Heatmap")
    data = df.corr()
    st.write(px.imshow(data, text_auto = '.2f', aspect='auto', color_continuous_scale='viridis'))
    '* Price has very good correlation with carat, x, y and z features'
    ###############################################################

    # st.title("Pairplot")
    # fig = sns.pairplot(df, hue="cut")
    # st.pyplot(fig)



    
    





        


    