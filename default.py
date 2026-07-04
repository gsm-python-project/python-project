from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import random


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
            "npc2" : moreta(self)
        }

        from page0 import prologue # import문, 각 챕터랑 엔딩을 불러온다.
        from page1 import Chapter1
        from page2 import Chapter2
        from ending import TrueEnding, FalseEnding, HiddenEnding
        from answerUI import Answer_default
        from CharacterProfile import Profile, Character_Profile # 파일 이름을 profile로 하니 모듈 profile로 인식해서 파일 이름 변경
        from evidence import evidence, slect, evidence2

        self.prologue = prologue(self) # 변수에 추가
        self.chapter1 = Chapter1(self, self.characters)  # 캐릭터 넘겨주기
        self.chapter2 = Chapter2(self, self.characters)  # 캐릭터 넘겨주기
        self.trueending = TrueEnding(self)
        self.falseending = FalseEnding(self)
        self.answerUI= Answer_default(self)
        self.startUI=startdisplay(self)
        self.profileMain = Profile(self, self.characters)
        self.profile_character = Character_Profile(self, self.characters)
        self.hiddenending = HiddenEnding(self)
        self.evidence = evidence(self)
        self.slect=slect(self)
        self.evidence2=evidence2(self)

        self.addWidget(self.prologue) # 페이지 추가 인덱스:0
        self.addWidget(self.chapter1) # 인덱스:1
        self.addWidget(self.chapter2) # 인덱스:2
        self.addWidget(self.trueending) # 인덱스:3
        self.addWidget(self.falseending) # 인덱스:4
        self.addWidget(self.answerUI) # 인덱스:5
        self.addWidget(self.startUI) # 인덱스:6
        self.addWidget(self.profileMain) # 인덱스: 7
        self.addWidget(self.profile_character) # 인덱스: 8
        self.addWidget(self.hiddenending) # 인덱스: 9
        self.addWidget(self.evidence) # 인덱스: 10
        self.addWidget(self.slect) # 인덱스: 11
        self.addWidget(self.evidence2) # 인덱스: 12

        self.setCurrentIndex(6) # 인덱스가 6인 페이지(start)로 이동.

class App_default(QWidget):
    def __init__(self):
        super().__init__()
        
        self.q=0

        self.typing=False

        self.background = QLabel(self)
        self.background.setGeometry(0, 0, 1600, 900)
        self.background.setPixmap(QPixmap("png/bg/background.png").scaled(1600, 900))
        self.background.lower()  # 제일 뒤로
        
        self.subtitle_bg = QLabel(self)
        self.subtitle_bg.setGeometry(70, 750, 1430, 100)
        palette_bg = self.subtitle_bg.palette()
        palette_bg.setColor(QPalette.Window, QColor(0, 0, 0, 100))  # 51 = 255 * 0.2 (20%)
        self.subtitle_bg.setPalette(palette_bg)
        self.subtitle_bg.setAutoFillBackground(True)
        
        self.subtitle=QLabel(self)
        self.subtitle.setGeometry(100,750,1400,100)
        self.subtitle.setWordWrap(True)

        # subtitle이 박스보다 위에 있어야 함
        self.subtitle_bg.raise_()
        self.subtitle.raise_()   # subtitle이 bg보다 나중에 raise_() → 글자가 맨 위

        self._full_text = ""     # 이번 단계에서 보여줄 전체 텍스트
        self._char_index = 0     # 현재까지 출력한 글자 수
        self._typing_timer = QTimer(self)
        self._typing_timer.setInterval(40)  # 글자당 40ms
        self._typing_timer.timeout.connect(self._type_next_char)
        
        #글자 스타일
        self.palette = self.subtitle.palette()
        self.palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
        self.subtitle.setPalette(self.palette)

        font_path="fonts/defaultfonts.otf"
        font_id=QFontDatabase.addApplicationFont(font_path)

        if font_id != -1:
            self.font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            self.global_font=QFont(self.font_family, 15)
            self.subtitle.setFont(self.global_font)

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

        self.note = ClickableLabel("png/SD/note.png", self)
        self.note.setGeometry(1480, 20, self.x, self.y)
        self.note.clicked.connect(self.on_click_note)
        self.note.setCursor(QCursor(Qt.PointingHandCursor))

        self.butterfly = ClickableLabel("png/SD/butterfly.png", self)
        self.butterfly.setGeometry(820, 210, self.x, self.y)
        self.butterfly.clicked.connect(self.on_click_butterfly)
        self.butterfly.setCursor(QCursor(Qt.PointingHandCursor))

        self.volt = ClickableLabel("png/SD/volt.png",self) # "" 사이에 이미지 경로 넣기!
        self.volt.setGeometry(90, 350, self.x, self.y)
        self.volt.clicked.connect(self.on_click_volt)
        self.volt.setCursor(QCursor(Qt.PointingHandCursor))

        self.colombina = ClickableLabel("png/SD/colombina.png", self) # "" 사이에 이미지 경로 넣기!
        self.colombina.setGeometry(450, 310, self.x, self.y)
        self.colombina.clicked.connect(self.on_click_colombina)
        self.colombina.setCursor(QCursor(Qt.PointingHandCursor))

        self.crow = ClickableLabel("png/SD/crow.png", self)
        self.crow.setGeometry(980, 470, self.x, self.y)
        self.crow.clicked.connect(self.on_click_crow)
        self.crow.setCursor(QCursor(Qt.PointingHandCursor))

        self.moreta = ClickableLabel("png/SD/moreta.png", self)
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

        self.subtitle.hide()

        self.background.setPixmap(QPixmap("png/bg/black.png").scaled(1600, 900))
        self.background.lower()  # 제일 뒤로

        self.label = QLabel("옥장판", self) 
        self.label.setGeometry(625, 300, 300, 100)
        self.label.setAlignment(Qt.AlignCenter) 
        self.label.hide()

        self.global_font=QFont(self.font_family, 40)
        self.label.setFont(self.global_font)
        palette = self.label.palette()
        palette.setColor(QPalette.WindowText, QColor("White"))
        self.label.setPalette(palette)

        self.btn=QPushButton("시작", self)
        self.btn.setGeometry(675, 450, self.x, self.y)
        self.btn.clicked.connect(self.next_prologue)
        self.btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn.hide()

                # 비 효과 오버레이
        self.rain = RainWidget(self, num_drops=250, on_finished=self.on_rain_finished)
        self.rain.setGeometry(0, 0, 1600, 900)
        self.rain.raise_()
        self.rain.start_rain()

        # 라벨/버튼 처음엔 투명하게 세팅
        self.label.hide()
        self.btn.hide()
        self._setup_fade(self.label)
        self._setup_fade(self.btn)

        QTimer.singleShot(3000, self.rain.stop_rain)  # 3초 비 내리다 그치기 시작


    def _setup_fade(self, widget):
        effect = QGraphicsOpacityEffect(widget)
        effect.setOpacity(0.0)
        widget.setGraphicsEffect(effect)
        widget._fade_effect = effect

    def _fade_in(self, widget, duration=800, delay=0):
        widget.show()
        anim = QPropertyAnimation(widget._fade_effect, b"opacity")
        anim.setDuration(duration)
        anim.setStartValue(0.0)
        anim.setEndValue(1.0)
        anim.setEasingCurve(QEasingCurve.InOutQuad)
        widget._fade_anim = anim
        QTimer.singleShot(delay, anim.start)

    def on_rain_finished(self):
        # 비가 다 그친 후 0.6초 정적 → 라벨 페이드인 → 조금 늦게 버튼 페이드인
        self._fade_in(self.label, duration=1000, delay=600)
        self._fade_in(self.btn, duration=1000, delay=1200)

    def resizeEvent(self, event):
        self.rain.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)

    def on_show(self):
        self.label.show()
        self.btn.show()

    def next_prologue(self):
        self.stack.setCurrentIndex(0) # 프롤로그로 이동
 
