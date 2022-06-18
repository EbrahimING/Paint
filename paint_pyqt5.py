import paint_stack, paint_unredo, sys, webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QColor, QPainter, QKeySequence, QImage
from PyQt5.QtWidgets import * #QLabel, QApplication, QWidget, QShortcut
from PyQt5.QtCore import Qt

class Canvas(QLabel):
    undo_redo = None
    qpixmap = None
    def __init__(self, height, width, background_color = QColor('#FFFFFF')):
        super().__init__()
        self.qpixmap = QPixmap(int(height), int(width))
        self.qpixmap.fill(background_color)
        self.setPixmap(self.qpixmap)
        self.pen_color = QColor('#000000')
        self.undo_redo = paint_unredo.unredo()
        self.undo_redo.push(self.pixmap().copy())
        # self.image() #idk-about-this-either
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
    def set_pen_color(self, color):
        self.pen_color = QtGui.QColor(color)
    def draw_point(self, x, y):
        painter = QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(4)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawPoint(x, y)
        painter.end()
        self.update()
    def draw_line(self, x0, y0, x1, y1):
        painter = QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(4)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawLine(x0, y0, x1, y1)
        painter.end()
        self.update()
    def mousePressEvent(self, e: QtGui.QMouseEvent):
        self.draw_point(e.x(), e.y())
        self.prev_point = (e.x(), e.y())
    def mouseMoveEvent(self, e):
        self.draw_line(self.prev_point[0], self.prev_point[1], e.x(), e.y())
        self.prev_point = (e.x(), e.y())
    def mouseReleaseEvent(self, e):
        self.prev_point = tuple()
        self.undo_redo.push(self.pixmap().copy())
    def undo(self):
        y = self.undo_redo.undo()
        if y != False:
            self.setPixmap(y)
            self.update()
    def redo(self):
        x = self.undo_redo.redo()
        if x != False:
            self.setPixmap(x)
            self.update()
    def clear(self):
        self.qpixmap.fill(Qt.white)
        self.setPixmap(self.qpixmap)
        self.update()
        self.undo_redo.Catch_clear()
        self.undo_redo.push(self.pixmap().copy())
    def save(self):
        filePath, format = QFileDialog.getSaveFileName(self, "Save Image", "",
                         "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        if filePath == "":
            return
        #self.image.save(filePath)
        self.pixmap().save(filePath)
class PaletteButton(QtWidgets.QPushButton):
    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QtCore.QSize(32, 32))
        self.color = color
        self.setStyleSheet("background-color: %s;" % color + "border-radius : 15; ")
class MainWindow(QtWidgets.QMainWindow):
    titleOpt = None
    def __init__(self):
        super().__init__()
        title = "Untitled - Paint"
        self.setWindowTitle(title) # title section
        # icon section
        self.setWindowIcon(QtGui.QIcon('paint.png'))
        # other section
        self.label = QLabel("Icon is set", self)
        self.show()
        self.colors = [
            '#000002', '#868687', '#900124', '#ed2832', '#2db153', '#13a5e7', '#4951cf',
            '#fdb0ce', '#fdca0f', '#eee3ab', '#9fdde8', '#7a96c2', '#cbc2ec', '#a42f3b',
            '#f45b7a', '#c24998', '#81588d', '#bcb0c2', '#dbcfc2',]
        app = QApplication.instance()
        screen = app.primaryScreen()
        geometry = screen.availableGeometry()
        self.canvas = Canvas(geometry.width()*0.60, geometry.height()*0.7)
        #self.canvas.undo #idk-about-this-;/
        w = QtWidgets.QWidget()
        w.setStyleSheet("background-color: #313234")
        l = QtWidgets.QVBoxLayout()  # vertical layout
        w.setLayout(l)
        l.addWidget(self.canvas)
        palette = QtWidgets.QHBoxLayout()  # horizontal layout
        self.add_palette_button(palette)
        l.addLayout(palette)
        self.setCentralWidget(w)
         # File menu section
        mainmenu = self.menuBar()
        filemenu = mainmenu.addMenu("File")
         # Edit menu section
        editmenu = mainmenu.addMenu("Edit")
         # Help menu section
        helpmenu = mainmenu.addMenu("Help")
         # Github link section
        Github = QAction("About" , self)
        helpmenu.addAction(Github)
        Github.triggered.connect(lambda: webbrowser.open('http://www.github.com/ebrahiming'))
        #Github.triggered.connect(self.Github)
         # undo section
        undo = QAction("Undo" , self)
        undo.setShortcut("Ctrl+Z")
        editmenu.addAction(undo)
        undo.triggered.connect(self.undo)
         # redo section
        redo = QAction("Redo" , self)
        redo.setShortcut("Ctrl+Shift+Z")
        editmenu.addAction(redo)
        redo.triggered.connect(self.redo)
         # clear section
        clear = QAction("Clear" , self)
        clear.setShortcut("Alt+C")
        filemenu.addAction(clear)
        clear.triggered.connect(self.clear)
         # save section
        save = QAction("Save" , self)
        save.setShortcut("Ctrl+S")
        filemenu.addAction(save)
        save.triggered.connect(self.save)
        """
        self.titleOpt = QtWidgets.QStyleOptionTitleBar()
        self.titleOpt.initFrom(self)
        self.titleOpt.titleBarFlags = (
            QtCore.Qt.Window | QtCore.Qt.MSWindowsOwnDC |
            QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint |
            QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowMinMaxButtonsHint | 
            QtCore.Qt.WindowCloseButtonHint
            )
        self.titleOpt.state |= (QtWidgets.QStyle.State_Active | 
            QtWidgets.QStyle.State_HasFocus)
        self.titleOpt.titleBarState = (int(self.windowState()) | 
            int(QtWidgets.QStyle.State_Active))
    def resizeEvent(self, event):
        super(QMainWindow, self).resizeEvent(event)
        # update the centralWidget contents margins, adding the titlebar height
        # to the top margin found before
        if (self.centralWidget() and 
            self.centralWidget().getContentsMargins()[1] + self.__topMargin != self.titleHeight):
                l, t, r, b = self.centralWidget().getContentsMargins()
                self.centralWidget().setContentsMargins(
                    l, self.titleHeight + self.__topMargin, r, b)
        # resize the width of the titlebar option, and move its buttons
        self.titleOpt.rect.setWidth(self.width())
        for ctrl, btn in self.ctrlButtons.items():
            rect = self.style().subControlRect(
                QtWidgets.QStyle.CC_TitleBar, self.titleOpt, ctrl, self)
            if rect:
                btn.setGeometry(rect)
        sysRect = self.style().subControlRect(QtWidgets.QStyle.CC_TitleBar, 
            self.titleOpt, QtWidgets.QStyle.SC_TitleBarSysMenu, self)
        if sysRect:
            self.systemButton.setGeometry(sysRect)
        self.titleOpt.titleBarState = int(self.windowState())
        if self.isActiveWindow():
            self.titleOpt.titleBarState |= int(QtWidgets.QStyle.State_Active)
        self.updateTitleBar()"""
    # Functions of MainWindow
    def undo(s):
        s.canvas.undo()
    def redo(s):
        s.canvas.redo()
    def clear(s):
        s.canvas.clear()
    def save(s):
        s.canvas.save()
    def Github(s):
        s.canvas.Github()
    def add_palette_button(self, palette):
        for c in self.colors:
            item = PaletteButton(c)
            item.pressed.connect(self.set_canvas_color)
            palette.addWidget(item)
    def set_canvas_color(self):
        sender = self.sender()
        self.canvas.set_pen_color(sender.color)
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
window.show()
app.exec_()