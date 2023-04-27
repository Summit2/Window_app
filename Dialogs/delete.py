from headers import *
class DeleteDialog(QDialog):
    def __init__(self,tbl_name = 'manager', columns = []  ):
        super(DeleteDialog, self).__init__( )

        self.tbl_name = tbl_name

        self.QBtn = QPushButton()
        self.QBtn.setText("Удалить запись")

        self.setWindowTitle(f"Удаление записи из таблицы '{table_info[self.tbl_name]['rus_name']}'")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.delete)
        layout = QVBoxLayout()

        self.deleteinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.deleteinput.setValidator(self.onlyInt)
        self.deleteinput.setPlaceholderText("Введите номер записи")
        layout.addWidget(self.deleteinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def delete(self):

        delrol = ""
        delrol = self.deleteinput.text()
        server = Server()
        
        try:       
            #взяли данные из таблицы
            server.DELETE(self.tbl_name,str(delrol)) 
            QMessageBox.information(QMessageBox(),'Успешно','Запись успешно удалена из таблицы')
            self.close()

            

            
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Ошибка', 'Не удалось удалить запись')
        server.exit()
