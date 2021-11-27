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

def del_menu(data):
    """
    - 데이터 받아와서
    - 삭제를 함
    - 원본 데이터(인 척하는 복사본을 만듭시다.)
    """
    ans = input("삭제할 데이터의 요일을 입력하세요.")

    # 요일로 필터링된 데이터프레임 출력
    condition = (data.요일 == ans) 
    filtered = data[condition]
    print(filtered)

    num = int(input("삭제할 행의 번호를 입력하세요."))

    new_data = data.drop([data.index[num]])
    print(new_data)

    data.to_csv('./new_data.csv')

def add_menu(data):
    print("추가할 데이터를 입력받겠습니다.\n")
    
    day = input("요일을 입력하세요 (ex.월요일)")
    campus = input("캠퍼스를 입력하세요 (ex.서울캠퍼스)")
    building = input("건물을 입력하세요 (ex.308관)")
    restaurant = input("식당을 입력하세요 (ex.참슬기식당)")
    mealtime = input("시간대를 입력하세요(ex.조식)")
    price = int(input("가격을 입력하세요(ex.3200)"))
    menu = input("메뉴를 입력하세요")
    kcal = int(input("칼로리를 입력하세요(ex.800)"))
    
    print(data.columns)

    new_data = [day, campus, building, restaurant, mealtime, price, menu, kcal]
    data.loc[len(data)] = new_data #['아이린',26,160]

    print(data)
    data.to_csv('./new_data2.csv')




