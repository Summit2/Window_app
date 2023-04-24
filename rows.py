from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
import sys,sqlite3

# import os

from about_tables import table_info
from posgre_server import Server


class RatingDialog(QDialog):
    def __init__(self):
        super(RatingDialog, self).__init__()

        

        self.QBtn = QPushButton()
        self.QBtn.setText("Оставить оценку")

        self.setWindowTitle(f"Оценить курс")
        self.setFixedWidth(300)
        self.setFixedHeight(250)

        # self.QBtn.clicked.connect('')

        layout = QVBoxLayout()
        
        # self.input1 = QLineEdit()
        # self.input1.setPlaceholderText('Оценка')
            
        # layout.addWidget(self.input1) 
            

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

        # Self.QBtn = QPushButton()   #create Push button
        # self.QBtn.setText("Register")

       
        self.setFixedWidth(300)
        self.setFixedHeight(250)
        
        self.QBtn.clicked.connect(self.add_score)

        # layout = QVBoxLayout()  #set verticle layout

        # self.nameinput = QLineEdit()
        # self.nameinput.setPlaceholderText("Name")
        # layout.addWidget(self.nameinput)

        # self.branchinput = QComboBox() # create and add value to combobox
        # self.branchinput.addItem("Mechanical")
        # self.branchinput.addItem("Civil")
        # self.branchinput.addItem("Electrical")
        # self.branchinput.addItem("Electronics and Communication")
        # self.branchinput.addItem("Computer Science")
        # self.branchinput.addItem("Information Technology")
        # layout.addWidget(self.branchinput)
        self.name = QLabel("Название курса:")

        layout.addWidget(self.name)
        self.courses_names = QComboBox()
        semidata=["С++ для чайников",
            "Оптика для тех, у кого лапки",
            "Java для чайников",
            "Основы программирования",
            "Python for nothing",
            "Ядерная физика для самых маленьких",
            "Интегралы и Дифференциальные уравнения",
            "Использование штанги для становления чемпионом"]
        self.courses_names.addItem(semidata[0])
        self.courses_names.addItem(semidata[1])
        self.courses_names.addItem(semidata[2])
        self.courses_names.addItem(semidata[3])
        self.courses_names.addItem(semidata[4])
        self.courses_names.addItem(semidata[5])
        self.courses_names.addItem(semidata[6])
        self.courses_names.addItem(semidata[7])
        layout.addWidget(self.courses_names)

        # self.mobileinput = QLineEdit()
        # self.mobileinput.setPlaceholderText("Mobile")
        # self.mobileinput.setInputMask('99999 99999') # set validator for user can only input interger input
        # layout.addWidget(self.mobileinput)

        self.score = QLabel("Oценка:")

        layout.addWidget(self.score)
        
        self.seminput = QComboBox()
        self.seminput.addItem("1")
        self.seminput.addItem("2")
        self.seminput.addItem("3")
        self.seminput.addItem("4")
        self.seminput.addItem("5")
        
        layout.addWidget(self.seminput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

# this function get value from all input box and insert these values in database.

    def add_score(self):

        
        c_name = self.courses_names.itemText(self.courses_names.currentIndex())
        grade = self.seminput.itemText(self.seminput.currentIndex())
        # print(c_name)
        # print(grade)
        
        serv = Server()
        print(c_name)
        serv.cur.execute( f"select id_course from courses where course_name = '{c_name}' ;")
        name_course  = (serv.cur.fetchall())[0][0]
        serv.cur.execute(f"insert into progress (id_student,id_course,is_complete,score) values (19,'{name_course}','true',{grade});")
        serv.exit()

        self.close()

class InsertDialog(QDialog):
    def __init__(self,tbl_name = 'students', columns = [], isAdmin = None):
        super(InsertDialog, self).__init__()

        self.tbl_name =tbl_name
        self.columns = columns

        self.QBtn = QPushButton()
        self.QBtn.setText("Register")

        self.setWindowTitle(f"Add {tbl_name}")
        self.setFixedWidth(300)
        self.setFixedHeight(250)

        self.QBtn.clicked.connect(self.add)

        layout = QVBoxLayout()
        

        #генератор для последовательного взятия колонок
        gen  = self.get_column()
        
        
        
        if self.tbl_name == 'students':
            
            self.input1 = QLineEdit()
            self.input1.setPlaceholderText(next(gen))
            self.input2 = QLineEdit()
            self.input2.setPlaceholderText(next(gen))
            self.input3 = QLineEdit()
            self.input3.setPlaceholderText(next(gen))
            self.input4 = QLineEdit()
            self.input4.setPlaceholderText(next(gen))
            self.input5 = QLineEdit()
            self.input5.setPlaceholderText(next(gen))
             
            layout.addWidget(self.input2) 
            layout.addWidget(self.input3) 
            layout.addWidget(self.input4) 
            layout.addWidget(self.input5) 


        elif self.tbl_name == 'manager':
        
            self.input1 = QLineEdit()
            self.input1.setPlaceholderText(next(gen))
            self.input2 = QLineEdit()
            self.input2.setPlaceholderText(next(gen))
            self.input3 = QLineEdit()
            self.input3.setPlaceholderText(next(gen))
            self.input4 = QLineEdit()
            self.input4.setPlaceholderText(next(gen))
            self.input5 = QLineEdit()
            self.input5.setPlaceholderText(next(gen))
            self.input6 = QLineEdit()
            self.input6.setPlaceholderText(next(gen))
            # layout.addWidget(self.input1)  
            layout.addWidget(self.input2) 
            layout.addWidget(self.input3) 
            layout.addWidget(self.input4) 
            layout.addWidget(self.input5) 
            layout.addWidget(self.input6) 

            
        elif self.tbl_name == 'teachers':
            self.input1 = QLineEdit()
            self.input1.setPlaceholderText(next(gen))
            self.input2 = QLineEdit()
            self.input2.setPlaceholderText(next(gen))
            self.input3 = QLineEdit()
            self.input3.setPlaceholderText(next(gen))
            self.input4 = QLineEdit()
            self.input4.setPlaceholderText(next(gen))
            self.input5 = QLineEdit()
            self.input5.setPlaceholderText(next(gen))
            
            # layout.addWidget(self.input1)  
            layout.addWidget(self.input2) 
            layout.addWidget(self.input3) 
            layout.addWidget(self.input4) 
            layout.addWidget(self.input5) 
             
            
        elif self.tbl_name == 'courses':
            self.input1 = QLineEdit()
            self.input1.setPlaceholderText(next(gen))
            self.input2 = QLineEdit()
            self.input2.setPlaceholderText(next(gen))
            self.input3 = QLineEdit()
            self.input3.setPlaceholderText(next(gen))
            self.input4 = QLineEdit()
            self.input4.setPlaceholderText(next(gen))
            self.input5 = QLineEdit()
            self.input5.setPlaceholderText(next(gen))
            self.input6 = QLineEdit()
            self.input6.setPlaceholderText(next(gen))
            # layout.addWidget(self.input1)  
            layout.addWidget(self.input2) 
            layout.addWidget(self.input3) 
            layout.addWidget(self.input4) 
            layout.addWidget(self.input5) 
            layout.addWidget(self.input6) 

        elif self.tbl_name == 'subject_area':
            self.input1 = QLineEdit()
            self.input1.setPlaceholderText(next(gen))
            
            # layout.addWidget(self.input1)  
            layout.addWidget(self.input2) 
            
        elif self.tbl_name == 'progress':
            self.input1 = QLineEdit()
            self.input1.setPlaceholderText(next(gen))
            self.input2 = QLineEdit()
            self.input2.setPlaceholderText(next(gen))
            self.input3 = QLineEdit()
            self.input3.setPlaceholderText(next(gen))
            self.input4 = QLineEdit()
            self.input4.setPlaceholderText(next(gen))
            self.input5 = QLineEdit()
            self.input5.setPlaceholderText(next(gen))
            
            
            layout.addWidget(self.input2) 
            layout.addWidget(self.input3) 
            layout.addWidget(self.input4) 
            layout.addWidget(self.input5) 

        layout.addWidget(self.QBtn)
        self.setLayout(layout)
    def get_column(self):
        for col in self.columns:
            yield str(col)
    def add(self):
        #массив значений для insert 
        self.insert_values = []

        if self.tbl_name == 'students':
            self.insert_values.append(f"'{self.input2.text()}'")
            self.insert_values.append(f"'{self.input3.text()}'")
            self.insert_values.append(f"'{self.input4.text()}'")
            self.insert_values.append(f"'{self.input5.text()}'")

        elif self.tbl_name == 'teachers':
            self.insert_values.append(f"'{self.input2.text()}'")
            self.insert_values.append(f"'{self.input3.text()}'")
            self.insert_values.append(f"'{self.input4.text()}'")
            self.insert_values.append(f"'{self.input5.text()}'")
            # self.insert_values.append(f"'{self.input6.text()}'")
        elif self.tbl_name == 'courses':
            self.insert_values.append(f"'{self.input2.text()}'")
            self.insert_values.append(self.input3.text())
            self.insert_values.append(self.input4.text())
            self.insert_values.append(self.input5.text())
            self.insert_values.append(self.input6.text())
        elif self.tbl_name == 'subject_area':
            self.insert_values.append(f"'{self.input2.text()}'")
        elif self.tbl_name == 'manager':
            self.insert_values.append(f"'{self.input2.text()}'")
            self.insert_values.append(f"'{self.input3.text()}'")
            self.insert_values.append(f"'{self.input4.text()}'")
            self.insert_values.append(f"'{self.input5.text()}'")
            self.insert_values.append(self.input6.text())
        elif self.tbl_name == 'progress':  
            self.insert_values.append(self.input2.text())
            self.insert_values.append(self.input3.text())
            self.insert_values.append(self.input4.text())
            self.insert_values.append(f"'{self.input5.text()}'")
            self.insert_values.append(self.input6.text()) 

        try:

            server = Server()

            server.INSERT(self.tbl_name, self.columns, self.insert_values)
            
            server.exit()

            QMessageBox.information(QMessageBox(),'Successful','Info added successfully to the database.')
            self.close()

        except Exception:
            # print(Exception)
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add student to the database.')

class SearchDialog(QDialog):
    def __init__(self, tbl_name = 'manager', columns = [] ):
        super(SearchDialog, self).__init__( )

        self.tbl_name = tbl_name

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
            QMessageBox.warning(QMessageBox(), 'Error', f'Could not Find {self.tbl_name } from the database.')

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
    def __init__(self, tbl_name = 'courses', isAdmin = 1):
        self.isAdmin=isAdmin
        if isAdmin == None:
            self.isAdmin=True 
        
        super(PushedTable, self).__init__()
        self.back_button_counter = 0
        #запомнили название таблицы
        self.tbl_name = tbl_name
        self.columns = table_info[tbl_name]['columns']

        #добавили графу связанные таблицы
        if self.isAdmin==True:
            file_menu = self.menuBar().addMenu("&File")
        #если есть связанные таблицы, добавим соответствующее поле
            if (len(table_info[self.tbl_name]['fkey'])!= 0):
                fkey_menu = self.menuBar().addMenu("&Просмотр подчиненных таблиц")


        if (self.isAdmin==False):

            self.report_menu = self.menuBar().addMenu("&Отчеты")
            
        if (self.isAdmin==False):
            self.add_rating = self.menuBar().addMenu("&Действия с курсами")
            # self.add_rating.addAction()
            # self.add_rating.triggered.connect(self.rating)
            about_action = QAction(QIcon("icon/info.png"),"Оценить курс", self)
            about_action.triggered.connect(self.rating)

            self.add_rating.addAction(about_action)

        help_menu = self.menuBar().addMenu("&About")
        self.setWindowTitle(f"Таблица '{self.tbl_name}'")
        
        self.setMinimumSize(800, 600)

        #добавляем вывод таблиц если просмотра:
        if (1):
            self.tableWidget = QTableWidget()
            self.setCentralWidget(self.tableWidget)
            self.tableWidget.setAlternatingRowColors(True)
            
            self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
            self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
            self.tableWidget.horizontalHeader().setStretchLastSection(True)
            self.tableWidget.verticalHeader().setVisible(False)
            self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
            self.tableWidget.verticalHeader().setStretchLastSection(False)
            if (self.isAdmin==True):
                self.tableWidget.setColumnCount(len(self.columns)) #указываем количество колонок
                self.tableWidget.setHorizontalHeaderLabels(table_info[self.tbl_name]['columns_rus']) #указываем названия колонок
            if self.isAdmin ==False:
                 self.tableWidget.setColumnCount(2)
                 if self.tbl_name =='manager':
                    self.tableWidget.setHorizontalHeaderLabels(['ФИО', 'email'])
                 elif self.tbl_name =='students':
                    self.tableWidget.setHorizontalHeaderLabels(['ФИО', 'email'])
                 elif self.tbl_name =='teachers':
                     self.tableWidget.setHorizontalHeaderLabels(['ФИО', 'email'])
                 else:
                     self.tableWidget.setHorizontalHeaderLabels([" ", ''])


        #добавляем отчеты для обычных пользователей
        if (self.isAdmin==False):
            
            self.reports = []
            #надо добавить кнопки на все таблицы
            
            #отчет на всех студентов
            self.reports.append( ("Все студенты"))
            report_all_students = QAction(QIcon(" "), "Все студенты", self)
            report_all_students.triggered.connect(lambda: self.get_report(0))
            self.report_menu.addAction(report_all_students)

            self.reports.append( "Цена курсов")
            report_price = QAction(QIcon(" "), "Цена курсов", self)
            report_price.triggered.connect(lambda: self.get_report(1))
            self.report_menu.addAction(report_price)

            self.reports.append( "Контакты преподавателей")
            report_teachers_contacts = QAction(QIcon(" "), "Контакты преподавателей", self)
            report_teachers_contacts.triggered.connect(lambda: self.get_report(2))
            self.report_menu.addAction(report_teachers_contacts)

            self.reports.append( "Рейтинг курсов")
            report_rating = QAction(QIcon(" "), "Рейтинг курсов", self)
            report_rating.triggered.connect(lambda: self.get_report(3))
            self.report_menu.addAction(report_rating)



        
            



        self.toolbar = QToolBar()
        self.toolbar.setMovable(False)
        self.addToolBar(self.toolbar)

        statusbar = QStatusBar()
        self.setStatusBar(statusbar)
        if (self.isAdmin==True):
            btn_ac_adduser = QAction(QIcon("icon/add.png"), "Add ", self)
            btn_ac_adduser.triggered.connect(self.insert)
            btn_ac_adduser.setStatusTip("Add")
            self.toolbar.addAction(btn_ac_adduser)
        if (self.isAdmin==True):
            btn_ac_refresh = QAction(QIcon("icon/refresh.png"),"Refresh",self)
            btn_ac_refresh.triggered.connect(self.loaddata)
            btn_ac_refresh.setStatusTip("Refresh")
            self.toolbar.addAction(btn_ac_refresh)

        if (self.isAdmin==True):
            btn_ac_delete = QAction(QIcon("icon/delete.png"), "Delete", self)
            btn_ac_delete.triggered.connect(self.delete)
            btn_ac_delete.setStatusTip("Delete")
            self.toolbar.addAction(btn_ac_delete)

        #Это кнопки на панели управления
        if (self.isAdmin==True):
            adduser_action = QAction(QIcon(" "),"Insert", self)
            adduser_action.triggered.connect(self.insert)
            file_menu.addAction(adduser_action)
        #здесь я добавляю кнопки на переход на связанные таблицы
        if (self.isAdmin==True):
            
            self.fkey_table = table_info[self.tbl_name]['fkey'] 
            #надо добавить кнопки на все таблицы
            if len(table_info[self.tbl_name]['fkey']) == 1:
                watch_fkey_action = QAction(QIcon(" "),str(table_info[self.tbl_name]['fkey'][0]), self)
                data = str(table_info[self.tbl_name]['fkey'][0])
                if type(data)!=None:
                    watch_fkey_action.triggered.connect(lambda: self.fkey_open(data))

                fkey_menu.addAction(watch_fkey_action)

            if len(table_info[self.tbl_name]['fkey'] ) == 2:
                watch_fkey_action1 = QAction(QIcon(" "),str(table_info[self.tbl_name]['fkey'][0]), self)
                data1 = str(table_info[self.tbl_name]['fkey'][0])
                if type(data1)!=None:
                    watch_fkey_action1.triggered.connect(lambda: self.fkey_open(data1))
                    

                watch_fkey_action2 = QAction(QIcon(" "),str(table_info[self.tbl_name]['fkey'][1]), self)
                data2 = str(table_info[self.tbl_name]['fkey'][1])
                if type(data2)!=None:
                    watch_fkey_action2.triggered.connect(lambda: self.fkey_open(data2))

                fkey_menu.addAction(watch_fkey_action1)
                fkey_menu.addAction(watch_fkey_action2)

        # searchuser_action = QAction(QIcon("icon/search.png"), "Search", self)
        # searchuser_action.triggered.connect(self.search)
        # file_menu.addAction(searchuser_action)
        if (self.isAdmin==True):
            deluser_action = QAction(QIcon("icon/trash.png"), "Delete", self)
            deluser_action.triggered.connect(self.delete)
            file_menu.addAction(deluser_action)


        if (self.isAdmin==False):
            about_action = QAction(QIcon("icon/info.png"),"Developer", self)
            about_action.triggered.connect(self.about)
            help_menu.addAction(about_action)

    #для пользователей просмотр отчетов
    def get_report(self, index):
        
        # print(self.reports[index])
        self.to_get_report = Server()
        
        if index == 0:
            

            self.report_table = Table('students',['ФИО'],'select fio from students group by fio;')
            
        elif index == 1:
            self.report_table = Table('courses', ['Название','Цена (руб)'],'select course_name as Название, sum(price) as Название from courses group by course_name;')

        elif index ==2:
            self.report_table = Table('teachers', ['Имя', 'Почта'] ,'select fio, email from teachers;')
        elif index ==3:
            self.report_table = Table(None, ['Название','Оценка по пятибальной шкале'], '''select course_name , round(sum(cast(score as numeric ))/count(score),2)  from courses 
	inner join progress on progress.id_course =  courses.id_course
		group by course_name;''')
        self.report_table.show()   
    
    
    def loaddata(self):
        
        #создали соединение
        server = Server()
        #взяли данные из таблицы
        table_data = server.SELECT(self.tbl_name, self.isAdmin) 
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(table_data):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))

        server.exit()
        

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
    
    
    #для админа добавим просмотр связанных таблиц
    @pyqtSlot()
    def fkey_open(self,fkey_table_name):
        
        

        self.w = Table(fkey_table_name)
        self.w.show()
    def back(self):

        #self.btn_back
        
        
        self.w.hide()
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
    def rating(self):
        dlg = RatingDialog()
        # print('succ')
        dlg.exec_()

