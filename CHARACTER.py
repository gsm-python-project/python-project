from PyQt5.QtWidgets import *
import sys

class Character:
    def __init__(self, age, name, communicationCount):
        self.age = age
        self.name = name
        self.communicationCount = communicationCount

    def communication(self):
        if self.communicationCount > 0:
            self.communicationCount -= 1
            return self.answer()
        return self.answer_Fail()

    def answer(self):
        pass

    def answer_Fail(self):
        self.w = Answer_Fail()
        self.w.exec_()  # PyQt5는 exec_() 사용
        
class butterfly(Character):
    def __init__(self, age=26, name="butterfly", communicationCount=5):
        super().__init__(age, name, communicationCount)

    def answer(self):
        print("butterfly")

class volt(Character):
    def __init__(self, age=26, name="volt", communicationCount=5):
        super().__init__(age, name, communicationCount)

    def answer(self):
        print("volt")

class colombina(Character):
    def __init__(self, age=27, name="colombina", communicationCount=5):
        super().__init__(age, name, communicationCount)

    def answer(self):
        print("colombina")

class crow(Character):
    def __init__(self, age=37, name="crow", communicationCount=3):
        super().__init__(age, name, communicationCount)

    def answer(self):
        print("crow")

class moreta(Character):
    def __init__(self, age=18, name="moreta", communicationCount=3):
        super().__init__(age, name, communicationCount)

    def answer(self):
        print("test")

class Answer_Fail(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("")
        self.resize(300, 150)

        layout = QVBoxLayout()
        self.label = QLabel("오늘은 더이상 대화할 수 없습니다.")
        self.btn_close = QPushButton("닫기")
        self.btn_close.resize(20, 50)
        self.btn_close.clicked.connect(self.close)

        layout.addWidget(self.label)
        layout.addWidget(self.btn_close)
        self.setLayout(layout)