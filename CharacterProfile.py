from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from default import App_default

class Profile(App_default):
    def __init__(self, stack, characters):
        super().__init__()
        self.stack = stack
        self.chapter = 1
        self.subtitle.hide()
        self.subtitle_bg.hide()

        self.cri1 = characters["cri1"]  # 새로 만들지 않고 받아서 사용
        self.cri2 = characters["cri2"]
        self.cri3 = characters["cri3"]
        self.npc1 = characters["npc1"]
        self.npc2 = characters["npc2"]

        self.x=300
        self.y=300
        
        self.background.setPixmap(QPixmap("png/profile/background.png").scaled(1600, 900))
        self.background.lower()  # 제일 뒤로

        from default import ClickableLabel
        self.back = ClickableLabel("png/button/back.png", self)
        self.back.setGeometry(0, 0, 80, 80)
        self.back.clicked.connect(self.on_click_back)
        self.back.setCursor(QCursor(Qt.PointingHandCursor))
        self.back.setScaledContents(True)

        self.butterfly = ClickableLabel("png/profile/butterfly", self)
        self.butterfly.setGeometry(429, 43, self.x, self.y)
        self.butterfly.clicked.connect(self.on_click_butterfly)
        self.butterfly.setCursor(QCursor(Qt.PointingHandCursor))

        self.colombina = ClickableLabel("png/profile/colombina", self)
        self.colombina.setGeometry(1000, 65, self.x, self.y)
        self.colombina.clicked.connect(self.on_click_colombina)
        self.colombina.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.volt = ClickableLabel("png/profile/volt", self)
        self.volt.setGeometry(232,466, 400, 400)
        self.volt.clicked.connect(self.on_click_volt)
        self.volt.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.crow = ClickableLabel("png/profile/crow", self)
        self.crow.setGeometry(1161,480, self.x, self.y)
        self.crow.clicked.connect(self.on_click_crow)
        self.crow.setCursor(QCursor(Qt.PointingHandCursor))

        self.moreta = ClickableLabel("png/profile/moreta", self)
        self.moreta.setGeometry(620, 628, self.x, self.y)
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
        
        self.subtitle.hide()
        self.subtitle_bg.hide()

        self.cri1 = characters["cri1"]  # 새로 만들지 않고 받아서 사용
        self.cri2 = characters["cri2"]
        self.cri3 = characters["cri3"]
        self.npc1 = characters["npc1"]
        self.npc2 = characters["npc2"]

        self.character=None

        self.x=100
        self.y=70

        self.character_img = QLabel(self)
        self.character_img.setGeometry(0, 0, 1600, 900)
        self.character_img.lower()  # 제일 뒤로

        from default import ClickableLabel
        self.back = ClickableLabel("png/button/back.png", self)
        self.back.setGeometry(10, 10, self.x, self.y)
        self.back.clicked.connect(self.on_click_back)
        self.back.setCursor(QCursor(Qt.PointingHandCursor))
        self.back.setScaledContents(True)

    def profile(self, character):
        self.character=character
        pixmap=QPixmap(f"png/profile/{character.name}_profile.png")
        self.character_img.setPixmap(pixmap.scaled(1600, 900, Qt.KeepAspectRatio))

    def on_click_back(self):
        self.stack.setCurrentIndex(7)