from typing import List
import sys

from PyQt5.QtWidgets import QApplication

import okno
from mainwindow import mw


def runapp(args: List[str]) -> None:
    app = QApplication(sys.argv)

    o = okno
    o.print
    sys.exit(app.exec())
