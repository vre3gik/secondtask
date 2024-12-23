import sys
from random import randint
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QMainWindow, QApplication
from ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.risovat = False
        self.gothis.clicked.connect(self.createellipse)

    def paintEvent(self, event):
        if self.risovat:
            paint = QPainter()
            paint.begin(self)
            self.draw(paint)
            paint.end()

    def draw(self, paint):
        paint.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        radius = randint(0, 500)
        paint.drawEllipse(randint(0, 600 - radius), randint(0, 600 - radius), radius, radius)
        self.risovat = False

    def createellipse(self):
        self.risovat = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
