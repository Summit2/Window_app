from headers import *

class SearchDialog(QDialog):
    def __init__(self, tbl_name = 'manager', is_Admin = None ):
        super(SearchDialog, self).__init__( )
        self.tbl_name = tbl_name
        if is_Admin ==None:
            self.isAdmin =True
        else:
            self.isAdmin = is_Admin
        self.tbl_name = tbl_name

        self.QBtn = QPushButton()
        self.QBtn.setText("Search")
        
        if self.tbl_name == 'courses' and self.isAdmin == False:

            self.setWindowTitle("Поиск по")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(lambda: self.search)

        layout = QVBoxLayout()

        self.searchinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.searchinput.setValidator(self.onlyInt)
        self.searchinput.setPlaceholderText("Roll No.")
        layout.addWidget(self.searchinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def search(self):

        searchrol = ""
        searchrol = self.searchinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            result = self.c.execute("SELECT * from students")
            row = result.fetchone()
            serachresult = "Rollno : "+str(row[0])+'\n'+"Name : "+str(row[1])+'\n'+"Branch : "+str(row[2])+'\n'+"Sem : "+str(row[3])+'\n'+"Address : "+str(row[4])
            QMessageBox.information(QMessageBox(), 'Successful', serachresult)
            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', f'Could not Find {self.tbl_name } from the database.')
