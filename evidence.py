from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from default import App_default

class evidence(App_default):
    def __init__(self, stack):
        super().__init__()
        self.stack=stack

        self.background.setPixmap(QPixmap("png/bg/evi.png").scaled(1600, 900))
        self.background.lower()  # 제일 뒤로

        self.messages=["남작의 수상한 부분을 네 군데 찾아보자."]

        self.x=100
        self.y=100

        from default import ClickableLabel
        self.smile = ClickableLabel("png/ev/blank.png", self)
        self.smile.setGeometry(955, 180, self.x, self.y)
        self.smile.clicked.connect(self.on_click_smile)
        self.smile.setCursor(QCursor(Qt.PointingHandCursor))
        self.smile_click = False

        self.imprint = ClickableLabel("png/ev/blank.png", self)
        self.imprint.setGeometry(902, 316, 200, self.y)
        self.imprint.clicked.connect(self.on_click_imprint)
        self.imprint.setCursor(QCursor(Qt.PointingHandCursor))
        self.imprint_click = False

        self.hurt = ClickableLabel("png/ev/blank.png", self)
        self.hurt.setGeometry(466, 426, self.x, self.y)
        self.hurt.clicked.connect(self.on_click_hurt)
        self.hurt.setCursor(QCursor(Qt.PointingHandCursor))
        self.hurt_click = False

        self.ink=ClickableLabel("png/ev/blank.png", self)
        self.ink.setGeometry(740,580, 200, 200)
        self.ink.clicked.connect(self.on_click_ink)
        self.ink.setCursor(QCursor(Qt.PointingHandCursor))
        self.ink_click = False

    def showEvent(self, a0):
        super().showEvent(a0)
        self._start_typing(self.q)

    def mousePressEvent(self, a0):
        if self.typing:
            self._finish_typing_immediately()
            return
        if self.q==0:
            self.subtitle_bg.hide()
            self.subtitle.hide()
        self.q+=1
        self._start_typing(self.q)

    def on_click_smile(self):
        self.ink_click=True
        popup= EvidencePopup2(
            name="[남작의 웃음]",
            description="자살이 사인이라면, 남작은 왜 웃고있을까? 남작의 웃음은 모순적이다. 독살이나 약물 복용의 가능성을 열어보자.",
            parent=self
        )
        popup.move(325, 10)
        popup.exec_()
        self.smile_click=True

    def on_click_imprint(self):
        self.imprint_click=True
        popup= EvidencePopup2(
            name="[목이 졸린 흔적]",
            description="목에 남아있는 흔적의 형태를 보아선, 목줄이 목을 조른 시점에 남작은 이미 죽은 상태였을 것이다.",
            parent=self
        )
        popup.move(762, 416)
        popup.exec_()
        

    def on_click_hurt(self):
        self.hurt_click=True
        popup= EvidencePopup2(
            name="[목의 자잘한 상처]",
            description="저항한 흔적이 있다. 몸싸움을 했던 것일까? 단순 자살이 아닐 가능성이 높다.",
            parent=self
        )

        popup.move(266, 576)
        popup.exec_()
        

    def on_click_ink(self):
        self.ink_click=True
        popup= EvidencePopup2(
            name="[옷에 묻어있는 잉크]",
            description="연회장에 잉크는 없다. 다른 장소에서 묻은 것일까?",
            parent=self
        )
        popup.move(590,460)
        popup.exec_()
        

    def nextstage(self):
        if self.ink_click and self.imprint_click and self.smile_click and self.hurt_click:
            self.stack.setCurrentIndex(11)

