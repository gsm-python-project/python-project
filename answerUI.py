from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from default import App_default

class Answer_default(App_default):
    def __init__(self, stack):
        super().__init__()
        self.stack=stack
        self.character = None

        self.chat_log = QTextEdit()
        self.chat_log.setReadOnly(True)

        self.back = QPushButton("돌아가기", self)
        self.back.setGeometry(50,50,200,200)
        self.back.clicked.connect(self.on_click_back)
        self.back.setCursor(QCursor(Qt.PointingHandCursor))

        self.send = QPushButton("전송", self)
        self.send.setGeometry(500,50,200,200)
        self.send.clicked.connect(self.on_click_send)
        self.send.setCursor(QCursor(Qt.PointingHandCursor))
        self.send.setShortcut('Return')

        layout=QVBoxLayout()
        self.input_box = QLineEdit(self)
        layout.addWidget

    def set_chatlog(self, character):
        self.character = character
        self.chat_log.clear()
        for sender, msg in character.history:
            self.chat_log.append(f"{sender}:{msg}")
    
    def on_click_back(self):
        self.stack.setCurrentIndex(self.chapter)

    def on_click_send(self):
        if not self.character:
            return
        user_input = self.input_box.text().strip()
        if not user_input:
            return
        self.chat_log.append(f"나 : {user_input}")
        self.input_box.clear()

        response=self.character.answer(user_input)
        self.chat_log.append(f"{self.character.name} : {response}")
