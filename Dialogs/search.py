from headers import *
from extra_table import Table
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
        self.QBtn.setText("Поиск")
        if self.isAdmin == True:
            self.setWindowTitle("Поиск по таблице")
             

        if self.tbl_name == 'courses' and self.isAdmin == False:

            self.setWindowTitle("Поиск по имени студентов")
            
        if self.tbl_name == 'teachers' and self.isAdmin == False:

            self.setWindowTitle("Начните вводить имя преподавателя")
        if self.tbl_name == 'courses' and self.isAdmin == False:

            self.setWindowTitle("Начните вводить название курса")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(lambda: self.search())

        layout = QVBoxLayout()

        self.searchinput = QLineEdit()
        # self.onlyInt = QIntValidator()
        # self.searchinput.setValidator(self.onlyInt)
        
        layout.addWidget(self.searchinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def search(self):

        searchrol = ""
        searchrol = self.searchinput.text()

        #выдаем ответ на поиск для пользователей
        if not self.isAdmin:
            if self.tbl_name == 'courses':
                self.extra_table = Table('courses',['Название','Цена',"Рейтинг"],f"""
                select course_name, round(sum(courses.price)/count(price),2), round(sum(cast (score as numeric))/(count(score)),2 ) from courses inner join progress on  
                    courses.id_course = progress.id_course where course_name like '{searchrol}%'
					group by course_name  ""","Поиск по названию курсов")
                self.extra_table.show()
                self.hide()
            elif self.tbl_name == 'teachers':
                self.extra_table = Table('teachers',["Имя", "Почта"],f"""select fio, email from teachers 
                where fio like '{searchrol}%';""","Поиск по имени преподавателей")
                self.extra_table.show()
                self.hide()
            elif self.tbl_name == 'students':
                self.extra_table = Table('students',['Имя', "Количество пройденных курсов"],f"""
                select fio, count(id_course) filter (where is_complete = True ) from students 
	                inner join progress on progress.id_student = students.id_student 
		                where fio like '{searchrol}%' group by fio;""",
                        "Поиск по имени студентов")
                self.extra_table.show()
                self.hide()

        if self.isAdmin==True:
            if self.tbl_name == 'courses':
                self.extra_table = Table('courses',table_info[self.tbl_name]['columns_rus'],f"""
                select * from courses where course_name like '{searchrol}%';
					 ""","Поиск по названию курсов")
                self.extra_table.show()
                self.hide()
            elif self.tbl_name == 'teachers':
                self.extra_table = Table('teachers',table_info[self.tbl_name]['columns_rus'],f"""select * from teachers 
                where fio like '{searchrol}%';""","Поиск по имени преподавателей")
                self.extra_table.show()
                self.hide()
            elif self.tbl_name == 'students':
                self.extra_table = Table('students',table_info[self.tbl_name]['columns_rus'],f"""
                select * from students 
	                
		                where fio like '{searchrol}%'""",
                        "Поиск по имени студентов")
                self.extra_table.show()
                self.hide()
            elif self.tbl_name == 'manager':
                self.extra_table = Table('students',table_info[self.tbl_name]['columns_rus'],f"""
                select * from manager 
	                
		                where fio like '{searchrol}%'""",
                        "Поиск по имени студентов")
                self.extra_table.show()
                self.hide()
            
                self.extra_table.show()
                self.hide()

        # try:
        #     self.conn = sqlite3.connect("database.db")
        #     self.c = self.conn.cursor()
        #     result = self.c.execute("SELECT * from students")
        #     row = result.fetchone()
        #     serachresult = "Rollno : "+str(row[0])+'\n'+"Name : "+str(row[1])+'\n'+"Branch : "+str(row[2])+'\n'+"Sem : "+str(row[3])+'\n'+"Address : "+str(row[4])
        #     QMessageBox.information(QMessageBox(), 'Successful', serachresult)
        #     self.conn.commit()
        #     self.c.close()
        #     self.conn.close()
        # except Exception:
        #     QMessageBox.warning(QMessageBox(), 'Error', f'Could not Find {self.tbl_name } from the database.')
