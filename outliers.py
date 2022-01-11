#%%
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 
import matplotlib.pyplot as plt 
# from sklearn.neighbors import LocalOutlierFactor

data = pd.read_csv('https://raw.githubusercontent.com/DHI/tsod/main/tests/data/example.csv')
data.to_csv('data/anomaly.csv', index=None)
# fig = plt.plot(data['value'])

#%%
def first_plot(data):
    # fig = plt.figure()

    fig, ax = plt.subplots()
    # ax.plot(data['value'])

    plt.scatter(data.index, data['value'], c='b', s=15)
    plt.plot(data.index, data['value'])
    plt.title("Spotted Outliers")
    plt.xlabel("Time")
    plt.ylabel("Value")

    plt.ylim([-0.1,3.1])
    return fig

# fig, ax = plt.subplots()
# ax.plot(data['value'])
fig1 = first_plot(data)
#
# new plot with anomalies
#%%
data = pd.read_csv('https://raw.githubusercontent.com/DHI/tsod/main/tests/data/example.csv')
q_low = data["value"].quantile(0.05)
q_hi  = data["value"].quantile(0.95)

df_filtered = data[(data["value"] < q_hi) & (data["value"] > q_low)]
df_filtered['identifier'] = 'b'

#%%
##
og_set = set(data.index.to_list())
new_set = set(df_filtered.index.tolist())
og_set - new_set

filtered_df_values = pd.DataFrame(data.loc[og_set - new_set])
filtered_df_values = filtered_df_values.sort_values('datetime')
filtered_df_values['identifier'] = 'r'
final_df = df_filtered.combine_first(filtered_df_values)


#%%
# fig2, ax = plt.subplots()

# ax.scatter(data=final_df, x='datetime', y='value', c='identifier', cmap='Set3')
# ax.set(title='', xlabel='Time', ylabel='')

# ax.axes.xaxis.set_ticklabels([0,20,40,60,80,100,120])
# ax.set_xticks([0,20,40,60,80,100,120])

#%%
# fig3 = plt.Figure()
# plt.scatter(final_df.index, final_df['value'],c=final_df['identifier'],)
# plt.plot(final_df.index, final_df['value'])
# plt.title("Spotted Outliers")
# plt.xlabel("Time")
# plt.ylabel("Value")
# plt.show()

def outlier_spotter():
    # fig = plt.figure()
    fig3, ax = plt.subplots()
    plt.scatter(final_df.index, final_df['value'],c=final_df['identifier'], s=15)
    plt.plot(final_df.index, final_df['value'])
    plt.title("Spotted Outliers")
    plt.xlabel("Time")
    plt.ylabel("Value")
    return fig3

first_fig = outlier_spotter()


#%%
outliers_removed = final_df.copy(deep=True)

outliers_removed = outliers_removed[outliers_removed['identifier'] == 'b']
third_fig = first_plot(outliers_removed)
#%%

def return_outliers():
    st.title('Outlier detection')
    
    st.markdown("""
                Imagine you have a dataset with the following data:\n              
                """)
    
    col1, col2, col3 = st.columns([1,2.5,1])
    col2.dataframe(data)

    st.markdown("""
                It is hard to spot wether something is wrong with this dataset by looking at it in a table manner. 
                Therefore, if we plot the data, something different becomes visible:         
                """)
    
    st.pyplot(fig1)
    st.markdown("""
                Several of these points are showing very strange values on the y-axis. 
                These can be spotted and filtered out by so called: Anomaly Detection algorithms.
                A simple anomaly detection algorithm applied here labels anomalies if they are outside a certain boundary.
                However, there are countless techniques to achieve this results, one more complex than the other.
                If you think that you dataset could benefit from removing outliers, consider removing them!              
                """)
    
    st.pyplot(first_fig)
    # st.pyplot(fig3)

    st.markdown("""
                The following Figure shows the same data, but with the outliers removed:        
                """)
    st.pyplot(third_fig)

    st.markdown("""
                A few observations can be made from this visualization. To start, the overall dynamics of the dataset have not changed. 
                Plenty of information is still available, only the outliers have been removed.        
                """)

    


    