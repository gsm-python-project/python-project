from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from default import App_default

class Profile_default(App_default):
    def __init__(self, stack, characters):
        super().__init__(stack, characters)
        self.stack = stack



