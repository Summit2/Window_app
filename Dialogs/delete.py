from headers import *
class DeleteDialog(QDialog):
    def __init__(self,tbl_name = 'manager', columns = []  ):
        super(DeleteDialog, self).__init__( )

        self.tbl_name = tbl_name

        self.QBtn = QPushButton()
        self.QBtn.setText("Delete")

        self.setWindowTitle("Delete")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.delete)
        layout = QVBoxLayout()

        self.deleteinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.deleteinput.setValidator(self.onlyInt)
        self.deleteinput.setPlaceholderText("Roll No.")
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
            QMessageBox.information(QMessageBox(),'Successful','Deleted From Table Successful')
            self.close()

            

            
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Delete from the database.')
        server.exit()
