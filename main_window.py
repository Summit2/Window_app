
import sys
from PySide6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QToolButton, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
# #PyQt5 imports
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *

from all_tables import All_tables
from auth import AuthDialog
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.isAdmin = None
        self.setWindowTitle("Панель управления сервером")
        self.setFixedSize(400,500) 
        self.tables_button = QPushButton("Таблицы")
        
       
        self.layout = QVBoxLayout(self)
        
        self.layout.addWidget(self.tables_button)
        
        # self.tables_button.move(0, 100)
        # self.label.setText('Button clicked!')

        self.tables_button.clicked.connect(self.tables)
        
    # @QtCore.Slot()
    # def authentification(self):
    #     self.auth = AuthDialog()
    
    @QtCore.Slot()
    def tables(self):
        
        self.tables_button.hide()
        # self.t = All_tables()
        # self.layout.addWidget(self.t)
    

        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # widget = MainWindow()
    
    # widget.show()

    passdlg = AuthDialog()
    if(1):#passdlg.exec_() == QDialog.Accepted):
        window = MainWindow()
        window.isAdmin = passdlg.isAdmin
        window.show()
        
    sys.exit(app.exec())