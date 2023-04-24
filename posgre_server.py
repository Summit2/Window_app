from about_tables import table_info
import psycopg2
class Server:
    def __init__(self) -> None:
# Connect to your postgres DB
        self.conn = psycopg2.connect(
            dbname="cloud_courses",
            user="postgres",
            password="1111"
        )

        # Open a cursor to perform database operations
        self.cur = self.conn.cursor()
    def INSERT(self, tbl_name = '',columns= None,values = []):
        '''
        входные данные:
            название таблицы\n
            массив колонок\n
            значения колонок (кроме ID)


        '''
        if columns == None:
            columns = table_info[tbl_name]['columns']
        col = ','.join(columns[1:])
        v = ','.join(values)

        print(f'INSERT INTO {tbl_name} ({col}) values ({v});')
        # print(values)
        self.cur.execute(f'INSERT INTO {tbl_name} ({col}) values ({v});')
    def UPDATE(self,name = ''):
            pass
    def SELECT(self, tbl_name = '', isAdmin = True):
        '''
        возвращает массив строк переданной таблицы
        '''
        if not isAdmin and (tbl_name =='manager' or tbl_name == 'students' or tbl_name == 'teachers'):
             if tbl_name =='manager':
                  self.cur.execute(f"SELECT full_name as ФИО, email FROM {tbl_name} order by {table_info[tbl_name]['columns'][0]};")
             elif tbl_name =='students':
                  self.cur.execute(f"SELECT fio as ФИО, email FROM {tbl_name} order by {table_info[tbl_name]['columns'][0]};")
             elif tbl_name =='teachers':
                  self.cur.execute(f"SELECT fio as ФИО, email FROM {tbl_name} order by {table_info[tbl_name]['columns'][0]};")
         # Execute a query
        else:
            self.cur.execute(f"SELECT * FROM {tbl_name} order by {table_info[tbl_name]['columns'][0]};")

        # Retrieve query results
        records = self.cur.fetchall()
        return records
    def DELETE(self, tbl_name = '', index = -1):
        self.cur.execute( f"DELETE from {tbl_name} where {table_info[tbl_name]['columns'][0]}={index};")
    def exit(self):
            self.conn.commit()
            if self.conn is not None:
                self.conn.close()
    
if __name__ == '__main__':
        test = Server()
        print(test.SELECT('courses'))
        test.INSERT('courses',None,("'Perfect English 2'",'1000','54','5','3'))

        print(test.SELECT('courses'))
        # test.DELETE('courses',str(44))
        print(test.SELECT('courses')) 
        test.exit()