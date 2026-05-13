from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from default import App_default

class prologue(App_default):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack

        self.btn_next_prologue = QPushButton("next", self)
        self.btn_next_prologue.setGeometry(50, 50, 250, 100)
        self.btn_next_prologue.clicked.connect(self.on_click_prologue)

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("black"))  # PyQt5는 ColorRole 네임스페이스 없이 사용
        self.setPalette(palette)

    def on_click_prologue(self):
        self.stack.setCurrentIndex(1)

    def prologue_end(self):
        self.btn_next_prologue.show()