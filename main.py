import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout

class Character:
    def __init__(self, age, name, communicationCount):
        self.age = age
        self.name= name
        self.communicationCount = communicationCount

    def communication(self):
        if self.communicationCount>0:
            self.communicationCount-=1
            return self.answer()
        return False

    def click(self):
        return self.communication()
    
    def answer(self):
        pass
        ## gemini 연결해서 창에 띄우기
        

class butterfly(Character):
    def __init__(self, age, name, communicationCount):
        super().__init__(age, name, communicationCount)


class volt(Character):
    def __init__(self, age, name, communicationCount):
        super().__init__(age, name, communicationCount)


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("가면 무도회")
        self.setFixedSize(1100,800)

        self.butterfly=QPushButton("나비",self)
        self.butterfly.setGeometry(50,50,1000,80)
        self.butterfly.clicked.connect(self.on_click_butterfly)

        self.volt=QPushButton("볼트", self)
        self.volt.setGeometry(50,140,1000,80)
        self.volt.clicked.connect(self.on_click_volt)


        self.cri1 = butterfly(age=20, name="나비", communicationCount=5)
        self.cri2 = volt(age=20, name="volt", communicationCount=5)

    def on_click_butterfly(self):
        return self.cri1.click()
    
    def on_click_volt(self):
        return self.cri2.click()
        


app=QApplication(sys.argv)
window=App()
window.show()
sys.exit(app.exec())