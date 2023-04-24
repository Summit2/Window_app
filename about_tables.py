
table_info ={

    'students' : {
        'columns': ['id_student','fio','login','pswd', 'email'],
        'fkey': ['progress']
    },
    'manager': {
        'columns': ['id_manager','full_name','login','pswd','email','id_area'],
        'fkey': []
    },
    'teachers':
    {
        'columns': ['id_teacher','fio','login','pswd', 'email']
        ,
        'fkey':['courses']
    },
    'courses':
    {
        'columns': ['id_course','course_name', 'price','duration','id_area','id_teacher'],
        'fkey': ['progress']
    },
    'subject_area':
    {
        'columns': ['id_area','area_name']
        ,
        'fkey': ['courses', 'manager']
    },
    'progress':
    {
        'columns': ['id_progress','id_student','id_course','is_complete','score'],
        'fkey': []
    }




}



def get_column(column):
        for col in column:
            yield col
