import pandas as pd
import streamlit as st

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv"
df = pd.read_csv(url)

column_selections = ['Class_Section', 'Exam_Version', 'Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups','Letter_Grade']
row_selection = st.selectbox("Select a row: ", column_selections)
if row_selection in column_selections:
    column_selections.remove(row_selection)
column_selection = st.selectbox("Select a column: ", column_selections)
measure_selection = st.selectbox('Select a measure: ', ['Completion_Time','Student_Score'])
df_pivot = df.pivot_table(index=row_selection, columns=column_selection, values=measure_selection, aggfunc='mean')
st.dataframe(df_pivot)

