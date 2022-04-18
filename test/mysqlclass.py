import pymysql

class conMysql():

    def connection(self):
        try:
            con=pymysql.connect('120.92.18.211','yangyue','yangyue123456',)
            cur=con.curses()
            cur.execute("SELECT VERSION()")
        except:
            pass
        finally:



if __name__ == "__main__":
    run_test.run_case()