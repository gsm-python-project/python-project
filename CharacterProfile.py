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

class Character_Profile(Profile):
    def __init__(self, stack, characters):
        super().__init__(stack, characters)

        self.character=None

        self.character_img = QLabel(self)
        self.character_img.setGeometry(0, 0, 1600, 900)

    def profile(self, character):
        pixmap=QPixmap(f"{character.name}_profile.png")
        self.character_img.setPixmap(pixmap.scaled(1600, 900, Qt.KeepAspectRatio))