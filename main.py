import sys
from PyQt5.QtWidgets import *

from default import Mainfront

app = QApplication(sys.argv)
window = Mainfront()
window.show()
sys.exit(app.exec_())  # PyQt5는 exec_() 사용