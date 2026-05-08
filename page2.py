import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
from default import Button

## 제 2장

class Chapter2(Button):
    def __init__(self):
        super().__init__()
        