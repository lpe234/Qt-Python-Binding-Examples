#!/usr/bin/env python
import sys

try:
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtGui

from add_group import Ui_Form


class Demo(QtGui.QWidget, Ui_Form):
    def __init__(self, parent = None):
        super(Demo, self).__init__(parent)

        self.setupUi(self)

    def show_and_raise(self):
        self.show()
        self.raise_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())