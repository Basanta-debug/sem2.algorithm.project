from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from connection import *
from classes import *
class Staff:
    def __init__(self, root):
        self.my_db = MyDb()
        self.update_index = ""
        self.root=root
        self.root.title('Staff Information form')
        self.root.geometry('1350x750+0+0')

        self.stf=Staffs()

        self.title=Label(self.root,text='Staff Management',font=('Times new roman',18,'bold'),bg='ORANGE',fg='BLACK',bd=10,relief=GROOVE)
        self.title.pack(side=TOP,fill=X)

        ###############################


        self.ID_var=StringVar()
        self.Name_var=StringVar()
        self.Address_var=StringVar()
        self.Contact_var=StringVar()
        self.faculty_var=StringVar()
        self.salary_var=StringVar()




############frame################

        self.frame1=Frame(self.root,bd=4,relief=RIDGE,bg='silver')
        self.frame1.place(x=0,y=45,width=700,height=360)

        self.frame2=Frame(self.root,bd=4,relief=RIDGE,bg='navajo white')
        self.frame2.place(x=0,y=400,width=1350,height=400)

        self.frame4=Frame(self.root,bd=4,relief=RIDGE,bg='silver')
        self.frame4.place(x=700,y=45,width=650,height=360)

        self.frame5=Frame(self.frame1,bd=4,relief=RIDGE,bg='silver')
        self.frame5.place(x=0,y=290,width=690,height=60)




        self.title_f1=Label(self.frame1,text='Manage Staff',font=('Times new roman',18,'bold'),bg='silver',fg='navajo white')
        self.title_f1.place(x=10,y=5)

        self.std_id=Label(self.frame1,text=' Staff ID',font=('Arial',17,'bold'),bg='silver')
        self.std_id.place(x=100,y=40)

        self.entry_id=Entry(self.frame1,textvariable=self.ID_var,bd=5,relief=GROOVE,font=('Arial',14),fg='black', bg='white')
        self.entry_id.place(x=250,y=40)

        self.stf_name=Label(self.frame1,text='Name',font=('Arial',17,'bold'),bg='silver')
        self.stf_name.place(x=100,y=80)

        self.entry_name=Entry(self.frame1,textvariable=self.Name_var,bd=5,relief=GROOVE,font=('Arial',14),fg='black', bg='white')
        self.entry_name.place(x=250,y=80)

        self.stf_add=Label(self.frame1,text='Address',font=('Arial',17,'bold'),bg='silver')
        self.stf_add.place(x=100,y=120)

        self.entry_add=Entry(self.frame1,textvariable=self.Address_var,bd=5,relief=GROOVE,font=('Arial',14),fg='black', bg='white')
        self.entry_add.place(x=250,y=120)

        self.std_con=Label(self.frame1,text='Contact',font=('Arial',17,'bold'),bg='silver')
        self.std_con.place(x=100,y=160)

        self.entry_con=Entry(self.frame1,textvariable=self.Contact_var,bd=5,relief=GROOVE,font=('Arial',14),fg='black', bg='white')
        self.entry_con.place(x=250,y=160)

        self.std_gen=Label(self.frame1,text='faculty',font=('Arial',17,'bold'),bg='silver')
        self.std_gen.place(x=100,y=200)
###############combobox##############

        self.combo_gender=ttk.Combobox(self.frame1,textvariable=self.faculty_var,font=('Arial',14,'bold'),state='readonly')
        self.combo_gender['values']=('Data','Algorithm','IOT')
        self.combo_gender.place(x=250,y=200)




        self.std_salary=Label(self.frame1,text='salary',font=('Arial',17,'bold'),bg='silver')
        self.std_salary.place(x=100,y=240)

        self.entry_salary=Entry(self.frame1,textvariable=self.salary_var,bd=5,relief=GROOVE,font=('Arial',14),fg='black', bg='white')
        self.entry_salary.place(x=250,y=240)


