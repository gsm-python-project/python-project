from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from default import App_default  
    
class ending(App_default):
    def __init__(self):
        super().__init__()
        
class HappyEnding(ending):
    def __init__(self, stack):
        super().__init__()
        self.stack=stack
        self.label = QLabel("해피 엔딩", self)
        self.label.setGeometry(50,50,200,50)

        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

class BadEnding(ending):
    def __init__(self,stack):
        super().__init__()
        self.stack=stack

class HiddenEnding(ending):
    def __init__(self,stack):
        super().__init__()
        self.stack=stack