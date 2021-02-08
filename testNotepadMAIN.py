from PyQt5 import QtCore, QtGui, Qtwidgets

from testNotepadGUI import Ui_MainWindow

from picamera import PiCamera
from time import sleep
import sys
import datetime

class code_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        # Ui_Form is the main designer generated class. so instantiate one. Precede the variable name with
        # the word 'self'
        
        self.ui = Ui_MainWindow()
        # now pass the main window object to it so that the setupUi method can draw all
        # the widgets into the window
        self.ui.setupUi(self)
        self.show()
         # add your own method functions below
        
    def someMethodName(self):
        print(self)
        
    def AnotherMethod(self):
        print(self)
 

#######################################################################################
    #                           END OF CLASS
#######################################################################################
if __name__ == "__main__":
    import sys
    # instiantiate an app object from the QApplication class 
    app = QtWidgets.QApplication(sys.argv)
    # instantiate an object containing the logic code
    MainWindow = code_MainWindow()
    sys.exit(app.exec_())


