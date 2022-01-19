import streamlit as st
# st.set_page_config(layout="wide")
import pandas as pd
import numpy as np
from PIL import Image 

from home import *
from fileformat import *
from columnnames import *
from texteditors import *
from number_of_variables import *
from sample_rate import *
from descriptives import *
from outliers import *
from missingvalues import *
# from streamlit_option_menu import option_menu

st.set_page_config(
     page_title="Data Validation",
    #  page_icon="🧊",
    #  layout="wide",
    #  initial_sidebar_state="expanded",
)

st.sidebar.title("Select Chapter")
st.sidebar.markdown("Each chapter explains a different aspect of validating your datasets.")


add_selectbox = st.sidebar.radio(
    "Choose a chapter:",
    ("Home","Chapter 1: File Format","Chapter 2: Text Editors" ,"Chapter 3: Column Names", "Chapter 4: Amount of Variables","Chapter 5: Sample Rate","Chapter 6: Descriptives","Chapter 7: Outliers","Chapter 8: Missing Values & Data Imputation"),format_func= lambda x: 'Home' if x == 'Home' else f"{x}"
    
)  


#! Home page
if add_selectbox == 'Home':
    return_homepage()
    
    
#! Page for the file format
if add_selectbox == 'Chapter 1: File Format':
    return_file_format()
  
if add_selectbox == 'Chapter 2: Text Editors':
    return_texteditors()
        
if add_selectbox == 'Chapter 3: Column Names':
    return_column_names()

if add_selectbox == 'Chapter 4: Amount of Variables':
    return_number_of_variables()
        
if add_selectbox == 'Chapter 5: Sample Rate':
    return_sample_rate()
    
    
    
if add_selectbox == 'Chapter 6: Descriptives':
    return_descriptives()
    
if add_selectbox == 'Chapter 7: Outliers':
    return_outliers()

if add_selectbox == 'Chapter 8: Missing Values & Data Imputation':
    return_missing_values()
# This removes the copyright of how the page is made
hide_st_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)