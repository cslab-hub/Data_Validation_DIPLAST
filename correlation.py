from select import select
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 
import matplotlib.pyplot as plt 

# import seaborn as sns
from statsmodels.tsa.stattools import grangercausalitytests

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
    st.table(iris_correlation.head(5).style.format(precision=2)\
        .set_table_styles([
                        {"selector":"caption",
                        "props":[("text-align","center")],
                        }

                        ], overwrite=False)\

            .set_caption('Table 1.'))
    corr = iris_correlation.corr().round(2)
    corr.style.background_gradient(cmap='coolwarm')
    st.table(corr.style.background_gradient(cmap='coolwarm')\
        .format(precision=2)\
        .set_table_styles([
                        {"selector":"caption",
                        "props":[("text-align","center")],
                        }

                        ], overwrite=False)\
            

            .set_caption('Table 2.'))

    st.title('Granger Causality')
    st.markdown("""The Granger Causality is a statistical test for finding out wether one timeseries is usefull in forecasting another.
    In other words, a variable X granger-causes variable Y, of the values of X provide statistical significant information about future values of Y.


    
    
    """)

    #build the time series, just a simple AR(1)
    np.random.seed(2)
    t1 = [0.1*np.random.normal()]
    for _ in range(45):
        t1.append(0.5*t1[-1] + 0.1*np.random.normal())

    t2 = [item + 0.1*np.random.normal() for item in t1]
    t2 = [item + 0.03*np.random.normal() for item in t1]

    t1 = t1[3:]
    t2 = t2[:-3]

    def grangercausality():
        fig, ax = plt.subplots(figsize=(8,3))

        plt.figure(figsize=(7,2))
        ax.plot(t1, color='b')
        ax.plot(t2, color='r')

        ax.annotate('Lagging Peak', xy=(12, 0.2),  xycoords='data',
            xytext=(0.6, 0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top',
            )

        ax.annotate('Lagging Low', xy=(28.5, -0.2),  xycoords='data',
            xytext=(0.9, 0.2), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.1),
            horizontalalignment='right', verticalalignment='top',
            )
        ax.set_title("Figure 1: Granger Causality with peaks highlighted by arrows.", y=-0.25)
        ax.legend(['Original', 'Lagged'], fontsize=8)

        return fig

    st.pyplot(grangercausality())

    selection_taken = st.slider(
        'Select how many monents in time to look back:',
        1, 6)

#
    ts_df = pd.DataFrame(columns=['t2', 't1'], data=zip(t2,t1))
    gc_res = grangercausalitytests(ts_df, selection_taken)
    for i,j in enumerate(gc_res.values()):
        combined = round(np.mean([j[0]['ssr_ftest'][1], j[0]['ssr_chi2test'][1]]),3)
        st.write(f"P-value after {i} lags <= {combined}")
