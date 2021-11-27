# 1) 만족도 조사 (def satisfy) 
# 2) 랭킹 출력 (def rank_prt)

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
                    data.to_csv('./new_data_satisfy.csv') # 나중에 통일해야 
                    break

                else :
                    print("잘못된 번호를 입력하셨습니다.\n")
                
            break
            
        else:
            print("잘못된 번호를 입력하셨습니다.")
