
import sys
from PySide6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QToolButton, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from test import All_tables
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Панель управления сервером")
        self.setFixedSize(400,500) 
        self.tables_button = QPushButton("Таблицы")
        
       
        self.layout = QVBoxLayout(self)
        
        self.layout.addWidget(self.tables_button)
        
        self.tables_button.move(0, 100)
        # self.label.setText('Button clicked!')

        self.tables_button.clicked.connect(self.tables)
        
    
    @QtCore.Slot()
    def tables(self):
        
        self.tables_button.hide()
        self.t = All_tables()
        self.layout.addWidget(self.t)
        

        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MainWindow()
    # widget.resize(400, 200)
    widget.show()

    sys.exit(app.exec())
