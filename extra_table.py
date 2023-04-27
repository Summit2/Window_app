from headers import *

class Table(QTableWidget):
    def __init__(self, tbl_name = None ,columns = None, SELECT = None, window_title = None):
        super().__init__()
        ''' создает отдельную висящую в воздухе табличку
            если надо что-то особенное, указывать надо все
            таблицу
            колонки
            свой селект
            и название окошка
        '''
       
        if window_title == None:
            self.setWindowTitle(" ")
        else:
            self.setWindowTitle(f'{window_title}')
        self.setMinimumSize(900, 600)
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
        
        elif fkey_table_name == 'courses' and columns == None:
                for i in range(len(table_data)):
                    temp = Server()
                    temp_student = (temp.cur.execute(f'select area_name from subject_area where id_area={table_data[i][4]}'))
                    temp_data = temp.cur.fetchall()[0][0]
                    # print(temp_data)
                    table_data[i] = list(table_data[i])
                    table_data[i][4] = temp_data
                    temp.exit()

                    temp = Server()
                    temp_student = (temp.cur.execute(f'select fio from teachers where id_teacher={table_data[i][5]}'))
                    temp_data = temp.cur.fetchall()[0][0]
                    # print(temp_data)
                    table_data[i] = list(table_data[i])
                    # print(table_data[i][2])
                    table_data[i][5] = temp_data
                    temp.exit()
                    # table_data[i][1] = list(table_data[i][1])
                    # table_data[i][1] = temp.cur.fetchall()[0][0]
        self.setRowCount(0)
        for row_number, row_data in enumerate(table_data):
            self.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.setItem(row_number, column_number,QTableWidgetItem(str(data)))
        server.exit()
        