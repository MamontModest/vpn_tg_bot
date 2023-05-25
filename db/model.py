import psycopg2



class DB:
    def __init__(self, db_name:str, host:str, port:int, user:str, password:str):
        self.db_name = db_name
        self.port = port
        self.user = host
        self.user = user
        self.conn = psycopg2.connect(dbname=db_name, user=user, password=password, host=host, port=port)

    def create_databases(self):
        cur = self.conn.cursor()
        query = '''CREATE TABLE IF NOT EXISTS USERS 
                (uid bigint primary key, vpn_key_id integer,vpn_key varchar(70), datetime timestamp);
                
                CREATE TABLE IF NOT EXISTS PAYMENTS
                (uid bigint, payment_id varchar(100), payment_date timestamp, price float, system_of_payment  varchar(20));
                
                CREATE TABLE IF NOT EXISTS SERVERS
                (id serial primary key, host  varchar(14), password varchar(30), port integer, username varchar(20));

        '''
        cur.execute(query)
        cur.close()
        self.conn.commit()

    def create_user(self, uid:int):
        cur = self.conn.cursor()
        query = '''INSERT INTO USERS (uid)VALUES ($1)'''
        cur.execute(query, [uid])
        cur.close()
    def select_all_user(self)->set:
        cur = self.conn.cursor()
        query = '''SELECT uid FROM USERS where 1=1'''
        cur.execute(query)
        cash_users = set()
        for i in cur.fetchall():
            cash_users.add(i[0])
        cur.close()
        return cash_users

    def add_server(self, host, password, port, username):
        cur = self.conn.cursor()
        query = '''INSERT INTO SERVERS (host, password, port, username) values (%s, %s, %s, %s)'''
        cur.execute(query, [host, password, int(port), username])
        cur.close()
        self.conn.commit()
        return

