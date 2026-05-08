
from PyQt6.QtWidgets import QApplication, QStackedWidget, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
from CHARACTER import butterfly, volt, colombina
import sys

class Mainfront(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("가면 무도회") # 창 이름
        self.setFixedSize(1100,800) # 창 사이즈, setFixedSize는 창 크기 수정이 불가능하게 만들어줌

        from page0 import prologue
        from page1 import Chapter1
        from page2 import Chapter2

        self.prologue = prologue(self) # chapter 호출
        self.chapter1 = Chapter1(self)
        self.chapter2 = Chapter2()

        self.addWidget(self.prologue) #페이지 추가
        self.addWidget(self.chapter1)
        self.addWidget(self.chapter2)

        self.setCurrentIndex(0) #0번 인덱스(self.prologue)로 이동


class App_default(QWidget):
    def __init__(self):
        super().__init__()

class Button(App_default):
    def __init__(self):
        super().__init__()

        self.x=1000
        self.y=80
        self.butterfly=QPushButton("나비",self) # 나비 버튼. 아직 UI 구현 안됨
        self.butterfly.setGeometry(50,50,1000,80)
        self.butterfly.clicked.connect(self.on_click_butterfly)

        self.volt=QPushButton("볼트", self) # 볼트 버튼. 아직 UI 구현 안됨
        self.volt.setGeometry(50,140,1000,80)
        self.volt.clicked.connect(self.on_click_volt)

        self.colombina=QPushButton("콜롬비나", self)
        self.colombina.setGeometry(50,230,self.x,self.y)
        self.colombina.clicked.connect(self.on_click_colombina)

        self.cri1 = butterfly(age=20, name="나비", communicationCount=5) # 캐릭터 불러오기
        self.cri2 = volt(age=20, name="volt", communicationCount=5)
        self.cri3 = colombina(age=20, name="colombina", communicationCount=5)

    def on_click_butterfly(self): # 나비 버튼을 눌렀을 때 Character class의 communication 함수를 호출
        return self.cri1.communication()
    
    def on_click_volt(self):
        return self.cri2.communication()
    
    def on_click_colombina(self):
        return self.cri3.communication()
        
