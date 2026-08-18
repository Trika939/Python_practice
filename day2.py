
## Streamlit is use to write Basic Web Application for Data Analysis and ML Projects(UI)-user interface
import streamlit as st
import pandas as pd

st.set_page_config(page_title="MY Applicatrion",layout="wide")
st.header("MY FIRST WEB APPLICATION")
st.subheader("This application is for data analysis tools")

n1=st.number_input("Enter A Number")
n2=st.number_input("Enter B Number")
if st.button("Addition"):
   st.header ("Addition = "+str(n1+n2))

st.slider("Enter age",0,120)   
st.slider("Enter Distance in KM",0.0,200.0)

st.selectbox("select course",['Data Science','Data Analytics','Business Analytics'])
st.radio("Select Gender",['Male','Female'])

col1,col2,col3,col4,col5,=st.columns(5)
with col1:
   st.metric("Total sale",786654)
with col2:   
    st.metric("Total profit",666545)
with col3:
   st.metric("Total sale",786654)
with col4:   
    st.metric("Total profit",666545)   
with col5:
   st.metric("Total sale",786654)

path=st.file_uploader("select your file",type=['cvs','xlsx'])
df=pd.read_excel(path)
st.dataframe(df)


    