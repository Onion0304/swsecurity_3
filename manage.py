# 1) 요일 설정 (def day)
# 2) 프로그램 마무리 - 초기 화면으로 이동 (def finish)
# 3) 메뉴 삭제 (def del_menu)
# 4) 메뉴 추가 (def add_menu)

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
    input("\n초기화면으로 돌아가시려면 enter를 눌러주세요.\n")


def del_menu(data):
    try:
        data.drop(['Unnamed: 0'], axis = 1, inplace = True) # pandas에서 자동생성되는 Unnamed: 0 컬럼 제거 
    except KeyError:
        print()

    week = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

    while(1):
        ans = input("삭제할 데이터의 요일을 입력하세요.")
        if ans not in week:
            continue
        else:
            break

    # 요일로 필터링된 데이터프레임 출력
    condition = (data.요일 == ans) 
    filtered = data[condition]
    while(1):
        if (len(filtered) == 0):
            print("해당하는 데이터가 없습니다.")
            break
        else:
            print(filtered) # 이용자에게 대상 데이터 보여주기 

        num = int(input("삭제할 행의 번호를 입력하세요."))

        ans = input(str(num) + "을 입력하셨습니다. 정말 삭제할까요? (Y/N)")
        if (ans == 'Y') or (ans == 'y'):
            new_data = data.drop([data.index[num]])
            print("삭제 후 메뉴 데이터를 출력합니다.")
            print(new_data)
            new_data.to_csv('./menu_info.csv')
            return
        else: 
            break


def add_menu(data):
    try:
        data.drop(['Unnamed: 0'], axis = 1, inplace = True) # pandas에서 자동생성되는 Unnamed: 0 컬럼 제거 
    except KeyError:
        print()

    print("추가할 데이터를 입력받겠습니다.\n")

    day = input("요일을 입력하세요 (ex.월요일)")
    campus = input("캠퍼스를 입력하세요 (ex.서울캠퍼스)")
    building = input("건물을 입력하세요 (ex.308관)")
    restaurant = input("식당을 입력하세요 (ex.참슬기식당)")
    mealtime = input("시간대를 입력하세요(ex.조식)")
    while(1):
        try:
            price = int(input("가격을 입력하세요(ex.3200)"))
        except ValueError:
            print("잘못된 타입의 값입니다. 다시 입력받겠습니다.")
            continue
        else:
            break
    menu = input("메뉴를 입력하세요")
    while(1):
        try:
            kcal = int(input("칼로리를 입력하세요(ex.800)"))
        except ValueError:
            print("잘못된 타입의 값입니다. 다시 입력받겠습니다.")
            continue
        else:
            break

    new_data = [day, campus, building, restaurant, mealtime, price, menu, kcal, 0] # 마지막 0은 '만족도' 초기화 값 
    print("새 데이터는 ", new_data)
    print(data.columns)
    data.loc[len(data)] = new_data  

    print(data)
    data.to_csv('./menu_info.csv')