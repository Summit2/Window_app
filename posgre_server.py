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
    def INSERT(self, name = ''):
            pass
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
            
            if self.conn is not None:
                self.conn.close()
                print('Database connection closed.')
if __name__ == '__main__':
        test = Server()
        print(test.SELECT('manager'))