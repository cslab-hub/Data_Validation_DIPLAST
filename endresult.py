import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 

def return_endresult():
    
    st.title('End result')

    st.markdown("""
    If everything went well, you should now have a dataset that looks like the following:
    """)

    st.table(pd.DataFrame({
                'Time': ['21-12-21 10:00:00', '21-12-21 10:00:01','21-12-21 10:00:02','21-12-21 10:00:03'],
                'Temperature_Sensor1': [10, 10, 11, 10],
                'Pressure_Sensor1': [14,15,14,14]
            }))