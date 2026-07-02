from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from default import App_default

class evidence(App_default):
    def __init__(self, stack):
        super().__init__()
        self.stack=stack
