import pandas as pd
import numpy as np
import streamlit as st
import re
url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/webtraffic.log"
data = pd.read_csv(url, sep=" ", header=0, skiprows=3)
slow_ok = (data['time-taken']>500)&(data['sc-status']==200)
st.dataframe(data[slow_ok])