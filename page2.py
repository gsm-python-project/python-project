from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from default import Button, ClickableLabel

class Chapter2(Button):
    def __init__(self, stack, characters):
        super().__init__(characters)
        self.stack = stack

        # 버튼 클릭 시 범인 후보 3명을 띄워줌.
        self.cri_slct = QPushButton("범인 선택하기", self) # 버튼 생성, 범인 선택하기를 누르면 다른 버튼들이 안 보이고 범인을 선택하는 창이 나타남.
        # self.cri_slct.hide()
        self.cri_slct.setGeometry(50, 140, self.x, self.y)
        self.cri_slct.clicked.connect(self.criminal_show)
        self.cri_slct.setCursor(QCursor(Qt.PointingHandCursor))

        # 범인 선택 후 네 를 클릭해야 넘어가짐(잘못 선택했을 때 바꿀 수 있도록!!)
        self.btn_next_Ending = QPushButton("네", self) # 버튼 생성, 범인을 클릭할 시에 나타남.
        self.btn_next_Ending.hide()
        self.btn_next_Ending.setGeometry(50, 50, 250, 100)
        self.btn_next_Ending.clicked.connect(self.on_click_chapter2)
        self.btn_next_Ending.setCursor(QCursor(Qt.PointingHandCursor))

        # 범인 1,2,3은 임의로 넣어놓은 값이고 나중에 이름으로 바꿀 거임!
        # 버튼 클릭 시 3이나 4를 반환하여 엔딩을 가른다.
        self.btn_cri1 = ClickableLabel("image1.png", self) # 버튼 생성
        self.btn_cri1.hide()
        self.btn_cri1.setGeometry(50, 210, self.x, self.y)
        self.btn_cri1.clicked.connect(self.nocriminal)
        self.btn_cri1.setCursor(QCursor(Qt.PointingHandCursor))

        self.btn_cri2 = ClickableLabel("image1.png", self) # 버튼 생성
        self.btn_cri2.hide()
        self.btn_cri2.setGeometry(50, 360, self.x, self.y)
        self.btn_cri2.clicked.connect(self.nocriminal)
        self.btn_cri2.setCursor(QCursor(Qt.PointingHandCursor))

        self.btn_cri3 = ClickableLabel("image1.png", self) # 버튼 생성
        self.btn_cri3.hide()
        self.btn_cri3.setGeometry(50, 510, self.x, self.y)
        self.btn_cri3.clicked.connect(self.criminal)
        self.btn_cri3.setCursor(QCursor(Qt.PointingHandCursor))

    def criminal_show(self): # 범인 선택 버튼 클릭시 실행
        self.btn_cri1.show() 
        self.btn_cri2.show()
        self.btn_cri3.show()
        self.cri_slct.hide()
        self.butterfly.hide()
        self.colombina.hide()
        self.volt.hide()
        self.crow.hide()
        self.moreta.hide()

    def criminal(self):
        self.result = 3 # result라는 변수에 3 저장
        return self.chapter2_end()

    def nocriminal(self):
        self.result = 4 # result라는 변수에 4 저장
        return self.chapter2_end()

    def on_click_chapter2(self):
        self.stack.setCurrentIndex(self.result) # 위 저장 값에 따라 어떤 엔딩이 달라짐!!

    def chapter2_end(self):
        self.btn_next_Ending.show()