import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout

from page0 import prologue
from page1 import Chapter1
from page2 import Chapter2



app=QApplication(sys.argv) # 앱 관리자. 얘 없이 창만 만들면 오류남!
window=Chapter1() # 실제 앱
window.show()
sys.exit(app.exec()) # mainloop를 만듦. 창이 자기 맘대로 꺼지지 않게