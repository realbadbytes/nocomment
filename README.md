# Why

Enable developers to document their code flawlessly and easily by removing the requirement for a developer to know standard docstring syntax, like RST.

# How

git clone http://github.com/realbadbytes/nocomment

cd nocomment

sudo python3 -m pip install -r requirements.txt

./core.py [target module]

NOTE: Target module must be in current directory. Output will be test_output.py

# Show me

**Sample run**

```user@ubuntu:~/nocomment$ ./core.py test_file_dialog
10/28/2018 11:12:12 PM nocomment starts
10/28/2018 11:12:12 PM Found classe(s): [<class 'test_file_dialog.App'>]
Enter brief function description for __init__: Init function for class instance
10/28/2018 11:12:24 PM Ingesting doc for __init__ with signature (self)
Enter type and description for parameter param:self in __init__: self object
Enter return value description: None
Enter brief function description for openFileNameDialog: Provides a dialog for opening a single file.
10/28/2018 11:12:44 PM Ingesting doc for openFileNameDialog with signature (self)
Enter type and description for parameter param:self in openFileNameDialog: self object
Enter return value description: File handle object
Enter brief function description for testfunc1: Fake function for testing
10/28/2018 11:13:01 PM Ingesting doc for testfunc1 with signature ()
Enter return value description: None
Enter brief function description for openFileNamesDialog: Provide dialog to open multiple files at once.
10/28/2018 11:13:11 PM Ingesting doc for openFileNamesDialog with signature (self)
Enter type and description for parameter param:self in openFileNamesDialog: self object
Enter return value description: List of file handles
Enter brief function description for saveFileDialog: Provide option to save a file.
10/28/2018 11:13:29 PM Ingesting doc for saveFileDialog with signature (self)
Enter type and description for parameter param:self in saveFileDialog: self object
Enter return value description: Save success or failure int
Enter brief function description for initUI: Initialize the user interface
10/28/2018 11:13:42 PM Ingesting doc for initUI with signature (self)
Enter type and description for parameter param:self in initUI: self object
Enter return value description: UI handle
10/28/2018 11:13:47 PM Generating Restview docstring for __init__
10/28/2018 11:13:47 PM Generating Restview docstring for openFileNameDialog
10/28/2018 11:13:47 PM Generating Restview docstring for testfunc1
10/28/2018 11:13:47 PM Generating Restview docstring for openFileNamesDialog
10/28/2018 11:13:47 PM Generating Restview docstring for saveFileDialog
10/28/2018 11:13:47 PM Generating Restview docstring for initUI
```

**Sample output with newly added docstrings**

 ```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

def testfunc1():
""" Fake function for testing

:returns: None
"""

    pass
 
class App(QWidget):
 
    def __init__(self):
    """ Init function for class instance
    
    :param self: self object
    :returns: None
    """
    
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
    """ Initialize the user interface
    
    :param self: self object
    :returns: UI handle
    """
    
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.openFileNameDialog()
        self.openFileNamesDialog()
        self.saveFileDialog()
 
        self.show()
 
    def openFileNameDialog(self):    
    """ Provides a dialog for opening a single file.
    
    :param self: self object
    :returns: File handle object
    """
    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
 
    def openFileNamesDialog(self):    
    """ Provide dialog to open multiple files at once.
    
    :param self: self object
    :returns: List of file handles
    """
    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)
 
    def saveFileDialog(self):    
    """ Provide option to save a file.
    
    :param self: self object
    :returns: Save success or failure int
    """
    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
```

