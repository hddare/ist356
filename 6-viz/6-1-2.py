


import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

mobile = pd.read_csv('./6-viz/data/mobile_user_behavior_dataset.csv')
st.dataframe(mobile)
