from Dialogs.search import SearchDialog
from Dialogs.rating import RatingDialog
from Dialogs.delete import DeleteDialog
from Dialogs.about import AboutDialog
from Dialogs.insert import InsertDialog
from extra_table import Table
from headers import *





class PushedTable(QMainWindow):
    def __init__(self, tbl_name = 'courses', isAdmin = False):
        self.isAdmin=isAdmin
        if isAdmin == None:
            self.isAdmin=True 
        
        super(PushedTable, self).__init__()
        self.back_button_counter = 0
        #запомнили название таблицы
        self.tbl_name = tbl_name
        self.columns = table_info[tbl_name]['columns']

        # file_menu = self.menuBar().addMenu("&Действия")    
        #добавили графу связанные таблицы
        if self.isAdmin==True:
            file_menu = self.menuBar().addMenu("&Действия")
        
        #если есть связанные таблицы, добавим соответствующее поле
            if (len(table_info[self.tbl_name]['fkey'])!= 0):
                fkey_menu = self.menuBar().addMenu("&Просмотр подчиненных таблиц")
        #добавляем поиск для админа
        if self.isAdmin==True:
            # pass
            searchuser_action = QAction(QIcon("icon/search.png"), "Поиск", self)
            searchuser_action.triggered.connect(self.search)
            file_menu.addAction(searchuser_action)

        if (self.isAdmin==False):

            self.report_menu = self.menuBar().addMenu("&Отчеты")
            
        if (self.isAdmin==False):
            self.add_rating = self.menuBar().addMenu("&Действия")
            # self.add_rating.addAction()
            # self.add_rating.triggered.connect(self.rating)
            about_action = QAction(QIcon("icon/info.png"),"Оценить курс", self)
            about_action.triggered.connect(self.rating)

            self.add_rating.addAction(about_action)
            # поиск для всех 

            searchcourses_action = QAction(QIcon("icon.png"), "Поиск по названию курсов", self)
            searchcourses_action.triggered.connect(lambda: self.search('courses',self.isAdmin))
            self.add_rating.addAction(searchcourses_action)
            searchteacher_action = QAction(QIcon("icon.png"), "Поиск по имени преподавателей", self)
            searchteacher_action.triggered.connect(lambda: self.search('teachers',self.isAdmin))
            self.add_rating.addAction(searchteacher_action)
            searchuser_action = QAction(QIcon("icon.png"), "Поиск по имени студентов", self)
            searchuser_action.triggered.connect(lambda: self.search('students', self.isAdmin))
            self.add_rating.addAction(searchuser_action)

        help_menu = self.menuBar().addMenu("&About")
        if (self.isAdmin==False):
            self.setWindowTitle(f"АС электронных мультимедийных курсов. Панель управления пользователя")
        else:
            self.setWindowTitle(f"АС электронных мультимедийных курсов. Панель управления администратора")
        
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
                 
                 if self.tbl_name =='manager' or self.tbl_name =='students' or self.tbl_name =='teachers':
                     self.tableWidget.setColumnCount(2)
                 if self.tbl_name =='manager':
                    
                    self.tableWidget.setHorizontalHeaderLabels(['ФИО', 'email'])
                    
                 elif self.tbl_name =='students':
                    self.tableWidget.setHorizontalHeaderLabels(['ФИО', 'email'])
                 elif self.tbl_name =='teachers':
                     self.tableWidget.setHorizontalHeaderLabels(['ФИО', 'email'])
                

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
        

        
        if (self.isAdmin==True):
            deluser_action = QAction(QIcon("icon/trash.png"), "Delete", self)
            deluser_action.triggered.connect(self.delete)
            file_menu.addAction(deluser_action)

        #кнопка поиска
        if (1):
            about_action = QAction(QIcon("icon/info.png"),"Developer", self)
            about_action.triggered.connect(self.about)
            help_menu.addAction(about_action)

    #для пользователей просмотр отчетов
    def get_report(self, index):
        
        # print(self.reports[index])
        self.to_get_report = Server()
        
        if index == 0:
            self.report_table = Table('students',['ФИО'],'select fio from students group by fio;', 'Отчет о всех студентах')
            
        elif index == 1:
            self.report_table = Table('courses', ['Название','Цена (руб)'],"""
            select course_name as Название, sum(price) as Название from courses group by course_name;""","""
            Отчет о ценах курсов""")

        elif index == 2:
            self.report_table = Table('teachers', ['Имя', 'Почта'] ,'select fio, email from teachers;',
                                      """Отчет о данных учителей
                                      """)
        elif index == 3:
            self.report_table = Table(None, ['Название','Оценка по пятибальной шкале'], '''select course_name , round(sum(cast(score as numeric ))/count(score),2)  from courses 
	inner join progress on progress.id_course =  courses.id_course
		group by course_name;''',''' Отчет об оценках курсов''')
        self.report_table.show()   
    
    #загрузка данных с сервера
    def loaddata(self):
        
        #создали соединение
        server = Server()
        #взяли данные из таблицы
        table_data = server.SELECT(self.tbl_name, self.isAdmin) 
        if self.tbl_name == 'progress':
            
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

    def search(self,tbl_name, is_Admin):
        '''нужно указать is_Admin'''
        dlg = SearchDialog(tbl_name, is_Admin)
        dlg.exec_()

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()
    def rating(self):
        dlg = RatingDialog()
        dlg.exec_()


        

if __name__=='__main__':
    app = QApplication(sys.argv)
    
    
    window = PushedTable()
    window.show()
    window.loaddata()

    sys.exit(app.exec_())
