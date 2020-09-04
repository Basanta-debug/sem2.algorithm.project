
from Student_info import *
from staff_info import *
from fee_fontend import *

class Dashboard:
    def __init__(self,root):
        self.root=root
        self.root.title('dashboard')
        self.root.geometry('1000x650+200+0')



        self.bg_icon=PhotoImage(file="C:\\Users\\User\\Desktop\\back.png")

        self.bg_lbl=Label(self.root,image=self.bg_icon)
        self.bg_lbl.pack()

        self.title=Label(self.root,text='Dash Board',font=('Arial',40,'bold'),bg='navajo white',fg='red',bd=8,relief=GROOVE)
        self.title.place(x=0,y=0,relwidth=1)

        self.title_Frame = LabelFrame(root, font = ('arial',50,'bold'), width = 500, height = 100, bg = 'navajo white', relief = 'raise', bd = 13)
        self.title_Frame.place(x=200,y=125)

        self.frame1 = LabelFrame(root, font = ('arial',50,'bold'), width = 500, height = 100, bg = 'navajo white', relief = 'raise', bd = 13)
        self.frame1.place(x=200,y=250)

        self.frame2 = LabelFrame(root, font = ('arial',50,'bold'), width = 500, height = 100, bg = 'navajo white', relief = 'raise', bd = 13)
        self.frame2.place(x=200,y=375)





        self.Label_1 = Label(self.title_Frame, text = 'STUDENT PROFILE', font = ('arial',25,'bold'),bg='navajo white')
        self.Label_1.place(x=20,y=20)
        self.Label_2 = Label(self.frame1, text = 'FEE REPORT', font = ('arial',25,'bold'), bg='navajo white')
        self.Label_2.place(x=20,y=20)
        self.Label_3 = Label(self.frame2, text = 'STAFF DETAILS', font = ('arial',25,'bold'),bg='navajo white')
        self.Label_3.place(x=20,y=20)






        self.btn_add=Button(self.title_Frame,text='View',width=7,font=('Arial',18,'bold'),bg='silver',fg='white',command=self.stdent)
        self.btn_add.place(x=350,y=15)

        self.btn_upd=Button(self.frame2,text='View',width=7,font=('Arial',18,'bold'),bg='silver',fg='white',command=self.staff)
        self.btn_upd.place(x=350,y=15)

        self.btn_upd=Button(self.frame1,text='View',width=7,font=('Arial',18,'bold'),bg='silver',fg='white',command=self.fees)
        self.btn_upd.place(x=350,y=15)




    def stdent(self):
       self.window = Toplevel(self.root)
       Student(self.window)

    def staff(self):
       self.window = Toplevel(self.root)
       Staff(self.window)

    def fees(self):
        self.window = Toplevel(self.root)
        Fee(self.window)










