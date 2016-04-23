import sys,pymysql
reload(sys)
sys.setdefaultencoding('utf-8')


conn = pymysql.connect(host='localhost',user='root',passwd='password_pinglian',db='pay',port=3306,charset="utf8")
cur = conn.cursor()

cur.execute("SELECT * FROM customers")
for r in cur:
    print("row_number:" , (cur.rownumber) )        
    print("id:"+str(r[0])+",first_name:"+str(r[1])+",last_name:"+str(r[2]))

cur.close()    
conn.close()


