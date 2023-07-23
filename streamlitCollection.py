import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title('Collection Dashboard')

DATE_COLUMN = 'freeze_dt'
DATA_URL = (r'Collection2023_streamlit.csv')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    data=data.groupby(['main_branch','customer_class','month'])['amount'].agg(['sum'])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

st.subheader('Collection By Month')
df= pd.read_csv(DATA_URL)
df=df.groupby(['Main_Branch','CUSTOMER_CLASS','month'])['Amount'].agg(['sum'])
fig=plt.figure(figsize=(15,8))
plt.plot(df['main_branch'],df['amount'])
st.pyplot(fig)

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
