import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic
import random


class Circle:
    def __init__(self, x, y, diameter):
        self.x = x
        self.y = y
        self.diameter = diameter


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.button = self.findChild(QWidget, 'button')
        self.button.clicked.connect(self.generate_circle)
        self.circles = []

    def generate_circle(self):
        x = random.randint(0, self.width() - 50)
        y = random.randint(0, self.height() - 50)
        diameter = random.randint(10, 100)
        circle = Circle(x, y, diameter)
        self.circles.append(circle)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(255, 255, 0))

        for circle in self.circles:
            painter.drawEllipse(circle.x, circle.y, circle.diameter, circle.diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
