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
        self.smile.clicked.connect(self.on_click_smile)
        self.smile.setCursor(QCursor(Qt.PointingHandCursor))
        self.smile_click = False

        self.imprint = ClickableLabel("png/.png", self)
        self.imprint.setGeometry(1480, 20, self.x, self.y)
        self.imprint.clicked.connect(self.on_click_imprint)
        self.imprint.setCursor(QCursor(Qt.PointingHandCursor))
        self.imprint_click = False

        self.hurt = ClickableLabel("png/.png", self)
        self.hurt.setGeometry(1480, 20, self.x, self.y)
        self.hurt.clicked.connect(self.on_click_hurt)
        self.hurt.setCursor(QCursor(Qt.PointingHandCursor))
        self.hurt_click = False

        self.ink=ClickableLabel("png/.png", self)
        self.ink.setGeometry(1480, 20, self.x, self.y)
        self.ink.clicked.connect(self.on_click_ink)
        self.ink.setCursor(QCursor(Qt.PointingHandCursor))
        self.ink_click = False



    def on_click_smile(self):
        pass

    def on_click_imprint(self):
        pass

    def on_click_hurt(self):
        pass

    def on_click_ink(self):
        pass

    def nextstage(self):
        if self.ink_click and self.imprint_click and self.smile_click and self.hurt_click:
            self.stack.setCurrentIndex(11)

        

class slect(App_default):
    def __init__(self, stack):
        super().__init__()
        self.stack= stack

        self.x=100
        self.y=100

        self.background.setPixmap(QPixmap("png/.png").scaled(1600, 900))
        self.background.lower()  # 제일 뒤로

        from default import ClickableLabel
        self.study=ClickableLabel("png/.png", self)
        self.study.setGeometry(1480, 20, self.x, self.y)
        self.study.clicked.connect(self.on_click_study)
        self.study.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.storage=ClickableLabel("png/.png", self)
        self.storage.setGeometry(1480, 20, self.x, self.y)
        self.storage.clicked.connect(self.on_click_storage)
        self.storage.setCursor(QCursor(Qt.PointingHandCursor))

        self.bookstore=ClickableLabel("png/.png", self)
        self.bookstore.setGeometry(1480, 20, self.x, self.y)
        self.bookstore.clicked.connect(self.on_click_bookstore)
        self.bookstore.setCursor(QCursor(Qt.PointingHandCursor))

    def on_click_study(self):
        pass

    def on_click_storage(self):
        self.stack.setCurrentIndex(12)

    def on_click_bookstore(self):
        pass


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
        self.glass.clicked.connect(self.on_click_glass)
        self.glass.setCursor(QCursor(Qt.PointingHandCursor))

        self.pendant = ClickableLabel("png/note.png", self)
        self.pendant.setGeometry(1480, 20, self.x, self.y)
        self.pendant.clicked.connect(self.on_click_pendant)
        self.pendant.setCursor(QCursor(Qt.PointingHandCursor))

        self.handkerchief = ClickableLabel("png/note.png", self)
        self.handkerchief.setGeometry(1480, 20, self.x, self.y)
        self.handkerchief.clicked.connect(self.on_click_handkerchief)
        self.handkerchief.setCursor(QCursor(Qt.PointingHandCursor))

        self.glove = ClickableLabel("png/note.png", self)
        self.glove.setGeometry(1480, 20, self.x, self.y)
        self.glove.clicked.connect(self.on_click_glove)
        self.glove.setCursor(QCursor(Qt.PointingHandCursor))

        self.letter = ClickableLabel("png/note.png", self)
        self.letter.setGeometry(1480, 20, self.x, self.y)
        self.letter.clicked.connect(self.on_click_letter)
        self.letter.setCursor(QCursor(Qt.PointingHandCursor))
        
    def on_click_glass(self):
        pass
    
    def on_click_pendant(self):
        pass

    def on_click_handkerchief(self):
        pass

    def on_click_glove(self):
        pass

    def on_click_letter(self):
        pass