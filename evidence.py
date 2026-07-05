from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from default import App_default

class evidence(App_default):
    def __init__(self, stack):
        super().__init__()
        self.stack=stack

        self.background.setPixmap(QPixmap("png/bg/ev.png").scaled(1600, 900))
        self.background.lower()  # 제일 뒤로

        self.subtitle_bg.hide()

        self.x=100
        self.y=100

        from default import ClickableLabel
        self.smile = ClickableLabel("png/ev/.png", self)
        self.smile.setGeometry(1480, 20, self.x, self.y)
        self.smile.clicked.connect(self.on_click_smile)
        self.smile.setCursor(QCursor(Qt.PointingHandCursor))
        self.smile_click = False

        self.imprint = ClickableLabel("png/ev/.png", self)
        self.imprint.setGeometry(1480, 20, self.x, self.y)
        self.imprint.clicked.connect(self.on_click_imprint)
        self.imprint.setCursor(QCursor(Qt.PointingHandCursor))
        self.imprint_click = False

        self.hurt = ClickableLabel("png/ev/.png", self)
        self.hurt.setGeometry(1480, 20, self.x, self.y)
        self.hurt.clicked.connect(self.on_click_hurt)
        self.hurt.setCursor(QCursor(Qt.PointingHandCursor))
        self.hurt_click = False

        self.ink=ClickableLabel("png/ev/.png", self)
        self.ink.setGeometry(1480, 20, self.x, self.y)
        self.ink.clicked.connect(self.on_click_ink)
        self.ink.setCursor(QCursor(Qt.PointingHandCursor))
        self.ink_click = False



    def on_click_smile(self):
        popup= EvidencePopup(
            name="[남작의 웃음]",
            description="자살이 사인이라면, 남작은 왜 웃고있을까? 남작의 웃음은 모순적이다. 독살이나 약물 복용의 가능성을 열어보자.",
            parent=self
        )

        popup.exec_()
        self.smile_click=True

    def on_click_imprint(self):
        popup= EvidencePopup(
            name="[목이 졸린 흔적]",
            description="목에 남아있는 흔적의 형태를 보아선, 목줄이 목을 조른 시점에 남작은 이미 죽은 상태였을 것이다.",
            parent=self
        )

        popup.exec_()
        self.imprint_click=True

    def on_click_hurt(self):
        popup= EvidencePopup(
            name="[목의 자잘한 상처]",
            description="저항한 흔적이 있다. 몸싸움을 했던 것일까? 단순 자살이 아닐 가능성이 높다.",
            parent=self
        )

        popup.exec_()
        self.hurt_click=True

    def on_click_ink(self):
        popup= EvidencePopup(
            name="[옷에 묻어있는 잉크]",
            description="연회장에 잉크는 없다. 다른 장소에서 묻은 것일까?",
            parent=self
        )

        popup.exec_()
        self.ink_click=True

    def nextstage(self):
        if self.ink_click and self.imprint_click and self.smile_click and self.hurt_click:
            self.stack.setCurrentIndex(11)

class slect(App_default):
    def __init__(self, stack):
        super().__init__()
        self.stack= stack

        self.x=100
        self.y=100

        self.subtitle_bg.hide()

        self.background.setPixmap(QPixmap("png/.png").scaled(1600, 900))
        self.background.lower()  # 제일 뒤로

        from default import ClickableLabel
        self.study=ClickableLabel("png/.png", self)
        self.study.setGeometry(1480, 20, self.x, self.y)
        self.study.clicked.connect(self.on_click_study)
        self.study.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.storage=ClickableLabel("png/.png", self)
        self.storage.setGeometry(1480, 20, self.x, self.y)
        self.storage.clicked.connect(self.on_click_storage)
        self.storage.setCursor(QCursor(Qt.PointingHandCursor))

        self.bookstore=ClickableLabel("png/.png", self)
        self.bookstore.setGeometry(1480, 20, self.x, self.y)
        self.bookstore.clicked.connect(self.on_click_bookstore)
        self.bookstore.setCursor(QCursor(Qt.PointingHandCursor))

    def on_click_study(self):
        popup=EVPopup(
            description="이곳은 아닌 것 같다. 다시 생각해보자.",
            parent=self
        )
        popup.exec_()

    def on_click_storage(self):
        self.stack.setCurrentIndex(2)

    def on_click_bookstore(self):
        popup=EVPopup(
            description="이곳은 아닌 것 같다. 다시 생각해보자.",
            parent=self
        )
        popup.exec_()


