
from PyQt6.QtWidgets import QApplication, QStackedWidget, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
from CHARACTER import butterfly, volt, colombina
import sys
from default import App_default
from page1 import Chapter1

##여기에 처음 프롤로그처럼 상황 설명 하는 장면 만들기
class prologue(App_default):
    def __init__(self,stack):
        super().__init__()
        self.stack=stack # self.stack에 Mainfront 저장(왜냐면 Widget에는 화면 전환 기능이 없어서 Widstackedwidget을 불러와야하기 때문에!)
        self.chapter1=Chapter1(stack)

        self.btn_next_prologue = QPushButton("next", self) #버튼!
        
        self.btn_next_prologue.setGeometry(50,50,250,100) # 버튼 크기 설정
        self.btn_next_prologue.clicked.connect(self.on_click_prologue) # on_click_prologue 함수와 연결

    def on_click_prologue(self):
        self.stack.setCurrentIndex(1) # 인덱스가 1인 페이지로 이동



    

        