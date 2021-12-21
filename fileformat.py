import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 

def return_file_format():
    st.title('What is the file format of your data?')

    st.markdown("""
                ### Take a look at your dataset in the folder where it is stored.\n
                The file contains a specific file extension which is found after the filename.\n
                For example, a file called dataset.csv has the file format comma-separated-value.\n
                Excel files would have the name: .xlsx or .xsl.
                
                After you have found your file format, you can find it in the drop-down menu below:
                """)


    option = st.selectbox(
        'What is the file format of your data?',
        ['','csv','excel','txt','parquet','other'], format_func=lambda x: 'Select an option' if x == '' else x)
    

    if option == 'csv':
        st.success('You have an ideal data format!')
        "CSV files are structured in a [row, column] manner and are easy to work with."
        
        st.table(pd.DataFrame({
            'Sensor1': [1.21, 1.25, 1.31, 1.27],
            'Sensor2': [10.21, 10.33, 11.12, 10.87]
        }).style.format('{:.2f}'))
        
        st.success('Also try saving your data with a comma that separates values: Var1, Var2 instead of Var1; Var2')
        
    
    if option == 'excel':
        st.error('Better data formats are available!')
        st.markdown("""
        #### Issue 1: The data are saved in other Sheets instead of different files.\n
        CSV files are structured in a [row, column] manner and are easy to work with.\n
        In addition, other programs could experience issues when inporting excel data.
        """)
        
        col1, col2, col3 = st.columns([1,2.5,1])
        # with col1:
        #     st.write("")

        with col2:
            image = Image.open('images/excel_example.png')
            st.image(image, caption='Figure 1: Example of how Excel structures data.', use_column_width=True)

        st.success('Tip: Try to convert the Excel file to a .csv file for easier processing!')
        # with col3:
        #     st.write("")
            
            
        
            
    if option == 'txt':
        st.success('You have an ideal data format!')
        st.markdown("TXT files are just like .csv files, organised in a [row, column] manner and therefore are easy to work with.")
        

    if option == 'parquet':
        st.warning('Parquet is not the ideal data format')
        st.markdown('Parquet files are a column-based dataset which can be used, but not many websites support documentation for this data type. Please check if you could ask from your data supplier if the data could be supplied in .csv or .txt format')

    if option == 'other':
        st.error('Your dataset format is commonly used')
        st.markdown('Please ask your data supplier for a .csv or .txt version of your data, because it is highly likely that errors will occur in the future due to the data format you own.')
        