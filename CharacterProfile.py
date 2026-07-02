from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from default import App_default

class Profile(App_default):
    def __init__(self, stack, characters):
        super().__init__()
        self.stack = stack
        self.chapter = 1

        self.cri1 = characters["cri1"]  # 새로 만들지 않고 받아서 사용
        self.cri2 = characters["cri2"]
        self.cri3 = characters["cri3"]
        self.npc1 = characters["npc1"]
        self.npc2 = characters["npc2"]

        self.x=100
        self.y=100

        self.back = QPushButton("이전으로 돌아가기", self)
        self.back.setGeometry(0,0,200,100)
        self.back.clicked.connect(self.on_click_back)
        self.back.setCursor(QCursor(Qt.PointingHandCursor))

        from default import ClickableLabel

        self.butterfly = ClickableLabel("", self)
        self.butterfly.setGeometry(0, 0, self.x, self.y)
        self.butterfly.clicked.connect(self.on_click_butterfly)
        self.butterfly.setCursor(QCursor(Qt.PointingHandCursor))

        self.colombina = ClickableLabel("", self)
        self.colombina.setGeometry(50, 320, self.x, self.y)
        self.colombina.clicked.connect(self.on_click_colombina)
        self.colombina.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.volt = ClickableLabel("", self)
        self.volt.setGeometry(50, 320, self.x, self.y)
        self.volt.clicked.connect(self.on_click_volt)
        self.volt.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.crow = ClickableLabel("", self)
        self.crow.setGeometry(50, 320, self.x, self.y)
        self.crow.clicked.connect(self.on_click_crow)
        self.crow.setCursor(QCursor(Qt.PointingHandCursor))

        self.moreta = ClickableLabel("", self)
        self.moreta.setGeometry(50, 320, self.x, self.y)
        self.moreta.clicked.connect(self.on_click_moreta)
        self.moreta.setCursor(QCursor(Qt.PointingHandCursor))
        
    def on_click_back(self):
        self.stack.setCurrentIndex(self.chapter)

    def on_click_butterfly(self):
        self.stack.profile_character.profile(self.cri1)
        self.stack.setCurrentIndex(8)
    
    def on_click_colombina(self):
        self.stack.profile_character.profile(self.cri2)
        self.stack.setCurrentIndex(8)
        
    def on_click_volt(self):
        self.stack.profile_character.profile(self.cri3)
        self.stack.setCurrentIndex(8)
        
    def on_click_crow(self):
        self.stack.profile_character.profile(self.npc1)
        self.stack.setCurrentIndex(8)
        
    def on_click_moreta(self):
        self.stack.profile_character.profile(self.npc2)
        self.stack.setCurrentIndex(8)


class Character_Profile(App_default):
    def __init__(self, stack, characters):
        super().__init__()
        self.stack=stack

        self.cri1 = characters["cri1"]  # 새로 만들지 않고 받아서 사용
        self.cri2 = characters["cri2"]
        self.cri3 = characters["cri3"]
        self.npc1 = characters["npc1"]
        self.npc2 = characters["npc2"]

        self.character=None

        self.x=100
        self.y=100

        self.character_img = QLabel(self)
        self.character_img.setGeometry(0, 0, 1600, 900)
        self.character_img.lower()  # 제일 뒤로

        self.back=QPushButton("이전으로 돌아가기", self)
        self.back.setGeometry(1500,800,self.x,self.y)
        self.back.clicked.connect(self.on_click_back)
        self.back.setCursor(QCursor(Qt.PointingHandCursor))

    def profile(self, character):
        self.character=character
        pixmap=QPixmap(f"png/{character.name}_profile.png")
        self.character_img.setPixmap(pixmap.scaled(1600, 900, Qt.KeepAspectRatio))

    def on_click_back(self):
        self.stack.setCurrentIndex(7)