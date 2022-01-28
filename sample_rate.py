import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 



def return_sample_rate():
    
    st.title('Determine the Sample Rate')
    st.markdown("It is very likely that one of the first variables in your dataset looks like the following (highlighted in green):")
    # st.markdown(<font color=‘red’>THIS TEXT WILL BE RED</font>, unsafe_allow_html=True)))

    def color_column(val):
        color = 'lightgreen'
        return f'background-color: {color}'


    col1, col2, col3 = st.columns([1,5,1])

    with col2:
        st.table(pd.DataFrame({
                'Time': ['21-12-21 10:00:00', '21-12-21 10:00:01','21-12-21 10:00:02','21-12-21 10:00:03'],
                'Sensor1': [10, 10, 11, 10],
                'Sensor2': [14,15,14,14]
            }).style.set_table_styles([
                        {"selector":"caption",
                        "props":[("text-align","center")],
                        }

                        ], overwrite=False)\
                        .set_caption('Table 1.')\
                        .set_table_styles({"Time" : [
                                        {
                                            "selector" :"th",
                                            "props": "background-color:lightgreen;"
                                        }
                                    ]
                              }, overwrite=False)\
                        .applymap(color_column, subset=['Time'])           
                        )





    st.markdown("""
                In this dataset, the time variable reflects each moment an observation is recorded.
                This means that every second, each variable in your dataset takes a measurement.
                \n
                It could, however, also be the case that your data looks like the following, where every 5 minutes the data is recorded:
                """)
    
    col1, col2, col3 = st.columns([1,2.5,1])
    
    with col2:
        st.table(pd.DataFrame({
                'Time': ['21-12-21 10:00:00', '21-12-21 10:05:00','21-12-21 10:10:00','21-12-21 10:15:00'],
                'Sensor1': [10, 10, 11, 10],
                'Sensor2': [14,15,14,14]
            }).style.set_table_styles([
                        {"selector":"caption",
                        "props":[("text-align","center")],
                        }

                        ], overwrite=False)\
                        .set_caption('Table 2.')\
                        .set_table_styles({"Time" : [
                                        {
                                            "selector" :"th",
                                            "props": "background-color:lightgreen;"
                                        }
                                    ]
                              }, overwrite=False)\
                        .applymap(color_column, subset=['Time'])           
                        )
    
    # st.markdown('Which means that every 5 minutes your data is recorded.')
    
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
            }).style.applymap(color_column, subset=['Time']))
    
    st.markdown("""
                In this case, there is no notion of time. The only information available is the order of the observations.
                In this case, we advice you to figure out what the sample rate of you dataset is. 
                
                In addition, it is also possible to change the sample rate in your dataset. 
                Consider the following dataframe where each minute a sample is taken from a variable called 'Measure'.
                This dataset could be reduced in size by taken the average of sequential rows, which is visible in Table in the following two tables: 
                """)
    
    st.title('How to improve')

    st.success('Tip 1: Calculate rolling average to smooth out observations')
    
    st.markdown("""
    Consider the following dataset where the Variable 'var1' measures a random variable that counts up.
    However, it could be that the dataset is way to big, and needs some resampling to reduce the number of observations.
    Therefore, a technique called 'resampling' takes the average value for some time periods to reduce the dataset.
    """)

    # Create sample dataframe with resample example
    index = pd.date_range('1-1-2000', periods=9, freq='T')
    series = pd.Series(range(1,10), index=index)
    dataframe = pd.DataFrame(series, columns=['Measurement'])
    dataframe = dataframe.reset_index()
    dataframe.columns = ['Time','var1']
    dataframe["Time"] = pd.to_datetime(dataframe["Time"])
    dataframe["Time"] = dataframe["Time"].dt.strftime("%Y-%m-%d %H:%M:%S")
    
    df_values = dataframe.rolling(2).mean() 
    df = dataframe.iloc[::2, :]
    df['var1'] = df_values['var1']
    df = df.iloc[1:,:]
    df['var1'] = ['2.5','4.5','6.5','8.5']

    col1, col2, col3 = st.columns([1,2.5,1])
    with col2:
        st.dataframe(dataframe)
        st.table(df.round(2))







## Combine multiple table styles

    # with col2:
    #     st.table(pd.DataFrame({
    #             'Time': ['21-12-21 10:00:00', '21-12-21 10:00:01','21-12-21 10:00:02','21-12-21 10:00:03'],
    #             'Sensor1': [10, 10, 11, 10],
    #             'Sensor2': [14,15,14,14]
    #         }).style.set_table_styles([
    #                         {
    #                             "selector":"thead",
    #                             "props": [("background-color", "dodgerblue"), ("color", "white"),
    #                                       ("border", "3px solid red"),
    #                                       ("font-size", "2rem"), ("font-style", "italic")],
      
    #                         },
    #                         {
    #                             "selector":"th.row_heading",
    #                             "props": [("background-color", "orange"), ("color", "green"),
    #                                       ("border", "3px solid black"),
    #                                       ("font-size", "2rem"), ("font-style", "italic")]
    #                         },
    #                        {"selector":"caption",
    #                         "props":[("text-align","center")],
    #                        }

    #                     ], overwrite=False)\
    #                     .set_caption('test')\
    #                     .set_table_styles({"Time" : [
    #                                     {
    #                                         "selector" :"td",
    #                                         "props": "border: 2px solid red; color:green; background-color:yellow;"
    #                                     }
    #                                 ]
    #                           }, overwrite=False))