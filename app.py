import streamlit as st
import pandas as pd
import numpy as np
def main():
    st.title('경기도 병원 정보')



       
    menu = ['홈','지역','병원']
    choice = st.sidebar.selectbox('메뉴',menu)
    st.title('Uber pickups in NYC')

    if st.button("click button"):
      
      
      add_selectbox = st.sidebar.selectbox("병원 검색", ("시군명", "병원이름", "전화번호"))



    


if __name__ == '__main__' :
    main()