from PyQt5.QtWidgets import QApplication #піключення модулей
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QFileDialog
from ui import Ui_MainWindow
class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
app = QApplication([]) #створення додадку
ex = Widget() #створення віджету
ex.show() #показ вікна




app.exec_() #закриття додатку
