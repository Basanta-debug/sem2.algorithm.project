

from classes import *
from Dash_board import *
from Registration import *
from math import *
class login_system:
    def __init__(self,root):

        self.db=MyDb()
        self.root=root
        self.root.title('login System')
        self.root.geometry('1000x650+200+0')




        #for image##########################

        self.bg_icon=PhotoImage(file="C:\\Users\\User\\Desktop\\back.png")
        self.user_icon=PhotoImage(file="C:\\Users\\User\\Desktop\\user_icon.png")
        self.psw_icon=PhotoImage(file="C:\\Users\\User\\Desktop\\password_icon.png")


        #####variables#################
        self.u_name=StringVar()
        self.p_d=StringVar()

        bg_lbl=Label(self.root,image=self.bg_icon)
        bg_lbl.pack()


        title=Label(self.root,text='login System',font=('Arial',40,'bold'),bg='yellow',fg='red',bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        frame1=Frame(self.root,bg='white')
        frame1.place(x=300,y=100)

        user_icon=Label(frame1,image=self.user_icon,bd=0)
        user_icon.grid(row=0,column=0,columnspan=2,pady=20)

        lbluser=Label(frame1,text='Username',font=('Arial',20,'bold'),bg='white')
        lbluser.grid(row=1,column=0,padx=20,pady=20)

        lblpass=Label(frame1,text='Password',font=('Arial',20,'bold'),bg='white')
        lblpass.grid(row=2,column=0,padx=20,pady=20)

        entry_user=Entry(frame1,bd=5,relief=GROOVE,textvariable=self.u_name,font=('Arial',15),fg='black', bg='salmon')
        entry_user.grid(row=1,column=1,padx=15)


        entry_pass=Entry(frame1,bd=5,relief=GROOVE,textvariable=self.p_d,font=('Arial',15),fg='black', bg='salmon',show='*')
        entry_pass.grid(row=2,column=1,padx=15)
###########################################################################################
        btn_log=Button(frame1,text='Login',width=10,font=('Arial',15,'bold'),bg='yellow',fg='red',command=self.login)
        btn_log.grid(row=3,column=1,pady=10)

        btn_fgt_psw=Button(frame1,text='Change password ?',font=('Arial',15,'bold'),bg='white',bd=0,fg='red',command=self.forget_pass_gui)
        btn_fgt_psw.grid(row=3,column=0,pady=10)

        btn_reg=Button(self.root,text='Register',width=10,font=('Arial',15,'bold'),bg='yellow',fg='red',command=self.reg)
        btn_reg.place(x=550,y=600)

        lblask=Label(self.root,text='Do not have account?',font=('Arial',20,'bold'),bg='silver')
        lblask.place(x=250,y=600)


    def reg(self):
        from Registration import User_form
        self.uf=User_form()
        self.uf.gui()




    def login(self):

        try:
            self.algo_python = MyDb()
            self.username = self.u_name.get()
            self.password = self.p_d.get()
            print(self.username)
            print(self.password)
            qry = """ SELECT * FROM registration WHERE username=%s and password=%s"""
            values = (self.username, self.password)
            user = self.algo_python.get_data_p(qry, values)
            if self.username=="" or self.password=="":
                messagebox.showerror('Error','Required all the information')

            else:
                if len(user) == 1:
                    messagebox.showinfo('Success', 'Login successful!')
                    self.call()
                else:
                    messagebox.showerror('Error','Wrong username and password')
        except Exception as e:
            print(e)


    def call(self):
        self.window = Toplevel(self.root)
        Dashboard(self.window)



    

############################################################################################################
    def forget_password(self):
        if self.combo_question.get()=='select' or self.enter_ans.get()=='' or self.enter_new_p.get()=='':
            messagebox.showerror('Error','All fields are required',parent=self.root2)
        else:
            try:
                con=mysql.connector.connect(user='root', host='localhost', password='Basanta@9865', port=3306, database='Project')
                cur=con.cursor()
                cur.execute( "SELECT * FROM registration WHERE username =%s and security_question=%s and answwer=%s",(self.username.get(),self.combo_question.get(),self.enter_ans.get()))

                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','Please select correct security question or answer',parent=self.root2)
                else:
                    cur.execute("update registration set password=%s where username =%s",(self.enter_new_p.get(),self.username.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo('Success','Password has been reset,Please login with new password',parent=self.root2)

            except Exception as es:
                messagebox.showerror('Error',f'Error due to:{str(es)}',parent=self.root2)

    def forget_pass_gui(self):
        self.username=self.u_name
        self.password=self.p_d

        if self.username.get()==''or self.password.get()=='':
            messagebox.showerror('Error','please enter username and password you want to change to')
        else:
            try:
                con=mysql.connector.connect(user='root', host='localhost', password='Basanta@9865', port=3306, database='Project')
                cur=con.cursor()
                cur.execute( "SELECT * FROM registration WHERE username =%s and password=%s",self.username.get(),self.password.get())

                row=cur.fetchone()
                if row==None:

                    con.close()
                    self.root2=Toplevel()
                    self.root2.title('password change')
                    self.root2.config(bg='white')
                    self.root2.geometry('400x400+450+150')
                    self.root2.focus_force()
                    self.root2.grab_set()


                    title=Label(self.root2,text=' Change Password',font=('times new roman',20,'bold'),bg='white',fg='red')
                    title.place(x=0,y=0,relwidth=1)

                    self.lb_sec_que = Label(self.root2, text="Security Question:", font=('arial', 20, 'bold'), fg='green',bg='white')
                    self.lb_sec_que.place(x=80,y=50)


                    self.combo_question=ttk.Combobox(self.root2,width=20,font=('Arial',15,'bold'),state='readonly')
                    self.combo_question['values']=('Your birth place','Your father name','Your Favourite sports')
                    self.combo_question.place(x=80,y=90)

                    self.lb_ans = Label(self.root2, text="Answer:", font=('arial', 20, 'bold'), fg='green',bg='white')
                    self.lb_ans.place(x=130, y=150)

                    self.enter_ans = Entry(self.root2,width=20, font=('arial', 20, 'bold'),fg='black',bg='silver')
                    self.enter_ans.place(x=60, y=200)

                    self.lb_new_p = Label(self.root2, text="New Password:", font=('arial', 20, 'bold'), fg='green',bg='white')
                    self.lb_new_p.place(x=120, y=250)

                    self.enter_new_p = Entry(self.root2,width=20, font=('arial', 20, 'bold'),fg='black',bg='silver')
                    self.enter_new_p.place(x=60, y=300)

                    self.btn_reset_psw=Button(self.root2,text='Reset',width=10,font=('Arial',15,'bold'),bg='Blue',fg='white',command=self.forget_password)
                    self.btn_reset_psw.place(x=130,y=350)
            except Exception as es:
                 messagebox.showerror('Error',f'Error due to:{str(es)}',parent=self.root)












    # def changepsw(self,username,loginpassword,newpassword):
    #     qry="update registration set password=%s where username=%s and password=%s"
    #     values=(newpassword,username,loginpassword)
    #     self.db.iud(qry,values)
    #     return True
    #
    # def updatepassword(self,username,password):
    #     qry="select username from registration where username=%s and password=%s"
    #     values=(username,password)
    #     self.db.get_data_p(qry,values)
    #     return True


    # def forget_pass(self):
    #     self.username=self.u_name
    #     if self.username.get()=="":
    #         messagebox.showerror('Error','please enter username you want to change password')
    #     else:
    #         try:
    #             self.algo_python = MyDb()
    #
    #             print(self.username)
    #
    #             qry = """ SELECT * FROM registration WHERE username=%s and password=%s"""
    #             values = (self.username)
    #             user = self.algo_python.get_data_p(qry, values)
    #
    #             if len(user) == 1:
    #                 messagebox.showinfo('Success', 'Login successful!')
    #                 self.forget_pass_gui()
    #             else:
    #                 messagebox.showerror('Error','Please enter the valid username')
    #         except Exception as es:
    #             messagebox.showerror('Error',f'Error due to:{str(es)}',parent=self.root)



root = Tk()
login_system(root)
root.mainloop()


