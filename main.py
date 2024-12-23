import sys
import io
from random import randint
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>600</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>yellowellipse</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="gothis">
    <property name="geometry">
     <rect>
      <x>250</x>
      <y>250</y>
      <width>100</width>
      <height>100</height>
     </rect>
    </property>
    <property name="text">
     <string>РИСОВАТЬ</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>399</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.risovat = False
        self.gothis.clicked.connect(self.createellipse)

    def paintEvent(self, event):
        if self.risovat:
            paint = QPainter()
            paint.begin(self)
            self.draw(paint)
            paint.end()

    def draw(self, paint):
        paint.setBrush(QColor("yellow"))
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