class Raindrop:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.reset(random_y=True)
 
    def reset(self, random_y=False):
        self.x = random.uniform(0, self.width)
        self.y = random.uniform(-self.height, 0) if not random_y else random.uniform(0, self.height)
        self.length = random.uniform(10, 22)          # 빗줄기 길이
        self.speed = random.uniform(12, 28)             # 낙하 속도 (눈보다 훨씬 빠름)
        self.drift = random.uniform(-0.5, 0.5)          # 바람에 의한 살짝의 기울기
        self.opacity = random.uniform(0.5, 0.9)
        self.thickness = random.uniform(3.0, 6.0)
 
    def update(self, respawn=True):
        self.y += self.speed
        self.x += self.drift
        if self.y - self.length > self.height:
            if respawn:
                self.reset()
            # respawn=False면 화면 밖으로 나간 채로 그대로 둠 (widget에서 걸러냄)
 
class RainWidget(QWidget):
    """투명 배경 위에 빗방울만 그리는 오버레이 위젯"""
 
    def __init__(self, parent=None, num_drops=250, on_finished=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.num_drops = num_drops
        self.drops = []
        self.max_active = num_drops        # 최종 목표 빗방울 수
        self.active = int(num_drops * 0.1)  # 처음엔 10%만 활성화
        self.ramp_amount = 1                 # 한 번에 늘릴 개수

        self.is_stopping = False   # 그치는 중인지 여부 (새 빗방울 리스폰 금지)
        self.is_running = False

        self.on_finished = on_finished
 
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_tick)
        
        time=QTimer(self)
        time.timeout.connect(self.stop_rain)
        time.setSingleShot(True)
        time.start(2000)
 
    def resizeEvent(self, event):
        w, h = self.width(), self.height()
        if not self.drops and w > 0 and h > 0:
            self.drops = [Raindrop(w, h) for _ in range(self.num_drops)]
        else:
            for d in self.drops:
                d.width, d.height = w, h
        super().resizeEvent(event)
 
    def start_rain(self):
        self.is_stopping = False
        self.is_running = True
        if not self.timer.isActive():
            self.timer.start(16)
 
    def stop_rain(self):
        self.is_stopping = True
 
    def on_tick(self):
        for d in self.drops[:self.active]:
            d.update(respawn=not self.is_stopping)

        if self.is_running and not self.is_stopping and self.active < self.max_active:
            self.active = min(self.active + self.ramp_amount, self.max_active)
 
        if self.is_stopping: # 그치는 중에는 리스폰 대신 화면 밖으로 나간 빗방울을 제거
            self.drops = [d for d in self.drops if d.y - d.length <= d.height]
            if not self.drops:
                self.timer.stop()
                self.is_running = False
                self.is_stopping = False
                if self.on_finished:
                    self.on_finished()
            
        self.update()
 
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
 
        for d in self.drops[:self.active]:
            color = QColor(240, 175, 12)
            color.setAlphaF(d.opacity)
            pen = QPen(color)
            pen.setWidthF(d.thickness)
            painter.setPen(pen)
            # 살짝 기울어진 선으로 빗줄기 표현 (drift 방향 반영)
            x2 = d.x - d.drift * 4
            y2 = d.y - d.length
            painter.drawLine(QLineF(d.x, d.y, x2, y2))
