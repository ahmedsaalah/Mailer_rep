import pymysql.cursors


class usermodel ():
    conn = None 
    cur = None 
    def __init__(self):

        if self.cur and self.con:
            self.cur.close() 
            self.conn.close() 
        self.conn= pymysql.connect(host='localhost',  user='root', password='', db='mailer')
        self.cur = self.conn.cursor()

    def getifExist(self,email,pw):
        
        sql = "SELECT * FROM `users` WHERE `email`=%s And `password`=%s "
        self.cur.execute(sql,  (email,pw))
        result = self.cur.fetchone()
        return result
