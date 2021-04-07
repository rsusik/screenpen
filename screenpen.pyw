#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Author:       Robert Susik
# License:      MIT
# Email:        robert.susik@gmail.com
# ----------------------------------------------------------------------------

import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QToolBar, QAction, QDialog
from PyQt5.QtGui import QIcon, QScreen

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QLineEdit,
    QPlainTextEdit
)

import numpy as np

from matplotlib.backends.qt_compat import QtCore, QtWidgets
if QtCore.qVersion() >= "5.":
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

import win32api
import win32con
import win32gui
# https://stackoverflow.com/questions/58157159/making-a-fullscreen-paint-program-with-transparent-background-of-my-application
class MyWidget(QtWidgets.QMainWindow):
    def __init__(self, pixmap: QtGui.QPixmap = None): # app: QApplication
        super().__init__()
        #self.setGeometry(30,30,600,400)
        #self.setGeometry(300, 300, 280, 270)
        #self.setStyleSheet("background:transparent")
        #self.setAttribute(Qt.WA_TranslucentBackground)
        #self.showMaximized()
        #self.show()
        
        print(pixmap.size())
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        avGeom = QtWidgets.QDesktopWidget().screenGeometry()
        print(avGeom)
        print(self.size())
        #avGeom.setY(avGeom.y() - 30)
        #avGeom.setY(avGeom.y())
        self.setGeometry(avGeom)
        #self.setGeometry(30, 30, 400, 400)
        #self.setGeometry(30, 30, 400, 400)
        self.activateWindow()
        #self.raise()
        #self.showMaximized()
        self.show()
        

        self.imageDraw = QtGui.QImage(self.size(), QtGui.QImage.Format_ARGB32)
        #self.imageDraw.fill(QtCore.Qt.transparent)
        qp = QtGui.QPainter(self.imageDraw)
        qp.drawPixmap(self.imageDraw.rect(), pixmap, pixmap.rect())
        qp.end()
        
        self.imageDraw_bck = QtGui.QImage(self.size(), QtGui.QImage.Format_ARGB32)
        qp2 = QtGui.QPainter(self.imageDraw_bck)
        qp2.drawPixmap(self.imageDraw_bck.rect(), pixmap, pixmap.rect())
        qp2.end()

        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.lastPoint = QtCore.QPoint()

        
        self.drawing = False
        self.curr_method = 'drawPath'
        self.curr_color = Qt.red #QtGui.QColor(100, 10, 10, 0)
        self.curr_style = Qt.SolidLine
        self.curr_capstyle = Qt.RoundCap
        self.curr_joinstyle = Qt.RoundJoin
        self.curr_width = 3
        self.curr_br = QtGui.QBrush(self.curr_color)
        self.curr_pen = QtGui.QPen() # self.color, 3, Qt.SolidLine
        self._setupTools()


        self._createToolBars()

        from datetime import datetime
        #self.setAttribute(Qt.WA_TranslucentBackground, True)

        fuchsia = (0, 0, 0)  # Transparency color
        hwnd = self.winId()
        print(f'pos: {self.pos()}')
        print(f'width: {self.width()}, height: {self.height()}')
        

        #win32gui.SetWindowLong (hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong (hwnd, win32con.GWL_EXSTYLE ) | win32con.WS_EX_LAYERED ) #  win32con.WS_EX_TRANSPARENT | win32con.WS_EX_LAYERED |
        #win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 90, win32con.LWA_COLORKEY) 
        #win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 90, win32con.LWA_ALPHA)
        #win32gui.SetWindowLong (hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong (hwnd, win32con.GWL_EXSTYLE ) | win32con.WS_TILEDWINDOW )
        #win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_ALPHA)

        #self.setAttribute(Qt.WA_NoSystemBackground, True)
        #self.setAttribute(Qt.WA_TranslucentBackground, True)
        #self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setStyleSheet("background:transparent")
        #self.setAttribute(Qt.WA_NoMousePropagation, True)
        #self.setAttribute(Qt.WA_AcceptTouchEvents, True)
        #self.setAttribute(Qt.WA_InputMethodEnabled, True)
        
    def drawChart(self, qp:QtGui.QPainter, p1:QtCore.QPoint):
        fig = Figure((6, 4))
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        x = np.linspace(0, 9, 256)
        y = np.sin(x)
        ax.plot(x, y)
        ax.grid(True)
        canvas.draw()
        self.drawMatplotlib(qp, canvas, p1)

    def drawMatplotlib(self, qp:QtGui.QPainter, canvas:FigureCanvas, p1:QtCore.QPoint):
        size = canvas.size()
        width, height = size.width(), size.height()
        im = QtGui.QImage(canvas.buffer_rgba(), width, height, QtGui.QImage.Format_ARGB32)
        p2 = QtCore.QPoint(p1.x()+width, p1.y()+height) 
        qp.drawImage(QtCore.QRect(
            p1, 
            p2
        ), im, im.rect())

    def _setupTools(self):
        self.curr_br.setColor(self.curr_color)
        self.curr_pen.setStyle(self.curr_style)
        self.curr_pen.setCapStyle(self.curr_capstyle)
        self.curr_pen.setJoinStyle(self.curr_joinstyle)
        self.curr_pen.setBrush(self.curr_br)
        self.curr_pen.setWidth(self.curr_width)

    def setColor(self, color):
        def _setColor():
            self.curr_color = color
            self._setupTools()
        
        return _setColor

    def setWidth(self, color=None, width=None):
        def _setWidth():
            self.curr_width = width
            self._setupTools()
        
        return _setWidth

    def setAction(self, action):
        def _setAction():
            self.curr_method = action
        
        return _setAction

    class CustomDialog(QDialog):
        def ok_success(self, *args):
            print(args)
            exec(self.code.toPlainText(), {'self': self.parent, **globals()})
            self.accept()

        def __init__(self, parent=None):
            super().__init__(parent=parent)
            self.parent = parent
            self.setStyleSheet("background:silver")
            self.setWindowTitle("Chart")

            QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

            self.buttonBox = QDialogButtonBox(QBtn)
            self.buttonBox.accepted.connect(self.ok_success)
            self.buttonBox.rejected.connect(self.reject)

            self.code    = QPlainTextEdit()
            self.code.setPlainText('''
def drawChart(qp:QtGui.QPainter, p1:QtCore.QPoint):
    fig = Figure((6, 4))
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    ###### YOU CAN CREATE CUSTOM CHART HERE ######
    x = np.linspace(0, 9, 256)
    y = np.sin(x)
    ax.plot(x, y)
    ax.grid(True)
    ##############################################
    canvas.draw()
    self.drawMatplotlib(qp, canvas, p1)
setattr(self, 'drawChart', drawChart)
            ''')

            self.layout = QVBoxLayout()
            self.layout.addWidget(self.buttonBox)
            self.layout.addWidget(self.code)
            self.setLayout(self.layout)

    def showChart(self):
        def _showChart():
            dlg = self.CustomDialog(self)
            if dlg.exec_():
                self.curr_method = 'drawChart'
            else:
                pass
        
        return _showChart

    def addAction(self, name, icon, fun):
        action = QAction(icon, name, self)
        action.triggered.connect(fun)
        return action


    def _createToolBars(self):
        penToolBar = QToolBar("Color", self)
        penToolBar.setStyleSheet("background-color: #eee;")
        self.addToolBar(penToolBar)
        penToolBar.addAction(
            self.addAction("&ColorGreen",QIcon("./img/green.svg"),self.setColor(Qt.green))
        )
        penToolBar.addAction(
            self.addAction("&ColorRed",QIcon("./img/red.svg"),self.setColor(Qt.red))
        )
        penToolBar.addAction(
            self.addAction("&ColorBlue",QIcon("./img/blue.svg"),self.setColor(Qt.blue))
        )
        penToolBar.addAction(
            self.addAction("&ColorYellow",QIcon("./img/yellow.svg"),self.setColor(QtGui.QColor(240, 240, 0)))
        )
        penToolBar.addAction(
            self.addAction("&ColorViolet",QIcon("./img/violet.svg"),self.setColor(QtGui.QColor(118, 0, 191)))
        )

        penToolBar.addAction(
            self.addAction("&WidthThin",QIcon("./img/thin.svg"),self.setWidth(width=3))
        )
        penToolBar.addAction(
            self.addAction("&WidthMedium",QIcon("./img/medium.svg"),self.setWidth(width=9))
        )
        penToolBar.addAction(
            self.addAction("&WidthThick",QIcon("./img/thick.svg"),self.setWidth(width=27))
        )

        actionBar = QToolBar("Action", self)
        actionBar.setStyleSheet("background-color: #eee;")
        self.addToolBar(actionBar)
        actionBar.addAction(
            self.addAction("&ShapeLine",QIcon("./img/line.svg"),self.setAction('drawPath'))
        )
        actionBar.addAction(
            self.addAction("&ShapeRect",QIcon("./img/rect.svg"),self.setAction('drawRect'))
        )
        actionBar.addAction(
            self.addAction("&Chart",QIcon("./img/chart.png"),self.showChart())
        )

        

    def scaleCoords(self, coords):
        canvas_size = self.imageDraw.size()
        window_size = self.size()
        x_scale = canvas_size.width() / window_size.width()
        y_scale = canvas_size.height() / window_size.height()
        return QtCore.QPoint(coords.x()*x_scale, coords.y()*y_scale)

    def paintEvent(self, event):
        qp = QtGui.QPainter(self.imageDraw)
        canvasPainter = QtGui.QPainter(self)

        qp.setCompositionMode (QtGui.QPainter.CompositionMode_Source)
        canvasPainter.setCompositionMode (QtGui.QPainter.CompositionMode_Source)


        if Qt.LeftButton and self.drawing:
            qp.setPen(self.curr_pen)
            qp.setBrush(self.curr_br)
            if self.curr_method in ['drawRect']:
                qp.setBrush(Qt.NoBrush)
                self.curr_args = [QtCore.QRect(self.begin, self.end)]
                qp.drawImage(self.imageDraw.rect(), self.imageDraw_bck, self.imageDraw_bck.rect())
                
                getattr(qp, self.curr_method)(*self.curr_args)
                qp.setBrush(self.curr_br)

            elif self.curr_method in ['drawChart']:
                qp.drawImage(self.imageDraw.rect(), self.imageDraw_bck, self.imageDraw_bck.rect())
                self.drawChart(qp, self.end)

            elif self.curr_method in ['drawPath']:
                if self.lastPoint != self.end:
                    qp.setBrush(Qt.NoBrush)
                    qp.setPen(self.curr_pen)
                    self.path.cubicTo(self.end, self.end, self.end)
                    self.curr_args = [self.path]
                    getattr(qp, self.curr_method)(*self.curr_args)
                    self.lastPoint = self.end
                    self.update()
                    qp.setBrush(self.curr_br)

        qp.setCompositionMode (QtGui.QPainter.CompositionMode_SourceOver)
        qp.end()
        
        canvasPainter.drawImage(self.rect(), self.imageDraw, self.imageDraw.rect())
        canvasPainter.setCompositionMode (QtGui.QPainter.CompositionMode_SourceOver)

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            exit()
        if event.button() == Qt.LeftButton:
            self.drawing = True
        if self.curr_method in ['drawRect', 'drawChart']:
            qp = QtGui.QPainter(self.imageDraw_bck)
            qp.drawImage(self.imageDraw_bck.rect(), self.imageDraw, self.imageDraw.rect())
            qp.end()
            self.begin = self.scaleCoords(event.pos())
            self.end = self.scaleCoords(event.pos())
            
        elif self.curr_method in ['drawPath']:
            self.path = QtGui.QPainterPath()
            self.begin = self.scaleCoords(event.pos())
            self.end = self.scaleCoords(event.pos())
            self.path.moveTo(self.begin)
            self.lastPoint = self.scaleCoords(event.pos())
        self.update()

    def mouseMoveEvent(self, event):
        self.end = self.scaleCoords(event.pos())
        self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False
            self.path = None

            self.begin = self.scaleCoords(event.pos())
            self.end = self.scaleCoords(event.pos())



            self.update()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    #date = datetime.now()
    #filename = date.strftime('%Y-%m-%d_%H-%M-%S.jpg')
    #QScreen.grabWindow(app.primaryScreen(), QApplication.desktop().winId(), self.pos().x(), self.pos().y(), self.width(), self.height()).save(filename, 'png')
    
    pixmap = QScreen.grabWindow(
        app.primaryScreen(), 
        QApplication.desktop().winId(), 
        0, 
        0, 
        app.primaryScreen().size().width(), 
        app.primaryScreen().size().height()
    )#.save('screen.png', 'png')
        
    window = MyWidget(pixmap)
    sys.exit(app.exec_())