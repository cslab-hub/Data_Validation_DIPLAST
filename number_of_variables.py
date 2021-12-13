import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 

def return_number_of_variables():
    
    st.title('How many variables are in your dataset?')
    
    option = st.selectbox(
        'Select the number of variables in your dataset',
        ['','<10','10-20','21-100','100+'], format_func=lambda x: 'Select an option' if x == '' else x)
    
    
    if option == '<10':
        st.success('You have an ideal number of variables!')
        st.write("You have only collected the important variables that belong to your goal.")
        
    