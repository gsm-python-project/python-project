from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from CHARACTER import butterfly, volt, colombina
import sys
from default import Button

## 제 2장

class Chapter2(Button):
    def __init__(self, stack):
        super().__init__()
        self.stack=stack

        self.btn_next_Ending = QPushButton("엔딩 보러가기", self)
        self.btn_next_Ending.setGeometry(50,50,250,100)
        self.btn_next_Ending.clicked.connect(self.on_click_chapter2)

    def on_click_chapter2(self):
        self.stack.setCurrentIndex(3)

    