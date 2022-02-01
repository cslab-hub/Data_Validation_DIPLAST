import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 
import matplotlib.pyplot as plt 
import seaborn as sns

def return_correlation():
    
    hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    
    st.title('Create Correlation plots')
    
    st.markdown("""
    Correlation is a statistical term which refers to how close two variables have a linear relationship to each other.
    Variables that have a linear relationship tell us less about our dataset, since measuring one tells you something about the other.
    In other words, if two variables have a high correlation, we can drop on of the two!
    """)

    iris_correlation = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")
    iris_correlation = iris_correlation.iloc[:,:4]
    iris_correlation.columns = ['temperature1','temperature2','temperature3','temperature4']
    st.table(iris_correlation.head(5).style.set_precision(2)\
        .set_table_styles([
                        {"selector":"caption",
                        "props":[("text-align","center")],
                        }

                        ], overwrite=False)\

            .set_caption('Table 1.'))
    corr = iris_correlation.corr().round(2)
    corr.style.background_gradient(cmap='coolwarm')
    st.table(corr.style.background_gradient(cmap='coolwarm').set_precision(2)\
        .set_table_styles([
                        {"selector":"caption",
                        "props":[("text-align","center")],
                        }

                        ], overwrite=False)\
            

            .set_caption('Table 2.'))
    
