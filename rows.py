from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
import sys,sqlite3,time

import os

from about_tables import table_info
from posgre_server import Server

class InsertDialog(QDialog):
    def __init__(self,tbl_name = 'students', columns = []):
        super(InsertDialog, self).__init__( )

        self.tbl_name =tbl_name
        self.columns = columns

        self.QBtn = QPushButton()
        self.QBtn.setText("Register")

        self.setWindowTitle(f"Add {tbl_name}")
        self.setFixedWidth(300)
        self.setFixedHeight(250)

        self.QBtn.clicked.connect(self.add)

        layout = QVBoxLayout()
        
        self.values = []
        for items in self.columns[1:] :
            self.nameinput = QLineEdit()
            self.nameinput.setPlaceholderText(items)
            layout.addWidget(self.nameinput)
            
        # self.branchinput = QComboBox()
        # for items in columns[1:] :

        #     self.branchinput.addItem(items)
        # #     self.branchinput.addItem("Civil")
        # # self.branchinput.addItem("Electrical")
        # # self.branchinput.addItem("Electronics and Communication")
        # # self.branchinput.addItem("Computer Science")
        # # self.branchinput.addItem("Information Technology")
        # layout.addWidget(self.branchinput)

        # self.seminput = QComboBox()
        # self.seminput.addItem("1")
        # self.seminput.addItem("2")
        # self.seminput.addItem("3")
        # self.seminput.addItem("4")
        # self.seminput.addItem("5")
        # self.seminput.addItem("6")
        # self.seminput.addItem("7")
        # self.seminput.addItem("8")
        # layout.addWidget(self.seminput)

        # self.mobileinput = QLineEdit()
        # self.mobileinput.setPlaceholderText("Mobile")
        # # self.mobileinput.setInputMask('99999 99999')
        # layout.addWidget(self.mobileinput)

        # self.addressinput = QLineEdit()
        # self.addressinput.setPlaceholderText("Address")
        # layout.addWidget(self.addressinput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def add(self):

        # name = ""
        # branch = ""
        # sem = -1
        # mobile = -1
        # address = ""

        # name = self.nameinput.text()
        # branch = self.branchinput.itemText(self.branchinput.currentIndex())
        # sem = self.seminput.itemText(self.seminput.currentIndex())
        # mobile = self.mobileinput.text()
        # address = self.addressinput.text()

        
        
        self.values = []
        for items in self.columns[1:] :
            
           
            self.values.append(self.nameinput.text())

        try:

            # self.conn = sqlite3.connect("database.db")
            # self.c = self.conn.cursor()
            # self.c.execute("INSERT INTO students (name,branch,sem,Mobile,address) VALUES (?,?,?,?,?)",(name,branch,sem,mobile,address))
            # self.conn.commit()
            # self.c.close()
            # self.conn.close()
            server = Server()
            server.INSERT(self.tbl_name, self.columns, self.values)
            # server.INSERT("INSERT INTO students (name,branch,sem,Mobile,address) VALUES (?,?,?,?,?)",(name,branch,sem,mobile,address))
            
            server.exit()

            QMessageBox.information(QMessageBox(),'Successful','Info added successfully to the database.')
            self.close()

        except Exception:
            print(Exception)
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add student to the database.')

class SearchDialog(QDialog):
    def __init__(self, tbl_name = 'students', columns = [] ):
        super(SearchDialog, self).__init__( )

        self.QBtn = QPushButton()
        self.QBtn.setText("Search")

        self.setWindowTitle("Search user")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.search)
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
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Find student from the database.')

class DeleteDialog(QDialog):
    def __init__(self,tbl_name = 'students', columns = []  ):
        super(DeleteDialog, self).__init__( )

        self.QBtn = QPushButton()
        self.QBtn.setText("Delete")

        self.setWindowTitle("Delete Student")
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
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("DELETE from students WHERE roll="+str(delrol))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(),'Successful','Deleted From Table Successful')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Delete student from the database.')




