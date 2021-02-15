import mysql.connector as mysql

try:
    con = mysql.connect(user="root", password="root",
                        host="127.0.0.1", database="world")
    print("Connected: ", con.is_connected())
    c = con.cursor()
    c.execute("select * from country")
    print(c.fetchall())
except Exception as ex:
    print(ex)

finally:
    if con.is_connected():
        con.close()
    print("connection closed")
print("end")