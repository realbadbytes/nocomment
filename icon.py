#!/usr/bin/python3

import sys
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QIcon

def main():
    app = QApplication(sys.argv)
    mainwindow = QWidget()
    mainwindow.setWindowTitle('PySide2 Icon')
    mainwindow.setWindowIcon(QIcon('code-icon.png'))
    mainwindow.show()
    app.exec_()

if __name__ == '__main__':
    main()
