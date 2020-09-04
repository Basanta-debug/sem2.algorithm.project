from tkinter import *
from tkinter import messagebox
from connection import *
from tkinter import ttk
class User_form:
    def __init__(self):
        self.my_db = MyDb()
        self.gui()

    def gui(self):
        self.wn =Tk()
        self.wn.title('Register User')
        self.wn.geometry('1000x650+200+0')


        title=Label(self.wn,text='Register User',font=('Arial',40,'bold'),bg='salmon',fg='Black',bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)
        # =========label and entry for user name and password
        self.lb_name = Label(self.wn, text="Name:", font=('arial', 20, 'bold'), fg='blue')
        self.lb_name.place(x=30, y=100)

        self.enter_name = Entry(self.wn,width=15, font=('arial', 20, 'bold'), fg='black')
        self.enter_name.place(x=180, y=100)

        self.lb_pass = Label(self.wn, text="Password:", font=('arial', 20, 'bold'), fg='blue')
        self.lb_pass.place(x=30, y=175)

        self.enter_pass = Entry(self.wn,width=15, font=('arial', 20, 'bold'), fg='black', show='*')
        self.enter_pass.place(x=180, y=175)

        self.lb_contact = Label(self.wn, text="Contact:", font=('arial', 20, 'bold'), fg='blue')
        self.lb_contact.place(x=30, y=250)

        self.enter_contact = Entry(self.wn,width=15, font=('arial', 20, 'bold'))
        self.enter_contact.place(x=180, y=250)

        # =========label and entry for address and age
        self.lb_add = Label(self.wn, text="Email", font=('arial', 20, 'bold'), fg='blue')
        self.lb_add.place(x=450, y=100)

        self.enter_add = Entry(self.wn, font=('arial', 20, 'bold'))
        self.enter_add.place(x=600, y=100)

        self.lb_age = Label(self.wn, text="Age:", font=('arial', 20, 'bold'), fg='blue')
        self.lb_age.place(x=450, y=175)

        self.enter_age = Entry(self.wn, font=('arial', 20, 'bold'))
        self.enter_age.place(x=600, y=175)

        self.lb_address = Label(self.wn, text="Address:", font=('arial', 20, 'bold'), fg='blue')
        self.lb_address.place(x=450, y=250)

        self.enter_address = Entry(self.wn, font=('arial', 20, 'bold'))
        self.enter_address.place(x=600, y=250)

        ###################################
        self.lb_sec_que = Label(self.wn, text="Security Question:", font=('arial', 20, 'bold'), fg='blue')
        self.lb_sec_que.place(x=30, y=325)


        self.combo_question=ttk.Combobox(self.wn,width=13,font=('Arial',15,'bold'),state='readonly')
        self.combo_question['values']=('Your birth place','Your father name','Your Favourite sports')
        self.combo_question.place(x=300,y=325)



        self.lb_ans = Label(self.wn, text="Answer:", font=('arial', 20, 'bold'), fg='blue')
        self.lb_ans.place(x=500, y=325)

        self.enter_ans = Entry(self.wn,width=17, font=('arial', 20, 'bold'))
        self.enter_ans.place(x=650, y=325)



#########################################################
        self.btn_submit = Button(self.wn, text='Submit', fg='black', font=('arial', 15, 'bold'),
                                 command=self.register)
        self.btn_submit.place(x=350, y=400)

        self.btn_reset = Button(self.wn, text='Reset', fg='black', font=('arial', 15, 'bold'),
                                command=self.btn_reset_user)
        self.btn_reset.place(x=200, y=400)
        self.wn.mainloop()

    def btn_reset_user(self):
        self.enter_name.delete(0, END)
        self.enter_pass.delete(0, END)
        self.enter_contact.delete(0, END)
        self.enter_add.delete(0, END)
        self.enter_age.delete(0, END)

    def register(self):

            username = self.enter_name.get()
            password = self.enter_pass.get()
            contact = self.enter_contact.get()
            address = self.enter_add.get()
            question = self.combo_question.get()
            answer = self.enter_ans.get()
            age = self.enter_age.get()
            if username == " " or password == '' or question == ''or answer == ''or contact == '' or address == ''or age == '':
                messagebox.showwarning("Error", "Enter data in everyboxes carefully ")

            elif type(contact)==str:
                messagebox.showerror('ERROR','plesase enter valid number')

            else:
                qry="SELECT username from registration order by username"
                list=self.my_db.get_data(qry)
                rex=self.binary_search_iterative(list,username)
                print(rex)


                if rex!=-1:
                    messagebox.showerror('Try again','username already existed')

            #
                else:
                    qry = """INSERT INTO registration (username, password,security_question,answwer)
                                    VALUES (%s,%s,%s,%s)"""
                    values = (username, password,question,answer)
                    self.my_db.iud(qry, values)
                    messagebox.showinfo("Success", "Registered Successfully ")






    def binary_search_iterative(self,list, key):
        start = 0
        end = len(list) - 1
        while start <= end:
            mid = (start + end) // 2
            if list[mid][0] == key:
                return mid
            elif list[mid][0] > key:
                end = mid - 1
            else:
                start = mid + 1
        return -1



