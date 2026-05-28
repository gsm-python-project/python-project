from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from default import App_default  

class ending(App_default):
    def __init__(self):
        super().__init__()
        
class HappyEnding(ending):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack # stack에 mainfront 클래스 저장
        
        self.label = QLabel("해피 엔딩", self) 
        self.label.setGeometry(50, 50, 200, 50)
        self.label.setAlignment(Qt.AlignCenter)

class BadEnding(ending):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack # stack에 mainfront 클래스 저장

class HiddenEnding(ending):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack # stack에 mainfront 클래스 저장