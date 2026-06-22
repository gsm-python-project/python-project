from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from default import Button, ClickableLabel

class Chapter2(Button):
    def __init__(self, stack, characters):
        super().__init__(stack,characters)
        self.stack = stack

        self.x=400
        self.y=300
        
        # 버튼 클릭 시 범인 후보 3명을 띄워줌.
        self.cri_slct = QPushButton("범인 선택하기", self) # 버튼 생성, 범인 선택하기를 누르면 다른 버튼들이 안 보이고 범인을 선택하는 창이 나타남.
        self.cri_slct.hide()
        self.cri_slct.setGeometry(1370, 765, 200, 100)
        self.cri_slct.clicked.connect(self.criminal_show)
        self.cri_slct.setCursor(QCursor(Qt.PointingHandCursor))

        # 범인 선택 후 네 를 클릭해야 넘어가짐(잘못 선택했을 때 바꿀 수 있도록!!)
        self.btn_next_Ending = QPushButton("네", self) # 버튼 생성, 범인을 클릭할 시에 나타남.
        self.btn_next_Ending.hide()
        self.btn_next_Ending.setGeometry(1380, 780, 200, 100)
        self.btn_next_Ending.clicked.connect(self.on_click_chapter2)
        self.btn_next_Ending.setCursor(QCursor(Qt.PointingHandCursor))

        # 범인 1,2,3은 임의로 넣어놓은 값이고 나중에 이름으로 바꿀 거임!
        # 버튼 클릭 시 3이나 4를 반환하여 엔딩을 가른다.
        self.btn_cri1 = ClickableLabel("butterfly.png", self) # 버튼 생성
        self.btn_cri1.hide()
        self.btn_cri1.setGeometry(50, 300, self.x, self.y)
        self.btn_cri1.clicked.connect(self.nocriminal)
        self.btn_cri1.setCursor(QCursor(Qt.PointingHandCursor))

        self.btn_cri2 = ClickableLabel("volt.png", self) # 버튼 생성
        self.btn_cri2.hide()
        self.btn_cri2.setGeometry(800, 300, self.x, self.y)
        self.btn_cri2.clicked.connect(self.criminal)
        self.btn_cri2.setCursor(QCursor(Qt.PointingHandCursor))

        self.btn_cri3 = ClickableLabel("colombina.png", self) # 버튼 생성
        self.btn_cri3.hide()
        self.btn_cri3.setGeometry(1300, 300, self.x, self.y)
        self.btn_cri3.clicked.connect(self.nocriminal)
        self.btn_cri3.setCursor(QCursor(Qt.PointingHandCursor))

        self.cri_slct.hide()
        self.butterfly.hide()
        self.colombina.hide()
        self.volt.hide()
        self.crow.hide()
        self.moreta.hide()
        self.subtitle.raise_()

        self.background.setPixmap(QPixmap("black.png").scaled(1600, 900))
        self.background.lower()  # 제일 뒤로
        
        
        self.messages = ["",
                        "당신은 흩어진 증거를 모아 퍼즐을 맞추어 가기 시작했다.",
                        "모든 증언은 부서진 유리 조각과 같다. 날카롭고 위험하며, 함부로 만졌다간 진실보다 먼저 상처를 입게 된다.",
                        "이제 진실은 질문 속에 있고, 정답은 교묘한 대답 뒤에 숨어 있다. 당신의 날카로운 추리력을 발현하여 정교하게 설계된 거짓말의 빈틈을 파고 들어 이 비극의 마침표를 찍을 진범을 가려내야 한다."]
        self._start_typing(self.q)

    def mousePressEvent(self, a0):
        if self.typing:
            self._finish_typing_immediately()
            return
        if self.q==0:
            self.background.setPixmap(QPixmap("black.png").scaled(1600, 900))
            self.background.lower()  # 제일 뒤로
        elif self.q==1:
            self.background.setPixmap(QPixmap("black.png").scaled(1600, 900))
            self.background.lower()  # 제일 뒤로
        elif self.q==3:
            self.background.setPixmap(QPixmap("background.png").scaled(1600, 900))
            self.background.lower()  # 제일 뒤로
            self.cri_slct.show()
            self.butterfly.show()
            self.colombina.show()
            self.volt.show()
            self.crow.show()
            self.moreta.show()
            self.subtitle.hide()

        self.q+=1
        self._start_typing(self.q)

    def showEvent(self, a0):
        super().showEvent(a0)
        if self.stack.currentWidget() is self:
            self.play_bgm("chapter1.mp3")
        
    def criminal_show(self): # 범인 선택 버튼 클릭시 실행
        self.btn_cri1.show() 
        self.btn_cri2.show()
        self.btn_cri3.show()
        self.cri_slct.deleteLater()
        self.butterfly.deleteLater()
        self.colombina.deleteLater()
        self.volt.deleteLater()
        self.crow.deleteLater()
        self.moreta.deleteLater()

    def criminal(self):
        self.result = 3 # result라는 변수에 3 저장
        return self.chapter2_end()

    def nocriminal(self):
        self.result = 4 # result라는 변수에 4 저장
        return self.chapter2_end()

    def on_click_chapter2(self):
        self.stop_bgm()
        self.stack.setCurrentIndex(self.result) # 위 저장 값에 따라 어떤 엔딩이 달라짐!!

    def chapter2_end(self):
        self.btn_next_Ending.show()