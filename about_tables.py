
table_info ={

    'students' : {
        'columns': ['id_student','fio','login','pswd', 'email'],
        'columns_rus': ["Номер студента","ФИО",'Логин',"Пароль","Почта"],
        'fkey': ['progress']
    },
    'manager': {
        'columns': ['id_manager','full_name','login','pswd','email','id_area'],
        'columns_rus': ["Номер менеджера", "ФИО",'Логин',"Пароль","Почта","Номер предм.области"],
        'fkey': []
    },
    'teachers':
    {
        'columns': ['id_teacher','fio','login','pswd', 'email']
        ,
        'columns_rus': ["Номер преподавателя","ФИО",'Логин',"Пароль","Почта"],
        'fkey':['courses']
    },
    'courses':
    {
        'columns': ['id_course','course_name', 'price','duration','id_area','id_teacher'],
        'columns_rus': ["Номер курса","Название курса","Цена","Длительность","Номер предм.области","Номер преподавателя"],
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
        'columns_rus': ["Номер записи", "Студент","Курс","Выполенение","Оценка"],
        'fkey': []
    }




}



def get_column(column):
        for col in column:
            yield col
