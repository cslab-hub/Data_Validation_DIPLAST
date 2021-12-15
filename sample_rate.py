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

    
    st.markdown('''In this dataset, the time variable reflects each moment an observation is recorded.
                This means that every second, each variable in your dataset takes a measurement.''')
    
    st.markdown('It could, however, also be the case that your data looks like the following:')
    
    st.table(pd.DataFrame({
            'Time': ['21-12-21 10:00:00', '21-12-21 10:05:00','21-12-21 10:10:00','21-12-21 10:15:00'],
            'Sensor1': [10, 10, 11, 10],
            'Sensor2': [14,15,14,14]
        }))
    
    st.markdown('Which means that every 5 minutes your data is recorded.')
    
    st.warning('It depends on your goal wheter or not every second or every 5 minutes is prefered')
    
    st.markdown('''For example, imagine that the dataset your interested in measures the total stock of a certain mateial.
                It is ofcourse not neccesary to measure the total stock every second.
                However, when the pressure or temperature in an Extruder is to be analysed, more observations help alot!''')
    
    
    
    st.error('Watch out if your data looks like the following:')
    st.table(pd.DataFrame({
            'Time': ['0', '1','2','3'],
            'Sensor1': [10, 10, 11, 10],
            'Sensor2': [14,15,14,14]
        }))
    
    st.markdown('''In this case, there is no notion of time. The only information available is the order of the observations.
                In this case, we advice you to figure out what the sample rate of you dataset is.''')
    
    st.write('test')
    # st.success('Tip 1: Calculate rolling average to smooth out observations')
    # st.success('Also try saving your data with a comma that separates values: Var1, Var2 instead of Var1; Var2')
    
    # Create sample dataframe with resample example
    index = pd.date_range('1-1-2000', periods=9, freq='D')
    series = pd.Series(range(9), index=index)
    dataframe = pd.DataFrame(series, columns=['Measurement'])
    # dataframe = dataframe.style.format({'date': lambda x: "{}".format(x.strftime('%m/%d/%Y %H:%M:%S'))}).set_table_styles('styles')
    dataframe = dataframe.reset_index()
    dataframe.columns = ['Time','Measurement']
    dataframe["Time"] = pd.to_datetime(dataframe["Time"])
    dataframe["Time"] = dataframe["Time"].dt.strftime("%Y-%m-%d %H:%M:%S")
# st.dataframe(df
    st.dataframe(dataframe)