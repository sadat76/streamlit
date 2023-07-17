import os
import streamlit as st
import pandas as pd
st.write('Hello')
  path = "Collection_All.xlsx"
    if not os.path.isfile(path):
        path = f"https://github.com/sadat76/streamlit/main/{path}"
    data = pd.read_excel(path)
#df=pd.read_excel(r'C:\Users\engsa\OneDrive\الأرشيف\2023\00\PowerBI\Projects\Collection_2\Collection_All.xlsx')
st.write(data)
st.write('finish')
