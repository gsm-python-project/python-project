from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
import sys
from default import App_default, Mainfront

class EndingFront(App_default):
    def __init__(self):
        super().__init__()

    
class ending:
    def __init__(self, slct):
        self.slct=slct
        
    def decision(self): # 무슨 엔딩을 호출해야하는지 검사(범인을 맞췄는지 안 맞췄는지, 진엔딩 조건을 만족했는지 등)
        pass

class HappyEnding(ending):
    def __init__(self, slct):
        super().__init__(slct)

