
table_info ={

    'students' : {
        'columns': ['id_student','fio','login','pswd', 'email'],
        'columns_rus': ["Студент","ФИО",'Логин',"Пароль","Почта"],
        'fkey': ['progress']
    },
    'manager': {
        'columns': ['id_manager','full_name','login','pswd','email','id_area'],
        'columns_rus': ["Менеджер", "ФИО",'Логин',"Пароль","Почта","Предм.область"],
        'fkey': []
    },
    'teachers':
    {
        'columns': ['id_teacher','fio','login','pswd', 'email']
        ,
        'columns_rus': ["Преподаватель","ФИО",'Логин',"Пароль","Почта"],
        'fkey':['courses']
    },
    'courses':
    {
        'columns': ['id_course','course_name', 'price','duration','id_area','id_teacher'],
        'columns_rus': ["Курс","Название курса","Цена(руб.)","Длительность(час)","Предм.область","Преподаватель"],
        'fkey': ['progress']
    },
    'subject_area':
    {
        'columns': ['id_area','area_name']
        ,
        'columns_rus': ["Номер области","Название"],
        'fkey': ['courses', 'manager']
    },
    'progress':
    {
        'columns': ['id_progress','id_student','id_course','is_complete','score'],
        'columns_rus': ["Запись", "Студент","Курс","Выполенение","Оценка"],
        'fkey': []
    },
    # Названия таблиц на русском языке
    




}
tables_rus= ['Студенты','Менеджеры','Преподаватели','Курсы','Предметные области','Рейтинг курсов']



def get_column(column):
        for col in column:
            yield col
