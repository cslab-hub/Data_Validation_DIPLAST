import streamlit as st
import pandas as pd
pd.set_option('display.colheader_justify', 'center')
import numpy as np
from PIL import Image 


def return_descriptives():

    # hide_table_row_index = """
    #         <style>
    #         tbody th {display:none}
    #         .blank {display:none}
    #         </style>
    #         """
    # st.markdown(hide_table_row_index, unsafe_allow_html=True)
    
    st.title('Descriptives of your dataset')
    
    st.markdown("""
                It is also to check the initial descriptives of your dataset.
                There are several ways to achieve this. 
                For example, consider the following dataset:
                """)
    # st.success('Tip: Calculate the Mean, ST.Dev, Variance, Min & Max of each variable in your dataset.')

    index = pd.date_range('1-1-2000', periods=9, freq='T')
    series = pd.Series(range(1,10), index=index)
    dataframe = pd.DataFrame(series, columns=['Measurement'])
    # dataframe = dataframe.style.format({'date': lambda x: "{}".format(x.strftime('%m/%d/%Y %H:%M:%S'))}).set_table_styles('styles')
    dataframe = dataframe.reset_index()
    dataframe.columns = ['Time','var1']
    dataframe["Time"] = pd.to_datetime(dataframe["Time"])
    dataframe["Time"] = dataframe["Time"].dt.strftime("%Y-%m-%d %H:%M:%S")


    dataframe['var2'] = dataframe['var1'] + np.random.randint(10,size=9)
    dataframe['var3'] = 1 + np.random.uniform(low=0.0001, high=0.1,size=9)
    dataframe['var4'] = 3
    dataframe['var5'] = 'one'
    dataframe = dataframe[['Time','var2','var3','var4','var5']]

    col1, col2, col3 = st.columns([1,5,1])

    with col2:
        # st.table(dataframe.style.set_table_styles([
        #                         {"selector":"caption",
        #                         "props":[("text-align","center")],
        #                         }

        #                         ], overwrite=False)\

        #         .set_caption('Table 1.'))

        st.write(dataframe.style.set_table_styles([
                        {"selector":"caption",
                        "props":[("text-align","center"),("caption-side","top")],
                        },
                        {"selector":"th",
                        "props":[("text-align","center")],
                        },
                        
                        {"selector":"td",
                        "props":[("text-align","center")],
                        },
                        {"selector":"",
                        "props":[("margin-left","auto"),("margin-right","auto")],
                        }

                        ], overwrite=False)\

            .set_caption('Table 1: Sample dataset.')\
            .hide_index()\
            .set_table_styles({"Time" : [
                            {
                                "selector" :"th",
                                "props": "background-color:lightgreen;"
                            },
                            {
                                "selector" :"td",
                                "props": "background-color:lightgreen;"
                            }
                        ]
                    }, overwrite=False)\
            # .applymap(lambda x: "background-color: lightgreen", subset="var1")\
           
            .to_html()           
            , unsafe_allow_html=True)


    st.markdown("""
                It is possible to learn a lot about the dataset by inspecting these summary statistics.
                For example, we can already see that the variable called: 'var4' does not deviate in measurement.
                This could indicate that this variable does not provide any new information to us, we could remove it! \n

                Second, we can see that the Mean of Variable var2 is much higher than Var3 or var4. 
                If this behavior is expected it is okay, but you should check every value to know what the variable represents.
                """)
    col1, col2, col3 = st.columns([1,5,1])
    
    with col2:
        # st.table(dataframe.describe().apply(lambda s: s.apply('{0:.2f}'.format)).style.set_table_styles([
        #                         {"selector":"caption",
        #                         "props":[("text-align","center")],
        #                         }

        #                         ], overwrite=False)\

        #         .set_caption('Table 2.'))

        st.write(dataframe.describe().style.set_table_styles([
                        {"selector":"caption",
                        "props":[("text-align","center"),("caption-side","top")],
                        },
                        {"selector":"th",
                        "props":[("text-align","center")],
                        },
                        
                        {"selector":"td",
                        "props":[("text-align","center")],
                        },
                        {"selector":"",
                        "props":[("margin-left","auto"),("margin-right","auto")],
                        }

                        ], overwrite=False)\

            .set_caption('Table 2: Descriptives of the dataset.')\
            .format(precision=2)\
            # .hide_index()\
            # .set_table_styles({"Time" : [
            #                 {
            #                     "selector" :"th",
            #                     "props": "background-color:lightgreen;"
            #                 },
            #                 {
            #                     "selector" :"td",
            #                     "props": "background-color:lightgreen;"
            #                 }
            #             ]
            #         }, overwrite=False)\
            # .applymap(lambda x: "background-color: lightgreen", subset="var1")\
           
            .to_html()           
            , unsafe_allow_html=True)


    st.markdown("# Density plot of variables")

    st.markdown("""
                A quick inspection of your dataset can also be performed by looking at Density plots of your data.
                These density plots look at the distribution of all the values measured by a variable.
                It could be helpfull to think about a 'safe' range of values where you expect a sensor's data to fall into.
                If then these density plots show a complete different story, this could be an indication to check what is going on.
                """)

    iris = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")
    iris['sepal_width'] = iris['sepal_width'] + 90
    iris['sepal_length'] = iris['sepal_length'] + 90
    iris.columns = ['Temp1','Temp2','Temp3','Temp4','Temp5']

    import matplotlib.pyplot as plt
    iris_plot = iris[['Temp1','Temp2']].plot(kind='density', figsize=(8,4))
    iris_plot.set_xlabel("Temperature")
    iris_plot.set_ylabel("Density")
    st.pyplot(iris_plot.figure, clear_figure=True)


    st.markdown('# Data types of variables')
    st.markdown("""
                It is also possible to check the data types of your variables. 
                Consider again Table 1 above in this page, here are the first two rows visualized in Table 2.
                These values all are of different kinds. For example, 'var3' is measuring a numerical value with decimals.
                On the other hand, 'var4' is measuring a numerical value of whole numbers. 
                In addition, 'var5' is measuring a word which does not resemble numbers. 
                """)

    # st.table(dataframe.head(2).style.set_table_styles([
    #                     {"selector":"caption",
    #                     "props":[("text-align","center")],
    #                     }

    #                     ], overwrite=False)\

    #         .set_caption('Table 3.'))

    st.write(dataframe.head(2).style.set_table_styles([
                        {"selector":"caption",
                        "props":[("text-align","center"),("caption-side","top")],
                        },
                        {"selector":"th",
                        "props":[("text-align","center")],
                        },
                        
                        {"selector":"td",
                        "props":[("text-align","center")],
                        },
                        {"selector":"",
                        "props":[("margin-left","auto"),("margin-right","auto")],
                        }

                        ], overwrite=False)\

            .set_caption('Table 3: Sample dataset.')\
            .hide_index()\
            .set_table_styles({"Time" : [
                            {
                                "selector" :"th",
                                "props": "background-color:lightgreen;"
                            },
                            {
                                "selector" :"td",
                                "props": "background-color:lightgreen;"
                            }
                        ]
                    }, overwrite=False)\
            # .applymap(lambda x: "background-color: lightgreen", subset="var1")\
           
            .to_html()           
            , unsafe_allow_html=True)

    dtype_df = dataframe.dtypes.value_counts().reset_index()

    dtype_df.columns = ['VariableType','Count']
    dtype_df['VariableType'] = dtype_df['VariableType'].astype(str)
    dtypefig, dtypeax = plt.subplots(figsize=(8,4))
    dtypeax.set_yticks(np.arange(0,3,1))
    # fig.set_size_inches(24.5, 16.5)
    dtypeax.bar(dtype_df['VariableType'],dtype_df['Count'])
    st.pyplot(dtypefig)