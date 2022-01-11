import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 


def missing_values():
    
    st.title('Determine at what moments in time an observation is made.')
    # st.markdown("It is very likely that one of the first variables in your dataset looks like the following:")
    
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
