#importing libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#reading the file
df = pd.read_csv('tips.csv')

#setting page configration 
st.set_page_config(page_title='Tips',layout='wide',initial_sidebar_state='auto')

#sidebar

#create the side bar details 
st.sidebar.image('Screenshot 2024-09-16 033402.png',width=150)
st.sidebar.write('')
st.sidebar.write('Filter: ')

#creating the select boxes
cat_filter =  st.sidebar.selectbox('Categorical filter',[None,'sex','day','time','smoker'])

#separate 
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.markdown('Made by Eng \ Mohamed_Ahmed')
st.sidebar.markdown('[Linkedin]((www.linkedin.com/in/mohamed-ahmed-260183254))')


#body

#Row A
st.markdown("<h1 style='text-align: center;'>Tips Report</h1>", unsafe_allow_html=True)
st.write(' ')
a1, a2, a3, a4 = st.columns(4)
a1.metric('Max. Total Bill',df['total_bill'].max())
a2.metric('Min. Total Bill',df['total_bill'].min())
a3.metric('Max. Tip',df['tip'].max())
a4.metric('Min. Tip',df['tip'].min())

#Row B
st.subheader('Total_bill vs Tips')
fig = px.scatter(df,x='total_bill',y='tip',color= cat_filter)
st.plotly_chart(fig, use_container_width=True)