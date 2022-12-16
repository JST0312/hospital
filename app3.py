
import streamlit as st
from app_data import run_home_app
from app_from import run_from_app


def main():
    st.title('Hospital information')
    video_file = open('data/video.mp4' , 'rb')
    st.video(video_file)
    









menu =["메뉴를 선택하세요.",'Data','지역','병원']
choice = st.sidebar.selectbox('전국 경기도 병원 ',menu)   

    
if choice == 'Data' :
        run_home_app()
elif choice =='EDA' :
       pass
elif choice == 'ML' :
        pass










menu =["메뉴를 선택하세요.",'영업상태','지역','병원']  
choice = st.sidebar.selectbox('선택',menu)


   
   

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
  
if choice =='가평군' :
        run_from_app()
elif choice =='안산시' :
        run_from_app()
elif choice == 'ML' :
        pass
elif choice =='EDA' :
       pass
elif choice == 'ML' :
        pass










  

    
    
    





    


if __name__ == '__main__' :
        main()