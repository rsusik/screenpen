#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Author:       Robert Susik
# Email:        robert.susik@gmail.com
# ----------------------------------------------------------------------------

#from .version import __version__  # noqa: F401,E402

import pkg_resources

try:
    import PyQt5
    print("PyQt5 is installed.")
    pyqt_version = 5
except ImportError:
    try:
        import PyQt6
        print("PyQt6 is installed.")
        pyqt_version = 6
    except ImportError:
        print("PyQt5 nor PyQt6 is installed.")
        print("Please install PyQt5 or PyQt6 by running:")
        print("pip install PyQt5")
        print("or")
        print("pip install PyQt6")
        print("Exiting...")
        exit(1)


try:
    pkg_resources.get_distribution("PySide6")
    print('\033[41m', end='')
    print('=========================> WARNING <===========================')
    print('>       PySide6 is installed but PyQt5 only is expected.      <')
    print('>          Errors may appear. Please remove PySide6.          <')
    print('===============================================================\033[0m')
except pkg_resources.DistributionNotFound:
    pass

import subprocess
import sys
from datetime import datetime

if pyqt_version == 5:
    from PyQt5 import QtGui
    from PyQt5 import QtWidgets
    from PyQt5 import QtCore
    from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
    from PyQt5.QtCore import QPoint, Qt, QSize
    from PyQt5.QtWidgets import QToolBar, QAction, QDialog, QToolButton, QMenu, QColorDialog
    from PyQt5.QtGui import (
        QIcon, QScreen, QPalette, QColor, QCursor,
        QSyntaxHighlighter, QPixmap, QKeySequence
    )

    from PyQt5.QtWidgets import (
        QApplication, QDialog, QDialogButtonBox, QLabel, QMainWindow,
        QPushButton, QVBoxLayout, QListWidget, QListWidgetItem, QFormLayout,
        QHBoxLayout, QGridLayout,
        QLineEdit, QPlainTextEdit,
        QShortcut
    )

    def _create_palette():
        return QPalette()
    
    PALETTE_PROPS = {
        'window': QPalette.Window,
        'windowText': QPalette.WindowText,
        'base': QPalette.Base,
        'alternateBase': QPalette.AlternateBase,
        'toolTipBase': QPalette.ToolTipBase,
        'toolTipText': QPalette.ToolTipText,
        'text': QPalette.Text,
        'button': QPalette.Button,
        'buttonText': QPalette.ButtonText,
        'brightText': QPalette.BrightText,
        'link': QPalette.Link,
        'highlight': QPalette.Highlight,
        'highlightedText': QPalette.HighlightedText,
    }

    def _get_color_from_RGB(r, g, b):
        return QColor(r, g, b)

    def _set_palette_color(palette, property, value):
        return palette.setColor(property, value)
    
    # _set_palette_color(_create_palette(), PALETTE_PROPS['window'], _get_color_from_RGB(53, 53, 53))
    
    ALIGNMENT = {
        'center': QtCore.Qt.AlignCenter,
        'left': QtCore.Qt.AlignLeft,
        'right': QtCore.Qt.AlignRight,
    }

    COLORS = {
        'black': Qt.black,
        'white': Qt.white,
        'red': Qt.red,
        'green': Qt.green,
        'blue': Qt.blue,
        'cyan': Qt.cyan,
        'magenta': Qt.magenta,
        'yellow': Qt.yellow,
        'gray': Qt.gray,
        'darkGray': Qt.darkGray,
        'lightGray': Qt.lightGray,
        'transparent': Qt.transparent,
        'darkRed': Qt.darkRed,
        'darkGreen': Qt.darkGreen,
        'darkBlue': Qt.darkBlue,
        'darkCyan': Qt.darkCyan,
        'darkMagenta': Qt.darkMagenta,
        'darkYellow': Qt.darkYellow,
    }

    def _execute_dialog(dlg):
        return dlg.exec_()
    
    WINDOW_ATTRS = {
        'translucentBackground': QtCore.Qt.WA_TranslucentBackground,
    }

    IMAGE_FORMATS = {
        'ARGB32': QtGui.QImage.Format_ARGB32,
    }

    PEN_STYLES = {
        'solidLine': Qt.SolidLine,
        'dashLine': Qt.DashLine,
        'dotLine': Qt.DotLine,
        'dashDotLine': Qt.DashDotLine,
        'roundCap': Qt.RoundCap,
        'squareCap': Qt.SquareCap,
        'flatCap': Qt.FlatCap,
        'roundJoin': Qt.RoundJoin,
    }

    TOOLBAR_AREAS = {
        'leftToolBarArea': Qt.LeftToolBarArea,
        'rightToolBarArea': Qt.RightToolBarArea,
        'topToolBarArea': Qt.TopToolBarArea,
        'bottomToolBarArea': Qt.BottomToolBarArea,
    }

    TOOL_BUTTON_STYLE = {
        'toolButtonIconOnly': Qt.ToolButtonIconOnly,
    }

    POPUP_MODE = {
        'instantPopup': QToolButton.InstantPopup
    }

    COMPOSITION_MODE = {
        'source': QtGui.QPainter.CompositionMode_Source,
        'source_over': QtGui.QPainter.CompositionMode_SourceOver,
    }

    BUTTONS = {
        'left': Qt.LeftButton,
        'right': Qt.RightButton,
        'middle': Qt.MiddleButton,
    }

    BRUSHES = {
        'no_brush': Qt.NoBrush,
    }

    CURSORS = {
        'arrow_cursor': Qt.ArrowCursor,
    }

    KEYS = {
        'escape': Qt.Key_Escape,
        'enter': Qt.Key_Enter,
        'return': Qt.Key_Return,
        'shift': Qt.Key_Shift,
    }

    def _path_move_to(path, point):
        return path.moveTo(point)
    
    def _path_cubic_to(path, point1, point2, point3):
        return path.cubicTo(point1, point2, point3)
    
    DIALOG_BUTTONS = {
        'ok': QDialogButtonBox.Ok,
        'cancel': QDialogButtonBox.Cancel,
    }


