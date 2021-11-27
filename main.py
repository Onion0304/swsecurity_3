from menu import *
from restaurant import *
from rank import *
"""
서울/안성 --> 조/중/석식
[1] 서울 [1][1]조 [1][2] 중 [1][3] 석
[2] 안성 [2][1]조 [2][2] 중 [2][3] 석

1) 3차원으로 간다. --> [][][]
2) 식당별로 나눈다. 서울&참슬기 / 서울&긱식 / 안성 

menu_sol --> [1] 참슬기 [2] 긱식 [~][0] 식당&조식 [~][1] 식당&중식 [~][2] 식당&석식 
menu_ans --> [1] 안성식당 [2] blank [~][0] 식당&조식 [~][1] 식당&중식 [~][2] 식당&석식 

==> ranking에도 적용 
rank_sol 
rank_ans
얘네는 위랑 구성 똑같고, 컨텐츠만 integer 0으로 초기화 
"""

# menu --> 서울/안성 메뉴 제공
menu = [["참슬기 중식","만두"], ["기숙사 조식","떡볶이"], ["기숙사 중식","고기"], ["기숙사 석식","마라탕"] , ["안성캠 중식","음"]] # 메뉴 수정해야
menu_sol = [[[], ["참슬기 중식","만두"], []], # 참슬기 --> 중식만 제공
            [["기숙사 조식","떡볶이"], ["기숙사 중식","고기"], ["기숙사 석식","마라탕"]]] # 긱식 --> 조/중/석식 모두 제공
menu_ans = [[], ["안성캠 중식","음"], []] # 안성 --> 중식만 제공 

# ranking --> 서울/안성 랭킹 제공
ranking = [[0,0], [0,0], [0,0], [0,0] , [0,0]] # 0으로 초기화 
rank_sol = [[[], [0,0], []], # 참슬기 --> 중식만 제공
            [[0,0], [0,0], [0,0]]] # 긱식
rank_ans = [[], [0,0], []] # 안성 

while(True):
    print("알고싶은 메뉴를 선택하세요\n")
    print("1. 서울캠퍼스 학식\n")
    print("2. 안성캠퍼스 학식\n")
    print("3. 식당 위치/운영시간\n")
    choice = int(input())

    if (choice == 1):
        while(True):
            print("서울캠퍼스 학식을 선택하셨습니다. \n")
            print("학식 시간대를 선택하세요\n")
            print("1. 조식\n")
            print("2. 중식\n")
            print("3. 석식\n")
            choice = int(input())
            if (choice == 1): 
                menu_prt(menu_sol[0][choice-1]) # 메뉴 출력
                print(menu_sol[0][choice-1])
                print("보기위함")
                menu_prt(menu_sol[1][choice-1]) # 메뉴 출력
                
                while(True):
                    choice = input("만족도 조사를 하시려면 해당 메뉴의 숫자 입력, \n메뉴 랭킹을 보시려면 # 입력, \n프로그램을 종료하시려면 0 입력")
                    
                    if choice == '#':
                        print("랭킹출력해야")
                        break
                        # 랭킹
                    elif choice == '0':
                        print("종료해야")
                        break
                        # 종료
                    else: # 만족도 조사 
                        if (int(choice) < int(len(menu_sol[0][choice-1])) + int(len(menu_sol[1][choice-1]))) or (int(choice) > int(len(menu_sol[0][choice-1])) + int(len(menu_sol[1][choice-1]))): # 메뉴 길이 밖
                            print("다시 입력하세요.\n")
                        else:             
                            print("오늘의 학식은 어떠셨나요?\n\n")
                            print("1. 별로에요\n2. 보통이에요\n3. 좋아요\n")
                            score = int(input())
                            #ranking[1][idx] += score --> 수정해ㅑㅇ 


                            
                break
            elif (choice == 2):
                #idx = menu_prt(menu[0]) # 메뉴 출력
                #idx = menu_prt(menu[2]) # 메뉴 출력
                menu_prt(menu_sol[0][choice-1]) # 메뉴 출력
                menu_prt(menu_sol[1][choice-1]) # 메뉴 출력
                break
            elif (choice == 3):
                #idx = menu_prt(menu[3]) # 메뉴 출력
                menu_prt(menu_sol[0][choice-1]) # 메뉴 출력
                menu_prt(menu_sol[1][choice-1]) # 메뉴 출력
                break
            else:
                print("잘못된 동작입니다.\n")
                continue

        break
    elif (choice == 2):
        while(True):
            print("안성캠퍼스 학식을 선택하셨습니다. \n")
            print("학식 시간대를 선택하세요\n")
            print("1. 조식 (운영하지 않습니다)\n")
            print("2. 중식\n")
            print("3. 석식 (운영하지 않습니다)\n")
            choice = int(input())
            if (choice == 2): 
                #idx = menu_prt(menu[4]) # 메뉴 출력
                menu_prt(menu_sol[1][choice-1]) # 메뉴 출력
                break
            else:
                print("운영하지 않습니다.\n")
                continue
        break
    elif (choice == 3):
        info()
        break
    else:
        print("잘못된 동작입니다.\n")
        continue




