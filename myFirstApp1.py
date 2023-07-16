import streamlit as st
import pandas as pd
st.write('Hello')
df=pd.read_excel(r'C:\Users\engsa\OneDrive\الأرشيف\2023\00\PowerBI\Projects\Collection_2\Collection_All.xlsx')
st.write(df)
st.write('finish')
