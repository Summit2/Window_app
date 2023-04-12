import psycopg2
class Server:
    def __init__(self) -> None:
        
        """ Connect to the PostgreSQL database server """
        conn = None
        try:
            

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect("dbname=cloud_courses user=postgres password=1111")
            
            # create a cursor
            cur = conn.cursor()
            
        # execute a statement
            
            l = cur.execute('SELECT * from progress')
            print(l)
            # display the PostgreSQL database server version
            db_version = cur.fetchone()
            print(db_version)
        
        # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')

    def INSERT(self, name = ''):
        pass
    def UPDATE(self,name = ''):
        pass
    def SELECT(self, name = ''):
        pass
if __name__ == '__main__':
    test = Server()