elif pyqt_version == 6:
    from PyQt6 import QtGui
    from PyQt6 import QtWidgets
    from PyQt6 import QtCore
    from PyQt6.QtWidgets import QMainWindow, QApplication #, QDesktopWidget
    from PyQt6.QtCore import QPoint, Qt, QSize
    from PyQt6.QtWidgets import QToolBar, QDialog, QToolButton, QMenu, QColorDialog
    from PyQt6.QtGui import (
        QGuiApplication,
        QIcon, QScreen, QPalette, QColor, QCursor,
        QSyntaxHighlighter, QPixmap, QKeySequence,
        QAction, QShortcut
    )

    from PyQt6.QtWidgets import (
        QApplication, QDialog, QDialogButtonBox, QLabel, QMainWindow,
        QPushButton, QVBoxLayout, QListWidget, QListWidgetItem, QFormLayout,
        QHBoxLayout, QGridLayout,
        QLineEdit, QPlainTextEdit,
        #QShortcut
    )

    def _create_palette():
        return QPalette()

    PALETTE_PROPS = {
        'window': 'window',
        'windowText': 'windowText',
        'base': 'base',
        'alternateBase': 'alternateBase',
        'toolTipBase': 'toolTipBase',
        'toolTipText': 'toolTipText',
        'text': 'text',
        'button': 'button',
        'buttonText': 'buttonText',
        'brightText': 'brightText',
        'link': 'link',
        'highlight': 'highlight',
        'highlightedText': 'highlightedText',
    }


    def _get_color_from_RGB(r, g, b):
        return QColor(r, g, b)

    def _set_palette_color(palette, property, value):
        return getattr(palette, property)().setColor(value)

    # _set_palette_color(_create_palette(), PALETTE_PROPS['window'], _get_color_from_RGB(53, 53, 53))

    ALIGNMENT = {
        'center': Qt.AlignmentFlag.AlignCenter,
        'left': Qt.AlignmentFlag.AlignLeft,
        'right': Qt.AlignmentFlag.AlignRight,
    }

    COLORS = {
        'black': QtGui.QColorConstants.Black,
        'white': QtGui.QColorConstants.White,
        'red': QtGui.QColorConstants.Red,
        'green': QtGui.QColorConstants.Green,
        'blue': QtGui.QColorConstants.Blue,
        'cyan': QtGui.QColorConstants.Cyan,
        'magenta': QtGui.QColorConstants.Magenta,
        'yellow': QtGui.QColorConstants.Yellow,
        'gray': QtGui.QColorConstants.Gray,
        'darkGray': QtGui.QColorConstants.DarkGray,
        'lightGray': QtGui.QColorConstants.LightGray,
        'transparent': QtGui.QColorConstants.Transparent,
        'darkRed': QtGui.QColorConstants.DarkRed,
        'darkGreen': QtGui.QColorConstants.DarkGreen,
        'darkBlue': QtGui.QColorConstants.DarkBlue,
        'darkCyan': QtGui.QColorConstants.DarkCyan,
        'darkMagenta': QtGui.QColorConstants.DarkMagenta,
        'darkYellow': QtGui.QColorConstants.DarkYellow,
    }

    def _execute_dialog(dlg):
        return dlg.exec()
    
    WINDOW_ATTRS = {
        'translucentBackground': QtCore.Qt.WidgetAttribute.WA_TranslucentBackground,
    }
    
    IMAGE_FORMATS = {
        'ARGB32': QtGui.QImage.Format.Format_ARGB32,
    }

    PEN_STYLES = {
        'solidLine': QtCore.Qt.PenStyle.SolidLine,
        'dashLine': QtCore.Qt.PenStyle.DashLine,
        'dotLine': QtCore.Qt.PenStyle.DotLine,
        'dashDotLine': QtCore.Qt.PenStyle.DashDotLine,
        'roundCap': QtCore.Qt.PenCapStyle.RoundCap,
        'squareCap': QtCore.Qt.PenCapStyle.SquareCap,
        'flatCap': QtCore.Qt.PenCapStyle.FlatCap,
        'roundJoin': QtCore.Qt.PenJoinStyle.RoundJoin,
    }

    TOOLBAR_AREAS = {
        'leftToolBarArea': Qt.ToolBarArea.LeftToolBarArea,
        'rightToolBarArea': Qt.ToolBarArea.RightToolBarArea,
        'topToolBarArea': Qt.ToolBarArea.TopToolBarArea,
        'bottomToolBarArea': Qt.ToolBarArea.BottomToolBarArea,
    }

    TOOL_BUTTON_STYLE = {
        'toolButtonIconOnly': QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly,
    }

    POPUP_MODE = {
        'instantPopup': QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup
    }

    COMPOSITION_MODE = {
        'source': QtGui.QPainter.CompositionMode.CompositionMode_Source,
        'source_over': QtGui.QPainter.CompositionMode.CompositionMode_SourceOver,
    }

    BUTTONS = {
        'left': QtCore.Qt.MouseButton.LeftButton,
        'right': QtCore.Qt.MouseButton.RightButton,
        'middle': QtCore.Qt.MouseButton.MiddleButton,
    }

    BRUSHES = {
        'no_brush': QtCore.Qt.BrushStyle.NoBrush,
    }

    CURSORS = {
        'arrow_cursor': QtCore.Qt.CursorShape.ArrowCursor,
    }

    KEYS = {
        'escape': QtCore.Qt.Key.Key_Escape,
        'enter': QtCore.Qt.Key.Key_Enter,
        'return': QtCore.Qt.Key.Key_Return,
        'shift': QtCore.Qt.Key.Key_Shift,
    }

    def _path_move_to(path, point):
        path.moveTo(point.x(), point.y())

    def _path_cubic_to(path, point1, point2, point3):
        return path.cubicTo(
            point1.x(), point1.y(), 
            point2.x(), point2.y(), 
            point3.x(), point3.y(), 
        )
    
    DIALOG_BUTTONS = {
        'ok': QDialogButtonBox.StandardButton.Ok,
        'cancel': QDialogButtonBox.StandardButton.Cancel,
    }
    

