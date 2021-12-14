import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 

def return_number_of_variables():
    
    st.title('How many variables are in your dataset?')
    
    option = st.selectbox(
        'Select the number of variables in your dataset',
        ['','<10','10-30','31+'], format_func=lambda x: 'Select an option' if x == '' else x)
    
    
    if option == '<10':
        st.success('You have an ideal number of variables!')
        st.write("You have only collected the important variables that belong to your goal.")
        
    if option == '10-30':
        st.warning('You are in the safe zone, but keep in mind that the number of variables can be reduced further')
        
    if option == '31+':
        st.error('Too many variables!')
        st.markdown('Here are some tips to reduce the number of variables')
        st.success('Try finding variables that do not contain any deviation')
        st.markdown('''Most likely, quite a lot of your variables are set variables.
                    What we mean by set variables are variables that monitor the settings of a machine.
                    For example, the set variable of temperature can be 90 degrees, and the variables that measures temperature has the actual readings 90.1, 90.0, 89.9, 90 etc.
                    
                    ''')
    