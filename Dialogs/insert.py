from headers import *
class InsertDialog(QDialog):
    def __init__(self,tbl_name = 'students', columns = [], isAdmin = None):
        '''
        для каждого inserta для конкретной таблице, если есть внешние ключи,
        дать пользователю не вписывать номер, а выбирать внешний ключ через select из другой таблицы
        '''
        super(InsertDialog, self).__init__()

        self.tbl_name =tbl_name
        self.columns = columns

        self.QBtn = QPushButton()
        self.QBtn.setText("Добавить запись")

        self.setWindowTitle(f"Новая запись в таблицу '{table_info[tbl_name]['rus_name']}'")
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

            # добавим предметную область, выведя все возможные 
            self.area_box_name = QLabel("Предметная область")
            
            self.area_box = QComboBox()
            #теперь в area box надо добавить все предметные области запросом
            s = Server()
            s.cur.execute('select id_area, area_name from subject_area;')
            self.all_areas = s.cur.fetchall()
            for a in self.all_areas:
                self.area_box.addItem(f"{a[1]}")
            s.exit()
            # self.input6 = QLineEdit()
            # self.input6.setPlaceholderText(next(gen))
            # layout.addWidget(self.input1)  
            layout.addWidget(self.input2) 
            layout.addWidget(self.input3) 
            layout.addWidget(self.input4) 
            layout.addWidget(self.input5) 
            
            
            
            # layout.addWidget(self.input6) 
            layout.addWidget(self.area_box_name)
            layout.addWidget(self.area_box) 

            
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
            next(gen)
            self.input2 = QLineEdit()
            self.input2.setPlaceholderText(next(gen))
            
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
        for col in table_info[self.tbl_name]['columns_rus']:
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
            #надо добавить предметную область по индексу
            area = self.area_box.itemText(self.area_box.currentIndex())
            print(area)
            s = Server()
            s.cur.execute(f"select id_area from subject_area where area_name = '{area}'")
            area_for_manager = (s.cur.fetchall())[0][0]
            print(area_for_manager)
            
            s.exit()
            self.insert_values.append(str(area_for_manager))
        elif self.tbl_name == 'progress':  
            self.insert_values.append(self.input2.text())
            self.insert_values.append(self.input3.text())
            self.insert_values.append(self.input4.text())
            self.insert_values.append(f"'{self.input5.text()}'")
            self.insert_values.append(self.input6.text()) 

        try:

            server = Server()
            print(self.tbl_name, table_info[self.tbl_name]['columns'], self.insert_values)
            server.INSERT(self.tbl_name, table_info[self.tbl_name]['columns'], self.insert_values)
            
            server.exit()

            QMessageBox.information(QMessageBox(),'Успех','Информация успешно добавлена. Обновите базу')
            self.close()

        except Exception:
            # print(Exception)
            QMessageBox.warning(QMessageBox(), 'Ошибка', 'Не удалось добавить запись')
