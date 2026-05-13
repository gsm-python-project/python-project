from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from default import Button

class Chapter2(Button):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack

        self.cri_slct = QPushButton("범인 선택하기", self)
        self.cri_slct.hide()
        self.cri_slct.setGeometry(50, 140, self.x, self.y)
        self.cri_slct.clicked.connect(self.criminal_show)

        self.btn_next_Ending = QPushButton("네", self)
        self.btn_next_Ending.hide()
        self.btn_next_Ending.setGeometry(50, 50, 250, 100)
        self.btn_next_Ending.clicked.connect(self.on_click_chapter2)

        self.btn_cri1 = QPushButton("범인1", self)
        self.btn_cri1.hide()
        self.btn_cri1.setGeometry(50, 210, self.x, self.y)
        self.btn_cri1.clicked.connect(self.nocriminal)

        self.btn_cri2 = QPushButton("범인2", self)
        self.btn_cri2.hide()
        self.btn_cri2.setGeometry(50, 310, self.x, self.y)
        self.btn_cri2.clicked.connect(self.nocriminal)

        self.btn_cri3 = QPushButton("범인3", self)
        self.btn_cri3.hide()
        self.btn_cri3.setGeometry(50, 410, self.x, self.y)
        self.btn_cri3.clicked.connect(self.criminal)

    def criminal_show(self):
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
        self.result = 3
        return self.chapter2_end()

    def nocriminal(self):
        self.result = 4
        return self.chapter2_end()

    def on_click_chapter2(self):
        self.stack.setCurrentIndex(self.result)

    def chapter2_end(self):
        self.btn_next_Ending.show()