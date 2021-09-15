import pymysql


class OpMysql:
    def __init__(self, host, port, user, password, database, charset='utf8'):
        self.conn = pymysql.connect(
            host=host,
            user=user,
            port=port,
            password=password,
            database=database,
            charset=charset
        )
        self.cs = self.conn.cursor(pymysql.cursors.DictCursor)

    def __enter__(self):
        return self.cs

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cs.close()
        self.conn.close()


def main():
    with OpMysql('172.10.70.171', 3307, 'root', '123456', 'server-user') as f:
        f.execute('SELECT * FROM user_info')
        find_all = f.fetchall()
        for x in find_all:
            print(x)


if __name__ == '__main__':
    main()
