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



    import os
    # st.write(os.listdir("data/"))

    import os

    def files(path):  
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                yield file

    filelist = []
    for file in files("data/delimiter_tests/"):  
        extension = file.split('.')[-1]
        if str(extension) in ['csv','txt','xlxs']:
            filelist.append(file)

    option = st.selectbox(
     'Which dataset do you want to investigate?',
     ([i for i in filelist]))

    st.write('You selected:', option)
    main_path = 'data/delimiter_tests/'
    st.write('delimiter used in this file was automatically detected and determined on = ',get_delimiter(main_path + option))

    dataset = pd.read_csv(main_path + option,delimiter=get_delimiter(main_path+option))
    dataset = dataset.iloc[0:int(dataset.shape[0] / 100),:]
    st.write(dataset.shape)

    st.dataframe(dataset.head(20), height=500)


    # options = st.multiselect(
    #  'Which variables do you want to keep?',
    #  [i for i in dataset.columns],dataset.columns[1], key=0)

    # st.dataframe(dataset[options])

    visualized_options = st.multiselect(
     'Which variables do you want to keep?',
     [i for i in dataset.columns],dataset.columns[1], key=1)

    import matplotlib.pyplot as plt 
    import matplotlib.colors as mcolors
    colors = ['b','g','r','c','m','y','k','black']

    # for i,j in enumerate(visualized_options):
    #     fig, ax = plt.subplots(figsize=(8,3))
    #     ax.plot(dataset[j], label=j, c=colors[i],linewidth=1)
    #     ax.legend()
    #     st.pyplot(fig)



    # new test
    from matplotlib import gridspec
    import math

    N = len(visualized_options)
    cols = 2
    rows = int(math.ceil(N / cols))
    colors = ['b','g','r','c','m','y','k','black']

    gs = gridspec.GridSpec(rows, cols)
    fig = plt.figure()
    for n in range(N):
        ax = fig.add_subplot(gs[n])
        ax.plot(dataset[visualized_options[n]], label=visualized_options[n], c=colors[n],linewidth=1)
        ax.legend(fontsize=7)
    fig.tight_layout()
    st.pyplot(fig)


    st.title('test')

    from tdda.constraints import discover_df, verify_df

    constraints = discover_df(dataset)
    constraints_path = 'tdda_tests/' + option.split('.')[0] + '.tdda'
    with open(constraints_path, 'w') as f:
        f.write(constraints.to_json())
        
    #Show the generated constraints
    st.write(str(constraints))
    st.title('verify')
    v1 = verify_df(dataset, constraints_path, type_checking='strict', epsilon=0)
    st.write(str(v1))

    st.title('profiling')
    st.title('profiling2')

    from pandas_profiling import ProfileReport
    from streamlit_pandas_profiling import st_profile_report
    profile = ProfileReport(dataset, title="Pandas Profiling Report", minimal=True)
    st_profile_report(profile)