##########button############
        self.btn_add=Button(self.frame5,text='ADD',width=8,font=('Arial',14,'bold'),bg='navajo white',fg='red',command=self.add_staff)
        self.btn_add.place(x=20,y=5)

        self.btn_upd=Button(self.frame5,text='UPDATE',width=8,font=('Arial',14,'bold'),bg='navajo white',fg='red',command=self.update_std)
        self.btn_upd.place(x=180,y=5)

        self.btn_dlt=Button(self.frame5,text='DELETE',width=8,font=('Arial',14,'bold'),bg='navajo white',fg='red',command=self.delete_data)
        self.btn_dlt.place(x=340,y=5)

        self.btn_rst=Button(self.frame5,text='RESET',width=8,font=('Arial',14,'bold'),bg='navajo white',fg='red',command=self.reset_data)
        self.btn_rst.place(x=480,y=5)


        ######################

        self.search=Label(self.frame4,text='Search By',bg='silver',fg='navajo white',font=('Arial',15,'bold'))
        self.search.place(x=50,y=10)


        self.combo_search=ttk.Combobox(self.frame4,width=10,font=('Arial',15,'bold'),state='readonly')
        self.combo_search['values']=('Staff_ID','Name')
        self.combo_search.place(x=200,y=10)

        self.entry_search=Entry(self.frame4,bd=5,relief=GROOVE,font=('Arial',14),fg='black', bg='white')
        self.entry_search.place(x=350,y=10)

        self.btn_search=Button(self.frame4,text='Search',width=10,bd=0.5,font=('Arial',14,'bold'),bg='black',fg='white',command=self.search_staff)
        self.btn_search.place(x=350,y=80)

        self.btn_show=Button(self.frame4,text='Show All',width=10,bd=0.5,font=('Arial',14,'bold'),bg='black',fg='white',command=self.show_all)
        self.btn_show.place(x=200,y=80)
        ####################################3


        frame3=Frame(self.frame2,bd=4,relief=GROOVE,bg='blue')
        frame3.place(x=0,y=0,width=1350,height=500)

        self.scroll_x=Scrollbar(frame3,orient=HORIZONTAL)
        self.scroll_y=Scrollbar(frame3,orient=VERTICAL)




        self.Staff_tree = ttk.Treeview(frame3, columns=('ID', 'Name', 'Address', 'Contact', 'faculty','salary'),xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM,fill=X)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.scroll_x.config(command=self.Staff_tree.xview)
        self.scroll_y.config(command=self.Staff_tree.yview)


        self.Staff_tree['show'] = 'headings'
        self.Staff_tree.column('ID', width=160)
        self.Staff_tree.column('Name', width=160)
        self.Staff_tree.column('Address', width=160)
        self.Staff_tree.column('Contact', width=160)
        self.Staff_tree.column('faculty', width=160)
        self.Staff_tree.column('salary', width=140)
        self.Staff_tree.heading('ID', text='ID')
        self.Staff_tree.heading('Name', text='Name')
        self.Staff_tree.heading('Address', text='Address')
        self.Staff_tree.heading('Contact', text='Contact')
        self.Staff_tree.heading('faculty', text='faculty')
        self.Staff_tree.heading('salary', text='salary')
        self.Staff_tree.pack(fill=BOTH,expand=1)
        self.show_info_in_tree()



    #############variablesss####
    def add_staff(self):
        id = self.ID_var.get()
        name = self.Name_var.get()
        address = self.Address_var.get()
        contact = self.Contact_var.get()
        gender = self.faculty_var.get()
        salary = self.salary_var.get()
        if self.stf.add_staff(id, name, address,contact,gender,salary):
            messagebox.showinfo("staff", "staff Added")
            self.show_info_in_tree()
            self.reset_data()
        else:
            messagebox.showerror("Error")



    def show_info_in_tree(self):
        all_items = self.stf.show_staff()
        self.Staff_tree.delete(*self.Staff_tree.get_children())
        for i in all_items:
            self.Staff_tree.insert("", "end", text="a", values=i)
        self.Staff_tree.bind("<Double-1>",self.select_details)


    def update_std(self):
        id = self.ID_var.get()
        name = self.Name_var.get()
        address = self.Address_var.get()
        contact = self.Contact_var.get()
        gender = self.faculty_var.get()
        salary = self.salary_var.get()
        if self.stf.stf_update_details(  name, address,contact,gender,salary,id):
            messagebox.showinfo("stf", "Staff details Updated")
            self.show_info_in_tree()
        else:
            messagebox.showerror("Error", "Staff details can not be Updated")


    def select_details(self, event):
        sel_item = self.Staff_tree.selection()[0]
        ind = self.Staff_tree.index(sel_item)

        self.update_index = ind
        all_items = self.stf.show_staff()
        selected_data = all_items[ind]
        self.entry_id.delete(0, 'end')
        self.entry_id.insert(0, selected_data[0])

        self.entry_name.delete(0, 'end')
        self.entry_name.insert(0, selected_data[1])

        self.entry_add.delete(0, 'end')
        self.entry_add.insert(0, selected_data[2])

        self.entry_con.delete(0, 'end')
        self.entry_con.insert(0, selected_data[3])

        self.combo_gender.set(value="")
        self.combo_gender.set(value=selected_data[4])

        self.entry_salary.delete(0, 'end')
        self.entry_salary.insert(0, selected_data[5])

    def reset_data(self):
        self.ID_var.set('')
        self.Name_var.set('')
        self.Address_var.set('')
        self.Contact_var.set('')
        self.faculty_var.set('')
        self.salary_var.set('')

    def delete_data(self):
        id = self.ID_var.get()
        name = self.Name_var.get()
        address = self.Address_var.get()
        contact = self.Contact_var.get()

        salary = self.salary_var.get()
        faculty = self.faculty_var.get()

        if id == "":
            messagebox.showerror("Error", "Select Item first")
        elif not  id == '' or name == '' or address == '' or contact == '' or salary == ''or faculty =='':
            self.stf.delete_item(id)
            self.show_info_in_tree()
            messagebox.showinfo("Success", "Delete success")

    def search_staff(self):

        opt =self.entry_search.get()
        val=self.combo_search.get()

        all_items = self.stf.search_items_by_name(opt,val)
        self.Staff_tree.delete(*self.Staff_tree.get_children())
        print(val)
        print(opt)
        for i in all_items:
            self.Staff_tree.insert("", "end", text=i[0], value=(i))

    def show_all(self):
        self.show_info_in_tree()

































































