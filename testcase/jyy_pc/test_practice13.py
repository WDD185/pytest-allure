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
        # f.execute(r"insert into user_info(name, age, phone_number)  values ('刘欢', 17, 13878767654)")
        f.execute(r"select user_info.name from user_info inner join  user_order "
                  r"on user_info.order_id = user_order.order_id where user_order.order_createtime"
                  r" between '2021-08-01'and '2021-09-01'")
        find_all = f.fetchall()
        lst = []
        for x in find_all:
            lst.append(x)
        print(lst)


if __name__ == '__main__':
    main()
