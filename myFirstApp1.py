import streamlit as st
import pandas as pd
st.write('Hello')
## Data
 data = pd.read_excel('Collection_All.xlsx',sheet_name = 'Sheet1')
  st.write(data)
st.write('finish')
