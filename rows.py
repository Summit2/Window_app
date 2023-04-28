from Dialogs.search import SearchDialog
from Dialogs.rating import RatingDialog
from Dialogs.delete import DeleteDialog
from Dialogs.about import AboutDialog
from Dialogs.insert import InsertDialog
from extra_table import Table
from headers import *





class PushedTable(QMainWindow):
    def __init__(self, tbl_name = 'courses', isAdmin = None):
        self.isAdmin=isAdmin
        if isAdmin == None:
            self.isAdmin=False 
        # self.is_loaded = False #если таблица не загружена, мы не подпадем в update таблицы
        super(PushedTable, self).__init__()
        self.back_button_counter = 0
        #запомнили название таблицы
        self.tbl_name = tbl_name
        self.columns = table_info[tbl_name]['columns']

        self.tableWidget = QTableWidget()

        #добавим возможность изменения внутри таблицы
        self.tableWidget.setRowCount(0)
        self.tableWidget.itemChanged.connect(self.handle_item_changed)

        


        # file_menu = self.menuBar().addMenu("&Действия")    
        #добавили графу связанные таблицы
        if self.isAdmin==True:
            file_menu = self.menuBar().addMenu("&Действия")
        
        #если есть связанные таблицы, добавим соответствующее поле
            # if (len(table_info[self.tbl_name]['fkey'])!= 0):
            #     fkey_menu = self.menuBar().addMenu("&Просмотр подчиненных таблиц")
        #добавляем поиск для админа
        if self.isAdmin==True and (self.tbl_name == 'students' or self.tbl_name == 'courses' or self.tbl_name == 'teachers'):
            # pass
            searchuser_action = QAction(QIcon("icon/seach.png"), "Поиск", self)
            searchuser_action.triggered.connect(lambda: self.search(self.tbl_name, True))
            file_menu.addAction(searchuser_action)
        
        #отчеты
        if (1):

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

        help_menu = self.menuBar().addMenu("&О разработчике")
        if (self.isAdmin==False):
            self.setWindowTitle(f"АС электронных мультимедийных курсов. Панель управления пользователя.\n Таблица '{table_info[self.tbl_name]['rus_name']}'")
        else:
            self.setWindowTitle(f"АС электронных мультимедийных курсов. Панель управления администратора.\n Таблица '{table_info[self.tbl_name]['rus_name']}'")
        
        self.setMinimumSize(900, 600)

        #добавляем вывод таблиц если просмотра:
        if (1):
            
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
        if (1):
            
            self.reports = []
            #надо добавить кнопки на все таблицы
            
            #отчет на всех студентов
            self.reports.append( ("Все студенты"))
            report_all_students = QAction(QIcon(" "), "Все студенты", self)
            report_all_students.triggered.connect(lambda: self.get_report(0))
            self.report_menu.addAction(report_all_students)

            self.reports.append( "Цена курсов")
            report_price = QAction(QIcon(" "), "Цена курсов по возрастанию", self)
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



        # button_edit = QPushButton("Изменить", self)
        # button_edit.setGeometry(1060, 60, 100, 40)
        # button_edit.clicked.connect(lambda: self.edit_data(self))

            



        self.toolbar = QToolBar()
        self.toolbar.setMovable(False)
        self.addToolBar(self.toolbar)

        statusbar = QStatusBar()
        self.setStatusBar(statusbar)
        if (self.isAdmin==True):
            btn_ac_adduser = QAction(QIcon("icon/add.png"), "Добавить запись", self)
            btn_ac_adduser.triggered.connect(self.insert)
            btn_ac_adduser.setStatusTip("Добавить запись")
            self.toolbar.addAction(btn_ac_adduser)
        if (self.isAdmin==True):
            btn_ac_refresh = QAction(QIcon("icon/refresh.png"),"Перезагрузить базу",self)
            btn_ac_refresh.triggered.connect(self.loaddata)
            btn_ac_refresh.setStatusTip("Перезагрузить базу")
            self.toolbar.addAction(btn_ac_refresh)

        if (self.isAdmin==True):
            btn_ac_delete = QAction(QIcon("icon/delete.png"), "Delete", self)
            btn_ac_delete.triggered.connect(self.delete)
            btn_ac_delete.setStatusTip("Delete")
            self.toolbar.addAction(btn_ac_delete)

        #Это кнопки на панели управления
        if (self.isAdmin==True):

            adduser_action = QAction(QIcon(" "),"Добавить запись", self)
            adduser_action.triggered.connect(self.insert)
            file_menu.addAction(adduser_action)
        #здесь я добавляю кнопки на переход на связанные таблицы

        # def edit_data(self, table_name):
        #         try:
        #             selected_row = table_name.currentRow()
        #             player_id = table_name.item(selected_row, 0).text()
        #             last_name = table_name.item(selected_row, 1).text()
        #             first_name = table_name.item(selected_row, 2).text()
        #             age = table_name.item(selected_row, 3).text()
        #             position = table_name.item(selected_row, 4).text()

        #             cursor.execute("UPDATE CSKA_players SET last_name = %s, first_name = %s, age = %s, position = %s WHERE player_id = %s", (last_name, first_name, age, position, player_id,))
        #             conn.commit()
        #             self.admin_window.append("запись успешно изменена")
        #         except:
        #             self.admin_window.append("запись не удалось изменить")

        # if (self.isAdmin==True):
            
        #     self.fkey_table = table_info[self.tbl_name]['fkey'] 
        #     #надо добавить кнопки на все таблицы
        #     if len(table_info[self.tbl_name]['fkey']) == 1:
        #         watch_fkey_action = QAction(QIcon(" "),str(table_info[self.tbl_name]['fkey'][0]), self)
        #         data = str(table_info[self.tbl_name]['fkey'][0])
        #         if type(data)!=None:
        #             watch_fkey_action.triggered.connect(lambda: self.fkey_open(data))

        #         fkey_menu.addAction(watch_fkey_action)

        #     if len(table_info[self.tbl_name]['fkey'] ) == 2:
        #         watch_fkey_action1 = QAction(QIcon(" "),str(table_info[self.tbl_name]['fkey'][0]), self)
        #         data1 = str(table_info[self.tbl_name]['fkey'][0])
        #         if type(data1)!=None:
        #             watch_fkey_action1.triggered.connect(lambda: self.fkey_open(data1))
                    

        #         watch_fkey_action2 = QAction(QIcon(" "),str(table_info[self.tbl_name]['fkey'][1]), self)
        #         data2 = str(table_info[self.tbl_name]['fkey'][1])
        #         if type(data2)!=None:
        #             watch_fkey_action2.triggered.connect(lambda: self.fkey_open(data2))

        #         fkey_menu.addAction(watch_fkey_action1)
        #         fkey_menu.addAction(watch_fkey_action2)
        

            1
        #удаление записи
        if (self.isAdmin==True):
            deluser_action = QAction(QIcon("icon/trash.png"), "Удалить запись", self)
            deluser_action.triggered.connect(self.delete)
            file_menu.addAction(deluser_action)

        #кнопка поиска
        if (1):
            about_action = QAction(QIcon("icon/info.png"),"Разработчик", self)
            about_action.triggered.connect(self.about)
            help_menu.addAction(about_action)



    #функция для изменения информации в таблице
    def handle_item_changed(self, item):
        row = item.row() #Строка
        column = item.column()   #столбец
        # print('row,column =', row, column)
        value = item.text()  
        table = self.tbl_name
        data = self.table_data
        # проверка на то, что мы не пытаемся заменить какой-либо id
        if not (column ==0 or (self.tbl_name == 'manager' and column == 5) or (self.tbl_name == 'courses' and (column == 4 or column == 5)) or
        (self.tbl_name == 'progress' and (column == 1 or column == 2 or column ==4))):
            
            # print(f"Cell {row},{column} changed to {value}")
            s = Server()
            s.cur.execute(f"""update {table} set {table_info[table]['columns'][column]} = '{value}'
                                      where {table_info[table]['columns'][0]} = {data[row][0]} ; """)
            s.exit()
        

    #для пользователей просмотр отчетов
    def get_report(self, index):
        
        # print(self.reports[index])
        self.to_get_report = Server()
        
        if index == 0:
            self.report_table = Table('students',['ФИО'],'select fio from students group by fio;', 'Отчет о всех студентах')
            
        elif index == 1:
            self.report_table = Table('courses', ['Название','Цена (руб)'],"""
            select course_name as Название, sum(price) as pr  from courses group by course_name order by pr ;""","""
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
        
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        self.is_loaded = True
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
        elif self.tbl_name == 'courses':
            
            for i in range(len(table_data)):
                temp = Server()
                temp_area = (temp.cur.execute(f'select area_name from subject_area where id_area={table_data[i][4]}'))
                temp_data = temp.cur.fetchall()[0][0]
                # print(temp_data)
                table_data[i] = list(table_data[i])
                table_data[i][4] = temp_data
                temp.exit()

                temp = Server()
                temp_teacher = (temp.cur.execute(f'select fio from teachers where id_teacher={table_data[i][5]}'))
                temp_data = temp.cur.fetchall()[0][0]
                # print(temp_data)
                table_data[i] = list(table_data[i])
                # print(table_data[i][2])
                table_data[i][5] = temp_data
                temp.exit()
        elif self.tbl_name == 'manager':
            
            for i in range(len(table_data)):
                temp = Server()
                temp_area = (temp.cur.execute(f'select area_name from subject_area where id_area={table_data[i][5]}'))
                temp_data = temp.cur.fetchall()[0][0]
                # print(temp_data)
                table_data[i] = list(table_data[i])
                table_data[i][5] = temp_data
                temp.exit()

                
        

        #Запомнили данные для возможности изменения таблицы
        self.table_data = table_data
        # print(table_data)
        # печатаем таблицы
        for row_number, row_data in enumerate(table_data):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))

        server.exit()
        
        self.is_loaded == False
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
