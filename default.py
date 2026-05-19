from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from CHARACTER import butterfly, volt, colombina, crow, moreta

class Mainfront(QStackedWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("가면 무도회") # 팝업창의 이름
        self.setFixedSize(1600, 900) #팝업창의 사이즈

        self.characters={
            "cri1" : butterfly(),
            "cri2":volt(), # 변수에 butterfly 클래스 저장
            "cri3" : colombina(),
            "npc1" : crow(),
            "npc2" : moreta()}
        

        from page0 import prologue # import문, 각 챕터랑 엔딩을 불러온다.
        from page1 import Chapter1
        from page2 import Chapter2
        from ending import HappyEnding, BadEnding

        self.prologue = prologue(self) # 변수에 추가
        self.chapter1 = Chapter1(self, self.characters)  # 캐릭터 넘겨주기
        self.chapter2 = Chapter2(self, self.characters)  # 캐릭터 넘겨주기
        self.happyending = HappyEnding(self)
        self.badending = BadEnding(self)
        

        self.addWidget(self.prologue) # 페이지 추가 인덱스:0
        self.addWidget(self.chapter1) # 인덱스:1
        self.addWidget(self.chapter2) # 인덱스:2
        self.addWidget(self.happyending) # 인덱스:3
        self.addWidget(self.badending) # 인덱스:4

        self.setCurrentIndex(0) # 인덱스가 0인 페이지로 이동.


class App_default(QWidget):
    # shared_history=[]
    def __init__(self):
        super().__init__()

class Button(App_default): # 버튼. chapterr 1, chapter2에서 사용!
    def __init__(self, characters):
        super().__init__()

        self.x = 100 # 버튼의 가로 사이즈
        self.y = 100 # 버튼의 세로 사이즈/

        self.butterfly = ClickableLabel("image1.png", self)
        self.butterfly.setGeometry(500,10,self.x, self.y)
        self.butterfly.clicked.connect(self.on_click_butterfly)
        self.butterfly.setCursor(QCursor(Qt.PointingHandCursor))

        self.volt = ClickableLabel("image.png",self) # "" 사이에 이미지 경로 넣기!
        self.volt.setGeometry(1000, 100, self.x, self.y)
        self.volt.clicked.connect(self.on_click_volt)
        self.volt.setCursor(QCursor(Qt.PointingHandCursor))

        self.colombina = ClickableLabel("image1.png", self) # "" 사이에 이미지 경로 넣기!
        self.colombina.setGeometry(50, 230, self.x, self.y)
        self.colombina.clicked.connect(self.on_click_colombina)
        self.colombina.setCursor(QCursor(Qt.PointingHandCursor))

        self.crow = ClickableLabel("image1.png", self)
        self.crow.setGeometry(50, 320, self.x, self.y)
        self.crow.clicked.connect(self.on_click_crow)
        self.crow.setCursor(QCursor(Qt.PointingHandCursor))

        self.moreta = ClickableLabel("image1.png", self)
        self.moreta.setGeometry(50, 410, self.x, self.y)
        self.moreta.clicked.connect(self.on_click_moreta)
        self.moreta.setCursor(QCursor(Qt.PointingHandCursor))

        self.cri1 = characters["cri1"]  # 새로 만들지 않고 받아서 사용
        self.cri2 = characters["cri2"]
        self.cri3 = characters["cri3"]
        self.npc1 = characters["npc1"]
        self.npc2 = characters["npc2"]


    def on_click_butterfly(self): # 버튼과 그 버튼에 맞는 클래스의 communication(answer)과 연결.
        return self.cri1.communication(self.question)

    def on_click_volt(self):
        return self.cri2.communication(self.question)

    def on_click_colombina(self):
        return self.cri3.communication(self.question)

    def on_click_crow(self):
        return self.npc1.communication(self.question)

    def on_click_moreta(self):
        return self.npc2.communication(self.question)

class ClickableLabel(QLabel): # 이미지 기본 설정 클래스
    clicked = pyqtSignal() #clicked 이벤트 재정의

    def __init__(self,image_path,parent = None):
        super().__init__(parent)
        pixmap = QPixmap(image_path) # pixmap 메소드로 imagepath 저장
        self.setPixmap(pixmap)
        self.setPixmap(pixmap.scaled(1000, 80, Qt.KeepAspectRatio)) # 크기
        
    def mousePressEvent(self, ev):
        if ev.button() == Qt.LeftButton:
            self.clicked.emit()