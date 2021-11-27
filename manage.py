# -1) 요일 지정 -> csv 요일만 
# 0) 마무리 (def finish)
# ----------------
# 1) 메뉴 삭제
# 2) 메뉴 추가
# 3) 식당 정보 삭제
# 4) 식당 정보 추가 
# 를 구현해야 하는데, 1234가 비슷할 것으로 예상됨.
# 진행 상황에 따라 여기는 유동적으로 function 변화 가능 
import time

def day():
    while(True):
        print("오늘의 요일을 선택해주세요.\n\n")
        print("1. 월요일\n")
        print("2. 화요일\n")
        print("3. 수요일\n")
        print("4. 목요일\n")
        print("5. 금요일\n")
        print("6. 토요일\n")
        print("7. 일요일\n")
        day_day = int(input("요일별 숫자를 입력해주세요.\n"))
        if (day_day > 0) and (day_day < 8):
            return day_day
        else :
            print("잘못된 번호를 입력하셨습니다.\n")

def finish():
    print("20초 뒤 초기 화면으로 이동합니다.")
    time.sleep(20)


"""
def menu_prt(lst, identifier): # 메뉴 출력을 위한 함수 
    if identifier == 0: # 메뉴 처음 출력하는 경우 
        idx = 0
        for i in range(len(lst)):
            print("%d. %s" % (i + 1, lst[i]))
            idx = i + 1
        return idx
        
    else: # 직전에 다른 리스트의 값을 출력했고, 연달아 출력하려는 경우
        for i in range(len(lst)):
            print("%d. %s" % (identifier + i + 1, lst[i]))
        return 
"""