class slect(App_default):
    def __init__(self, stack):
        super().__init__()
        self.stack= stack

        self.x=200
        self.y=100

        self.background.setPixmap(QPixmap("png/bg/slect.png").scaled(1600, 900))
        self.background.lower()  # 제일 뒤로

        self.messages=["정말 남작은 이곳에서 죽었을까?"]

        self.study=QPushButton("넓은 책방", self)
        self.study.setGeometry(700, 300, self.x, self.y)
        self.study.clicked.connect(self.on_click_study)
        self.study.setCursor(QCursor(Qt.PointingHandCursor))
        self.study.hide()
        
        self.storage=QPushButton("어두운 창고", self)
        self.storage.setGeometry(300, 300, self.x, self.y)
        self.storage.clicked.connect(self.on_click_storage)
        self.storage.setCursor(QCursor(Qt.PointingHandCursor))
        self.storage.hide()

        self.bookstore=QPushButton("남작의 서재", self)
        self.bookstore.setGeometry(1050, 300, self.x, self.y)
        self.bookstore.clicked.connect(self.on_click_bookstore)
        self.bookstore.setCursor(QCursor(Qt.PointingHandCursor))
        self.bookstore.hide()

    def on_click_study(self):
        popup=EVPopup(
            description="창고는 외부인의 발길이 닿을 수 없는 곳이고, 만약 정말 창고였다면 몸에 자잘한 상처보다는 큰 상처가 생길 가능성이 크다. 다시 생각해보자.",
            parent=self
        )
        popup.exec_()

    def on_click_storage(self):
        popup=EVPopup(
            description="책방에 잉크나, 잉크와 관련된 물건은 없다. 다시 생각해보자.",
            parent=self
        )
        popup.exec_()
        

    def on_click_bookstore(self):
        self.stack.setCurrentIndex(2)

    def showEvent(self, a0):
        super().showEvent(a0)
        self._start_typing(self.q)

    def mousePressEvent(self, a0):
        super().mousePressEvent(a0)
        if self.typing:
            self._finish_typing_immediately()
            return
        if self.q==0:
            self.subtitle_bg.hide()
            self.subtitle.hide()

            self.study.show()
            self.bookstore.show()
            self.storage.show()
        self.q+=1
        self._start_typing(self.q)
        


class evidence2(App_default):
    def __init__(self, stack):
        super().__init__()
        self.stack=stack

        self.subtitle_bg.hide()

        self.background.setPixmap(QPixmap("png/bg/ev.png").scaled(1600, 900))
        self.background.lower()  # 제일 뒤로

        self.x=80
        self.y=80

        from default import ClickableLabel
        self.glass = ClickableLabel("png/ev/glass.png", self)
        self.glass.setGeometry(900,330, self.x, 120)
        self.glass.clicked.connect(self.on_click_glass)
        self.glass.setCursor(QCursor(Qt.PointingHandCursor))
        self.glass.setScaledContents(True)

        self.pendant = ClickableLabel("png/ev/pendant.png", self)
        self.pendant.setGeometry(120, 500, self.x, 100)
        self.pendant.clicked.connect(self.on_click_pendant)
        self.pendant.setCursor(QCursor(Qt.PointingHandCursor))
        self.pendant.setScaledContents(True)

        self.handkerchief = ClickableLabel("png/ev/handkerchief.png", self)
        self.handkerchief.setGeometry(1462, 580, self.x, self.y)
        self.handkerchief.clicked.connect(self.on_click_handkerchief)
        self.handkerchief.setCursor(QCursor(Qt.PointingHandCursor))
        self.handkerchief.setScaledContents(True)

        self.glove = ClickableLabel("png/ev/glove.png", self)
        self.glove.setGeometry(980, 180, self.x, self.y)
        self.glove.clicked.connect(self.on_click_glove)
        self.glove.setCursor(QCursor(Qt.PointingHandCursor))
        self.glove.setScaledContents(True)

        self.letter = ClickableLabel("png/ev/letter.png", self)
        self.letter.setGeometry(480, 365, self.x, self.y)
        self.letter.clicked.connect(self.on_click_letter)
        self.letter.setCursor(QCursor(Qt.PointingHandCursor))
        self.letter.setScaledContents(True)

        self.back = ClickableLabel("png/button/back.png", self)
        self.back.setGeometry(10, 10, self.x, self.y)
        self.back.clicked.connect(self.on_click_back)
        self.back.setCursor(QCursor(Qt.PointingHandCursor))
        self.back.setScaledContents(True)
        
    def on_click_glass(self):
        popup = EvidencePopup(
        name="[유리병]",
        description="독이 들어있었던 유리병이다.",
        parent=self
    )
        popup.move(650,470)
        popup.exec_()  # 팝업 띄우기 (닫을 때까지 대기)
    
    def on_click_pendant(self):
        popup= EvidencePopup(
            name="[펜던트]",
            description="붉은색의 보석이 눈에 띈다. 나비의 것으로 보인다.",
            parent=self
        )
        popup.move(220,600)
        popup.exec_()

    def on_click_handkerchief(self):
        popup= EvidencePopup(
            name="[손수건]",
            description="검은색 손수건이다. 아래에 M이라는 자수가 새겨져있다. 모레타의 것일까?",
            parent=self
        )
        popup.move(862,680)
        popup.exec_()
        

    def on_click_glove(self):
        popup= EvidencePopup(
            name="[남성용 장갑]",
            description="남성용 검은 장갑이다. 오늘 연회에서 장갑을 낀 남성은 볼토와 콜롬비나 뿐이다.",
            parent=self
        )
        popup.move(720,280)
        popup.exec_()

    def on_click_letter(self):
        popup= EvidencePopup(
            name="[의문의 쪽지]",
            description="\"서류는 잠시 가져가겠네.\"라는 글이 쓰여져있다. 누구의 것일까?",
            parent=self
        )
        popup.move(280,485)

        popup.exec_()

    def on_click_back(self):
        self.stack.setCurrentIndex(2)


