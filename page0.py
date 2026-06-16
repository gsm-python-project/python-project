from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from default import App_default


class prologue(App_default):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack # stack에 mainfront를 저장. (왜냐면 Widget에는 화면 전환 기능이 없어서 Widstackedwidget을 불러와야하기 때문에!)

        self.x=200
        self.y=100

        self.q=0

        self.background = QLabel(self)
        self.background.setGeometry(0, 0, 1600, 900)
        self.background.setPixmap(QPixmap("background.png").scaled(1600, 900))
        self.background.lower()  # 제일 뒤로

        # chapter1으로 넘어가는 버튼 설정
        self.btn_next_prologue = QPushButton("next", self) # 버튼 생성
        self.btn_next_prologue.setGeometry(1370, 765, self.x, self.y) # 버튼 크기 설정
        self.btn_next_prologue.clicked.connect(self.on_click_prologue) # 버튼과 함수를 연결
        self.btn_next_prologue.setCursor(QCursor(Qt.PointingHandCursor)) # 커서 변경
        self.btn_next_prologue.hide() # 버튼 숨기기
    
    def mousePressEvent(self, event):
        self.q+=1
        if self.q==0:
            pass
        elif self.q==1:
            pass
        elif self.q==2:
            pass
        elif self.q==3:
            pass
        else:
            self.btn_next_prologue.show()

    def on_click_prologue(self): # 버튼 클릭 시 인덱스가 1인 페이지로 넘어가게 해주는 함수
        self.stack.setCurrentIndex(1) 

