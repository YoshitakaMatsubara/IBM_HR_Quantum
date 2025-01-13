import streamlit as st
import pandas as pd
import ydata_profiling
from streamlit_pandas_profiling import st_profile_report

st.title("IBM HR dataset")
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")
# df_jp = df
# df_jp.columns = [
#     "年齢",
#     "離職",
#     "出張頻度",
#     "日給率",
#     "部署",
#     "自宅からの距離",
#     "学歴",
#     "専攻分野",
#     "従業員数",
#     "従業員番号",
#     "職場環境満足度",
#     "性別",
#     "時給",
#     "職務専念度",
#     "職位",
#     "職務役割",
#     "職務満足度",
#     "婚姻状況",
#     "月収",
#     "月給率",
#     "勤務経験のある会社数",
#     "18歳以上かどうか",
#     "残業",
#     "給与増加率",
#     "業績評価",
#     "人間関係満足度",
#     "標準労働時間",
#     "ストックオプションレベル",
#     "総勤務年数",
#     "昨年の研修回数",
#     "ワークライフバランス",
#     "会社での勤務年数",
#     "現在の役職での勤務年数",
#     "最終昇進からの年数",
#     "現在の上司との勤務年数"
# ]

st.write(df)
pr = df.profile_report()
st_profile_report(pr)