class EVPopup(QDialog):
    def __init__(self, description, parent=None):
        super().__init__(parent)
        self.setFixedSize(600, 300)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 타이틀바 제거

        # 배경색
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(30, 30, 30))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # 폰트 설정
        font_path="fonts/defaultfonts.otf"
        font_id=QFontDatabase.addApplicationFont(font_path)

        if font_id != -1:
            self.font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            self.global_font=QFont(self.font_family, 15)
        self.global_font.setBold(True)

        # 증거 설명
        self.desc_label = QLabel(description, self)
        self.desc_label.setGeometry(50, 100, 500, 80)

        self.desc_label.setWordWrap(True)
        self.desc_label.setAlignment(Qt.AlignTop)
        self.desc_label.setFont(self.global_font)

        palette_desc = self.desc_label.palette()
        palette_desc.setColor(QPalette.WindowText, QColor(200, 200, 200))
        self.desc_label.setPalette(palette_desc)

        # 닫기 버튼 (오른쪽 하단)
        self.close_btn = QPushButton("닫기", self)
        self.close_btn.setGeometry(490, 150, 100, 40)
        self.close_btn.clicked.connect(self.close)
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))


class EvidencePopup(QDialog):
    def __init__(self, name, description, parent=None):
        super().__init__(parent)

        self.parent=parent
        self.setFixedSize(600, 200)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 타이틀바 제거

        # 배경색
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(30, 30, 30))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # 증거 이름 (오른쪽 상단)
        self.name_label = QLabel(name, self)
        self.name_label.setGeometry(50, 10, 300, 60)
        self.name_label.setWordWrap(True)
        
        font_path="fonts/defaultfonts.otf"
        font_id=QFontDatabase.addApplicationFont(font_path)

        if font_id != -1:
            self.font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            self.global_font=QFont(self.font_family, 13)

        self.global_font.setBold(True)
        self.name_label.setFont(self.global_font)
        palette_name = self.name_label.palette()
        palette_name.setColor(QPalette.WindowText, QColor("white"))
        self.name_label.setPalette(palette_name)

        # 증거 설명
        self.desc_label = QLabel(description, self)
        self.desc_label.setGeometry(50, 70, 500, 120)
        self.desc_label.setWordWrap(True)
        self.desc_label.setAlignment(Qt.AlignTop)
        self.desc_label.setFont(self.global_font)
        palette_desc = self.desc_label.palette()
        palette_desc.setColor(QPalette.WindowText, QColor(200, 200, 200))
        self.desc_label.setPalette(palette_desc)

        # 닫기 버튼
        self.close_btn = QPushButton("X", self)
        self.close_btn.setGeometry(550, 150, 40, 40)
        self.close_btn.clicked.connect(self.close)
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))

class EvidencePopup2(EvidencePopup):
    def __init__(self, name, description, parent=None):
        super().__init__(name, description, parent)

        self.close_btn.clicked.connect(self.on_click_btn)

    def on_click_btn(self):
        self.parent.nextstage()