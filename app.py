import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# setting page configuration
st.set_page_config(page_title="Sara Enterproses",layout="wide")
st.header("SARA ENTERPRISES")
st.text("Dashboard for sales dataset of Medical Products from Sara Enterprise with slicers plots and dataframes")

#loading dataset
df=pd.read_excel(r"C:\Users\RITS\Downloads\Financial_Sample.xlsx")
df

# data cleaning(Remove null value)
for col in df.columns:
    if df[col].isnull().sum()>0:
        if df[col].dtype =='str':
            df[col] = df[col].fillna(df[col].mode()[0])
        else:
            df[col] = df[col].fillna(round(df[col].mean(),2))



# Slicers
col1 , col2 , col3 , col4 , col5 = st.columns(5)
with col1:
    country = st.selectbox("Select Country",['All']+list(df.Country.unique()))
    if country != "All":
        df = df[df['Country']==country]
with col2:
    segment = st.selectbox("Select Segment",['All']+list(df.Segment.unique()))
    if segment != "All":
        df = df[df['Segment']==segment]
with col3:
    product = st.selectbox("Select Product",['All']+list(df.Product.unique()))
    if product != "All":
        df = df[df['Product']==product]
with col4:
    db = st.selectbox("Select Discount Band",['All']+list(df['Discount Band'].unique()))
    if db != "All":
        df = df[df['Discount Band']==db]
with col5:
    year = st.selectbox("Select Year",['All']+list(df['Year'].unique()))
    if year != "All":
        df = df[df['Year']==year]


# KPIs (Key Point Indicators)
col1 , col2 , col3 , col4 , col5 = st.columns(5)
li = [' Sales','Profit','Units Sold','COGS','Discounts']
cols = [col1,col2,col3,col4,col5]
i = 0
for col in cols:
    with col:
        if df[li[i]].sum()/1000000>1:
            st.metric("Total "+str(li[i]) , str(round(df[li[i]].sum()/1000000,2))+"M")
        elif df[li[i]].sum()/1000>1:
            st.metric("Total "+str(li[i]) , str(round(df[li[i]].sum()/1000,2))+"K")
        else:
            st.metric("Total "+str(li[i]) , str(round(df[li[i]].sum(),2)))       
    i=i+1

# Plotting/Graphs
col1 , col2 = st.columns(2)
x_axis = ['Country','Segment','Product','Discount Band']
y_axis = ['Profit',' Sales','Units Sold','COGS']
with col1:
    colx,coly = st.columns(2)
    with colx:
        x = st.selectbox("Select X-Axis",x_axis)
    with coly:
        y = st.selectbox("Select Data Point",y_axis)
    pbs = df.groupby(x).agg({y:'sum'}).reset_index()
    fig , ax = plt.subplots( figsize=(12,4) )
    ax.bar(pbs[x],pbs[y])
    st.pyplot(fig)
with col2:
    cola,colb = st.columns(2)
    x_axis = ['Month Name','Month Number',"Year"]
    with cola:
        x = st.selectbox("Select Trend",x_axis)
    with colb:
        y = st.selectbox("Select Data",y_axis)
    pbm = df.groupby(x).agg({y:'sum'}).reset_index()
    fig2 , ax2 = plt.subplots( figsize=(12,4) )
    ax2.plot( pbm[x],pbm[y] )
    st.pyplot(fig2)

# Sample Dataset
st.text("This is the filter dataset of shape "+str(df.shape))
st.dataframe(df , height=250)
    