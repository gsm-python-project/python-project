from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from CHARACTER import butterfly, volt, colombina, crow, moreta

class Mainfront(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("가면 무도회")
        self.setFixedSize(1200, 800)

        from page0 import prologue
        from page1 import Chapter1
        from page2 import Chapter2
        from ending import HappyEnding, BadEnding

        self.prologue = prologue(self)
        self.chapter1 = Chapter1(self)
        self.chapter2 = Chapter2(self)
        self.happyending = HappyEnding(self)
        self.badending = BadEnding(self)

        self.addWidget(self.prologue)
        self.addWidget(self.chapter1)
        self.addWidget(self.chapter2)
        self.addWidget(self.happyending)
        self.addWidget(self.badending)

        self.setCurrentIndex(0)


class App_default(QWidget):
    def __init__(self):
        super().__init__()


class Button(App_default):
    def __init__(self):
        super().__init__()

        self.x = 1000
        self.y = 80

        self.butterfly = QPushButton("나비", self)
        self.butterfly.setGeometry(50, 50, 1000, 80)
        self.butterfly.clicked.connect(self.on_click_butterfly)
        # self.butterfly.setCursor(QCursor(Qt.PointingHandCursor))  # PyQt5 커서 변경 방법

        self.volt = QPushButton("볼트", self)
        self.volt.setGeometry(50, 140, 1000, 80)
        self.volt.clicked.connect(self.on_click_volt)

        self.colombina = QPushButton("콜롬비나", self)
        self.colombina.setGeometry(50, 230, self.x, self.y)
        self.colombina.clicked.connect(self.on_click_colombina)

        self.crow = QPushButton("까마귀", self)
        self.crow.setGeometry(50, 320, self.x, self.y)
        self.crow.clicked.connect(self.on_click_crow)

        self.moreta = QPushButton("모레타", self)
        self.moreta.setGeometry(50, 410, self.x, self.y)
        self.moreta.clicked.connect(self.on_click_moreta)

        self.cri1 = butterfly()
        self.cri2 = volt()
        self.cri3 = colombina()
        self.npc1 = crow()
        self.npc2 = moreta()

    def on_click_butterfly(self):
        return self.cri1.communication()

    def on_click_volt(self):
        return self.cri2.communication()

    def on_click_colombina(self):
        return self.cri3.communication()

    def on_click_crow(self):
        return self.npc1.communication()

    def on_click_moreta(self):
        return self.npc2.communication()