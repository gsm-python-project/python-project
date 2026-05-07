import tkinter as tk

class Character:
    def __init__(self, age, name):
        self.age = age
        self.name= name

    def communication():
        if click()==True:

            return 0
        

    def clik():
        pass
        

class butterfly(Character):
    def __init__(self, age, name):
        super().__init__(age, name)
    
    def communication():
        pass

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("가면 무도회")
        self.geometry("1000x800")

    

app=App()
app.mainloop()