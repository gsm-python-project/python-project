from PyQt6.QtWidgets import QApplication, QStackedWidget, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
from CHARACTER import butterfly, volt, colombina
import sys
from default import Button
from page2 import Chapter2

class Chapter1(Button):
    def __init__(self, stack):
        super().__init__()
        self.stack=stack
        self.chapter2=Chapter2()
        self.btn_chapter1 = QPushButton("next", self)
        self.btn_chapter1.clicked.connect(self.on_click_chapter1)
        self.btn_chapter1.setGeometry(50,50,250,100)

    def on_click_chapter1(self):
        self.stack.setCurrentIndex(2)