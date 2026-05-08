
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout
from CHARACTER import butterfly, volt, colombina

class App_default(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("가면 무도회") # 창 이름
        self.setFixedSize(1100,800) # 창 사이즈, setFixedSize는 창 크기 수정이 불가능하게 만들어줌

class Button(App_default):
    def __init__(self):
        super().__init__()

        self.x=1000
        self.y=80
        self.butterfly=QPushButton("나비",self) # 나비 버튼. 아직 UI 구현 안됨
        self.butterfly.setGeometry(50,50,1000,80)
        self.butterfly.clicked.connect(self.on_click_butterfly)

        self.volt=QPushButton("볼트", self) # 볼트 버튼. 아직 UI 구현 안됨
        self.volt.setGeometry(50,140,1000,80)
        self.volt.clicked.connect(self.on_click_volt)

        self.colombina=QPushButton("콜롬비나", self)
        self.colombina.setGeometry(50,230,self.x,self.y)

        self.cri1 = butterfly(age=20, name="나비", communicationCount=5) # 캐릭터 불러오기
        self.cri2 = volt(age=20, name="volt", communicationCount=5)
        self.cri3 = colombina(age=20, name=colombina, communicationCount=5)

    def on_click_butterfly(self): # 나비 버튼을 눌렀을 때 Character class의 communication 함수를 호출
        return self.cri1.communication()
    
    def on_click_volt(self):
        return self.cri2.communication()
    
    def on_click_colombina(self):
        return self.cri3.communication()
        
