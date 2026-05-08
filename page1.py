from PyQt6.QtWidgets import QApplication, QStackedWidget, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
from CHARACTER import butterfly, volt, colombina
from default import Button
from page2 import Chapter2

class Chapter1(Button):
    def __init__(self, stack):
        super().__init__()
        self.stack=stack # self.stack에 Mainfront 저장(왜냐면 Widget에는 화면 전환 기능이 없어서 Widstackedwidget을 불러와야하기 때문에!)
        self.chapter2=Chapter2(stack) # Chapter2 불러오기

        self.btn_next_chapter1 = QPushButton("next1", self) # 버튼 생성
        self.btn_next_chapter1.setGeometry(50,50,250,100) # 버튼 크기 조절
        self.btn_next_chapter1.clicked.connect(self.on_click_chapter1) # on_click_chapter1 함수에 연결


    def on_click_chapter1(self):
        self.stack.setCurrentIndex(2) # 인덱스가 2인 페이지로 이동