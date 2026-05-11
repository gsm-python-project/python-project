
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from CHARACTER import butterfly, volt, colombina, crow, moreta

class Mainfront(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("가면 무도회") # 창 이름
        self.setFixedSize(1200,800) # 창 사이즈, setFixedSize는 창 크기 수정이 불가능하게 만들어줌

        from page0 import prologue
        from page1 import Chapter1
        from page2 import Chapter2
        from ending import EndingFront

        self.prologue = prologue(self) # chapter 호출
        self.chapter1 = Chapter1(self)
        self.chapter2 = Chapter2(self)
        self.ending = EndingFront()

        self.addWidget(self.prologue) #페이지 추가
        self.addWidget(self.chapter1)
        self.addWidget(self.chapter2)
        self.addWidget(self.ending)

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
        # butterfly.setCursor(QCursor(Qt.CursorShape.PointingHandCursor)) # 버튼 위에 마우스 커서 올리면 손모양으로 변경

        self.volt=QPushButton("볼트", self) # 볼트 버튼. 아직 UI 구현 안됨
        self.volt.setGeometry(50,140,1000,80)
        self.volt.clicked.connect(self.on_click_volt) # 버튼 클릭시 대화

        self.colombina=QPushButton("콜롬비나", self)
        self.colombina.setGeometry(50,230,self.x,self.y)
        self.colombina.clicked.connect(self.on_click_colombina)

        self.crow=QPushButton("까마귀", self)
        self.crow.setGeometry(50, 320, self.x, self.y)
        self.crow.clicked.connect(self.on_click_crow)

        self.moreta=QPushButton("모레타", self)
        self.moreta.setGeometry(50,410,self.x,self.y)
        self.moreta.clicked.connect(self.on_click_moreta)

        self.cri1 = butterfly() # 캐릭터 불러오기
        self.cri2 = volt()
        self.cri3 = colombina()
        self.npc1= crow()
        self.npc2 = moreta()

    def on_click_butterfly(self): # 나비 버튼을 눌렀을 때 Character class의 communication 함수를 호출
        print("test")
        return self.cri1.communication()
    
    def on_click_volt(self):
        print("volt")
        return self.cri2.communication()
    
    def on_click_colombina(self):
        print("colombia")
        return self.cri3.communication()
    
    def on_click_crow(self):
        return self.npc1.communication()
    
    def on_click_moreta(self):
        return self.npc2.communication()