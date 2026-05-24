from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from default import App_default

class Answer_default(App_default):
    def __init__(self, stack):
        super().__init__()
        self.stack=stack
        self.character = None
        self.chapter = 1
        self.waiting=False

        #배경화면 색 설명
        self.background = QLabel(self)
        self.background.setGeometry(0, 0, 1600, 900)
        self.background.setPixmap(QPixmap("background.png").scaled(1600, 900))
        self.background.lower()  # 제일 뒤로

        self.chat_log = QTextEdit(self)
        self.chat_log.setReadOnly(True)
        self.chat_log.setGeometry(500, 0, 1100, 750)  # 둘 다 고정

        palette_chat_log = self.chat_log.palette()
        palette_chat_log.setColor(QPalette.Base, Qt.transparent)
        palette_chat_log.setColor(QPalette.Text, QColor("white"))
        self.chat_log.setPalette(palette_chat_log)

        self.back = QPushButton("돌아가기", self)
        self.back.setGeometry(500, 850, 200, 50)
        self.back.clicked.connect(self.on_click_back)
        self.back.setCursor(QCursor(Qt.PointingHandCursor))

        self.send = QPushButton("전송", self)
        self.send.setGeometry(1400, 800, 200, 50)
        self.send.clicked.connect(self.on_click_send)
        self.send.setCursor(QCursor(Qt.PointingHandCursor))
        self.send.setShortcut('Return')

        self.character_img = QLabel(self)
        self.character_img.setGeometry(0, 0, 500, 900)

        self.input_box = QLineEdit(self)
        self.input_box.setGeometry(500, 800, 900, 50)

        self.palette_input_box = self.input_box.palette()
        self.palette_input_box.setColor(QPalette.Base, Qt.transparent)
        self.palette_input_box.setColor(QPalette.Text, QColor("white"))
        self.input_box.setPalette(self.palette_input_box)

        font = QFont()
        font.setPointSize(12)  # 글자 크기
        self.chat_log.setFont(font)
        self.input_box.setFont(font)

    def set_chatlog(self, character):
        self.character = character
        self.chat_log.clear()
        pixmap=QPixmap(f"{character.name}.png")
        self.character_img.setPixmap(pixmap.scaled(500, 900, Qt.KeepAspectRatio))

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
    
        self.waiting=True
        self.send.setEnabled(False)
        self.input_box.clear()

        response=self.character.communication(user_input)
        if not response is None:
            self.chat_log.append(f"나 : {user_input}")
            self.chat_log.append(f"{self.character.name} : {response}")

        self.waiting=False
        self.send.setEnabled(True)