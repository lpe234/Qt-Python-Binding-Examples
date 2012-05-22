#!/usr/bin/python
"""
Detect platform name and SIP/Python/PyQt/PySide version.

Tested environment:

    OS X 10.6.8
    Ubuntu 12.04 LTS

References:
 - http://www.pyside.org/docs/pyside/pysideversion.html
"""

if __name__ == "__main__":
    import sys
    import platform
    import PySide
    from PySide import QtCore

    print 'Platform: %s' % sys.platform
    print "Python version: %s" % platform.python_version()
    print "Qt version: %s" % QtCore.__version__
    print "PySide version: %s" % PySide.__version__
