# 1) filter_day --> 요일 추출 후 결과물 출력 
# 2) menu_prt --> 캠퍼스, 시간대 추출 후 filter_day 실행 
# 코드가 반복되어서 함수를 분리했어요. 

def filter_day(today, data): # 요일 추출 
    if (today == 1): # 월요일 추출
            filter3 = data['요일'] == '월요일'
            data4 = data[filter3]
            print(data4.loc[:,['건물', '식당', '메뉴', '가격', '칼로리']])
            return 
        
    elif (today == 2): # 화요일 추출
            filter3 = data['요일'] == '화요일'
            data4 = data[filter3]
            print(data4.loc[:,['건물', '식당', '메뉴', '가격', '칼로리']])
            return
        
    elif (today == 3): # 수요일 추출
            filter3 = data['요일'] == '수요일'
            data4 = data[filter3]
            print(data4.loc[:,['건물', '식당', '메뉴', '가격', '칼로리']])
            return
        
    elif (today == 4): # 목요일 추출
            filter3 = data['요일'] == '목요일'
            data4 = data[filter3]
            print(data4.loc[:,['건물', '식당', '메뉴', '가격', '칼로리']])
            return
        
    elif (today == 5): # 금요일 추출
            filter3 = data['요일'] == '금요일'
            data4 = data[filter3]
            print(data4.loc[:,['건물', '식당', '메뉴', '가격', '칼로리']])
            return
        
    elif (today == 6): # 토요일 추출
            filter3 = data['요일'] == '토요일'
            data4 = data[filter3]
            print(data4.loc[:,['건물', '식당', '메뉴', '가격', '칼로리']])
            return
        
    else: # 일요일 추출
            filter3 = data['요일'] == '일요일'
            data4 = data[filter3]
            print(data4.loc[:,['건물', '식당', '메뉴', '가격', '칼로리']])
            return
        


def menu_prt(cam, cam_time, today, data) : 
    if (cam == 1): # 서울캠 추출 
        filter = data['캠퍼스 '] == '서울캠퍼스'
        data2 = data[filter]
        
        if (cam_time == 1): # 조식 추출
            filter2 = data2['시간대'] == '조식'
            data3 = data2[filter2]
            filter_day(today, data3)
           
        elif (cam_time == 2): # 중식 추출
            filter2 = data2['시간대'] == '중식'
            data3 = data2[filter2]
            filter_day(today, data3)
            
        else: # 석식 추출
            filter2 = data2['시간대'] == '석식'
            data3 = data2[filter2]
            filter_day(today, data3)
            
    else: # cam == 2일 경우, 안성캠 데이터 필터링
        filter = data['캠퍼스 '] == '안성캠퍼스'
        data2 = data[filter]
        
        if (cam_time == 1): # 조식 추출
            filter2 = data2['시간대'] == '조식'
            data3 = data2[filter2]
            filter_day(today, data3)
           
        elif (cam_time == 2): # 중식 추출
            filter2 = data2['시간대'] == '중식'
            data3 = data2[filter2]
            filter_day(today, data3)
            
        else: # 석식 추출
            filter2 = data2['시간대'] == '석식'
            data3 = data2[filter2]
            filter_day(today, data3)