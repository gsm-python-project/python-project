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

        self.x=100
        self.y=100

        from default import ClickableLabel
        self.smile = ClickableLabel("png/note.png", self)
        self.smile.setGeometry(1480, 20, self.x, self.y)
        self.smile.clicked.connect(self.on_click_note)
        self.smile.setCursor(QCursor(Qt.PointingHandCursor))

        

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

        self.x=100
        self.y=100

        from default import ClickableLabel
        self.glass = ClickableLabel("png/note.png", self)
        self.glass.setGeometry(1480, 20, self.x, self.y)
        self.glass.clicked.connect(self.on_click_note)
        self.glass.setCursor(QCursor(Qt.PointingHandCursor))

        self.pendant = ClickableLabel("png/note.png", self)
        self.pendant.setGeometry(1480, 20, self.x, self.y)
        self.pendant.clicked.connect(self.on_click_note)
        self.pendant.setCursor(QCursor(Qt.PointingHandCursor))

        self.handkerchief = ClickableLabel("png/note.png", self)
        self.handkerchief.setGeometry(1480, 20, self.x, self.y)
        self.handkerchief.clicked.connect(self.on_click_note)
        self.handkerchief.setCursor(QCursor(Qt.PointingHandCursor))

        self.glove = ClickableLabel("png/note.png", self)
        self.glove.setGeometry(1480, 20, self.x, self.y)
        self.glove.clicked.connect(self.on_click_note)
        self.glove.setCursor(QCursor(Qt.PointingHandCursor))

        self.letter = ClickableLabel("png/note.png", self)
        self.letter.setGeometry(1480, 20, self.x, self.y)
        self.letter.clicked.connect(self.on_click_note)
        self.letter.setCursor(QCursor(Qt.PointingHandCursor))
        