import numpy as np
import platform
from datetime import datetime
from xml.dom import minidom
import os
from types import SimpleNamespace
import importlib

from matplotlib.backends.qt_compat import QtCore, QtWidgets
if QtCore.qVersion() >= "5.":
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

from screenpen.version import __version__

dir_path = os.path.dirname(os.path.realpath(__file__))
syntax_py_path = f'{dir_path}/utils/syntax.py'
spec = importlib.util.spec_from_file_location('syntax', syntax_py_path)
syntax = importlib.util.module_from_spec(spec)
sys.modules['syntax'] = syntax
spec.loader.exec_module(syntax)

class ScreenPenWindow(QMainWindow):
    def __init__(self, screen, screen_geom, pixmap: QtGui.QPixmap = None, transparent_background = True, icon_size = 50): # app: QApplication
        super().__init__()

        # PATHS
        try:
            prefix = sys._MEIPASS
            resources_xml_path = os.path.join(prefix, 'utils/resources.xml')
        except Exception:
            prefix = ''
            dir_path = os.path.dirname(os.path.realpath(__file__))
            resources_xml_path = f'{dir_path}/utils/resources.xml'

        

        self.files = SimpleNamespace(
            resources_xml = resources_xml_path
        )
        
        self.screen = screen
        self.screen_pixmap = pixmap
        self.screen_geom = screen_geom
        self.transparent_background = transparent_background
        self.icon_size = icon_size

        if self.transparent_background:
            self.setAttribute(WINDOW_ATTRS['translucentBackground'])
        self.move(screen_geom.topLeft())
        self.setGeometry(screen_geom)
        self.activateWindow()
        self.showFullScreen()
        self._createCanvas()
        self._clearCanvas()
        
        self.history = self.drawingHistory(30)
        self.history.append(self.screen_pixmap)

        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.lastPoint = QtCore.QPoint()

        self.drawing = False
        self.curr_method = 'drawPath'
        self.curr_color = COLORS['red']
        self.curr_style = PEN_STYLES['solidLine']
        self.curr_capstyle = PEN_STYLES['roundCap']
        self.curr_joinstyle = PEN_STYLES['roundJoin']
        self.curr_width = 3
        self.curr_br = QtGui.QBrush(self.curr_color)
        self.curr_pen = QtGui.QPen()
        self._setupTools()
        self._setupIcons()
        self._setupCodes()
        self._createToolBars()

        self.sc_undo = QShortcut(QKeySequence('Ctrl+Z'), self)
        self.sc_undo.activated.connect(self.undo)
        self.sc_redo = QShortcut(QKeySequence('Ctrl+Y'), self)
        self.sc_redo.activated.connect(self.redo)
        self.sc_quit_program = QShortcut(QKeySequence('Escape'), self)
        self.sc_quit_program.activated.connect(self.quit_program)

    def _setCursor(self, cursor, hotx = None, hoty = None):
        if hotx is None:
            hotx = 2
        if hoty is None:
            hoty = 2
        if type(cursor) == str:
            pixm = QtGui.QPixmap.fromImage(QtGui.QImage.fromData(bytes(self._applySvgConfig(self._icons[cursor], None), encoding='utf-8')))
            pixm = pixm.scaled(QSize(32, 32))
            self.setCursor(QCursor(pixm, int(hotx), int(hoty)))
        elif type(cursor) == Qt.CursorShape:
            self.setCursor(QCursor(cursor))
        elif type(cursor) == QPixmap:
            self.setCursor(QCursor(cursor, int(hotx), int(hoty)))

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return
        k = event.key()
        if (k==KEYS['shift']):
            self._setCursor('arrow2')

    def keyReleaseEvent(self, event):
        if event.isAutoRepeat():
            return
        k = event.key()
        if (k==KEYS['shift']):
            self._setCursor(Qt.ArrowCursor)

    def _setupIcons(self):
        self._icons = {}
        try:
            DOMTree = minidom.parse(self.files.resources_xml)
            icons = DOMTree.getElementsByTagName('icon')
            if len(icons) < 1:
                raise Exception('ERROR: there are no icons in resources.xml file')
            for icon in icons:
                if icon.getAttribute('name')=='':
                    raise Exception('ERROR: resources.xml: icon doesnt contain "name" attribute')
                self._icons[icon.getAttribute('name')] = icon.getElementsByTagName('svg')[0].toxml().replace('\n', '')
        except FileNotFoundError as ex:
            print('ERROR: There is no resources.xml file')
            raise ex

    class Code(object): pass
    def _setupCodes(self):
        self._codes = []
        try:
            DOMTree = minidom.parse(self.files.resources_xml)
            codes = DOMTree.getElementsByTagName('code')
            if len(codes) < 1:
                raise Exception('ERROR: there are no codes in resources.xml file')
            for code in codes:
                if code.getAttribute('name')=='':
                    raise Exception('ERROR: resources.xml: code doesnt contain "name" attribute')
                codeobj = self.Code()
                codeobj.name = code.getAttribute('name')
                codeobj.label = code.getAttribute('name')
                codeobj.code = code.firstChild.data
                self._codes += [codeobj]
        except FileNotFoundError as ex:
            print('ERROR: There is no resources.xml file')
            raise ex


    def _applySvgConfig(self, svg_str, custom_colors_dict=None):
        colors_dict = {
            'STROKE': 'white',
            'FILL': 'silver'
        }
        if custom_colors_dict is not None:
            colors_dict = {**colors_dict, **custom_colors_dict}
        parsed = svg_str
        for el in colors_dict:
            parsed = parsed.replace(f'{{{el}}}', colors_dict[el])
        return parsed

    def _getIcon(self, name, custom_colors_dict=None):
        return QIcon(QtGui.QPixmap.fromImage(QtGui.QImage.fromData(bytes(self._applySvgConfig(self._icons[name], custom_colors_dict), encoding='utf-8'))))

    def _createCanvas(self):
        self.background = QtGui.QImage(self.size(), IMAGE_FORMATS['ARGB32'])
        self.imageDraw = QtGui.QImage(self.size(), IMAGE_FORMATS['ARGB32'])
        self.imageDraw_bck = QtGui.QImage(self.size(), IMAGE_FORMATS['ARGB32'])
        self._clearBackground()
        
    def _clearBackground(self): # make background transparent
        if self.transparent_background:
            self.background.fill(COLORS['transparent'])
        else:
            qp2 = QtGui.QPainter(self.background)
            qp2.drawPixmap(self.background.rect(), self.screen_pixmap, self.screen_pixmap.rect())
            qp2.end()
        self.update()

    def _clearCanvas(self):
        self.imageDraw.fill(COLORS['transparent'])
        self.imageDraw_bck.fill(COLORS['transparent'])
        self.update()

    def drawMatplotlib(self, qp:QtGui.QPainter, canvas:FigureCanvas, p1:QtCore.QPoint):
        size = canvas.size()
        width, height = size.width(), size.height()
        im = QtGui.QImage(canvas.buffer_rgba(), width, height, IMAGE_FORMATS['ARGB32']).rgbSwapped()
        p2 = QtCore.QPoint(int(p1.x()+width), int(p1.y()+height))
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

    def _getEraserPen(self, color=COLORS['transparent'], size=30):
        pen = QtGui.QPen()
        pen.setBrush(QtGui.QBrush(color))
        pen.setStyle(PEN_STYLES['solidLine']) ; pen.setCapStyle(PEN_STYLES['roundCap']) 
        pen.setJoinStyle(PEN_STYLES['roundJoin']) ; pen.setWidth(size)
        return pen

    def setEraser(self):
        def _setEraser():
            pix = QPixmap()
            img = QtGui.QImage(QSize(32, 32), IMAGE_FORMATS['ARGB32'])
            img.fill(COLORS['transparent'])
            qp = QtGui.QPainter(img)
            qp.setPen(self._getEraserPen(QColor('#7acfe6'), 30))
            path = QtGui.QPainterPath()
            _path_move_to(path, QPoint(16, 16))
            _path_cubic_to(path, QPoint(16, 17), QPoint(16, 16), QPoint(16, 16))
            qp.drawPath(path)
            qp.setPen(self._getEraserPen(QColor('#eccdec'), 26))
            path = QtGui.QPainterPath()
            _path_move_to(path, QPoint(16, 16))
            _path_cubic_to(path, QPoint(16, 17), QPoint(16, 16), QPoint(16, 16))
            qp.drawPath(path)
            qp.end()
            pix = pix.fromImage(img)
            self.setAction('drawEraser')()
            self._setCursor(pix, 16, 16)
            self._setupTools()
        return _setEraser

    def setStyle(self, style):
        def _setStyle():
            self.curr_style = style
            self._setupTools()
        return _setStyle

    def setWidth(self, width):
        def _setWidth():
            self.curr_width = width
            self._setupTools()
        return _setWidth

    def setAction(self, action, cursor=None):
        def _setAction():
            self.curr_method = action
            if cursor is None:
                self._setCursor(CURSORS['arrow_cursor'])
        return _setAction

    class ChartDialog(QDialog):
        def ok_success(self, *args):
            sourcecode = '\n'.join(list(map(lambda x: f'    {x}', self.code.toPlainText().replace('\t', '').replace(' ', '').splitlines())))
            self.code = f'''
def drawChart(qp:QtGui.QPainter, p1:QtCore.QPoint):
{sourcecode}
    canvas = FigureCanvas(fig)
    canvas.draw()
    canvas.setStyleSheet("background-color:transparent;")

    renderer = canvas.get_renderer()
    fwidth, fheight = fig.get_size_inches()
    fig_bbox = fig.get_window_extent(renderer)
    self.drawMatplotlib(qp, canvas, p1)
setattr(self, 'drawChart', drawChart)
'''
            exec(self.code, {'self': self.parent, **globals()})
            self.accept()

        def __init__(self, parent):
            super().__init__(parent=parent)
            self.parent = parent
            self.setWindowTitle("Chart")



            QBtn = DIALOG_BUTTONS['ok'] | DIALOG_BUTTONS['cancel']

            self.buttonBox = QDialogButtonBox(QBtn)
            self.buttonBox.accepted.connect(self.ok_success)
            self.buttonBox.rejected.connect(self.reject)
            
            self.resize(800, 600)
            self.code    = QPlainTextEdit()
            highlight = syntax.PythonHighlighter(self.code.document())
            self.code.zoomIn(4)
            self.code.setPlainText('')

            l = QListWidget()
            for c in self.parent._codes:
                ech = QListWidgetItem(c.label)
                ech.code = c.code
                ech.name = c.name
                l.addItem(ech)
            def code_clicked(c):
                self.code.setPlainText(c.code)
            l.itemClicked.connect(code_clicked)
            self.layout = QVBoxLayout()
            
            buttons = QHBoxLayout()
            buttons.addWidget(self.buttonBox, 1)

            codelay = QHBoxLayout()
            codelay.addWidget(l)
            codelay.addWidget(self.code, 1)

            self.layout.addLayout(codelay)
            self.layout.addLayout(buttons)

            self.setLayout(self.layout)

    def showChart(self):
        def _showChart():
            self._setCursor(CURSORS['arrow_cursor'])
            dlg = self.ChartDialog(self)
            if _execute_dialog(dlg):
                self.curr_method = 'drawChart'
            else:
                pass
        
        return _showChart

    def removeDrawing(self):
        def _removeDrawing():
            self._clearCanvas()
        return _removeDrawing

    def captureScreen(self):
        for tb in self.toolBars:
            tb.hide()
        img = self.imageDraw.copy()
        qp = QtGui.QPainter(img)
        qp.drawPixmap(img.rect(), self.screen_pixmap, self.screen_pixmap.rect())
        qp.drawImage(img.rect(), self.background, self.background.rect())
        qp.drawImage(img.rect(), self.imageDraw, self.imageDraw.rect())
        qp.end()
        for tb in self.toolBars:
            tb.show()
        return img

    def saveDrawing(self):
        def _saveDrawing(n=0):
            filename = f'{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
            print(f'Saving {filename}')
            self.captureScreen().save(f'{filename}')
        return _saveDrawing

    def colorPicker(self):
        def _colorPicker():
            color = QColorDialog.getColor()

            if color.isValid():
                self.curr_color = color
        return _colorPicker

    def addAction(self, name, icon, fun):
        action = QAction(icon, name, self)
        action.triggered.connect(fun)
        return action


    def _createToolBars(self):
        penToolBar = QToolBar("Color", self)
        penToolBar.setIconSize(QSize(self.icon_size, self.icon_size))
        boardToolBar = QToolBar("Color", self)
        boardToolBar.setIconSize(QSize(self.icon_size, self.icon_size))
        actionBar = QToolBar("Action", self)
        actionBar.setIconSize(QSize(self.icon_size, self.icon_size))
        self.toolBars = [penToolBar, boardToolBar, actionBar]
        self.addToolBar(penToolBar)
        self.addToolBar(boardToolBar)
        self.addToolBar(TOOLBAR_AREAS['leftToolBarArea'], actionBar)
        
        avail_colors = {
            'red': COLORS['red'],
            'green': COLORS['green'],
            'blue': COLORS['blue'],
            'cyan': COLORS['cyan'],
            'magenta': COLORS['magenta'],
            'yellow': COLORS['yellow'],
            'black': COLORS['black'],
            'white': COLORS['white'],
            'orange': _get_color_from_RGB(255, 165, 0),
            'gray': _get_color_from_RGB(128, 128, 128),
        }

        for acol in avail_colors:
            penToolBar.addAction(
                self.addAction(f'{acol}', self._getIcon('rect_filled', {'FILL': acol, 'STROKE': 'none'}), self.setColor(avail_colors[acol]))
            )
        
        penToolBar.addAction(self.addAction(f'Color Picker', self._getIcon('color_picker'), self.colorPicker()))
        penToolBar.addAction(self.addAction(f'Eraser', self._getIcon('eraser'), self.setEraser()))

        actionBar.addAction(self.addAction("Path", self._getIcon('path'), self.setAction('drawPath')))
        actionBar.addAction(self.addAction("Rect", self._getIcon('rect'), self.setAction('drawRect')))
        actionBar.addAction(self.addAction("Line", self._getIcon('line'), self.setAction('drawLine')))
        actionBar.addAction(self.addAction("Point", self._getIcon('dot'), self.setAction('drawDot')))
        actionBar.addAction(self.addAction("Matplotlib chart", self._getIcon('mpl'), self.showChart()))
        
        

        lineTypeMenu = QMenu()
        lineTypeMenu.addAction(self.addAction('Solid', self._getIcon('line'), self.setStyle(PEN_STYLES['solidLine'])))
        lineTypeMenu.addAction(self.addAction('Dashed', self._getIcon('line_dashed'), self.setStyle(PEN_STYLES['dashLine'])))
        lineTypeButton = QToolButton(self)
        lineTypeButton.setToolButtonStyle(TOOL_BUTTON_STYLE['toolButtonIconOnly'])
        lineTypeButton.setIcon(self._getIcon('line_type'))
        lineTypeButton.setPopupMode(POPUP_MODE['instantPopup']) # MenuButtonPopup
        lineTypeButton.setMenu(lineTypeMenu)
        lineTypeButton.setToolTip('Line type')
        actionBar.addWidget(lineTypeButton)

        lineWidthMenu = QMenu()
        lineWidthMenu.addAction(self.addAction('Thin', self._getIcon('line_thin'), self.setWidth(width=3)))
        lineWidthMenu.addAction(self.addAction('Medium', self._getIcon('line_medium'), self.setWidth(width=15)))
        lineWidthMenu.addAction(self.addAction('Thick', self._getIcon('line_thick'), self.setWidth(width=25)))
        lineWidthButton = QToolButton(self)
        lineWidthButton.setToolButtonStyle(TOOL_BUTTON_STYLE['toolButtonIconOnly'])
        lineWidthButton.setIcon(self._getIcon('line_width'))
        lineWidthButton.setPopupMode(POPUP_MODE['instantPopup'])
        lineWidthButton.setMenu(lineWidthMenu)
        lineWidthButton.setToolTip('Line width')
        actionBar.addWidget(lineWidthButton)
        boardToolBar.addAction(self.addAction("Whiteboard", self._getIcon('board', custom_colors_dict={'FILL': 'white'}), self.setupBoard(COLORS['white'])))
        boardToolBar.addAction(self.addAction("Blackboard", self._getIcon('board', custom_colors_dict={'FILL': 'black'}), self.setupBoard(COLORS['black'])))
        boardToolBar.addAction(self.addAction("Transparent", self._getIcon('board_transparent', custom_colors_dict={'FILL': 'black'}), self._clearBackground))
        boardToolBar.addAction(self.addAction("Remove drawings", self._getIcon('remove'), self.removeDrawing()))
        
        actionBar.addAction(self.addAction("Save image", self._getIcon('save'), self.saveDrawing())) # self.style().standardIcon(QtWidgets.QStyle.SP_DialogSaveButton)

        
    def scaleCoords(self, coords):
        canvas_size = self.imageDraw.size()
        window_size = self.size()
        x_scale = canvas_size.width() / window_size.width()
        y_scale = canvas_size.height() / window_size.height()
        return QtCore.QPoint(int(coords.x()*x_scale), int(coords.y()*y_scale))

    def paintEvent(self, event):
        self._setupTools()

        qp = QtGui.QPainter(self.imageDraw)
        canvasPainter = QtGui.QPainter(self)



        qp.setCompositionMode(COMPOSITION_MODE['source'])
        canvasPainter.setCompositionMode(COMPOSITION_MODE['source_over'])

        if BUTTONS['left'] and self.drawing:
            qp.setPen(self.curr_pen)
            qp.setBrush(self.curr_br)
            if self.curr_method in ['drawRect']:
                qp.setBrush(BRUSHES['no_brush'])
                self.curr_args = [QtCore.QRect(self.begin, self.end)]
                qp.drawImage(self.imageDraw.rect(), self.imageDraw_bck, self.imageDraw_bck.rect())
                
                getattr(qp, self.curr_method)(*self.curr_args)
                qp.setBrush(self.curr_br)
            elif self.curr_method in ['drawDot']:
                self.curr_args = [self.end, 10, 10]
                qp.drawImage(self.imageDraw.rect(), self.imageDraw_bck, self.imageDraw_bck.rect())
                
                getattr(qp, 'drawEllipse')(*self.curr_args)

            elif self.curr_method in ['drawLine']:
                qp.setBrush(BRUSHES['no_brush'])
                self.curr_args = [self.begin, self.end]
                qp.drawImage(self.imageDraw.rect(), self.imageDraw_bck, self.imageDraw_bck.rect())
                
                getattr(qp, self.curr_method)(*self.curr_args)
                qp.setBrush(self.curr_br)

            elif self.curr_method in ['drawChart']:
                qp.drawImage(self.imageDraw.rect(), self.imageDraw_bck, self.imageDraw_bck.rect())
                try:
                    self.drawChart(qp, self.end)
                    self.update()
                except Exception as ex:
                    self.drawing = False
                    msgBox = QtWidgets.QMessageBox()
                    msgBox.setText(str(ex))
                    msgBox.exec()
                    
                    self.curr_method = 'drawPath'
                    self.update()
                    return


            elif self.curr_method in ['drawPath']:
                if self.lastPoint != self.end:
                    qp.setBrush(BRUSHES['no_brush'])
                    qp.setPen(self.curr_pen)
                    _path_cubic_to(self.path, self.end, self.end, self.end)
                    self.curr_args = [self.path]
                    getattr(qp, self.curr_method)(*self.curr_args)
                    self.lastPoint = self.end
                    self.update()
                    qp.setBrush(self.curr_br)

            elif self.curr_method in ['drawEraser']:
                if self.lastPoint != self.end:
                    qp.setBrush(BRUSHES['no_brush'])
                    qp.setPen(self._getEraserPen(COLORS['transparent']))
                    _path_cubic_to(self.path, self.end, self.end, self.end)
                    self.curr_args = [self.path]
                    getattr(qp, 'drawPath')(*self.curr_args)
                    self.lastPoint = self.end
                    self.update()
                    qp.setBrush(self.curr_br)

        qp.setCompositionMode(COMPOSITION_MODE['source_over'])
        qp.end()
        
        canvasPainter.drawImage(self.rect(), self.background, self.background.rect())
        canvasPainter.drawImage(self.rect(), self.imageDraw, self.imageDraw.rect())
        canvasPainter.setCompositionMode(COMPOSITION_MODE['source_over'])
        canvasPainter.end()


    def mousePressEvent(self, event):
        if event.button() == BUTTONS['right']:
            sys.exit(0)
            
        if event.button() == BUTTONS['left'] and self.childAt(event.pos()) is None:
            self.drawing = True

        if self.curr_method in ['drawRect', 'drawChart', 'drawLine', 'drawDot']:
            qp = QtGui.QPainter(self.imageDraw_bck)
            qp.drawImage(self.imageDraw_bck.rect(), self.imageDraw, self.imageDraw.rect())
            qp.end()
            self.begin = self.scaleCoords(event.pos())
            self.end = self.scaleCoords(event.pos())
            
        elif self.curr_method in ['drawPath', 'drawEraser']:
            self.path = QtGui.QPainterPath()
            self.begin = self.scaleCoords(event.pos())
            self.end = self.scaleCoords(event.pos())
            _path_move_to(self.path, self.begin)
            self.lastPoint = self.scaleCoords(event.pos())
        self.update()

    def mouseMoveEvent(self, event):
        self.end = self.scaleCoords(event.pos())
        self.update()


    class drawingHistory(list):
        def __init__(self, limit=4):
            self.limit = limit
            self.current = -1
        
        def append(self, el):
            if self.current < len(self):
                del self[self.current + 1:]
                
            if len(self) >= self.limit:
                del self[0]
                self.current = self.limit - 2
            super().append(el)
            self.current += 1
            
        def extend(self, l):
            for el in l:
                self.append(el)
            
        def undo(self):
            if self.current > 0:
                self.current -= 1
            return self[self.current]
        
        def redo(self):
            if self.current + 1 < len(self):
                self.current += 1
            return self[self.current]
            
    def drawPixmap(self, p):
        qp = QtGui.QPainter(self.imageDraw)
        qp.setCompositionMode (COMPOSITION_MODE['source'])
        qp.drawPixmap(self.imageDraw.rect(), p, p.rect())
        qp.end()

        qp2 = QtGui.QPainter(self.imageDraw_bck)
        qp2.setCompositionMode (COMPOSITION_MODE['source'])
        qp2.drawPixmap(self.imageDraw_bck.rect(), p, p.rect())
        qp2.end()

    def undo(self):
        p = self.history.undo()
        self.drawPixmap(p)
        self.update()

    def redo(self):
        p = self.history.redo()
        self.drawPixmap(p)
        self.update()

    def quit_program(self):
        sys.exit(0)

    def mouseReleaseEvent(self, event):
        if event.button() == BUTTONS['left'] and self.drawing == True:
            self.drawing = False
            self.path = None

            self.begin = self.scaleCoords(event.pos())
            self.end = self.scaleCoords(event.pos())

            self.update()
            p = QPixmap()
            p.convertFromImage(self.imageDraw)
            self.history.append(p)


    def setupBoard(self, color):
        def _setupBoard():
            self.background.fill(color)
            self.update()
        return _setupBoard


