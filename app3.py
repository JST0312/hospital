
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px
import altair as alt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def main():
        pass
primaryColor="red"
backgroundColor="red"
secondaryBackgroundColor="red"
textColor="red"
font="sans serif"      
        
        
menu =['Home','Data','EDA','Map']
st.sidebar.title('상세정보')
choice = st.sidebar.selectbox('전국 경기도 병원🚑 ',menu) 









if choice=='Home':
        st.title('Hospital information')
        video_file = open('data/video1.mp4' , 'rb')
        st.video(video_file)



elif choice == 'Data' :
        st.image('https://media.istockphoto.com/id/1291088795/ko/%EC%82%AC%EC%A7%84/ems-%EA%B5%AC%EA%B8%89%EB%8C%80%EC%9B%90%ED%8C%80%EC%9D%80-%EB%B6%80%EC%83%81%EB%8B%B9%ED%95%9C-%ED%99%98%EC%9E%90%EC%97%90%EA%B2%8C-%EC%9D%98%EB%A3%8C-%EB%8F%84%EC%9B%80%EC%9D%84-%EC%A0%9C%EA%B3%B5%ED%95%98%EA%B3%A0-%EB%93%A4%EA%B2%83%EC%97%90-%EC%8B%A4%EB%A0%A4-%EA%B5%AC%EA%B8%89%EC%B0%A8%EC%97%90-%EC%8B%A4%EB%A0%A4-%EA%B7%B8%EB%A5%BC-%EB%8D%B0%EB%A0%A4%EC%98%A4%EA%B8%B0-%EC%9C%84%ED%95%B4-%EC%8B%A0%EC%86%8D%ED%95%98%EA%B2%8C-%EB%B0%98%EC%9D%91%ED%95%A9%EB%8B%88%EB%8B%A4-%EC%9D%91%EA%B8%89-%EC%B9%98%EB%A3%8C-%EC%A1%B0%EC%88%98%EB%8A%94-%EA%B1%B0%EB%A6%AC%EC%97%90%EC%84%9C-%EA%B5%90%ED%86%B5-%EC%82%AC%EA%B3%A0-%ED%98%84%EC%9E%A5%EC%97%90.jpg?s=612x612&w=0&k=20&c=-OH7ox9Nsh6dtqUga3NbfHIxB4WryAIBvdunKpzKiiU=')
        df = pd.read_csv('data/hospcsv.csv')
        st.dataframe(df)
elif choice =='EDA' :
       df = pd.read_csv('data/hospcsv.csv')
       st.subheader('데이터 프레임 확인')
       st.dataframe(df.head(3))

       st.subheader('기본 통계 데이터')
       st.dataframe(df.describe())
       st.image('https://media.istockphoto.com/id/911803146/ko/%EC%82%AC%EC%A7%84/%EA%B9%9C%EB%B0%95%EC%9D%B4-%EB%B6%88%EB%B9%9B%EA%B3%BC-%ED%95%A8%EA%BB%98-%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C-%EA%B5%AC%EA%B8%89%EC%B0%A8-%EB%B0%98.jpg?s=612x612&w=0&k=20&c=W4JcLUkU6kTTN2GLmI8NBazDb3sud043dddgolnlj_8=')
       st.subheader('최대 / 최소 데이터 확인하기')
       column_list = df.columns[17:22]
       selected_column=st.selectbox('컬럼을 선택하세요',column_list)
       min = df[df[selected_column]==df[selected_column].min() ]
       max = df[df[selected_column]==df[selected_column].max() ]
       st.text('최소 데이터')
       st.dataframe(min)
       st.text('최대 데이터')
       st.dataframe(max)
       
       selected_list = st.multiselect('원하는 컬럼을 선택하세요',df.columns)
    
    



