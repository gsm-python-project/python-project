from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class Mainfront(QStackedWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("가면 무도회") # 팝업창의 이름
        self.setFixedSize(1600, 900) #팝업창의 사이즈

        from CHARACTER import butterfly, volt, colombina, crow, moreta
        self.characters={
            "cri1" : butterfly(),
            "cri2" : volt(), # 변수에 butterfly 클래스 저장
            "cri3" : colombina(),
            "npc1" : crow(),
            "npc2" : moreta()
        }

        from page0 import prologue # import문, 각 챕터랑 엔딩을 불러온다.
        from page1 import Chapter1
        from page2 import Chapter2
        from ending import TrueEnding, FalseEnding
        from answerUI import Answer_default

        self.prologue = prologue(self) # 변수에 추가
        self.chapter1 = Chapter1(self, self.characters)  # 캐릭터 넘겨주기
        self.chapter2 = Chapter2(self, self.characters)  # 캐릭터 넘겨주기
        self.trueending = TrueEnding(self)
        self.falseending = FalseEnding(self)
        self.answerUI= Answer_default(self)
        self.startUI=startdisplay(self)

        self.addWidget(self.prologue) # 페이지 추가 인덱스:0
        self.addWidget(self.chapter1) # 인덱스:1
        self.addWidget(self.chapter2) # 인덱스:2
        self.addWidget(self.trueending) # 인덱스:3
        self.addWidget(self.falseending) # 인덱스:4
        self.addWidget(self.answerUI) # 인덱스:5
        self.addWidget(self.startUI) # 인덱스:6

        self.setCurrentIndex(6) # 인덱스가 6인 페이지(start)로 이동.

class App_default(QWidget):
    def __init__(self):
        super().__init__()
        
        self.q=0

        self.typing=False

        self.background = QLabel(self)
        self.background.setGeometry(0, 0, 1600, 900)
        self.background.setPixmap(QPixmap("background.png").scaled(1600, 900))
        self.background.lower()  # 제일 뒤로
        
        self.subtitle=QLabel(self)
        self.subtitle.setGeometry(100,750,1500,100)
        self.subtitle.setWordWrap(True)
        self.subtitle.raise_()

        self._full_text = ""     # 이번 단계에서 보여줄 전체 텍스트
        self._char_index = 0     # 현재까지 출력한 글자 수
        self._typing_timer = QTimer(self)
        self._typing_timer.setInterval(40)  # 글자당 40ms
        self._typing_timer.timeout.connect(self._type_next_char)
        
        #글자 스타일
        palette = self.subtitle.palette()
        palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
        self.subtitle.setPalette(palette)

        font=QFont()
        font.setPointSize(15)
        self.subtitle.setFont(font)

        self.player = QMediaPlayer(self)

    def play_bgm(self, file_path, loop=True): #loop=True -> 무한반복
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
        self.player.setVolume(50)
        self.player.play()

        if loop:
            self.player.mediaStatusChanged.connect(self._loop_music)

    def _loop_music(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.player.setPosition(0)
            self.player.play()

    def stop_bgm(self):
        self.player.stop()

    def _start_typing(self, index):
        if index >= len(self.messages):
            self.subtitle.setText("")
            return

        self._full_text = self.messages[index]
        self._char_index = 0
        self.subtitle.setText("")
        self.typing = True
        self._typing_timer.start()

    def _type_next_char(self):
        if self._char_index >= len(self._full_text):
            self._typing_timer.stop()
            self.typing = False
            return

        self._char_index += 1
        self.subtitle.setText(self._full_text[:self._char_index])

    def _finish_typing_immediately(self): # 타이핑 중인 메시지 완성
            self._typing_timer.stop()
            self.subtitle.setText(self._full_text)
            self.typing = False


class Button(App_default): # 버튼. chapterr 1, chapter2에서 사용!
    def __init__(self, stack,characters):
        super().__init__()

        self.stack= stack
        self.x = 200 # 버튼의 가로 사이즈
        self.y = 300 # 버튼의 세로 사이즈/

        self.butterfly = ClickableLabel("butterfly.png", self)
        self.butterfly.setGeometry(820, 210, self.x, self.y)
        self.butterfly.clicked.connect(self.on_click_butterfly)
        self.butterfly.setCursor(QCursor(Qt.PointingHandCursor))

        self.volt = ClickableLabel("volt.png",self) # "" 사이에 이미지 경로 넣기!
        self.volt.setGeometry(90, 350, self.x, self.y)
        self.volt.clicked.connect(self.on_click_volt)
        self.volt.setCursor(QCursor(Qt.PointingHandCursor))

        self.colombina = ClickableLabel("colombina.png", self) # "" 사이에 이미지 경로 넣기!
        self.colombina.setGeometry(450, 310, self.x, self.y)
        self.colombina.clicked.connect(self.on_click_colombina)
        self.colombina.setCursor(QCursor(Qt.PointingHandCursor))

        self.crow = ClickableLabel("crow.png", self)
        self.crow.setGeometry(980, 470, self.x, self.y)
        self.crow.clicked.connect(self.on_click_crow)
        self.crow.setCursor(QCursor(Qt.PointingHandCursor))

        self.moreta = ClickableLabel("moreta.png", self)
        self.moreta.setGeometry(1150, 310, self.x, self.y)
        self.moreta.clicked.connect(self.on_click_moreta)
        self.moreta.setCursor(QCursor(Qt.PointingHandCursor))

        self.cri1 = characters["cri1"]  # 새로 만들지 않고 받아서 사용
        self.cri2 = characters["cri2"]
        self.cri3 = characters["cri3"]
        self.npc1 = characters["npc1"]
        self.npc2 = characters["npc2"]

    def on_click_note(self):
        self.stack.setCurrentIndex(7)

    def on_click_butterfly(self): # 버튼과 그 버튼에 맞는 클래스의 communication(answer)과 연결.
        self.stack.answerUI.set_chatlog(self.cri1)
        self.stack.setCurrentIndex(5)

    def on_click_volt(self):
        self.stack.answerUI.set_chatlog(self.cri2)
        self.stack.setCurrentIndex(5)

    def on_click_colombina(self):
        self.stack.answerUI.set_chatlog(self.cri3)
        self.stack.setCurrentIndex(5)

    def on_click_crow(self):
        self.stack.answerUI.set_chatlog(self.npc1)
        self.stack.setCurrentIndex(5)

    def on_click_moreta(self):
        self.stack.answerUI.set_chatlog(self.npc2)
        self.stack.setCurrentIndex(5)


class ClickableLabel(QLabel): # 이미지 기본 설정 클래스
    clicked = pyqtSignal() #clicked 이벤트 재정의

    def __init__(self,image_path,parent = None):
        super().__init__(parent)
        pixmap = QPixmap(image_path) # pixmap 메소드로 imagepath 저장
        self.setPixmap(pixmap)
        self.setPixmap(pixmap.scaled(200, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)) # 크기

        self.resize(pixmap.size()) 
        
    def mousePressEvent(self, ev):
        if ev.button() == Qt.LeftButton:
            self.clicked.emit()

class startdisplay(App_default):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack

        self.x = 200
        self.y=80

        self.background.setPixmap(QPixmap("black.png").scaled(1600, 900))
        self.background.lower()  # 제일 뒤로

        self.label = QLabel("옥장판", self) 
        self.label.setGeometry(625, 300, 300, 100)
        self.label.setAlignment(Qt.AlignCenter) 

        font=QFont()
        font.setPointSize(40)  # 글자 크기
        palette = self.label.palette()
        palette.setColor(QPalette.WindowText, QColor("White"))
        self.label.setPalette(palette)
        self.label.setFont(font)

        self.btn=QPushButton("시작", self)
        self.btn.setGeometry(675, 450, self.x, self.y)
        self.btn.clicked.connect(self.next_prologue)
        self.btn.setCursor(QCursor(Qt.PointingHandCursor))

    def next_prologue(self):
        self.stack.setCurrentIndex(0) # 프롤로그로 이동