from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from default import App_default

class evidence(App_default):
    def __init__(self, stack, characters):
        super().__init__()
        self.stack=stack

        self.cri1 = characters["cri1"]  # 새로 만들지 않고 받아서 사용
        self.cri2 = characters["cri2"]
        self.cri3 = characters["cri3"]
        self.npc1 = characters["npc1"]
        self.npc2 = characters["npc2"]

        
