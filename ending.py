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
        
        self.messages = ["",
                        "볼토는 한동안 아무말도 하지 않았다.",
                        "그리고 천천히 웃었다.",
                        "쓴웃음이었다.",
                        "가면 너머로 낮은 목소리가 흘러나왔다.",
                        "맞아. 남작은 내가 죽였어.",
                        "누군가는 그 자를 죽였을 거야. 그 자가 무슨 짓을 저지르고 다닌지 알기나 해?",
                        "잠시 침묵이 흘렀다.",
                        "볼토는 고개를 들어 남작이 죽은 서재를 바라보았다.",
                        "그 눈에는 분노도, 만족도 없었다.",
                        "그저 피로만 남아있을 뿐이었다.",
                        "나는 오늘 사과를 받으러 온 거야. 그 자가 내 어머니께 무슨 짓을 했는데. 그정도는 받을 자격 있잖아?",
                        "경비들이 그의 양팔을 붙잡았다. 볼토는 저항하지 않았다.",
                        "문을 나서기 직전, 그는 마지막으로 나를 돌아보았다.",
                        "그리고 조용히 말했다.",
                        "그는 끝까지 나를 모르더군.",
                        "문이 닫혔다.",
                        "그것이 볼토의 마지막 모습이었다.",
                        "...",
                        "진실이 밝혀졌다.",
                        "당신은 뒤도 돌아보지 않고 저택을 나섰다. 그의 등 뒤로는 화려했던 무도회장의 불빛이 하나 둘 꺼져가고 있었다.",
                        "남작이 탐욕으로 쌓아 올린 성벽은 진실이라는 단 하나의 균열 앞에 허망하게 무너져 내렸다.",
                        "무대는 끝났고, 배우는 사라졌으며, 이제 오직 진실만이 황폐한 저택의 객석을 지키고 있었다.",
                        "< 완벽한 거짓은 존재하지 않는다. >"]
        
        
        self.background.setPixmap(QPixmap("png/black.png").scaled(1600, 900))
        self.background.lower()  # 제일 뒤로

    
    def showEvent(self, a0):
        super().showEvent(a0)
        if self.stack.currentWidget() is self:
            self.play_bgm("bgm/TrueEnding.mp3")
    
    def mousePressEvent(self, a0):
        if self.typing:
            self._finish_typing_immediately()
            return
        if self.q==0:
            self.background.setPixmap(QPixmap("png/black.png").scaled(1600, 900))
            self.background.lower()  # 제일 뒤로
        elif self.q==22:
            self._typing_timer.setInterval(100)
            self.global_font=QFont(self.font_family, 27)
            self.subtitle.setFont(self.global_font)
            self.subtitle.setGeometry(200,370,1500,200)
        self.q+=1
        self._start_typing(self.q)


class FalseEnding(ending):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack # stack에 mainfront 클래스 저장
        

        self.background.setPixmap(QPixmap("png/black.png").scaled(1600, 900))
        self.background.lower()  # 제일 뒤로

        self.messages=["",
                      "당신의 손가락이 가리킨 곳에서는 그저 비명 섞인 억울한 항변이 터져나왔다.",
                      "원한은 깊었으나 그들의 손에 피는 묻어있지 않았다.",
                      "당신은 무언가 잘못되었음을 느꼈다.",
                      "억울한 희생자가 끌려가는 동안, 저 멀리 어둠 속에서 누군가 남은 와인을 비우며 조용히 미소지었다.",
                      "잘못 끼워진 퍼즐 조각은 결코 진실에 닿을 수 없다.",
                      "저택에 남은 것은 싸늘한 시신과, 영원히 가면 뒤에 숨어버린 진짜 괴물의 웃음소리뿐이다.",
                      "< 당신은 진실을 놓쳤습니다. >"] #q=5
        
    def showEvent(self, a0):
        super().showEvent(a0)
        if self.stack.currentWidget() is self:
            self.play_bgm("bgm/FalseEnding.mp3")

    def mousePressEvent(self, a0):
        if self.typing:
            self._finish_typing_immediately()
            return
        
        if self.q==0:
            pass
        elif self.q==1:
            pass
        elif self.q==4:
            
            self.background.setPixmap(QPixmap("png/falseending.png").scaled(1600, 900))
            self.background.lower()  # 제일 뒤로
        elif self.q==5:
            self._typing_timer.setInterval(100)
            self.global_font=QFont(self.font_family, 27)
            self.subtitle.setFont(self.global_font)
            self.subtitle.setGeometry(100,370,1500,200)
            
            palette = self.subtitle.palette()
            palette.setColor(QPalette.ColorRole.WindowText, QColor(161, 161, 161))
            self.subtitle.setPalette(palette)
            
        self.q+=1
        self._start_typing(self.q)


class HiddenEnding(ending):
    def __init__(self, stack):
        super().__init__()
        self.stack=stack

        self.messages=["",
                       "",
                       "제가 죽였습니다.",
                       "나비 씨의 팬던트도 제가 두었고, 검은색 손수건도 제것입니다.",
                       "하지만 몸싸움을 한 흔적이 있었고, 범인쪽이 우세해보였어요.",
                       "현장에 놓여있던 쪽지와, 흰 장갑이 있던 이유도 설명이 되지 않습니다!",
                       "... 그렇다면 그 팬던트와 제 손수건이 있던 이유는요?",
                       "선생님이라면 알아냈겠지만, 사인은 독살이죠. 제가 이걸 아는 이유가 뭐겠습니까. ",
                       "죄송합니다, 선생님.",
                       "...",
                       " 그렇게 모레타는 스스로 자백해 꽤나 큰 벌을 받게 되었다.",
                       "나는 그녀가 범인이라고 생각하지 않는다.",
                       "< 진실의 침묵. >"
                       ]
        
        self._start_typing(self.q)
        
        
    def mousePressEvent(self, a0):
        if self.typing:
            self._finish_typing_immediately()
            return
        
        if self.q==0:
            pass

        self.q+=1
        self._start_typing(self.q)

    def showEvent(self, a0):
        super().showEvent(a0)
        if self.stack.currentWidget() is self:
            self.play_bgm("bgm/HiddenEnding.mp3")