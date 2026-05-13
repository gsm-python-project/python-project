from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from CHARACTER import butterfly, volt, colombina, crow, moreta

class Mainfront(QStackedWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("가면 무도회") # 팝업창의 이름
        self.setFixedSize(1600, 900) #팝업창의 사이즈

        from page0 import prologue # import문, 각 챕터랑 엔딩을 불러온다.
        from page1 import Chapter1
        from page2 import Chapter2
        from ending import HappyEnding, BadEnding

        self.prologue = prologue(self) # 변수에 추가
        self.chapter1 = Chapter1(self)
        self.chapter2 = Chapter2(self)
        self.happyending = HappyEnding(self)
        self.badending = BadEnding(self)

        self.addWidget(self.prologue) # 페이지 추가 인덱스:0
        self.addWidget(self.chapter1) # 인덱스:1
        self.addWidget(self.chapter2) # 인덱스:2
        self.addWidget(self.happyending) # 인덱스:3
        self.addWidget(self.badending) # 인덱스:4

        self.setCurrentIndex(0) # 인덱스가 0인 페이지로 이동.


class App_default(QWidget):
    def __init__(self):
        super().__init__()


class Button(App_default): # 버튼. chapterr 1, chapter2에서 사용!
    def __init__(self):
        super().__init__()

        self.x = 1000 # 버튼의 가로 사이즈
        self.y = 80 # 버튼의 세로 사이즈/

        self.butterfly = QPushButton("나비", self) # 버튼 생성
        self.butterfly.setGeometry(50, 50, 1000, 80) # 버튼 사이즈, 위치 조절. 순서대로 x좌표 y좌표 가로사이즈, 세로사이즈.
        self.butterfly.clicked.connect(self.on_click_butterfly) # on_click_butterfly 함수에 연결.
        self.butterfly.setCursor(QCursor(Qt.PointingHandCursor)) # 커서 변경

        self.volt = QPushButton("볼트", self)
        self.volt.setGeometry(50, 140, 1000, 80)
        self.volt.clicked.connect(self.on_click_volt)
        self.volt.setCursor(QCursor(Qt.PointingHandCursor))

        self.colombina = QPushButton("콜롬비나", self)
        self.colombina.setGeometry(50, 230, self.x, self.y)
        self.colombina.clicked.connect(self.on_click_colombina)
        self.colombina.setCursor(QCursor(Qt.PointingHandCursor))

        self.crow = QPushButton("까마귀", self)
        self.crow.setGeometry(50, 320, self.x, self.y)
        self.crow.clicked.connect(self.on_click_crow)
        self.crow.setCursor(QCursor(Qt.PointingHandCursor))

        self.moreta = QPushButton("모레타", self)
        self.moreta.setGeometry(50, 410, self.x, self.y)
        self.moreta.clicked.connect(self.on_click_moreta)
        self.moreta.setCursor(QCursor(Qt.PointingHandCursor))

        self.cri1 = butterfly() # 변수에 butterfly 클래스 저장
        self.cri2 = volt()
        self.cri3 = colombina()
        self.npc1 = crow()
        self.npc2 = moreta()

    def on_click_butterfly(self): # 버튼과 그 버튼에 맞는 클래스의 communication(answer)과 연결.
        return self.cri1.communication()

    def on_click_volt(self):
        return self.cri2.communication()

    def on_click_colombina(self):
        return self.cri3.communication()

    def on_click_crow(self):
        return self.npc1.communication()

    def on_click_moreta(self):
        return self.npc2.communication()