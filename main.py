import csv
import time
import pandas as pd

from choice import *
from menu import *
from rank import * 
from info import *
from manage import *

data = pd.read_csv('C:/Users/ye303/Desktop/소프트웨어보안프로젝트/1127_prototype_수정/menu_including_rate.csv', encoding = 'utf-8')
infodata = pd.read_csv('C:/Users/ye303/Desktop/소프트웨어보안프로젝트/1127_prototype_수정/rest_info.csv', encoding = 'utf-8')

while(True): 
    # 프로그램 시작 ---------------------------------------------------------------------------
    print("알고싶은 메뉴를 선택하세요\n")
    print("1. 학식 메뉴\n")
    print("2. 학식 랭킹\n")
    print("3. 학식 만족도 조사\n")
    print("4. 식당 정보\n")
    print("5. 프로그램 종료\n")
    ans = int(input())

    if (ans == 1) : # 학식 메뉴 보여주기 ------------------------------------------------------
        cam = 0
        cam = campus() # 캠퍼스 선택
        cam_time = times() # 시간대(조식 / 중식 / 석식) 선택
        
        menu_prt(cam, cam_time, today, data)
        finish()
        

    elif (ans == 999) : # 관리자 모드 들어가기 ------------------------------------------------
        print("코드를 입력하세요.\n")
        manage_code = input()
        if (manage_code == "banana") : #관리자 모드 보안 acess 1 --------------------------------
            print("코드를 입력하세요.\n")
            manage_code2 = input()
            if (manage_code2 == "cat") : #관리자 모드 보안 acess 2 ------------------------------
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

                    if (ans == 1):  # 메뉴 삭제
                        del_menu(data)

                    else:  # 메뉴 추가 --> ans == 2인 경우
                        add_menu(data)

                elif (ans == 3):
                    # print(infodata)
                    print("\n원하시는 작업을 선택하세요.\n\n")
                    print("1. 식당 정보 삭제\n")
                    print("2. 식당 정보 추가\n")

                    ans = int(input())

                    if (ans == 1):  # 식당 정보 삭제
                        del_info(infodata)
                    else:  # 식당 정보 추가 --> ans == 2인 경우
                        add_info(infodata)
            else :
                break
        else :
            break



    elif (ans == 2) : # 랭킹 조회 ------------------------------------------------------------
        while(True):
            cam = 0
            cam_time = 0
            cam = campus()
            cam_time = times()
            rank_prt(cam, cam_time, today, data)
            finish()
            break
            
    elif (ans == 3) : # 만족도 조사 ----------------------------------------------------------
        while(1):
            answer = input("학식을 드셨나요? (yes/no) ")
            
            if (answer == "yes"): # 학식을 먹은 사람의 경우 만족도 조사 시행
                print("만족도 조사의 대상을 특정하겠습니다.")
                cam = 0
                cam_time = 0
                cam = campus()
                cam_time = times()
                menu_prt(cam, cam_time, today, data)
                satisfy(data)
                finish()
                break

            elif (answer == "no"): # 학식을 먹지 않은 사람의 경우 만족도 조사 참여 불가 
                print("학식을 먹은 뒤, 만족도 조사에 참여해주세요.")
                finish()
                break

            else: # 잘못된 입력
                print("yes 혹은 no로 대답해주세요.")



    elif (ans == 4) : # 식당 정보 보여주기 ----------------------------------------------------
        restaurant(infodata)
        finish()

    elif (ans == 5) : # 프로그램 종료하기 -----------------------------------------------------
        print("프로그램을 종료합니다.")
        exit(0)
    
    else : 
        print("잘못된 메뉴 번호를 선택하셨습니다.\n 번호를 다시 입력해주세요.\n\n")
    

