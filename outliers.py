import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 
import matplotlib.pyplot as plt 
# from sklearn.neighbors import LocalOutlierFactor

data = pd.read_csv('https://raw.githubusercontent.com/DHI/tsod/main/tests/data/example.csv')
data.to_csv('data/anomaly.csv', index=None)
fig = plt.plot(data['value'])

fig, ax = plt.subplots()
ax.plot(data['value'])


# new plot with anomalies

data = pd.read_csv('https://raw.githubusercontent.com/DHI/tsod/main/tests/data/example.csv')
q_low = data["value"].quantile(0.05)
q_hi  = data["value"].quantile(0.95)

df_filtered = data[(data["value"] < q_hi) & (data["value"] > q_low)]
df_filtered['identifier'] = 'b'


##
og_set = set(data.index.to_list())
new_set = set(df_filtered.index.tolist())
og_set - new_set

filtered_df_values = pd.DataFrame(data.loc[og_set - new_set])
filtered_df_values = filtered_df_values.sort_values('datetime')
filtered_df_values['identifier'] = 'r'
final_df = df_filtered.combine_first(filtered_df_values)

##
fig2, ax = plt.subplots()
ax.scatter(data=final_df, x='datetime', y='value', c='identifier', cmap='Set3')
ax.set(title='', xlabel='Time', ylabel='')

ax.axes.xaxis.set_ticklabels([0,20,40,60,80,100,120])
ax.set_xticks([0,20,40,60,80,100,120])




def return_outliers():
    st.title('Outlier detection')
    
    st.markdown("""
                Imagine you have a dataset with the following data:
                There could be anomalies here.
                
                """)
    st.dataframe(data)
    st.pyplot(fig)
    st.pyplot(fig2)

    


    