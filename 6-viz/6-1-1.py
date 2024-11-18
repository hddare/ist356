## Challenge 6-1-1

'''Using the `data/mobile_user_behavior_dataset.csv` file, create a streamlit to show:

1. the data in a dataframe 
2. select a category: gender or operating system
3. select a measure: Data useage, battery drain, screen on time, or app useage time
4. show a bar plot of the average of 3. by 2.'''

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

mobile = pd.read_csv('./6-viz/data/mobile_user_behavior_dataset.csv')
st.write(mobile.columns)

category = st.selectbox("Select a category",
                        ["Operating System", "Gender"])
measure = st.selectbox("Select a measure",
                       ["App Usage Time (min/day)",
                        "Screen On Time (hours/day)", "Battery Drain (mAh/day)",
                        "Data Usage (MB/day)"])

plot, series = plt.subplots()
sns.barplot(data=mobile,
            x= category,
            y= measure,
            estimator= "mean",
            errorbar= None,
            ax= series)
st.pyplot(plot)