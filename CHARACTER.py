
class Character: ## 캐릭터 기본 설정
    def __init__(self, age, name, communicationCount):
        self.age = age
        self.name= name
        self.communicationCount = communicationCount

    def communication(self): ## 여기서 대화 횟수를 확인하고 answer 함수로 넘어감
        if self.communicationCount>0:
            self.communicationCount-=1
            return self.answer()
        return self.answer_Fail()

    def answer(self):
        pass
        ## gemini 연결해서 창에 띄우기
        ## api key 받아와야함

    def answer_Fail(self):
        pass
        ## 오늘은 더이상 대화할 수 없습니다.<이런 안내멘트 띄워야함!

class butterfly(Character): ## 캐릭터 나비 가면 아직 구현 안됨
    def __init__(self, age=26, name="butterfly", communicationCount=5):
        super().__init__(age, name, communicationCount)

class volt(Character): ## 캐릭터 볼트 아직 구현 안됨
    def __init__(self, age=26, name="volt", communicationCount=5):
        super().__init__(age, name, communicationCount)

class colombina(Character):
    def __init__(self, age=27, name="colombina", communicationCount=5):
        super().__init__(age, name, communicationCount)

class crow(Character):
    def __init__(self, age=37, name="crow", communicationCount=3):
        super().__init__(age, name, communicationCount)
    
class moreta(Character):
    def __init__(self, age=18, name="moreta", communicationCount=3):
        super().__init__(age, name, communicationCount)
