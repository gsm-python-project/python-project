from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import google.generativeai as genai
from CHARACTER import butterfly, volt, colombina, crow, moreta

model = genai.GenerativeModel

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
    shared_history=[]
    def __init__(self):
        super().__init__()

        genai.configure(api_key="API 키 입력하기")
        self.Model= genai.GenerativeModel(
            model_name="모델 명 입력",
            system_instruction=""
        )

class Button(App_default): # 버튼. chapterr 1, chapter2에서 사용!
    def __init__(self):
        super().__init__()

        self.x = 200 # 버튼의 가로 사이즈
        self.y = 200 # 버튼의 세로 사이즈/

        self.butterfly = ClickableLabel("image1.png", self)
        self.butterfly.setGeometry(500,10,self.x, self.y)
        self.butterfly.clicked.connect(self.on_click_butterfly)
        self.butterfly.setCursor(QCursor(Qt.PointingHandCursor))

        self.volt = ClickableLabel("image1.png",self) # "" 사이에 이미지 경로 넣기!
        self.volt.setGeometry(50, 100, self.x, self.y)
        self.volt.clicked.connect(self.on_click_colombina)
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