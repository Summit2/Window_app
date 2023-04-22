
table_info ={

    'students' : {
        'columns': ['id_student','fio','login','pswd', 'email'],
        'fkey': None
    },
    'manager': {
        'columns': ['id_manager','full_name','login','pswd','email','id_area']
    },
    'teachers':
    {
        'columns': ['id_teacher','fio','login','pswd', 'email']
    },
    'courses':
    {
        'columns': ['id_course','course_name', 'price','duration','id_area','id_teacher']
    },
    'subject_area':
    {
        'columns': ['id_area','area_name']
    },
    'progress':
    {
        'columns': ['id_progress','id_student','id_course','is_complete','score']
    }




}



def get_column(column):
        for col in column:
            yield col
g = get_column( ['id_progress','id_student','id_course','is_complete','score'])
for _ in range(0, len( ['id_progress','id_student','id_course','is_complete','score'])):
    print(next(g))