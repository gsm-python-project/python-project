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
        self._char_queue=""
        self._init_typing_timer()

        self.subtitle_bg.hide()

        #배경화면
        self.background = QLabel(self)
        self.background.setGeometry(0, 0, 1600, 900)
        self.background.setPixmap(QPixmap("png/backgroundld.png").scaled(1600, 900))
        self.background.lower()  # 제일 뒤로

        self.chat_log = QTextEdit(self)
        self.chat_log.setReadOnly(True)
        self.chat_log.setGeometry(800, 0, 800, 800)  # 둘 다 고정

        palette_chat_log = self.chat_log.palette()
        palette_chat_log.setColor(QPalette.Base, QColor(0,0,0,150))
        palette_chat_log.setColor(QPalette.Text, QColor("white"))
        self.chat_log.setPalette(palette_chat_log)

        from default import ClickableLabel
        self.back = ClickableLabel("png/button/back.png", self)
        self.back.setGeometry(0, 0, 100, 50)
        self.back.clicked.connect(self.on_click_back)
        self.back.setCursor(QCursor(Qt.PointingHandCursor))
        self.back.raise_()

        self.send = QPushButton("전송", self)
        self.send.setGeometry(1400, 800, 200, 100)
        self.send.clicked.connect(self.on_click_send)
        self.send.setCursor(QCursor(Qt.PointingHandCursor))
        self.send.setShortcut('Return')

        self.character_img = QLabel(self)
        self.character_img.setGeometry(30, 0, 900, 900)

        self.input_box = QLineEdit(self)
        self.input_box.setGeometry(0, 800, 1400, 100)

        self.palette_input_box = self.input_box.palette()
        self.palette_input_box.setColor(QPalette.Base, QColor(0,0,0,150))
        self.palette_input_box.setColor(QPalette.Text, QColor("white"))
        self.input_box.setPalette(self.palette_input_box)

        self.global_font=QFont(self.font_family, 12)
        self.subtitle.setFont(self.global_font)
        self.chat_log.setFont(self.global_font)
        self.input_box.setFont(self.global_font)
        self.back.raise_()

    def set_chatlog(self, character):
        self.character = character
        self.chat_log.clear()
        pixmap=QPixmap(f"png/LD/{character.name}.png")
        self.character_img.setPixmap(pixmap.scaled(800, 900, Qt.KeepAspectRatio))

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

        self.character.history.append(("나", user_input))
        self.character.history.append(("",""))
        self.character.history.append((self.character.name, ""))
        
        self._refresh_chatlog()

        self.worker = Stream(self.character, user_input)
        self.worker.token_received.connect(self._on_token)
        self.worker.finished.connect(self._on_stream_finished)
        self.worker.error.connect(self._on_stream_error)
        self.worker.start()
        
    def _refresh_chatlog(self):
        self.chat_log.clear()
        for sender, msg in self.character.history:
            if sender == "" and msg == "":   # 빈 줄 구분용
                self.chat_log.append("")     # 그냥 빈 줄만
            else:
                self.chat_log.append(f"{sender} : {msg}")

    def _on_token(self, chunk: str):
        self._char_queue+=chunk

    def _init_typing_timer(self):
        self._char_queue=""
        self._typing_timer = QTimer(self)
        self._typing_timer.setInterval(30)
        self._typing_timer.timeout.connect(self._type_next_char)
        self._typing_timer.start()

    def _type_next_char(self):
        if not self._char_queue:
            return
        char=self._char_queue[0]
        self._char_queue=self._char_queue[1:]

        sender, current_text=self.character.history[-1]
        self.character.history[-1]=(sender,current_text + char)
        self._refresh_chatlog()
    
        self.chat_log.verticalScrollBar().setValue(
            self.chat_log.verticalScrollBar().maximum()
        )
        
    def _on_stream_error(self, error_msg:str):
        self.character.history[-1]=(self.character.name, f"[오류] {error_msg}")
        self._refresh_chatlog()
        self.waiting=False
        self.send.setEnabled(True)    
    
    def _on_stream_finished(self):
        self.character.history.append(("", ""))
        
        self.waiting=False
        self.send.setEnabled(True)


class Stream(QThread):
    token_received=pyqtSignal(str)
    error=pyqtSignal(str)

    def __init__(self, character, user_input):
        super().__init__()
        self.character = character
        self.user_input = user_input

    def run(self):
        try:
            result = self.character.communication(self.user_input)  # communication() 거치기
            if result is None:  # answer_Fail() 실행된 경우 (대화 횟수 0)
                self.finished.emit()
                return
            for chunk in result:  # answer()의 제너레이터를 여기서 순회
                self.token_received.emit(chunk)
            self.finished.emit()
        except Exception as e:
            self.error.emit(str(e))