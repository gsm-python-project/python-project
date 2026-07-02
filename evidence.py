from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from default import App_default

class evidence(App_default):
    def __init__(self, stack):
        super().__init__()
        self.stack=stack

        self.background.setPixmap(QPixmap("png/.png").scaled(1600, 900))
        self.background.lower()  # 제일 뒤로
        

class slect(App_default):
    def __init__(self, stack):
        super().__init__()
        self.stack= stack

        self.background.setPixmap(QPixmap("png/.png").scaled(1600, 900))
        self.background.lower()  # 제일 뒤로


class evidence2(App_default):
    def __init__(self, stack):
        super().__init__()
        self.stack=stack

        self.background.setPixmap(QPixmap("png/.png").scaled(1600, 900))
        self.background.lower()  # 제일 뒤로

        