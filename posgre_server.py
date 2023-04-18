import psycopg2
class Server:
    def __init__(self) -> None:
        
        """ Connect to the PostgreSQL database server """
        self.conn = None
        try:
            

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect("database=cloud_courses user=postgres password=1111")
            
            # create a cursor
            self.cur = self.conn.cursor()
            
        # execute a statement
            
            # l = self.cur.execute('SELECT * from progress')
            # print(l)
            # display the PostgreSQL database server version
            # db_version = cur.fetchone()
            # print(db_version)
        
        # close the communication with the PostgreSQL
            # self.cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        

    def INSERT(self, name = ''):
        pass
    def UPDATE(self,name = ''):
        pass
    def SELECT(self, name = ''):
        return self.cur.execute(f'SELECT * from {name};')
    def exit(self):
        
        if self.conn is not None:
            self.conn.close()
            print('Database connection closed.')
if __name__ == '__main__':
    test = Server()
    print(test.SELECT('students'))