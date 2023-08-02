#Example
import threading
import time

class Test(threading.Thread):    #Treading.Tread를 상속받는 Test 클래스를 만든다
    def run(self):             #Tread를 실행시킬때에는 보통 run함수 코드가 실행된다
        while True:            #무한반복 한다
            print("hi")        #hi를 출력한다
            time.sleep(1)      #1초 기다림

if __name__ == "__main__":
    test = Test()
    test.start()               #Test클래스 실행
    print("test")

#이렇게 실행시켰을 경우 hi가 출력됨과 동시에 test가 출력된다
#그 후 1초 간격으로 hi가 출력되는걸 볼수있다
    
    