import pymysql

# obj=SqlHelper()
# obj.connect()
# obj.modify()
# obj.close()


class SqlHelper():
    def connect(self):
        self.conn=pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='94188', db='exercise',charset='utf8')
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def get_list(self,sql,args):
        self.cursor.execute(sql,args)
        result=self.cursor.fetchall()
        return(result)

    def get_one(self,sql,args):
        self.cursor.execute(sql,args)
        result = self.cursor.fetchone()
        return (result)

    def modify(self,sql,args):
        self.cursor.execute(sql,args)
        self.conn.commit()

    def multiple_modify(self,sql,args):
        #self.cursor.executemany('insert into ba(id,name)'value(%s,%s),[(1,'abv'),(2,'ffff')])
        self.cursor.executemany(sql,args)

    def add_create(self,sql,args):
        self.cursor.execute(sql,args)
        self.conn.commit()
        return self.cursor.lastrowid  #获取最后的一个id并且返回

    def close(self):
        self.cursor.close()
        # 关闭连接
        self.conn.close()
