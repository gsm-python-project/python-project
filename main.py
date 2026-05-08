import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout

class Character: ## 캐릭터 기본 설정
    def __init__(self, age, name, communicationCount):
        self.age = age
        self.name= name
        self.communicationCount = communicationCount

    def communication(self): ## 여기서 대화 횟수를 확인하고 answer 함수로 넘어감
        if self.communicationCount>0:
            self.communicationCount-=1
            return self.answer()
        return self.answer_Fail()

    def answer(self):
        pass
        ## gemini 연결해서 창에 띄우기

    def answer_Fail(self):
        pass
        ## 오늘은 더이상 대화할 수 없습니다.<이런 안내멘트 띄워야함!
        

class butterfly(Character): ## 캐릭터 나비 가면 아직 구현 안됨
    def __init__(self, age, name, communicationCount):
        super().__init__(age, name, communicationCount)


class volt(Character): ## 캐릭터 볼트 아직 구현 안됨
    def __init__(self, age, name, communicationCount):
        super().__init__(age, name, communicationCount)


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("가면 무도회") # 창 이름
        self.setFixedSize(1100,800) # 창 사이즈, setFixedSize는 창 크기 수정이 불가능하게 만들어줌

        self.butterfly=QPushButton("나비",self) # 나비 버튼. 아직 UI 구현 안됨
        self.butterfly.setGeometry(50,50,1000,80)
        self.butterfly.clicked.connect(self.on_click_butterfly)

        self.volt=QPushButton("볼트", self) # 볼트 버튼. 아직 UI 구현 안됨
        self.volt.setGeometry(50,140,1000,80)
        self.volt.clicked.connect(self.on_click_volt)


        self.cri1 = butterfly(age=20, name="나비", communicationCount=5) # 캐릭터 불러오기
        self.cri2 = volt(age=20, name="volt", communicationCount=5)

    def on_click_butterfly(self): # 나비 버튼을 눌렀을 때 Character class의 communication 함수를 호출
        return self.cri1.communication()
    
    def on_click_volt(self):
        return self.cri2.communication()
        


app=QApplication(sys.argv) # 앱 관리자. 얘 없이 창만 만들면 오류남!
window=App() # 실제 앱
window.show()
sys.exit(app.exec()) # mainloop를 만듦. 창이 자기 맘대로 꺼지지 않게