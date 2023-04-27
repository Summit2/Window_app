
table_info ={

    'students' : {
        'columns': ['id_student','fio','login','pswd', 'email'],
        'columns_rus': ["Студент","ФИО",'Логин',"Пароль","Почта"],
        'fkey': ['progress'],
        'rus_name': "Студенты"
    },
    'manager': {
        'columns': ['id_manager','full_name','login','pswd','email','id_area'],
        'columns_rus': ["Менеджер", "ФИО",'Логин',"Пароль","Почта","Предм.область"],
        'fkey': [],
        'rus_name':'Менеджеры'
    },
    'teachers':
    {
        'columns': ['id_teacher','fio','login','pswd', 'email']
        ,
        'columns_rus': ["Преподаватель","ФИО",'Логин',"Пароль","Почта"],
        'fkey':['courses'],
        'rus_name': 'Преподаватели'
    },
    'courses':
    {
        'columns': ['id_course','course_name', 'price','duration','id_area','id_teacher'],
        'columns_rus': ["Курс","Название курса","Цена(руб.)","Длительность(час)","Предм.область","Преподаватель"],
        'fkey': ['progress'],
        'rus_name': 'Курсы'
    },
    'subject_area':
    {
        'columns': ['id_area','area_name']
        ,
        'columns_rus': ["Номер области","Название"],
        'fkey': ['courses', 'manager'],
        'rus_name': 'Предметные области'
    },
    'progress':
    {
        'columns': ['id_progress','id_student','id_course','is_complete','score'],
        'columns_rus': ["Запись", "Студент","Курс","Выполенение","Оценка"],
        'fkey': [],
        'rus_name':'Рейтинг курсов'
    },
    # Названия таблиц на русском языке
    




}
tables_rus= ['Студенты','Менеджеры','Преподаватели','Курсы','Предметные области','Рейтинг курсов']



def get_column(column):
        for col in column:
            yield col
