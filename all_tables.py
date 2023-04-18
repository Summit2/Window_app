import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QApplication, QWidget, QToolButton, QLabel, QVBoxLayout, QHBoxLayout
from table import Table

class All_tables(QWidget):    

    def __init__(self, parent=None, t = ['courses','teachers','students','subject_area','progress','manager','progress']):
        QWidget.__init__(self, parent)
        self.setWindowTitle("Таблицы")
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
        self.setLayout(self.widget_layout)

    @QtCore.Slot()
    def button_released(self):
        #Сохранили объект, который посылает нам сигнал
        sending_button = self.sender()
        
        button_name = sending_button.objectName()
        print(button_name[7:])
        self.table = Table(None, button_name[7:])
        self.table.show()
if __name__ == '__main__':
  app = QApplication(sys.argv)

  widget = All_tables()
  widget.show()

  sys.exit(app.exec())