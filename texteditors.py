import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 

def return_texteditors():
    
    st.title('Find a Text Editor.')
    st.markdown("""
             After you have collected your data in either .csv or .txt, we have to inspect our data.\n
             Most likely you are used to Excel, however, for data analysis purposes, there are better options!\n
             
             We recommend [Sublime Text](https://www.sublimetext.com/), which can open almost any file format.\n
             Another great advantage of Sublime Text is that it open files significantly faster.
             
             
             """)
    image = Image.open('images/sublime.png')
    st.image(image, caption='Figure 1: Example of Sublime Text', use_column_width=True)

    