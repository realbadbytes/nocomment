#!/usr/bin/python3

import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *

def main():
    app = QApplication(sys.argv)
    b1 = QTextEdit()
    b1.show()
    app.exec_()

if __name__ == '__main__':
    main()
