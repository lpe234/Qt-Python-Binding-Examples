# A Short Guide for Qt Designer 

## Synopsis

How to use Qt Designer in PySide project?

 - draw UI with Qt Designer, save it into foo.ui
 - convert foo.ui to foo.py by pyuic4
 - import it in your main.py
 - fix compatible problem in foo.py

## Demo

pyuic4 is provider by 'py27-pyside-tools' on Mac OS X MacPorts.

    pyuic4 add_group.ui -o add_group.py

import add_group.py in your main.py:

```
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
```

Problem:

```
TypeError: 'PySide.QtCore.QObject.setObjectName' called with wrong argument types:
  PySide.QtCore.QObject.setObjectName(QString)
Supported signatures:
  PySide.QtCore.QObject.setObjectName(unicode)
```

Solution:

edit add_group.py(generated from add_group.ui), replace `from PyQt4 import QtCore, QtGui` with

```
try:
    from PySide import QtCore, QtGui
except ImportError:
    from PyQt4 import QtCore, QtGui
```

## References

 - [Qt Designer Manual](http://developer.qt.nokia.com/doc/qt-4.8/designer-manual.html)
 - [PySide.QtUiTools](http://www.pyside.org/docs/pyside/PySide/QtUiTools/QUiLoader.html)