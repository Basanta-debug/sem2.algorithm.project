from connection import *
class Students:

    def __init__(self):
        self.my_db = MyDb()


    def add_stds(self, id,name,address,contact,gender,dob):
        try:
            qry = "insert into stdinfo (ID,Name,Address,Contact,Gender,DOB) VALUES (%s, %s, %s,%s, %s, %s)"
            values = (id,name,address,contact,gender,dob)
            self.my_db.iud(qry, values)
            return True
        except Exception as e:
            print(e)
            return False

    def show_info(self):

        try:
            qry = "SELECT * FROM stdinfo"
            all_items = self.my_db.get_data(qry)
            return all_items
        except Exception as e:
            print(e)

    def search_items_by_name(self, searchopt,searchval):

        try:
            qry = "SELECT * FROM stdinfo WHERE "+" "+searchval+" "+" LIKE '"+searchopt+"'"
            all_items = self.my_db.get_data(qry)
            print(all_items)
            return all_items
        except Exception as e:
            print(e)


    def update_details(self,  name, address,contact,gender,dob,id):
        try:
            qry = "UPDATE stdinfo SET Name = %s, Address = %s, Contact = %s, Gender = %s, DOB = %s WHERE ID = %s"
            values = ( name, address, contact,gender,dob,id)
            self.my_db.iud(qry, values)
            return True
        except Exception as e:
            print(e)

    def delete_item(self, index):
        try:
            qry = "DELETE FROM stdinfo WHERE ID = %s"
            values = (index,)
            self.my_db.iud(qry, values)
            return True
        except Exception as e:
            print(e)
            return False





class Staffs:
    def __init__(self):
        self.db = MyDb()

    def add_staff(self,id,name,address,contact,gender,salary):
        try:
            qry = "insert into staffinfo (Staff_ID,Name,Address,Contact,Gender,salary) VALUES (%s, %s, %s,%s, %s, %s)"
            values = (id,name,address,contact,gender,salary)
            self.db.iud(qry, values)
            return True
        except Exception as e:
            print(e)

    def show_staff(self):
        try:
            qry = "SELECT * FROM staffinfo"
            all_items = self.db.get_data(qry)
            return all_items
        except Exception as e:
            print(e)


    def stf_update_details(self, name, address,contact,gender,dob,id):
        try:
            qry = "UPDATE staffinfo SET  Name = %s, Address = %s, Contact = %s, Gender = %s, salary = %s WHERE Staff_ID = %s"
            values = ( name, address, contact,gender,dob,id)
            self.db.iud(qry, values)
            return True
        except Exception as e:
            print(e)



    def search_items_by_name(self, val,opt):
        try:
            qry = "SELECT * FROM staffinfo WHERE "+" "+opt+" "+" LIKE '"+val+"'"
            all_items = self.db.get_data(qry)
            print(all_items)
            return all_items
        except Exception as e:
            print(e)


    def delete_item(self, index):
        try:
            qry = "DELETE FROM staffinfo WHERE Staff_ID = %s"
            values = (index,)
            self.db.iud(qry, values)
            return True
        except Exception as e:
            print(e)
            return False

class std_fee:

    def __init__(self):
        self.my_db = MyDb()

    def insert(self, recpt,name,admsn,date,branch,sem,total,paid,due):
        try:
            qry = "insert into fee (Recipt,Name,Admission_no,Date,Branch,Semester,Total,Paid,Due) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s)"
            values = (recpt,name,admsn,date,branch,sem,total,paid,due)
            self.my_db.iud(qry, values)
            return True

        except Exception as e:
            print(e)

    def View(self):
        try:
            qry = "SELECT * FROM fee"
            all_items = self.my_db.get_data(qry)
            return all_items
        except Exception as e:
            print(e)




    def update_details(self,name,admsn,date,branch,sem,total,paid,due,recpt ):
        try:
            qry = "UPDATE fee SET Name = %s, Admission_no = %s, Date = %s, Branch = %s, Semester = %s,Total = %s, Paid = %s, Due = %s WHERE Recipt = %s"
            values = (name,admsn,date,branch,sem,total,paid,due,recpt)
            self.my_db.iud(qry, values)
            return True
        except Exception as e:
            print(e)

    def delete(self, index):
        try:
            qry = "DELETE FROM fee WHERE Recipt = %s"
            values = (index,)
            self.my_db.iud(qry, values)
            return True
        except Exception as e:
            print(e)
            return False























