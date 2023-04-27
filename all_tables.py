import sys
from table import Table
from auth import AuthDialog
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
from rows import PushedTable
from about_tables import table_info, tables_rus
class All_tables(QWidget):    

    def __init__(self, parent=None, t = list(table_info.keys())):
        QWidget.__init__(self, parent)
        self.setWindowTitle("Таблицы")
        self.isAdmin = None
        self.button_layout = QVBoxLayout()  # change to vertical layout
        self.widget_layout = QVBoxLayout()
        tables = t
        self.setFixedSize(220, 250)
        text = QLabel("Доступные таблицы:\n")
        self.widget_layout.addWidget(text)
        for i in range(len(tables)):
            button = QToolButton()
            button.setText(tables_rus[i])
            # print()
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
       
        self.window = PushedTable(button_name[7:],self.isAdmin)
        self.window.show()
        
        self.window.loaddata()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    admin_window = All_tables()
    passdlg = AuthDialog()
    passdlg.show()
    
    user_window = PushedTable()
    if (passdlg.exec_() == QDialog.Accepted):
        
        admin_window.isAdmin = passdlg.isAdmin
        if admin_window.isAdmin == False:
            user_table = PushedTable()
            # user_table.loaddata()
            user_table.show()
        else:
            admin_window.show()
        
        
    sys.exit(app.exec())
