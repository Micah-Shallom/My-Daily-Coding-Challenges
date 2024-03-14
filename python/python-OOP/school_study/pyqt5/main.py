import sys
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication , QPushButton, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        button = QPushButton("Next")
        self.setFixedSize(QSize(800,600))
        self.setCentralWidget(button)

app = QApplication(sys.argv)
gui = MainWindow()
gui.show()
sys.exit(app.exec_())