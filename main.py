import csv
import time
import pandas as pd
from choice import *
from menu import *
from rank import * 
from info import *
from manage import *

f = open('C:/Users/ye303/Desktop/소프트웨어보안프로젝트/3조_prototype/menu_contents.csv', 'r', encoding='utf-8')
lines = f.readlines()    
f.close()
# 메뉴 파일 입출력 관련 수작업 부분(?) 전부 pandas로 대체 

data = pd.read_csv('C:/Users/ye303/Desktop/소프트웨어보안프로젝트/3조_prototype/menu_contents.csv', encoding = 'utf-8')

while(True): 
    # 프로그램 시작 ---------------------------------------------------------------------------
    print("알고싶은 메뉴를 선택하세요\n")
    print("1. 학식 메뉴\n")
    print("2. 학식 랭킹\n")
    print("3. 학식 만족도 조사\n")
    print("4. 식당 정보\n")
    print("5. 프로그램 종료\n")
    ans = int(input())

    if (ans == 1) : # 학식 메뉴 보여주기
        cam = 0
        cam = campus() # 캠퍼스 선택
        cam_time = times() # 시간대(조식 / 중식 / 석식) 선택
        
        menu_prt(cam, cam_time, today, lines)

    elif (ans == 999) : # 관리자 모드 들어가기
        print("진입할 메뉴를 선택하세요. \n\n")
        print("1. 요일 설정\n")
        print("2. 메뉴 수정\n")
        print("3. 식당 수정\n")

        ans = int(input())

        if (ans == 1):
            today = day()
        elif (ans == 2):
            print("원하시는 메뉴를 선택하세요.\n\n")
            print("1. 메뉴 삭제\n")
            print("2. 메뉴 추가\n")

            ans = int(input())

            if (ans == 1): # 메뉴 삭제
                del_menu(data)

            else: # 메뉴 추가 --> ans == 2인 경우 
                add_menu(data)

        # elif (ans == 3):
            # 

    elif (ans == 4) : # 식당 정보 보여주기
        print(restaurant)

    elif (ans == 5) : # 프로그램 종료하기
        exit(0)
    
    else : 
        print("잘못된 메뉴 번호를 선택하셨습니다.\n 번호를 다시 입력해주세요.\n\n")
    

