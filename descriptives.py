import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 


def return_descriptives():
    st.title('Initial inspection of your dataset')
    
    st.markdown("""
                It is also valuable to check the initial descriptives of your dataset.
                There are several ways to achieve this. 
                For example, in Excel it is possible to select the columns of your dataset and calculate the following metrics:
                """)
    st.success('Tip: Calculate the Mean, ST.Dev, Variance, Min & Max of each variable in your dataset.')

    index = pd.date_range('1-1-2000', periods=9, freq='T')
    series = pd.Series(range(1,10), index=index)
    dataframe = pd.DataFrame(series, columns=['Measurement'])
    # dataframe = dataframe.style.format({'date': lambda x: "{}".format(x.strftime('%m/%d/%Y %H:%M:%S'))}).set_table_styles('styles')
    dataframe = dataframe.reset_index()
    dataframe.columns = ['Time','var1']
    dataframe["Time"] = pd.to_datetime(dataframe["Time"])
    dataframe["Time"] = dataframe["Time"].dt.strftime("%Y-%m-%d %H:%M:%S")


    dataframe['var2'] = dataframe['var1'] + np.random.randint(10,size=9)
    dataframe['var3'] = 1 + np.random.uniform(low=0.0001, high=0.1,size=9)
    dataframe['var4'] = 1
    dataframe = dataframe[['Time','var2','var3','var4']]
    st.table(dataframe)


    st.markdown("""
                It is possible to learn a lot about the dataset by inspecting these summary statistics:
                """)

    st.table(dataframe.describe())

    st.markdown("""
                For example, we can already see that the variable called: 'var4' does not deviate in measurement.
                This could indicate that this variable does not provide any new information to us, we could remove it!
                """)