#!/usr/bin/python3

import sys
from PySide2.QtWidgets import QApplication, QWidget


def main():
    app = QApplication(sys.argv)
    mainwindow = QWidget()
    mainwindow.resize(550,400)
    mainwindow.setWindowTitle("create_window demo")
    mainwindow.show()
    app.exec_()


if __name__ == '__main__':
    main()
