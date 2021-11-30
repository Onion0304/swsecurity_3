# 1) 만족도 조사 (def satisfy) 
# 2) 랭킹 출력 (def rank_prt)

import pandas as pd
from choice import *
from menu import *

def satisfy(data) : # 만족도 조사 대상을 한정한 이후의 과정 

    while(1):
        ans = int(input("만족도를 평가할 메뉴의 번호를 입력하세요: "))

        if (ans < len(data)): # 만족도 조사 시행 
            while(1):
                print("\n만족도를 입력해주세요.\n")
                print("1. 별로에요\n")
                print("2. 보통이에요\n")
                print("3. 좋아요\n")

                score = int(input())

                if (score == 1) or (score == 2) or (score == 3) :
                    data.at[ans,'만족도'] += score # 만족도를 원본 데이터에 반영  
                    print("만족도를 평가해주셔서 감사합니다.\n")
                    #data.to_csv('./new_data_satisfy.csv') # 나중에 통일해야 
                    data.to_csv('./menu_result_sample.csv')
                    break

                else :
                    print("잘못된 번호를 입력하셨습니다.\n")
                
            break
            
        else:
            print("잘못된 번호를 입력하셨습니다.")


def rank_prt(cam, cam_time, today, data) :
    # rating_sample에는 만족도가 임의로 반영되어있음. 이전에 실행된 결과라고 가정한 것.

    # 캠퍼스 & 시간대 반영 
    arr_campus=['서울캠퍼스', '안성캠퍼스']
    arr_time=['조식','중식','석식']
    arr_day=['월요일','화요일','수요일','목요일','금요일','토요일','일요일']

    for i in arr_campus:
        if(i == arr_campus[cam-1]):
            filter_whichCam = data['캠퍼스 '] == i  #서울캠(arr_campus[0]) or 안성캠(arr_campus[1])
            data_cam = data[filter_whichCam]
            
        for j in arr_time:
            check_for_empty_1 = data_cam.empty
            if(check_for_empty_1 == True):
                print("그 날은 식사가 없습니다\n")
            else:
                if(j == arr_time[cam_time-1]):
                    filter_whichTime = data_cam['시간대'] == j  #조식(arr_time[0]) or 중식(arr_time[1]) or 석식(arr_time[2])
                    data_time = data_cam[filter_whichTime]

        for j in arr_day:
            check_for_empty_2 = data_time.empty
            if(check_for_empty_2 == True):
                print("그 날은 식사가 없습니다.\n")
                return
            else:
                if(j == arr_day[today-1]):
                    filter_whichDay = data_time['요일'] == j  #조식(arr_time[0]) or 중식(arr_time[1]) or 석식(arr_time[2])
                    data_day = data_time[filter_whichDay]
    
    # 내림차순 정렬
    rank = data_day.sort_values(by=["만족도"], ascending=[False]) 
    
    # 순위를 보여줄 것이므로 index reset
    rank = rank.reset_index(drop=True)
    rank.index = rank.index + 1
    print(rank)