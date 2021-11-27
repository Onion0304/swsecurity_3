# 1) 캠퍼스 선택 (def campus)
# 2) 시간대 선택(def times)

def campus() :
    while(True) : 
        print("캠퍼스를 선택해 주세요.\n\n")
        print("1. 서울 캠퍼스\n")
        print("2. 안성 캠퍼스\n")

        ans = int(input())
    
        if (ans == 1) or (ans == 2) :
            return ans
        else :
            print("잘못된 번호를 입력하셨습니다.\n")


def times() :
    while(True) :
        print("시간대를 선택해 주세요.\n\n")
        print("1. 조식\n")
        print("2. 중식\n")
        print("3. 석식\n")
        
        ans = int(input())

        if (ans == 1) or (ans == 2) or (ans == 3) :
            return ans
        else :
            print("잘못된 번호를 입력하셨습니다.\n")