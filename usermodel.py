import pymysql.cursors


class usermodel ():
    conn = None 
    cur = None 
    def __init__(self):

        if self.cur and self.con:
            self.cur.close() 
            self.conn.close() 
        self.conn= pymysql.connect(host='localhost',  user='root', password='root', db='zakaria1')
        self.cur = self.conn.cursor()

    def getifExist(self,email,pw):
        
        sql = "SELECT * FROM `movies_links` "
        self.cur.execute(sql)
        result = self.cur.fetchall()
        for x in range(0, len(result)):
            for y in range(x+1 ,len(result)):
                if result[x].player == result[y].player and result[x].link == result[y].link and result[x].movie == result[y].movie :
                            self.cur.execute("DELETE FROM `movies_links` WHERE `id` = %s", (result[y].id))
                            self.conn.commit() 

        return result


    def removeDuplicateMovies():
        sql = "SELECT * FROM `users` WHERE `email`=%s And `password`=%s "
        self.cur.execute(sql,  (email,pw))
        result = self.cur.fetchone()






    def removeDuplicateSeries():
        return "Eede"