class AboutDialog(QDialog):
    def __init__(self):
        super(AboutDialog, self).__init__( )

        self.setFixedWidth(300)
        self.setFixedHeight(250)

        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("Ilya Sokolov, \nBMSTU STUDENT")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        labelpic = QLabel()
        pixmap = QPixmap('icon/logo.png')
        pixmap = pixmap.scaledToWidth(275)
        labelpic.setPixmap(pixmap)
        labelpic.setFixedHeight(150)

        layout.addWidget(title)

        layout.addWidget(QLabel("GROUP IU5-43B"))
        layout.addWidget(labelpic)


        layout.addWidget(self.buttonBox)

        self.setLayout(layout)



class PushedTable(QMainWindow):
    def __init__(self, tbl_name = 'manager'):
        super(PushedTable, self).__init__( )
        
        #запомнили название таблицы
        self.tbl_name = tbl_name
        self.columns = table_info[tbl_name]['columns']
        # self.conn = sqlite3.connect("database.db")
        # self.c = self.conn.cursor()
        # self.c.execute("CREATE TABLE IF NOT EXISTS students(roll INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT,branch TEXT,sem INTEGER,mobile INTEGER,address TEXT)")
        # self.c.close()

        file_menu = self.menuBar().addMenu("&File")

        help_menu = self.menuBar().addMenu("&About")
        self.setWindowTitle("Info")

        self.setMinimumSize(800, 600)

        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(len(self.columns)) #указываем количество колонок
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setHorizontalHeaderLabels(self.columns) #указываем названия колонок

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        btn_ac_adduser = QAction(QIcon("icon/add.png"), "Add ", self)
        btn_ac_adduser.triggered.connect(self.insert)
        btn_ac_adduser.setStatusTip("Add ")
        toolbar.addAction(btn_ac_adduser)

        btn_ac_refresh = QAction(QIcon("icon/refresh.png"),"Refresh",self)
        btn_ac_refresh.triggered.connect(self.loaddata)
        btn_ac_refresh.setStatusTip("Refresh")
        toolbar.addAction(btn_ac_refresh)

        btn_ac_search = QAction(QIcon("icon/search.png"), "Search", self)
        btn_ac_search.triggered.connect(self.search)
        btn_ac_search.setStatusTip("Search")
        toolbar.addAction(btn_ac_search)

        btn_ac_delete = QAction(QIcon("icon/trash.png"), "Delete", self)
        btn_ac_delete.triggered.connect(self.delete)
        btn_ac_delete.setStatusTip("Delete")
        toolbar.addAction(btn_ac_delete)

        adduser_action = QAction(QIcon("icon/add.png"),"Insert", self)
        adduser_action.triggered.connect(self.insert)
        file_menu.addAction(adduser_action)

        searchuser_action = QAction(QIcon("icon/search.png"), "Search", self)
        searchuser_action.triggered.connect(self.search)
        file_menu.addAction(searchuser_action)

        deluser_action = QAction(QIcon("icon/trash.png"), "Delete", self)
        deluser_action.triggered.connect(self.delete)
        file_menu.addAction(deluser_action)


        about_action = QAction(QIcon("icon/info.png"),"Developer", self)
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

    def loaddata(self):
        # self.connection = sqlite3.connect("database.db")
        # query = "SELECT * FROM students"
        # result = self.connection.execute(query)
        #создали соединение
        self.server = Server()
        #взяли данные из таблицы
        table_data = self.server.SELECT(self.tbl_name) 
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(table_data):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))
        # self.connection.close()

    def handlePaintRequest(self, printer):
        document = QTextDocument()
        cursor = QTextCursor(document)
        model = self.table.model()
        table = cursor.insertTable(
            model.rowCount(), model.columnCount())
        for row in range(table.rows()):
            for column in range(table.columns()):
                cursor.insertText(model.item(row, column).text())
                cursor.movePosition(QTextCursor.NextCell)
        document.print_(printer)

    def insert(self):
        dlg = InsertDialog(self.tbl_name, self.columns)
        dlg.exec_()

    def delete(self):
        dlg = DeleteDialog(self.tbl_name, self.columns)
        dlg.exec_()

    def search(self):
        dlg = SearchDialog(self.tbl_name, self.columns)
        dlg.exec_()

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()

if __name__=='__main__':
    app = QApplication(sys.argv)
    
    
    window = PushedTable()
    window.show()
    window.loaddata()

    sys.exit(app.exec_())
