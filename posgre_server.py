# import psycopg2

        
#         """ Connect to the PostgreSQL database server """
#         self.conn = psycopg2.connect("dbname=cloud_courses user=postgres password=1111")
#         self.cur = self.conn.cursor()
#         self.cur = self.conn.cursor()
#         # try:
            

#         #     # connect to the PostgreSQL server
#         #     print('Connecting to the PostgreSQL database...')
#         #     self.conn = psycopg2.connect("database=cloud_courses user=postgres password=1111")
            
#         #     # create a cursor
        
            
#         # # execute a statement
            
#         #     # l = self.cur.execute('SELECT * from progress')
#         #     # print(l)
#         #     # display the PostgreSQL database server version
#         #     # db_version = cur.fetchone()
#         #     # print(db_version)
        
#         # # close the communication with the PostgreSQL
#         #     # self.cur.close()
#         # except (Exception, psycopg2.DatabaseError) as error:
#         #     print(error)
        

#     
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
    def SELECT(self, name = ''):
         # Execute a query
        self.cur.execute(f"SELECT * FROM {name}")

        # Retrieve query results
        records = self.cur.fetchall()
        return records
    def exit(self):
            
            if self.conn is not None:
                self.conn.close()
                print('Database connection closed.')
if __name__ == '__main__':
        test = Server()
        print(test.SELECT('students'))