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

        self.messages = [
            "화려한 샹들리에 아래, 최고 부자로 소문난 남작의 가면 무도회에 초대된 당신은 아끼던 휴가까지 써가며 이 대저택에 왔다.",
            "기대에 걸맞은 화려함과 여러 사치품, 그리고 가면을 쓴 귀족들의 웃음 소리가 연회장을 가득 채우고 있었다.",  # q==1: 대사 없음
            "...", 
            "어느순간 남작이 보이지 않았다.",# q==3            
            "화려한 저택에 발을 들이자마자 들렸던 그 활기찬 소리는 마치 누군가 목을 조른 듯 어느 한 순간에 멎어버렸다.",  # q==4
            "무언가 일어날 것만 같은 예감이 들었다.", # q==5
            "예고도 없이 찾아온 칠흑같은 어둠.",  # q==6
            "세상은 단 3초 동안 숨을 죽였다.",
            "3초가 지나가고 무심하게 켜진 조명은 오로지 한 곳을 비추었다.", #q==7
            "파티의 주인공이자 탐욕스러운 지배자, 남작의 자리였다.",
            "범인은 이 짧은 찰나를 이용해 남작의 숨을 끊어놓았다. 완벽하게 계산된 어둠, 그리고 그 속에서 춤추듯 움직인 살의. 가장 화려한 순간에 시작된 가장 비극적인 무대.",
            "이제 당신은 이 아수라장 속에서 흩어진 증거를 찾아 첫 번째 발자국을 떼어야한다.",
            "과연 이 3초의 어둠 속에서 진실은 어디로 사라진 것일까?",
            "현재 알 수 있는 건 용의자 3명과 목격자 2명의 프로필 뿐이다.",
            "수수께끼의 진실은 당신에게 달려있다."
        ]
        
        self.background.setPixmap(QPixmap("png/prologue/prologue1.png").scaled(1600, 900))
        self.background.lower()  # 제일 뒤로

        # chapter1으로 넘어가는 버튼 설정
        self.btn_next_prologue = QPushButton("next", self) # 버튼 생성
        self.btn_next_prologue.setGeometry(1370, 765, self.x, self.y) # 버튼 크기 설정
        self.btn_next_prologue.clicked.connect(self.on_click_prologue) # 버튼과 함수를 연결
        self.btn_next_prologue.setCursor(QCursor(Qt.PointingHandCursor)) # 커서 변경
        self.btn_next_prologue.hide() # 버튼 숨기기


    def showEvent(self, a0):
        super().showEvent(a0)
        self.play_bgm("bgm/prologue.mp3")
        self._start_typing(self.q)
        

    def mousePressEvent(self, event):
        if self.typing:
            self._finish_typing_immediately()
            return
        
        if self.q==0:
            self.background.setPixmap(QPixmap("png/prologue/prologue2.png").scaled(1600, 900))
            self.background.lower()  # 제일 뒤로
            
        elif self.q==3:
            self.background.setPixmap(QPixmap("png/bg/black.png").scaled(1600, 900))
            self.background.lower()  # 제일 뒤로
        elif self.q==7:
            self.stop_bgm()
            self.play_bgm("bgm/prologue1.mp3")
            self.background.setPixmap(QPixmap("png/prologue/prologue3.png").scaled(1600, 900))
            self.background.lower()  # 제일 뒤로
        elif self.q==12:
            self.background.setPixmap(QPixmap("png/bg/black.png").scaled(1600, 900))
            self.background.lower()  # 제일 뒤로
        elif self.q==14:
            self.btn_next_prologue.show()
    
        self.q+=1
        self._start_typing(self.q)

    def on_click_prologue(self): # 버튼 클릭 시 인덱스가 1인 페이지로 넘어가게 해주는 함수
        self.stop_bgm()
        self.stack.setCurrentIndex(1) 
