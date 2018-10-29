#!/usr/bin/python3


import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *


def main():
    app = QApplication(sys.argv)
    dir_listing = QWidget()
    dir_listing.show()
    code_listing = QWidget()
    code_listing.show()
    app.exec_()


if __name__ == '__main__':
    main()
