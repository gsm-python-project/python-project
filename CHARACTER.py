from PyQt5.QtWidgets import *
from google import genai
import os
from dotenv import load_dotenv

class Character:
    def __init__(self, age=None, name=None, communicationCount=None):
        self.age = age # 인물의 나이
        self.name = name # 인물의 이름
        self.communicationCount = communicationCount # 대화 횟수
        self.history=[]
        load_dotenv()
        self.client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))
        self.chat =None

    def communication(self, user_input):
        if self.communicationCount > 0: # 만약 대화 횟수가 0보다 크다면 대답하고, 아니라면 대화 ㄴㄴ 팝업창 띄우기
            self.communicationCount -= 1
            return self.answer(user_input) # answer() 함수 호출
        return self.answer_Fail() # answer_Fail() 함수 호출

    def answer(self, user_input):
        if self.chat is None:
            self.chat = self.client.chats.create(
            model="gemini-2.0-flash",
            config={
                "system_instruction": self.prompt,
                "max_output_tokens": 100}
        )
        try:
            response= self.chat.send_message(user_input)
            self.history.append(("나", user_input))         # 메모리에 저장
            self.history.append((self.name, response.text)) # 메모리에 저장
            return response.text
        except Exception as e:
            return "잠시 후 다시 시도해주세요."  # 오류나도 앱 안 죽음
    
    def answer_Fail(self):
        self.w = Answer_Fail() # Answer_Fail() 클래스 불러오기
        self.w.exec_()  # Answer_Fail() 클래스 실행
        
class butterfly(Character):
    def __init__(self, age=26, name="butterfly", communicationCount=5): # 나이, 이름, 대화 횟수 결정
        self.prompt="" #캐릭터 prompt 설정
        super().__init__(age, name, communicationCount)

    def answer(self, user_input):
        print("butterfly")
        response = super().answer(user_input)
        return response

class volt(Character):
    def __init__(self, age=26, name="volt", communicationCount=5):
        self.prompt=""
        super().__init__(age, name, communicationCount)
        

    def answer(self, user_input):
        print("volt")
        response = super().answer(user_input)
        return response

class colombina(Character):
    def __init__(self, age=27, name="colombina", communicationCount=1):
        self.prompt=""
        super().__init__(age, name, communicationCount)
        

    def answer(self, user_input):
        print("colombina")
        response = super().answer(user_input)
        return response

class crow(Character):
    def __init__(self, age=37, name="crow", communicationCount=3):
        self.prompt=""
        super().__init__(age, name, communicationCount)
        

    def answer(self, user_input):
        print("crow")
        response = super().answer(user_input)
        return response

class moreta(Character):
    def __init__(self, age=18, name="moreta", communicationCount=3):
        self.prompt=""
        super().__init__(age, name, communicationCount)

    def answer(self, user_input):
        print("test")
        response = super().answer(user_input)
        return response

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