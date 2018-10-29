#!/usr/bin/python3

import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *

def main():
    app = QApplication(sys.argv)
    e1 = QLineEdit()
    e1.setFont(QFont("Arial", 24))
    e1.show()
    app.exec_()

if __name__ == '__main__':
    main()
