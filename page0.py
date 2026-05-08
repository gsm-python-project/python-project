
from PyQt6.QtWidgets import QApplication, QStackedWidget, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
from CHARACTER import butterfly, volt, colombina
import sys
from default import App_default, Mainfront
from page1 import Chapter1
##여기에 처음 프롤로그처럼 상황 설명 하는 장면 만들기
class prologue(App_default):
    def __init__(self,stack):
        super().__init__()
        self.stack=stack
        self.Mainfront=Mainfront
        self.chapter1=Chapter1(self.Mainfront)

        self.btn_prologue = QPushButton("next", self) #버튼!
        self.btn_prologue.setGeometry(50,50,250,100)
        self.btn_prologue.clicked.connect(self.on_click_prologue)

    def on_click_prologue(self):
        self.stack.setCurrentIndex(1)



    

        