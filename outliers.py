import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 
import matplotlib.pyplot as plt 
# from sklearn.neighbors import LocalOutlierFactor

data = pd.read_csv('https://raw.githubusercontent.com/DHI/tsod/main/tests/data/example.csv')
data.to_csv('data/anomaly.csv', index=None)
fig = plt.plot(data['value'])

fig, ax = plt.subplots()
ax.plot(data['value'])





def return_outliers():
    st.title('Outlier detection')
    
    st.markdown("""
                Imagine you have a dataset with the following data:
                
                
                """)
    
    st.pyplot(fig)
    
    
    