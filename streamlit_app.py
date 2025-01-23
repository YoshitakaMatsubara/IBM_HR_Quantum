import streamlit as st
import pandas as pd
import ydata_profiling
from streamlit_pandas_profiling import st_profile_report
#from autogluon.tabular import TabularDataset, TabularPredictor

st.title("IBM HR dataset")
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")
st.write(df)

if st.button("探索的データ分析"):
    pr = df.profile_report()
    st_profile_report(pr)

# if st.button("機械学習"):
#     train_data = TabularDataset("WA_Fn-UseC_-HR-Employee-Attrition.csv")
#     label = "Attrition"
#     predictor = TabularPredictor(label=label).fit(train_data, time_limit=60)
#     y_pred = predictor.predict(train_data.drop(columns=[label]))
#     st.write(y_pred.head())