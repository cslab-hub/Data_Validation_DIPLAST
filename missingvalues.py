import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 


def return_missing_values():
    
    hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """
    st.markdown(hide_table_row_index, unsafe_allow_html=True)


    st.title('It could occur that various variables did not measured all time points.')
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




    st.error('Bad Example 1: Each variable started recording at different timepoints.')
    st.markdown("""
    It could occur that one variable in your dataset did not measure correctly every timepoint. 
    In this case, we advice to remove all the observations where even a single variable measured nothing, in order to prevent errors in the future analysis.\n

    """)
    inconsistent_df = dataframe.copy(deep = True)
    inconsistent_df['var2'] = [np.nan, np.nan, np.nan,"4","5","6","7","8","9"]
    inconsistent_df['var3'] = [np.nan,np.nan,np.nan,np.nan,"5","6","7","8","9"]

    image = Image.open('images/down-arrow.png')

    col1, col2, col3 = st.columns([1,6,1])
    with col2:
        st.table(inconsistent_df.style.highlight_null(null_color="tomato")\
            .set_table_styles([
                        {"selector":"caption",
                        "props":[("text-align","center")],
                        }

                        ], overwrite=False)\

            .set_caption('Table 1.'))

    col1, col2, col3 , col4, col5 = st.columns(5)

    with col3 :
        st.image(image, width =75)
    
    col1, col2, col3 = st.columns([1,6,1])
    with col2:
        st.table(inconsistent_df.iloc[4:,:].style.set_table_styles([
                        {"selector":"caption",
                        "props":[("text-align","center")],
                        }

                        ], overwrite=False)\

            .set_caption('Table 2.'))


    st.error('Bad Example 2: There are  various missing values scattered around your dataset.')
    st.markdown("""
    It could occur that the variables in your dataset have scattered missing values. 
    In this case, it is possible to delete these observations as well, but also imputing them from their neighbours. 
    For example, in the following toy example dataset, it is possible to infer the linear pattern in the data. 
    This is also possible with other kind of measurements!

    """)
    inconsistent_df = dataframe.copy(deep = True)
    # inconsistent_df['var2'] = ["1","2","","4","5","","7","8","9"]
    inconsistent_df['var2'] = [1,2,np.nan,4,5,np.nan,7,8,9]
    inconsistent_df['var3'] = [1,np.nan,3,4,np.nan,6,np.nan,8,9]

    # inconsistent_df['var3'] = ["1","","3","4","","6","","8","9"]

    # col1, col2, col3 = st.columns([1,6,1])
    # with col2:
    #     st.table(inconsistent_df)
    #     inconsistent_df['var2'] = inconsistent_df['var2'].interpolate().astype(int)
    #     inconsistent_df['var3'] = inconsistent_df['var3'].interpolate().astype(int)

    #     st.table(inconsistent_df)

    col1, col2, col3 = st.columns([1,6,1])
    with col2:
        st.table(inconsistent_df.style.highlight_null(null_color="tomato")\
            .set_table_styles([
                        {"selector":"caption",
                        "props":[("text-align","center")],
                        }

                        ], overwrite=False)\

            .set_caption('Table 3.'))


    col1, col2, col3 , col4, col5 = st.columns(5)

    with col3 :
        st.image(image, width =75)
    
    col1, col2, col3 = st.columns([1,6,1])
    with col2:
        inconsistent_df['var2'] = inconsistent_df['var2'].interpolate().astype(int)
        inconsistent_df['var3'] = inconsistent_df['var3'].interpolate().astype(int)
        st.table(inconsistent_df.style.set_table_styles([
                        {"selector":"caption",
                        "props":[("text-align","center")],
                        }

                        ], overwrite=False)\

            .set_caption('Table 4.'))
