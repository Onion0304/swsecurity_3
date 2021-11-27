# 1) 메뉴 출력 (def menu_prt)

def menu_prt(cam, cam_time, today, data) : # menu_prt(cam, cam_time, lines)
    # print(data[:3])
    # '요일,캠퍼스, 건물,식당,시간대,가격,메뉴,칼로리\n', 
    # '월요일,서울캠퍼스,310관,참슬기식당,중식,3200,"(일품1) 부대찌개, 스크램블에그, 숙주무침, 건파래볶음 ",680\n',

    """
    for i in range(len(data)):
        fst = data.find(',') # 첫 번째 ',' 찾기
        day = data[:fst]
        if (today == 1) : # 월요일 찾기
    """
    subject = [] # 대상 값 저장 

    while(True): # 요일로 해당하는 값을 찾기
        if (today == 1) : # 월요일
            for i in range(len(data)):
                fst = data[i].find(',') # 첫 번째 ',' 찾기
                day = data[:fst]
                if (day == "월요일"):
                    subject.append(data[i])
        
        elif (today == 2) : # 화요일
            for i in range(len(data)):
                fst = data[i].find(',') # 첫 번째 ',' 찾기
                day = data[:fst]
                if (day == "화요일"):
                    subject.append(data[i])
        
        elif (today == 3) : # 수요일
            for i in range(len(data)):
                fst = data[i].find(',') # 첫 번째 ',' 찾기
                day = data[:fst]
                if (day == "수요일"):
                    subject.append(data[i])

        elif (today == 4) : # 목요일
            for i in range(len(data)):
                fst = data[i].find(',') # 첫 번째 ',' 찾기
                day = data[:fst]
                if (day == "목요일"):
                    subject.append(data[i]) 

        elif (today == 5) : # 금요일
            for i in range(len(data)):
                fst = data[i].find(',') # 첫 번째 ',' 찾기
                day = data[:fst]
                if (day == "금요일"):
                    subject.append(data[i])

        elif (today == 6) : # 토요일
            for i in range(len(data)):
                fst = data[i].find(',') # 첫 번째 ',' 찾기
                day = data[:fst]
                if (day == "토요일"):
                    subject.append(data[i])

        elif (today == 7) : # 일요일
            for i in range(len(data)):
                fst = data[i].find(',') # 첫 번째 ',' 찾기
                day = data[:fst]
                if (day == "일요일"):
                    subject.append(data[i]) 
        else :
            print("잘못된 번호를 입력하셨습니다.\n")                                  
    

    subject2 = []

    while(True) :
        if (cam == 1) : #서울 캠퍼스
            for i in range(len(subject)) :
                snd = subject[i].find(',')
                cam = subject[:snd]
                if (cam == "서울캠퍼스"):
                    subject2.append(subject[i])
        
        if (cam == 2) : #안성 캠퍼스
            for i in range(len(subject)) :
                snd = subject[i].find(',')
                cam = subject[:snd]
                if (cam == "안성캠퍼스"):
                    subject2.append(subject[i])

        else :
            print("잘못된 번호를 입력하셨습니다.\n") 

    print("subject2 출력\n----------------------------------------------------")
    print(subject2)

    subject3 = []   

    while(True) :
        if (cam_time == 1) : #조식
            for i in range(len(subject)) :
                five = subject[i].find(',')
                cam = subject[:five]
                if (cam_time == "조식"):
                    subject3.append(subject[i])

        elif (cam_time == 2) : #중식
            for i in range(len(subject)) :
                five = subject[i].find(',')
                cam = subject[:five]
                if (cam_time == "중식"):
                    subject3.append(subject[i])

        elif (cam_time == 3) : #석식
            for i in range(len(subject)) :
                five = subject[i].find(',')
                cam = subject[:five]
                if (cam_time == "석식"):
                    subject3.append(subject[i])
        
        else :
            print("잘못된 번호를 입력하셨습니다.\n") 


"""
    for i in range(subject):
        # '월요일,서울캠퍼스,310관,참슬기식당,중식,3200,"(일품1) 부대찌개, 스크램블에그, 숙주무침, 건파래볶음 "
        # 
        print(str(i) + ") " + ) # 식당/메뉴/칼로리 출력~
"""