class evidence2(App_default):
    def __init__(self, stack):
        super().__init__()
        self.stack=stack

        self.subtitle_bg.hide()

        self.background.setPixmap(QPixmap("png/.png").scaled(1600, 900))
        self.background.lower()  # 제일 뒤로

        self.x=100
        self.y=100

        from default import ClickableLabel
        self.glass = ClickableLabel("png/ev/glass.png", self)
        self.glass.setGeometry(180, 20, self.x, self.y)
        self.glass.clicked.connect(self.on_click_glass)
        self.glass.setCursor(QCursor(Qt.PointingHandCursor))

        self.pendant = ClickableLabel("png/ev/.png", self)
        self.pendant.setGeometry(1480, 20, self.x, self.y)
        self.pendant.clicked.connect(self.on_click_pendant)
        self.pendant.setCursor(QCursor(Qt.PointingHandCursor))

        self.handkerchief = ClickableLabel("png/ev/.png", self)
        self.handkerchief.setGeometry(1480, 20, self.x, self.y)
        self.handkerchief.clicked.connect(self.on_click_handkerchief)
        self.handkerchief.setCursor(QCursor(Qt.PointingHandCursor))

        self.glove = ClickableLabel("png/ev/.png", self)
        self.glove.setGeometry(1480, 20, self.x, self.y)
        self.glove.clicked.connect(self.on_click_glove)
        self.glove.setCursor(QCursor(Qt.PointingHandCursor))

        self.letter = ClickableLabel("png/ev/.png", self)
        self.letter.setGeometry(1480, 20, self.x, self.y)
        self.letter.clicked.connect(self.on_click_letter)
        self.letter.setCursor(QCursor(Qt.PointingHandCursor))

        self.back = ClickableLabel("png/button/ev/back.png", self)
        self.back.setGeometry(10, 10, self.x, self.y)
        self.back.clicked.connect(self.on_click_back)
        self.back.setCursor(QCursor(Qt.PointingHandCursor))
        
    def on_click_glass(self):
        popup = EvidencePopup(
        name="[유리병]",
        description="독이 들어있었던 유리병이다.",
        parent=self
    )
        popup.exec_()  # 팝업 띄우기 (닫을 때까지 대기)
    
    def on_click_pendant(self):
        popup= EvidencePopup(
            name="[펜던트]",
            description="붉은색의 보석이 눈에 띈다. 나비의 것으로 보인다.",
            parent=self
        )

        popup.exec_()

    def on_click_handkerchief(self):
        popup= EvidencePopup(
            name="[손수건]",
            description="검은색 손수건이다. 아래에 M이라는 자수가 새겨져있다. 모레타의 것일까?",
            parent=self
        )

        popup.exec_()
        

    def on_click_glove(self):
        popup= EvidencePopup(
            name="[흰 장갑]",
            description="남성용 흰 장갑이다. 오늘 연회에서 장갑을 낀 남성은 볼토와 콜롬비나 뿐이다.",
            parent=self
        )

        popup.exec_()

    def on_click_letter(self):
        popup= EvidencePopup(
            name="[의문의 쪽지]",
            description="\"서류는 잠시 가져가겠네.\"라는 글이 쓰여져있다. 누구의 것일까?",
            parent=self
        )

        popup.exec_()

    def on_click_back(self):
        self.stack.setCurrentIndex(2)


class EVPopup(QDialog):
    def __init__(self, description, parent=None):
        super().__init__(parent)
        self.setFixedSize(600, 200)
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
            self.global_font=QFont(self.font_family, 15)
        self.global_font.setBold(True)
        self.name_label.setFont(self.global_font)
        palette_name = self.name_label.palette()
        palette_name.setColor(QPalette.WindowText, QColor("white"))
        self.name_label.setPalette(palette_name)

        # 증거 설명
        self.desc_label = QLabel(description, self)
        self.desc_label.setGeometry(50, 100, 500, 80)
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