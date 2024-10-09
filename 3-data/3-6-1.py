import pandas as pd
import streamlit as st

def grade_attendance(participation: float) -> str:
    if participation == 0.0:
        return "AB"
    if participation <= 0.5:
        return "np"
    return "+" 

roster_url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/student_polls/roster.csv"
roster_df = pd.read_csv(roster_url)

polls = []
dates = ["2024-01-08", "2024-01-15", "2024-01-22", "2024-01-29"]
for date in dates:
    poll = f"https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/student_polls/poll-responses-{date}.csv"
    poll_df = pd.read_csv(poll)
    poll_df['date'] = date
    polls.append(poll_df)

polls_df = pd.concat(polls, ignore_index=True)

combined_df = pd.merge(roster_df, polls_df, how='left', left_on='netid', right_on='student_id')




poll_counts = combined_df.pivot_table(index='date', values='poll_num', aggfunc='max')

student_responses = combined_df.pivot_table(index='netid', columns='date', values='answer', aggfunc='count')
student_responses = student_responses.fillna(0)

for col in student_responses.columns:
    student_responses[col] = student_responses[col] / poll_counts.loc[col, 'poll_num']

for col in student_responses.columns:
    student_responses[col] = student_responses[col].apply(grade_attendance)

summary = student_responses.copy()
summary['sessions'] = len(summary.columns)
summary['AB'] = summary.apply(lambda row: row.value_counts().get('AB', 0), axis=1)
summary['np'] = summary.apply(lambda row: row.value_counts().get('np', 0), axis=1)
summary['%'] = ((summary['AB'] + summary['np']) / summary['sessions']) * 100
summary_with_names = pd.merge(roster_df, summary, left_on='netid', right_index=True)
st.title("Xavier Polling Report")
st.dataframe(summary_with_names)
st.download_button("Download Report", summary_with_names.to_csv(), "polling_report.csv", "text/csv")

