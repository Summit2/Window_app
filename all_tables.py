import sys
# from PySide6 import QtCore, QtWidgets, QtGui
# from PyQt6.QtWidgets import QApplication, QWidget, QToolButton, QLabel, QVBoxLayout, QHBoxLayout
from table import Table
from auth import AuthDialog
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *

from rows import PushedTable

from about_tables import table_info
class All_tables(QWidget):    

    def __init__(self, parent=None, t = list(table_info.keys())):
        QWidget.__init__(self, parent)
        self.setWindowTitle("Таблицы")
        self.isAdmin = None
        self.button_layout = QVBoxLayout()  # change to vertical layout
        self.widget_layout = QVBoxLayout()
        tables = t
        text = QLabel("Доступные таблицы:\n")
        self.widget_layout.addWidget(text)
        for i in range(len(tables)):
            button = QToolButton()
            button.setText(str(tables[i]))
            button.setObjectName(f'Button_{tables[i]}')
            button.released.connect(self.button_released)
            self.button_layout.addWidget(button)  # add button to vertical layout

        self.widget_layout.addLayout(self.button_layout)  # add vertical layout to main layout
        # self.widget_layout.addWidget(self.status_label)
        if self.layout() is None:
            self.setLayout(self.widget_layout)

    @pyqtSlot()
    def button_released(self):
        #Сохранили объект, который посылает нам сигнал
        sending_button = self.sender()
        
        button_name = sending_button.objectName()
        # print(button_name[7:])
        # self.table = Table(None, button_name[7:])
        self.window = PushedTable(button_name[7:],self.isAdmin)
        self.window.show()
        
        self.window.loaddata()
        #self.table.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    admin_window = All_tables()
    passdlg = AuthDialog()
    passdlg.show()
    
    user_window = PushedTable()
    if (passdlg.exec_() == QDialog.Accepted):
        
        admin_window.isAdmin = passdlg.isAdmin
        # print(window.isAdmin )
        # if admin_window.isAdmin == True:
        admin_window.show()
            
        # else:
        #     user_window.show()
        #     user_window.loaddata()

        
    sys.exit(app.exec())
