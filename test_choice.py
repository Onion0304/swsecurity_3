import unittest
from choice import *

class TddTest(unittest.TestCase) :

    def test_time(self): # Times 함수를 실행시키고, ans에 1 or 2 or 3을 입력했을 때 return이 1 or 2 or 3으로 제대로 나오지 않으면 오류---------
        time = times()

        test_time = [1, 2, 3]
        
        if time not in test_time:
            print("time은",time)
            print("Time should return 1, 2, 3 but it doesn't")
        else:
            print("정상적인 값을 입력받았습니다.")
            

    def test_campus(self): # Campus 함수를 실행시키고, ans에 1 or 2를 입력했을 때 return이 1 or 2로 제대로 나오지 않으면 오류---------------------
        cam = campus()

        test_campus = [1, 2]

        if campus not in test_campus:
            print("cam은", cam)
            print("Campus should return 1, 2 but it doesn't")


if __name__ == '__main__' :
    unittest.main()