elif choice == 'Map' :
        st.subheader('병원 분포 맵')
        df = pd.read_csv('data/hospcsv.csv')
        df=df.rename(columns={'위도':'lat','경도':'lon'})
        df2 = df.loc[ : , ['lat','lon']]
        st.map(df2,zoom=1)




        df = pd.read_csv('data/hospcsv.csv')
        st.subheader('각 지역별 병원 차트')
        fig6 = px.pie(df, '시군명',  title='병원 차트')
        st.plotly_chart(fig6)
        df = pd.read_csv('data/hospcsv.csv')   
        selected_list = st.multiselect('원하는 컬럼을 선택하세요',df.columns)
    
        if len(selected_list) == 0 :
                st.write('')
        else :
               st.dataframe(df[selected_list])








menu =["시군명를 선택하세요.",'안산시',     
 '고양시',     
 '부천시',     
 '수원시',     
 '용인시',    
 '성남시',     
 '시흥시',     
 '화성시',   
 '파주시',     
 '남양주시',     
 '의정부시',     
 '평택시',      
 '김포시',      
 '안양시',      
 '양주시',      
 '구리시',      
 '하남시',     
 '오산시',     
 '군포시',     
 '안성시',     
 '광명시',      
 '양평군',     
 '동두천시',    
 '이천시',     
 '광주시',      
 '포천시',     
 '의왕시',     
 '가평군',     
 '여주시',     
 '연천군',      
 '과천시'] 
choice = st.sidebar.selectbox('선택',menu)



if choice != '시군명를 선택하세요.': 
        df = pd.read_csv('data/hospcsv.csv')
        df=df.drop(columns=['인허가일자','소재지우편번호','폐업일자','특수구급차대수','일반구급차대수','인허가취소일자','소재지도로명주소','허가병상수'])
        st.dataframe(df[df['시군명'].isin([choice])]) 

elif choice =='메뉴':
        pass
    
    
   

elif choice=='병원':
        pass

  

   
   





menu =["메뉴를 선택하세요.",'영업중','폐업']  
choice = st.sidebar.selectbox('선택',menu)


if choice == '영업중':
        df = pd.read_csv('data/hospcsv.csv')
        df=df.drop(columns=['인허가일자','소재지우편번호','폐업일자','특수구급차대수','일반구급차대수','인허가취소일자','소재지도로명주소','허가병상수'])
        st.dataframe(df[df['영업상태명'].isin([choice])]) 
elif choice=='폐업':
        df = pd.read_csv('data/hospcsv.csv')
        df=df.drop(columns=['인허가일자','소재지우편번호','폐업일자','특수구급차대수','일반구급차대수','인허가취소일자','소재지도로명주소','허가병상수'])
        st.dataframe(df[df['영업상태명'].isin([choice])]) 
elif choice== '병원':
        pass





choice = st.sidebar.image('https://media.istockphoto.com/id/1185364077/ko/%EC%82%AC%EC%A7%84/%EA%B5%AC%EA%B8%89%EC%B0%A8.jpg?s=612x612&w=0&k=20&c=uQxdrE92SnKT35yLg9x8J1R8aWyR7HmdU9FqJGaPI30=')
choice=st.sidebar.image('https://media.istockphoto.com/id/673209194/ko/%EC%82%AC%EC%A7%84/%EB%9F%B0%EB%8D%98-%EC%8B%9C%EB%82%B4-%EB%B9%84%EC%83%81.jpg?s=612x612&w=0&k=20&c=RczUpqd_u6bZNFuC-BUCIsKWYKoJOJcI4lCre6RtwCY=')
choice=st.sidebar.image('https://media.istockphoto.com/id/1227544902/ko/%EC%82%AC%EC%A7%84/%EB%AF%B8%EA%B5%AD-%EC%9D%91%EA%B8%89-%EA%B5%AC%EA%B8%89%EC%B0%A8.jpg?s=612x612&w=0&k=20&c=RsD0kXIW_M3LK0skSYaIhv33829wvOnBjBfln4uqYRU=')





#시군명별로 그래프 만들기 

if __name__ == '__main__' :
        main()