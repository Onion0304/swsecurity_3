# 1) 식당 정보 출력 (def restaurant)
# 2) 식당 정보 삭제 (def del_info)
# 3) 식당 정보 추가 (def add_info)

def restaurant(data):
    print("식당 정보를 알려드리겠습니다.\n")
    print(data)
    

def del_info(data):
    try:
        data.drop(['Unnamed: 0'], axis = 1, inplace = True) # pandas에서 자동생성되는 Unnamed: 0 컬럼 제거 
    except KeyError:
        print()
        
    print(data)
    num = int(input("삭제할 행의 번호를 입력하세요.\n"))

    new_data = data.drop([data.index[num]])
    print(new_data)

    new_data.to_csv('./rest_info.csv')


def add_info(data):
    try:
        data.drop(['Unnamed: 0'], axis = 1, inplace = True) # pandas에서 자동생성되는 Unnamed: 0 컬럼 제거 
    except KeyError:
        print()

    print("추가할 데이터를 입력받겠습니다.\n")
    
    campus = input("캠퍼스를 입력하세요 (ex.서울캠퍼스):")
    restaurant = input("식당을 입력하세요 (ex.참슬기식당):")
    location = input("위치를 입력하세요(ex.310관 지하 4층):")
    breakfast = input("조식 운영 현황을 입력하세요(ex.7:00 ~ 9:00):")
    lunch = input("중식 운영 현황을 입력하세요(ex.11:00 ~ 14:00):")
    dinner = input("석식 운영 현황을 입력하세요(ex.17:30 ~ 18:20):")

    new_data = [campus, restaurant, location, breakfast, lunch, dinner]
    data.loc[len(data)] = new_data

    print(data)
    data.to_csv('./rest_info.csv')