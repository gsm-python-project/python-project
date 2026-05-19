from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from default import Button, ClickableLabel

class Chapter1(Button):
    def __init__(self, stack, characters):
        super().__init__(characters)
        self.stack = stack

        # chapter2로 넘어가는 버튼 설정
        self.btn_next_chapter1 = ClickableLabel("image1.png", self) # 버튼 생성
        self.btn_next_chapter1.setGeometry(50, 50, 250, 100) # 버튼 크기 설정
        self.btn_next_chapter1.clicked.connect(self.on_click_chapter1) # 버튼을 on_click_chapter1이라는 함수에 연결.
        self.btn_next_chapter1.setCursor(QCursor(Qt.PointingHandCursor)) # 커서 변경

    def on_click_chapter1(self): # 인덱스가 2인 페이지로 넘어가게 해주는 함수.
        self.stack.setCurrentIndex(2)

    def chapter1_end(self): # chapter1이 끝났을때, 버튼을 보이게 하는 함수.
        self.btn_next_chapter1.show()