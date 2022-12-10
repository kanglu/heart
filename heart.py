from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPen, QColor, QBrush, QPainter, QPaintEvent
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import (Qt, pyqtSignal, pyqtProperty,
                          QEasingCurve, QPropertyAnimation,
                          QSequentialAnimationGroup)
import sys
import random
import math


class Heart(QtWidgets.QLabel):

    def __init__(self):
        super().__init__()
        self.canvasRect = (600, 450)
        self.margin = 40
        self.beatFrequency = 50
        self._curFrame = 0
        self.maxFrame = 30
        self.frame = []
        self.genDataPoints()
        self.initSetup()

    def getCurFrame(self):
        return self._curFrame

    def setCurFrame(self, value):
        if value != self._curFrame:
            self._curFrame = value
            self.update()

    curFrame = pyqtProperty(int, getCurFrame, setCurFrame)

    def addMistForPoint(self, points, size, x, y):
        for s in range(0, int(6 * size)):
            xo = random.gauss(0, 0.5) * 10
            yo = random.gauss(0, 0.5) * 10
            points.append((0, int(x + xo), int(y + yo)))

        for s in range(0, 5):
            xo = random.gauss(0, 3) * 10
            yo = random.gauss(0, 3) * 10
            points.append((1, int(x + xo), int(y + yo)))

    def genHeart(self, points, size, cf):
        m = int(2 * math.pi * 1000)

        for radMult in range(0, m, 30):
            r = radMult / 1000.0
            x = math.pow(math.sin(r), 3)
            y = -(13 * math.cos(r) - 5 * math.cos(2 * r) - 2 * math.cos(3 * r) - math.cos(4 * r)) / 16

            # transform the coordinates to the Qt canvas
            factor = 0.30 * size - (cf / self.maxFrame) * 0.05
            x = x * self.canvasRect[0] * factor + self.canvasRect[0] / 2.0
            y = y * self.canvasRect[0] * factor + self.canvasRect[0] / 3.0

            self.addMistForPoint(points, size, x, y)

    def genDataPoints(self):
        self.frame = []
        for cf in range(0, self.maxFrame + 1):
            points = []

            # for each frame we will create the heart shape with a guassian mist around
            # the general shape

            for perc in range(100, 70, -5):
                self.genHeart(points, perc / 100.0, cf)

            self.frame.append(points)

    def newCanvas(self):
        pixmap = QtGui.QPixmap(self.canvasRect[0], self.canvasRect[1])
        pixmap.fill(QColor(0, 0, 0))
        return pixmap

    def initSetup(self):

        self.setPixmap(self.newCanvas())

        brush = QBrush(QColor(231, 78, 189))
        pen = QPen(brush, 3, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
        pen2 = QPen(brush, 1.5, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
        self.pens = [pen, pen2]

        dur = int(self.beatFrequency * 1000 / 60)

        self.animation = QPropertyAnimation(self, b"curFrame")
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setStartValue(0)
        self.animation.setEndValue(30)
        self.animation.setDuration(dur)  # time in ms

        self.animation2 = QPropertyAnimation(self, b"curFrame")
        self.animation2.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation2.setStartValue(30)
        self.animation2.setEndValue(0)
        self.animation2.setDuration(dur)  # time in ms

        self.animations_group = QSequentialAnimationGroup()
        self.animations_group.addAnimation(self.animation)
        self.animations_group.addAnimation(self.animation2)
        self.animations_group.setLoopCount(-1)
        self.animations_group.start()

    def paintEvent(self, e: QPaintEvent):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        for (t, x, y) in self.frame[self.curFrame]:
            p.setPen(self.pens[t])
            p.drawPoint(x, y)
        p.end()


class MainWindow(QMainWindow):

    curFrameChanged = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self._curFrame = 0
        self.initSetup()

    def initSetup(self):
        self.setStyleSheet("background-color: black;")
        self.label = Heart()
        self.setCentralWidget(self.label)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.label.canvasRect = (self.label.frameGeometry().width(), self.label.frameGeometry().height())
        self.label.genDataPoints()
        return super().resizeEvent(a0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Heart from 点燃我，温暖你")
    window.show()
    sys.exit(app.exec_())
