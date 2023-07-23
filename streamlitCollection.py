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
df =data.groupby(['branch_name','main_branch','customer_class','month'])['amount'].agg(['sum'])
df=df.reset_index()
df2=df['customer_class']
st.dataframe(df2)
fig = plt.figure(figsize=(15,8))
plt.plot(df['main_branch'],df['sum'])
st.pyplot(fig)

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data['branch_name'])
st.subheader('Collection By Month')
# df=pd.read_csv(DATA_URL)
# dfGroup=df.groupby(['Main_Branch','CUSTOMER_CLASS','month'])['Amount'].agg(['sum'])
# st.write(dfGroup)