def _grab_screen(screen_idx, screen):
    if pyqt_version == 5:
        screen_geom = QDesktopWidget().screenGeometry(screen_idx)
    else:
        screen_geom = QGuiApplication.screens()[screen_idx].geometry()

    return (
        screen_geom, 
        screen.grabWindow(
            0, 
            screen_geom.x(), 
            screen_geom.y(), 
            screen.size().width(), 
            screen.size().height()
        )
    )
    

def _get_screens(app):
    screens = []
    for screen_idx, screen in enumerate(app.screens()):
        screen_geom, screen_pixmap = _grab_screen(screen_idx, screen)
        screens.append([screen, screen_geom, screen_pixmap])
    return screens


def _is_transparency_supported():
    warn = 'INFO: Your system may support transparency but we cannot detect it. You may try to use -t parameter to force it.'
    try:
        if platform.system() == 'Linux':
            return '_NET_WM_WINDOW_OPACITY' in subprocess.run("xprop -root", shell=True, stdout=subprocess.PIPE).stdout.decode()
        else:
            print(warn)
            return False
    except:
        print(warn)
        return False


def show_screen_selection(screens):
    number_of_screens = len(screens)
    def _getScreenButton(pixmap, label):
        btn = QPushButton()
        ico = QIcon(pixmap)
        btn.setIcon(ico)
        btn.setIconSize(QSize(int(160), int(160//(pixmap.rect().width()/pixmap.rect().height()))))

        shad = QtWidgets.QGraphicsDropShadowEffect()
        shad.setOffset(-10, 10)
        shad.setColor(COLORS['black'])

        lay = QVBoxLayout(btn)
        lbl = QtWidgets.QLabel()
        lbl.setContentsMargins(0, 0, 0, 0)
        lbl.setStyleSheet("""color : white; font-weight:1000;""")
        lbl.setText(label)
        lbl.setGraphicsEffect(shad)
        lay.addWidget(lbl, alignment=ALIGNMENT['center'])
        return btn

    dlg = QDialog()
    dlg.layout = QGridLayout()
    dlg.layout.addWidget(QLabel('Select the screen') , 0, 0, 1, number_of_screens, alignment=ALIGNMENT['center'])

    def _getBtnAction(idx):
        def act():
            dlg.done(idx)
        return act

    for idx, scr in enumerate(screens):
        screen, screen_geom, screen_pixmap = scr
        label = f'Screen {idx+1}' if idx > 0 else f'Main screen'
        btn = _getScreenButton(screen_pixmap, label)
        btn.released.connect(_getBtnAction(idx+1))
        dlg.layout.addWidget(btn , 1, idx)
    dlg.setLayout(dlg.layout)
    return _execute_dialog(dlg)

def _setPalette(app):
    palette = _create_palette()
    _set_palette_color(palette, PALETTE_PROPS['window'], _get_color_from_RGB(53, 53, 53))
    _set_palette_color(palette, PALETTE_PROPS['windowText'], COLORS['white'])
    _set_palette_color(palette, PALETTE_PROPS['base'], _get_color_from_RGB(25, 25, 25))
    _set_palette_color(palette, PALETTE_PROPS['alternateBase'], _get_color_from_RGB(53, 53, 53))
    _set_palette_color(palette, PALETTE_PROPS['toolTipBase'], COLORS['black'])
    _set_palette_color(palette, PALETTE_PROPS['toolTipText'], COLORS['white'])
    _set_palette_color(palette, PALETTE_PROPS['text'], COLORS['white'])
    _set_palette_color(palette, PALETTE_PROPS['button'], _get_color_from_RGB(53, 53, 53))
    _set_palette_color(palette, PALETTE_PROPS['buttonText'], COLORS['white'])
    _set_palette_color(palette, PALETTE_PROPS['brightText'], COLORS['red'])
    _set_palette_color(palette, PALETTE_PROPS['link'], _get_color_from_RGB(42, 130, 218))
    _set_palette_color(palette, PALETTE_PROPS['highlight'], _get_color_from_RGB(42, 130, 218))
    _set_palette_color(palette, PALETTE_PROPS['highlightedText'], COLORS['black'])
    
    app.setPalette(palette)
    app.setStyle("Fusion")


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-v', '--version', dest='version', action='version', version=f'Version: {__version__}')
    parser.add_argument('-1', nargs='?', type=int, dest='screen', const='0')
    parser.add_argument('-2', nargs='?', type=int, dest='screen', const='1')
    parser.add_argument('-3', nargs='?', type=int, dest='screen', const='2')
    parser.add_argument('-t', '--transparent', dest='transparent', help='Force transparent background. If you are sure your WM support it.', action='store_true')
    parser.add_argument('-i', '--iconsize', type=int, dest='icon_size', help='Sets the icon size, default = 50', default=50)

    args = parser.parse_args()
    
    app = QApplication(sys.argv)
    _setPalette(app)

    number_of_screens = len(app.screens())

    screens = _get_screens(app)
    
    if number_of_screens > 1 and args.screen is None:
        args.screen = show_screen_selection(screens)
        if args.screen == 0 or args.screen is None:
            print('No screen chosen, exiting.')
            sys.exit(0)
        else:
            args.screen -= 1
    elif args.screen is None:
        args.screen = 0
        
    if args.screen >= len(screens):
        raise Exception(f'Error: You don\'t have so many screens ({args.screen+1}). Try lower number.')
    
    screen, screen_geom, pixmap = screens[args.screen]
    
    use_transparency = args.transparent or _is_transparency_supported()
    
    window = ScreenPenWindow(screen=screen, screen_geom=screen_geom, pixmap=pixmap,
                             transparent_background=use_transparency, icon_size=args.icon_size)
    sys.exit(_execute_dialog(app))

if __name__ == '__main__':
    main()