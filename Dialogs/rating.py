from headers import *
class RatingDialog(QDialog):
    def __init__(self):
        super(RatingDialog, self).__init__()

        

        self.QBtn = QPushButton()
        self.QBtn.setText("Оставить оценку")

        self.setWindowTitle(f"Оценить курс")
        self.setFixedWidth(300)
        self.setFixedHeight(250)

        

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
        data=["С++ для чайников",
            "Оптика для тех, у кого лапки",
            "Java для чайников",
            "Основы программирования",
            "Python for nothing",
            "Ядерная физика для самых маленьких",
            "Интегралы и Дифференциальные уравнения",
            "Использование штанги для становления чемпионом"]
        
        s = Server()
        s.cur.execute("""select course_name from courses;""")
        semidata = [i[0] for i in s.cur.fetchall()]
        
        s.exit()

        s =Server()
        s.cur.execute("select course_name from progress  inner join courses on progress.id_course = courses.id_course where progress.id_student = 19;")
        is_complete = [i[0] for i in s.cur.fetchall()]


        


        print(is_complete)
        for i in range(len( semidata )):
            if semidata[i] in is_complete:
                self.courses_names.addItem(semidata[i])
            # self.courses_names.addItem(semidata[1])
            # self.courses_names.addItem(semidata[2])
            # self.courses_names.addItem(semidata[3])
            # self.courses_names.addItem(semidata[4])
            # self.courses_names.addItem(semidata[5])
            # self.courses_names.addItem(semidata[6])
            # self.courses_names.addItem(semidata[7])
        layout.addWidget(self.courses_names)
        
        s.exit()
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
        print(name_course)
        serv.cur.execute(f"insert into progress (id_student,id_course,is_complete,score) values (19,'{name_course}','true',{grade});")
        serv.exit()

        self.close()