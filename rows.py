import sys
from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class ExactTable(QWidget):
    def __init__(self,tbl_name = ' ', tbl = {}):
        '''
        arguments  - tbl_name ->
                     tbl -> dict { rows : [colums] }
                        
                     '''
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Simple Table")
        self.setGeometry(100, 100, 400, 300)

        # Create a table widget
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3'])

        # Add data to the table
        for row in range(self.tableWidget.rowCount()):
            for column in range(self.tableWidget.columnCount()):
                value = QTableWidgetItem(str((row+1)*(column+1)))
                self.tableWidget.setItem(row, column, value)

        # Set the layout
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(self.tableWidget)
        self.setLayout(vboxLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    table = SimpleTable()
    table.show()
    sys.exit(app.exec())