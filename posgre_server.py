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
    def SELECT(self, tbl_name = ''):
        '''
        возвращает массив строк переданной таблицы
        '''
         # Execute a query
        self.cur.execute(f"SELECT * FROM {tbl_name};")

        # Retrieve query results
        records = self.cur.fetchall()
        return records
    def exit(self):
            self.conn.commit()
            if self.conn is not None:
                self.conn.close()
                
if __name__ == '__main__':
        test = Server()
        print(test.SELECT('courses'))
        test.INSERT('courses',('course_ngame','price','duration','id_area','id_teacher'),("'Perfect English'",'10000','54','1','1'))
        print(test.SELECT('courses'))
        test.exit()