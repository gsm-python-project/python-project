from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from default import Button

class Chapter1(Button):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack

        self.btn_next_chapter1 = QPushButton("next1", self)
        self.btn_next_chapter1.setGeometry(50, 50, 250, 100)
        self.btn_next_chapter1.clicked.connect(self.on_click_chapter1)

    def on_click_chapter1(self):
        self.stack.setCurrentIndex(2)

    def chapter1_end(self):
        self.btn_next_chapter1.show()