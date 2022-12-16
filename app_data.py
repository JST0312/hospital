import streamlit as st
import pandas as pd

def run_home_app() :
     df=pd.read_csv('data/hospcsv.csv')
     df=df.drop(columns=['인허가일자','소재지우편번호','폐업일자','특수구급차대수','일반구급차대수','인허가취소일자','소재지도로명주소','허가병상수'])
     st.dataframe(df)







