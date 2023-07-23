import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title('Collection Dashboard')

DATA_URL = (r'Collection2023_streamlit.csv')
data = pd.read_csv(DATA_URL)
lowercase = lambda x: str(x).lower()
data.rename(lowercase, axis='columns', inplace=True)
df =data.groupby(['main_branch','customer_class'])['amount'].agg(['sum'])
df=df.reset_index()
fig = plt.figure(figsize=(15,8))
plt.plot(df['main_branch'],df['sum'],c='r',lw='5',marker='*' ,markersize='10',ls='--')
#plt.title('')
plt.xlabel('xlable')
plt.ylabel('ylable')
st.pyplot(fig)
st.subheader('ScatterPlot')
fig = plt.figure(figsize=(15,8))
plt.scatter(df['main_branch'],df['sum'])
#plt.title('')
plt.xlabel('xlable')
plt.ylabel('ylable')
st.pyplot(fig)
st.subheader('Heatmap')
fig = plt.figure(figsize=(15,8))
sns.heatmap(df.corr(),annot=True)
#plt.title('')
plt.xlabel('xlable')
plt.ylabel('ylable')
st.pyplot(fig)

st.subheader('plotly')
select=st.selectbox("select an option",['RES','COM','GOVT'],key='A')
fig=px.scatter(data_frame =df,x='main_branch',y='sum',)
st.plotly_chart(fig)

st.subheader('Bar char')
fig=px.bar(data_frame=df,x= df['main_branch'],y=df['sum'],color='customer_class')
st.plotly_chart(fig)

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data['branch_name'])
st.subheader('Collection By Month')
# df=pd.read_csv(DATA_URL)
# dfGroup=df.groupby(['Main_Branch','CUSTOMER_CLASS','month'])['Amount'].agg(['sum'])
# st.write(dfGroup)