class Table(QTableWidget):
    def __init__(self, tbl_name = None ,columns = None, SELECT = None):
        super().__init__()

       

    
        
        # dlg = FkeyDialog(fkey_table_name, self.columns) 
        # # dlg.exec_()
        # dlg.show()
        
        self.setWindowTitle(" ")
        self.setMinimumSize(800, 600)
        fkey_table_name =tbl_name
        self.columns = columns
        self.setAlternatingRowColors(True)
        if columns == None:
            self.setColumnCount(len(table_info[fkey_table_name]['columns'])) #указываем количество колонок
        else:
            self.setColumnCount(len(self.columns))
        self.horizontalHeader().setCascadingSectionResizes(False)
        self.horizontalHeader().setSortIndicatorShown(False)
        self.horizontalHeader().setStretchLastSection(True)
        self.verticalHeader().setVisible(False)
        self.verticalHeader().setCascadingSectionResizes(False)
        self.verticalHeader().setStretchLastSection(False)
        if columns == None:
            self.setHorizontalHeaderLabels(table_info[fkey_table_name]['columns_rus'])#указываем названия колонок
        else:
            self.setHorizontalHeaderLabels(self.columns)

        #создали соединение
        server = Server()
        if SELECT==None:
            #взяли данные из таблицы
            table_data = server.SELECT(fkey_table_name) 
            
        else:
            
            self.to_get_report = Server()
        
        
            self.to_get_report.cur.execute(f'{SELECT}')

            #запоминаем информацию с селекта
            table_data = self.to_get_report.cur.fetchall()
            # print(table_data)
        # student_data = temp.cur.fetchall()
        # print(student_data)
        print(table_data)
        if fkey_table_name == 'progress':
            for i in range(len(table_data)):
                temp = Server()
                temp_student = (temp.cur.execute(f'select fio from students where id_student={table_data[i][1]}'))
                temp_data = temp.cur.fetchall()[0][0]
                # print(temp_data)
                table_data[i] = list(table_data[i])
                table_data[i][1] = temp_data
                temp.exit()

                temp = Server()
                temp_student = (temp.cur.execute(f'select course_name from courses where id_course={table_data[i][2]}'))
                temp_data = temp.cur.fetchall()[0][0]
                # print(temp_data)
                table_data[i] = list(table_data[i])
                # print(table_data[i][2])
                table_data[i][2] = temp_data
                temp.exit()
                # table_data[i][1] = list(table_data[i][1])
                # table_data[i][1] = temp.cur.fetchall()[0][0]
        self.setRowCount(0)
        for row_number, row_data in enumerate(table_data):
            self.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.setItem(row_number, column_number,QTableWidgetItem(str(data)))
        server.exit()
        
        

if __name__=='__main__':
    app = QApplication(sys.argv)
    
    
    window = PushedTable()
    window.show()
    window.loaddata()

    sys.exit(app.exec_())
