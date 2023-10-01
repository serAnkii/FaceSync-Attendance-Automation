import streamlit as st

import pandas as pd

import time

from datetime import datetime

timeobj = time.time()
date = datetime.fromtimestamp(timeobj).strftime('%d-%m-%Y')

dataframe = pd.read_csv("attendence/attendence_ +" + str(date) +'.csv')

st.dataframe(dataframe.style.highlight_max(axis=0))

