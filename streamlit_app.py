import streamlit as st
import pandas as pd
import ydata_profiling
from streamlit_pandas_profiling import st_profile_report

st.title("IBM HR dataset")
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")
st.write(df)

if st.button("探索的データ分析"):
    pr = df.profile_report()
    st_profile_report(pr)