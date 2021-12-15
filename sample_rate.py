import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 


def return_sample_rate():
    
    st.title('Determine at what moments in time an observation is made.')
    st.markdown("It is very likely that one of the first variables in your dataset looks like the following:")
    
    st.table(pd.DataFrame({
            'Time': ['21-12-21 10:00:00', '21-12-21 10:00:01','21-12-21 10:00:02','21-12-21 10:00:03'],
            'Sensor1': [10, 10, 11, 10],
            'Sensor2': [14,15,14,14]
        }))

    
    st.markdown('This means that every second, each variable in your dataset takes a measurement.')
    
    st.markdown('It could, however, also be the case that your data looks like the following:')
    
    st.table(pd.DataFrame({
            'Time': ['21-12-21 10:00:00', '21-12-21 10:05:00','21-12-21 10:10:00','21-12-21 10:15:00'],
            'Sensor1': [10, 10, 11, 10],
            'Sensor2': [14,15,14,14]
        }))
    
    st.markdown('Which means that every 5 minutes your data is recorded.')
    
    st.warning('It depends on your goal wheter or not every second or every 5 minutes is prefered')
    
    st.error('Watch out if your data looks like the following:')
    st.table(pd.DataFrame({
            'Time': ['0', '1','2','3'],
            'Sensor1': [10, 10, 11, 10],
            'Sensor2': [14,15,14,14]
        }))
    
    st.markdown('''In this case, there is no notion of time. The only information available is the order of the observations.
                In this case, we advice you to figure out what the sample rate of you dataset is.''')