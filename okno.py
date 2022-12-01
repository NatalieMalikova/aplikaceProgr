from typing import Optional

from PyQt5.QtCore import QSettings
from PyQt5.QtGui import (QResizeEvent, QMoveEvent)
from PyQt5.QtWidgets import (QApplication, QWidget, QAction, QMainWindow, QMenu)


class MainWindow(QMainWindow):

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("Aplikace s nastavením")
        self.settings = QSettings()

        self.resize_and_move()

        self.ds = None

        self.init_gui()

    def resize_and_move(self):

        size = self.settings.value("mainwindow/size", None)

        if size:
            self.resize(size)
        else:
            self.resize(500, 200)

        position = self.settings.value("mainwindow/position", None)

        if position:
            self.move(position)

    def resizeEvent(self, a0: QResizeEvent) -> None:
        self.settings.setValue("mainwindow/size", self.size())
        return super().resizeEvent(a0)

    def moveEvent(self, a0: QMoveEvent) -> None:
        self.settings.setValue("mainwindow/position", self.pos())
        return super().moveEvent(a0)

    # karta v okne... Aplikace->exit
    def init_gui(self):
        menu = QMenu('Aplikace', self)
        self.menuBar().addMenu(menu)

        self.action_end = QAction("Ukončit", self)
        self.action_end.triggered.connect(self.exit)

        menu.addAction(self.action_end)

    def exit(self):
        app = QApplication.instance()
        app.quit()
