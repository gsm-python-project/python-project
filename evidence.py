from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from default import App_default

class evidence(App_default):
    def __init__(self, stack):
        super().__init__()
        self.stack=stack

        self.background.setPixmap(QPixmap("png/.png").scaled(1600, 900))
        self.background.lower()  # 제일 뒤로

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
        self.smile_click=True

    def on_click_imprint(self):
        self.imprint_click=True

    def on_click_hurt(self):
        self.hurt_click=True

    def on_click_ink(self):
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
        pass

    def on_click_storage(self):
        self.stack.setCurrentIndex(12)

    def on_click_bookstore(self):
        pass


class evidence2(App_default):
    def __init__(self, stack):
        super().__init__()
        self.stack=stack

        self.background.setPixmap(QPixmap("png/.png").scaled(1600, 900))
        self.background.lower()  # 제일 뒤로

        self.x=100
        self.y=100

        from default import ClickableLabel
        self.glass = ClickableLabel("png/note.png", self)
        self.glass.setGeometry(1480, 20, self.x, self.y)
        self.glass.clicked.connect(self.on_click_glass)
        self.glass.setCursor(QCursor(Qt.PointingHandCursor))

        self.pendant = ClickableLabel("png/note.png", self)
        self.pendant.setGeometry(1480, 20, self.x, self.y)
        self.pendant.clicked.connect(self.on_click_pendant)
        self.pendant.setCursor(QCursor(Qt.PointingHandCursor))

        self.handkerchief = ClickableLabel("png/note.png", self)
        self.handkerchief.setGeometry(1480, 20, self.x, self.y)
        self.handkerchief.clicked.connect(self.on_click_handkerchief)
        self.handkerchief.setCursor(QCursor(Qt.PointingHandCursor))

        self.glove = ClickableLabel("png/note.png", self)
        self.glove.setGeometry(1480, 20, self.x, self.y)
        self.glove.clicked.connect(self.on_click_glove)
        self.glove.setCursor(QCursor(Qt.PointingHandCursor))

        self.letter = ClickableLabel("png/note.png", self)
        self.letter.setGeometry(1480, 20, self.x, self.y)
        self.letter.clicked.connect(self.on_click_letter)
        self.letter.setCursor(QCursor(Qt.PointingHandCursor))
        
    def on_click_glass(self):
        pass
    
    def on_click_pendant(self):
        pass

    def on_click_handkerchief(self):
        pass

    def on_click_glove(self):
        pass

    def on_click_letter(self):
        pass


class EvidencePopup(QDialog):
    def __init__(self, name, description, popup_image_path, parent=None):
        super().__init__(parent)
        self.setFixedSize(700, 500)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 타이틀바 제거

        # 배경색
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(30, 30, 30))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # 증거 이름 (오른쪽 상단)
        self.name_label = QLabel(name, self)
        self.name_label.setGeometry(360, 40, 300, 60)
        self.name_label.setWordWrap(True)

        self.global_font.setBold(True)
        self.name_label.setFont(self.global_font)
        palette_name = self.name_label.palette()
        palette_name.setColor(QPalette.WindowText, QColor("white"))
        self.name_label.setPalette(palette_name)

        # 증거 설명 (오른쪽 중간)
        self.desc_label = QLabel(description, self)
        self.desc_label.setGeometry(360, 120, 300, 250)
        self.desc_label.setWordWrap(True)
        self.desc_label.setAlignment(Qt.AlignTop)
        self.desc_label.setFont(self.global_font)
        palette_desc = self.desc_label.palette()
        palette_desc.setColor(QPalette.WindowText, QColor(200, 200, 200))
        self.desc_label.setPalette(palette_desc)

        # 닫기 버튼 (오른쪽 하단)
        self.close_btn = QPushButton("닫기", self)
        self.close_btn.setGeometry(560, 430, 100, 40)
        self.close_btn.clicked.connect(self.close)
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))