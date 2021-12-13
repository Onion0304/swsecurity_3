# 1) filter_day --> 요일 추출 후 결과물 출력 
# 2) menu_prt --> 캠퍼스, 시간대 추출 후 filter_day 실행 
# 코드가 반복되어서 함수를 분리했어요. 

def filter_day(today, data): # 요일 추출 
  arr_day=['월요일','화요일','수요일','목요일','금요일','토요일','일요일']

  for i in arr_day:
    if(i == arr_day[today-1]):
      filter_whichDay = data['요일'] == i
      data_day = data[filter_whichDay]
      if (len(data_day) == 0):
        print("현재 운영하지 않습니다.")
        return 1
      else:
        print(data_day.loc[:,['건물', '식당', '메뉴', '가격', '칼로리']])
        return 0
      #break


def menu_prt(cam, cam_time, today, data) : 
    arr_campus=['서울캠퍼스', '안성캠퍼스']
    arr_time=['조식','중식','석식']

    for i in arr_campus:
        if(i == arr_campus[cam-1]):
            filter_whichCam = data['캠퍼스'] == i  #서울캠(arr_campus[0]) or 안성캠(arr_campus[1])
            data_cam = data[filter_whichCam]
            
        for j in arr_time:
            if(j == arr_time[cam_time-1]):
                filter_whichTime = data_cam['시간대'] == j  #조식(arr_time[0]) or 중식(arr_time[1]) or 석식(arr_time[2])
                data_time = data_cam[filter_whichTime]
                idf = filter_day(today, data_time)
                return idf
   