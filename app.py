import streamlit as st
import pandas as pd

st.title("IBM HR dataset")
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")
st.write(df)