import pymysql


conn = pymysql.Connect(host='localhost', port=3306, user='root', passwd='root', db='sam', charset='utf8')
cur = conn.cursor()
