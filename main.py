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

st.sidebar.title("Select Chapter")
st.sidebar.markdown("Each chapter explains a different aspect of validating your datasets.")


add_selectbox = st.sidebar.radio(
    "Choose a chapter:",
    ("Home","File Format","Text Editors" ,"Column Names", "Amount of Variables","Sample Rate","Descriptives","Outliers","Missing Values & Data Imputation"),format_func= lambda x: 'Home' if x == 'Home' else f"{x}"
    
)                                                                                                                       


#! Home page
if add_selectbox == 'Home':
    return_homepage()
    
    
#! Page for the file format
if add_selectbox == 'File Format':
    return_file_format()
  
if add_selectbox == 'Text Editors':
    return_texteditors()
        
if add_selectbox == 'Column Names':
    return_column_names()

if add_selectbox == 'Amount of Variables':
    return_number_of_variables()
        
        
# This removes the copyright of how the page is made
hide_st_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)