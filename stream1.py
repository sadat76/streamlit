import streamlit as st
st.write('Hello')
import pandas as pd
import numpy as np
df= pd.DataFrame(np.random.randn(10, 2),columns=['x', 'y'])
st.line_chart(df)
st.write('finish')
