import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 


def return_sample_rate():
    
    st.title('Determine at what moments in time an observation is made.')
    st.markdown("It is very likely that one of the first variables in your dataset looks like the following:")
    
    def color_column(val):
        color = 'lightgreen'
        return f'background-color: {color}'

    col1, col2, col3 = st.columns([1,2.5,1])

    with col2:
        st.table(pd.DataFrame({
                'Time': ['21-12-21 10:00:00', '21-12-21 10:00:01','21-12-21 10:00:02','21-12-21 10:00:03'],
                'Sensor1': [10, 10, 11, 10],
                'Sensor2': [14,15,14,14]
            }).style.applymap(color_column, subset=['Time']))

    
    st.markdown('''In this dataset, the time variable reflects each moment an observation is recorded.
                This means that every second, each variable in your dataset takes a measurement.''')
    
    st.markdown('It could, however, also be the case that your data looks like the following:')
    col1, col2, col3 = st.columns([1,2.5,1])
    
    with col2:
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
    col1, col2, col3 = st.columns([1,2.5,1])

    with col2:
        st.table(pd.DataFrame({
                'Time': ['0', '1','2','3'],
                'Sensor1': [10, 10, 11, 10],
                'Sensor2': [14,15,14,14]
            }))
    
    st.markdown("""
                In this case, there is no notion of time. The only information available is the order of the observations.
                In this case, we advice you to figure out what the sample rate of you dataset is. \n
                
                In addition, it is also possible to change the sample rate in your dataset. \n
                Consider the following dataframe where each minute a sample is taken from a variable called 'Measure'.\n
                This dataset could be reduced in size by taken the average of sequential rows, which is visible in Table in the following two tables:

                
                
                """)
    
    st.success('Tip 1: Calculate rolling average to smooth out observations')
    
    # Create sample dataframe with resample example
    index = pd.date_range('1-1-2000', periods=9, freq='T')
    series = pd.Series(range(1,10), index=index)
    dataframe = pd.DataFrame(series, columns=['Measurement'])
    # dataframe = dataframe.style.format({'date': lambda x: "{}".format(x.strftime('%m/%d/%Y %H:%M:%S'))}).set_table_styles('styles')
    dataframe = dataframe.reset_index()
    dataframe.columns = ['Time','var1']
    dataframe["Time"] = pd.to_datetime(dataframe["Time"])
    dataframe["Time"] = dataframe["Time"].dt.strftime("%Y-%m-%d %H:%M:%S")
    
    df_values = dataframe.rolling(2).mean() 
    df = dataframe.iloc[::2, :]
    df['var1'] = df_values['var1']
    # df.drop('Measurement')
    df = df.iloc[0:,:]

    col1, col2, col3 = st.columns([1,2.5,1])
    with col2:
        st.dataframe(dataframe)
        st.caption('testtest')
        st.dataframe(df.iloc[1:,:])


    st.error('Bad Example 2: Each timestamp contains different observations.')
    st.markdown("""
    It could occur that one variable in your dataset did not measure correctly every timepoint. \n
    In this case, we advice to remove all the observations where even a single variable measured nothing, in order to prevent errors in the future analysis.\n

    """)
    inconsistent_df = dataframe.copy(deep = True)
    inconsistent_df['var2'] = ["","","","4","5","6","7","8","9"]
    inconsistent_df['var3'] = ["1","2","","4","5","6","7","8",""]


    col1, col2, col3 = st.columns([1,6,1])
    with col2:
        st.table(inconsistent_df)
        st.table(inconsistent_df.iloc[3:8,:])
