import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 

def return_endresult():
    
    hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    
    st.title('End result')

    path = 'data/delimiter_tests/turbine_semicolon.csv'
    import csv
    def get_delimiter(file_path, bytes = 4096):
        sniffer = csv.Sniffer()
        data = open(file_path, "r").read(bytes)
        delimiter = sniffer.sniff(data).delimiter
        return delimiter

    st.write('delimiter used in this file was automatically detected and determined on = ',get_delimiter(path))

    dataset = pd.read_csv(path,delimiter=get_delimiter(path))
    st.dataframe(dataset)