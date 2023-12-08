"""
1.数据库链接  conn cur
2.获取一条数据
3.获取条数
4.获取所有数据
5.关闭游标和数据库链接


"""
import pymysql.cursors
from Common.handle_config import conf


class HanDle_db:

    def __init__(self):
        self.conn = pymysql.connect(
            host=conf.get("mysql", "host"),
            port=conf.getint("mysql", "port"),
            user=conf.get("mysql", "user"),
            password=conf.get("mysql", "password"),
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor


        )
        self.cur = self.conn.cursor()

    def select_one_data(self, sql):
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def select_all_data(self, sql):
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def get_cont(self, sql):
        self.conn.commit()
        return self.cur.execute(sql)

    def update(self, sql):
        self.cur.execute(sql)
        self.conn.commit()

    def select_close(self):
        self.cur.close()
        self.conn.close()


select_db = HanDle_db()
# if __name__ == '__main__':
#
#     select_db = HanDle_db()
#     ss = select_db.select_one_data("SELECT * FROM `cmt-user-center`.ids_user WHERE mobile = \"18527409564\"")
#     print(ss)
#     select_db.select_close()