import unittest
from rank import *

class TddTest(unittest.TestCase) :

    def test_satisfy(self): # Satisfy 함수를 실행시키고, ans에 1 or 2 or 3을 입력했을 때 return이 1 or 2 or 3으로 제대로 나오지 않으면 오륲---------
        satisfy_choice = satisfy(data)

        test_satisfy = [1, 2, 3]

        if satisfy_choice not in test_satisfy:
            print("satisfy_choice은", satisfy_choice)
            print("satisfy_choice should return 1, 2, 3 but it doesn't")
        else:
            print("정상적인 값을 입력받았습니다.")