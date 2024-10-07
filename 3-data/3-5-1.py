import pandas as pd
import streamlit as st
df = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv')
st.dataframe(df)
choices =['Made_Own_Study_Guide','Did_Exam_Prep Assignment','Studied_In_Groups']
selected = st.selectbox("Select One", choices)
grouped = df.groupby(selected).agg({'Student_Score':['count','mean']})
st.dataframe(grouped)
'''
Create a streamlit to allow the user to select one of the following:

- one of: Made_Own_Study_Guide, Did_Exam_Prep Assignment, Studied_In_Groups	
- after the selection is made display a dataframe that summarized the count of students and the average student score by the selection
'''