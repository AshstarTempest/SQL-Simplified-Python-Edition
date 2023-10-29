import mysql.connector as m 
def conn():
    conn = m.connect(host="localhost",user="root",password="12345678",database="school")
    cur = conn.cursor()
    cur.execute("")

