from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from default import App_default  

class ending(App_default):
    def __init__(self):
        super().__init__()
        
class TrueEnding(ending):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack # stack에 mainfront 클래스 저장
        
        self.label = QLabel("해피 엔딩", self) 
        self.label.setGeometry(50, 50, 200, 50)
        self.label.setAlignment(Qt.AlignCenter)

class FalseEnding(ending):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack # stack에 mainfront 클래스 저장

        self.message=["당신의 손가락이 가리킨 곳에서는 그저 비명 섞인 억울한 항변이 터져나왔다.",
                      "원한은 깊었으니 그들의 손에 피는 묻어있지 않았다.",
                      "억울한 희생자가 끌려가는 동안, 저 멀리 어둠 속에서 누군가 남은 와인을 비우며 조용히 미소지었다.",
                      "잘못 끼워진 퍼즐 조각은 결코 진실에 닿을 수 없다.",
                      "저택에 남은 것은 싸늘한 시신과, 영원히 가면 뒤에 숨어버린 진짜 괴물의 웃음소리뿐이다.",
                      "GAMEOVER - 당신은 진실을 놓쳤습니다."] #q=5
        

    def mousePressEvent(self, a0):
        if self.q==0:
            pass
        elif self.q==1:
            self.background.setPixmap(QPixmap("black.png").scaled(1600, 900))
            self.background.lower()  # 제일 뒤로
        elif self.q==5:
            self.background.setPixmap

class HiddenEnding(ending):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack # stack에 mainfront 클래스 저장

        self.message = ["진실이 밝혀졌다.",
                        "당신은 뒤도 돌아보지 않고 저택을 나섰다. 그의 등 뒤로는 화려했던 무도회장의 불빛이 하나 둘 꺼져가고 있었다.",
                        "남작이 탐욕으로 쌓아 올린 성벽은 진실이라는 단 하나의 균열 앞에 허망하게 무너져 내렸다.",
                        "무대는 끝났고, 배우는 사라졌으며, 이제 오직 진실만이 황폐한 저택의 객석을 지키고 있었다.",
                        "GAMECLEAR - 완벽한 거짓은 존재하지 않는다."]
    
    def mousePressEvent(self, a0):
        pass