import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
#подключаем СУБД Postgre
from posgre_server import Server
#Подключаем вывод информации из таблицы
from rows import ExactTable

class Table(QWidget):    

    def __init__(self, parent=None, name = 'table'):
        QWidget.__init__(self, parent)
        self.setWindowTitle(f"Таблица {name}")
        
        self.setFixedSize(400,500)
        #добавление фона  
        self.layout = QVBoxLayout(self)

        self.insert_button = QPushButton(f"Просмотр таблицы {name}\n и связанных с ней")
        self.layout.addWidget(self.insert_button)
        self.insert_button.setGeometry(50, 50, 100, 50)

        self.update_button = QPushButton(f"Добавление записи в таблицу {name}")
        self.layout.addWidget(self.update_button)
        self.update_button.move(0, 100)

        
        

        self.insert_button.clicked.connect(self.insert)
        self.update_button.clicked.connect(self.update)
    
    @QtCore.Slot()
    def insert(self):
        pass
    
    @QtCore.Slot()
    def update(self):
        pass
    def button_released(self):
        #Сохранили объект, который посылает нам сигнал
        sending_button = self.sender()
        
        # self.status_label.setText('%s Clicked!' % str(sending_button.objectName()))
        #Отправляем название той таблицы, откуда пришел сигнал
        button_name = sending_button.objectName()
        # print(button_name[7:])
if __name__ == '__main__':
  app = QApplication(sys.argv)

  widget = Table()
  widget.show()

  sys.exit(app.exec())