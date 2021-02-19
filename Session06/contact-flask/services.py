import mysql.connector as mysql

class DatabaseService:
    def __init__(self):
        try:
            con = mysql.connect(user="root", password="root",
                                host="127.0.0.1", database="contactdb")
            cursor = con.cursor()
            self.cursor = cursor
            self.con = con
        except Exception as ex:
            print(ex)

    def get_all_contacts(self):
        query = "SELECT * FROM CONTACT"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def add_contact(self, name,mobile_no):
        query = """INSERT INTO CONTACT(CNAME, MOBILE_NO) VALUES(\"{0}\",\"{1}\")""".format(name, mobile_no)
        print(query)
        if(self.checkInjection(name) and self.checkInjection(mobile_no)):
            self.cursor.execute(query)
            self.con.commit()
            return
        else:
            return -1

    def remove_contact(self, name):
        query = "DELETE FROM CONTACT WHERE CONTACT.CNAME=\"" + name +"\""
        if(self.checkInjection(name)):
            self.cursor.execute(query)
            self.con.commit()
            return
        else:
            return -1
    
    def modify_contact(self, name, data):
        contact_params = ""
        for i,(j,k) in enumerate(data.items()):
            contact_params += j + "=\"" + str(k) + "\","
            if(not self.checkInjection(j) or not self.checkInjection(k)):
                return -1
        contact_params = contact_params[:-1]
        query = "UPDATE CONTACT SET " + contact_params +" WHERE CNAME=\"" + name + "\""
        self.cursor.execute(query)
        self.con.commit()
        return
    
    def checkInjection(self,inp):
        if "\"" in inp or "\'" in inp:
            return False
        else:
            return True