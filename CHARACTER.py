from PyQt5.QtWidgets import *
import sys

class Character:
    def __init__(self, age, name, communicationCount):
        self.age = age # 인물의 나이
        self.name = name # 인물의 이름
        self.communicationCount = communicationCount # 대화 횟수

    def communication(self):
        if self.communicationCount > 0: # 만약 대화 횟수가 0보다 크다면 대답하고, 아니라면 대화 ㄴㄴ 팝업창 띄우기
            self.communicationCount -= 1
            return self.answer() # answer() 함수 호출
        return self.answer_Fail() # answer_Fail() 함수 호출

    def answer(self):
        pass
        # gemini API 키 받아와야함
        # 프롬포트 입력!!

    def answer_Fail(self):
        self.w = Answer_Fail() # Answer_Fail() 클래스 불러오기
        self.w.exec_()  # Answer_Fail() 클래스 실행
        
class butterfly(Character):
    def __init__(self, age=26, name="butterfly", communicationCount=5): # 나이, 이름, 대화 횟수 결정
        super().__init__(age, name, communicationCount)

    def answer(self):
        print("butterfly") # 임의로 정해놓은 테스트 코드!! 바꿀 예정

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

class Answer_Fail(QDialog): # 대화 횟수가 0일 때 살행하는 팝업창
    def __init__(self, parent=None): # Parent를 받지 않아도 실행 ㄱㄴ, 반대로 받아도 실행 가능
        super().__init__(parent)

        self.setWindowTitle("") # 팝업창의 이름
        self.resize(300, 150)# 팝업창의 사이즈

        layout = QVBoxLayout()
        self.label = QLabel("오늘은 더이상 대화할 수 없습니다.") # 팝업창 문구
        self.btn_close = QPushButton("닫기") # 닫기 버튼 생성
        self.btn_close.resize(20, 50) # 받기 버튼의 사이즈
        self.btn_close.clicked.connect(self.close) # close 내장 함수와 연결

        layout.addWidget(self.label)
        layout.addWidget(self.btn_close)
        self.setLayout(layout)