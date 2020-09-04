from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from classes import *
class Student:
    def __init__(self,root):
        self.my_db = MyDb()
        self.update_index = ""
        self.root=root
        self.root.title('Student management form')
        self.root.geometry('1350x750+0+0')

        self.std=Students()

        self.title=Label(self.root,text='Student Management',font=('Times new roman',18,'bold'),bg='navajo white',fg='Black',bd=10,relief=GROOVE)
        self.title.pack(side=TOP,fill=X)

        ###############################


        self.ID_var=IntVar()
        self.Name_var=StringVar()
        self.Address_var=StringVar()
        self.Contact_var=IntVar()
        self.Gender_var=StringVar()
        self.DOB_var=IntVar()


        self.search_by=StringVar()
        self.search_txt=StringVar()




############frame################
        frame1=Frame(self.root,bd=4,relief=RIDGE,bg='silver')
        frame1.place(x=0,y=45,width=700,height=300)

        frame2=Frame(self.root,bd=4,relief=RIDGE,bg='navajo white')
        frame2.place(x=0,y=340,width=1350,height=400)

        frame4=Frame(self.root,bd=4,relief=RIDGE,bg='silver')
        frame4.place(x=700,y=45,width=648,height=300)


        self.title_f1=Label(frame1,text='Manage students',font=('Times new roman',18,'bold'),bg='silver',fg='white')
        self.title_f1.place(x=10,y=5)

        self.std_id=Label(frame1,text='ID',font=('Arial',17,'bold'),bg='silver')
        self.std_id.place(x=100,y=40)

        self.entry_id=Entry(frame1,textvariable=self.ID_var,bd=5,relief=GROOVE,font=('Arial',14),fg='black', bg='white')
        self.entry_id.place(x=250,y=40)

        self.std_name=Label(frame1,text='Name',font=('Arial',17,'bold'),bg='silver')
        self.std_name.place(x=100,y=80)

        self.entry_name=Entry(frame1,textvariable=self.Name_var,bd=5,relief=GROOVE,font=('Arial',14),fg='black', bg='white')
        self.entry_name.place(x=250,y=80)

        self.std_add=Label(frame1,text='Address',font=('Arial',17,'bold'),bg='silver')
        self.std_add.place(x=100,y=120)

        self.entry_add=Entry(frame1,textvariable=self.Address_var,bd=5,relief=GROOVE,font=('Arial',14),fg='black', bg='white')
        self.entry_add.place(x=250,y=120)

        self.std_con=Label(frame1,text='Contact',font=('Arial',17,'bold'),bg='silver')
        self.std_con.place(x=100,y=160)

        self.entry_con=Entry(frame1,textvariable=self.Contact_var,bd=5,relief=GROOVE,font=('Arial',14),fg='black', bg='white')
        self.entry_con.place(x=250,y=160)

        self.std_gen=Label(frame1,text='Gender',font=('Arial',17,'bold'),bg='silver')
        self.std_gen.place(x=100,y=200)
###############combobox##############

        self.combo_gender=ttk.Combobox(frame1,textvariable=self.Gender_var,font=('Arial',14,'bold'),state='readonly')
        self.combo_gender['values']=('male','female','other')
        self.combo_gender.place(x=250,y=200)
        self.combo_gender.current(0)




        self.std_dob=Label(frame1,text='DOB',font=('Arial',17,'bold'),bg='silver')
        self.std_dob.place(x=100,y=240)

        self.entry_dob=Entry(frame1,textvariable=self.DOB_var,bd=5,relief=GROOVE,font=('Arial',14),fg='black', bg='white')
        self.entry_dob.place(x=250,y=240)


##########button############
        self.btn_add=Button(frame1,text='ADD',width=8,font=('Arial',14,'bold'),bg='PINK',fg='red',command=self.add_std)
        self.btn_add.place(x=550,y=50)

        self.btn_upd=Button(frame1,text='UPDATE',width=8,font=('Arial',14,'bold'),bg='PINK',fg='red',command=self.update_std)
        self.btn_upd.place(x=550,y=100)

        self.btn_dlt=Button(frame1,text='DELETE',width=8,font=('Arial',14,'bold'),bg='PINK',fg='red',command=self.delete_data)
        self.btn_dlt.place(x=550,y=150)

        self.btn_rst=Button(frame1,text='RESET',width=8,font=('Arial',14,'bold'),bg='PINK',fg='red',command=self.reset_data)
        self.btn_rst.place(x=550,y=200)


        ######################

        self.search=Label(frame4,text='Search By',bg='silver',fg='black',font=('Arial',15,'bold'))
        self.search.place(x=50,y=10)


        self.combo_search=ttk.Combobox(frame4,textvariable=self.search_by,width=10,font=('Arial',15,'bold'),state='readonly')
        self.combo_search['values']=('ID','Name')
        self.combo_search.place(x=200,y=10)

        self.entry_search=Entry(frame4,textvariable=self.search_txt,bd=5,relief=GROOVE,font=('Arial',14),fg='black', bg='white')
        self.entry_search.place(x=350,y=10)

        self.btn_search=Button(frame4,text='Search',width=10,bd=0.5,font=('Arial',14,'bold'),bg='black',fg='white',command=self.search_item)
        self.btn_search.place(x=350,y=80)

        self.btn_show=Button(frame4,text='Show All',width=10,bd=0.5,font=('Arial',14,'bold'),bg='black',fg='white',command=self.show_all)
        self.btn_show.place(x=200,y=80)
        ####################################3


        frame3=Frame(frame2,bd=4,relief=GROOVE,bg='white')
        frame3.place(x=0,y=0,width=1350,height=350)

        self.scroll_x=Scrollbar(frame3,orient=HORIZONTAL)
        self.scroll_y=Scrollbar(frame3,orient=VERTICAL)




        self.Student_tree = ttk.Treeview(frame3, columns=('ID', 'Name', 'Address', 'Contact', 'Gender','DOB'),xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM,fill=X)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.scroll_x.config(command=self.Student_tree.xview)
        self.scroll_y.config(command=self.Student_tree.yview)


        self.Student_tree['show'] = 'headings'
        self.Student_tree.column('ID', width=160)
        self.Student_tree.column('Name', width=160)
        self.Student_tree.column('Address', width=160)
        self.Student_tree.column('Contact', width=160)
        self.Student_tree.column('Gender', width=160)
        self.Student_tree.column('DOB', width=140)
        self.Student_tree.heading('ID', text='ID')
        self.Student_tree.heading('Name', text='Name')
        self.Student_tree.heading('Address', text='Address')
        self.Student_tree.heading('Contact', text='Contact')
        self.Student_tree.heading('Gender', text='Gender')
        self.Student_tree.heading('DOB', text='DOB')
        self.Student_tree.pack(fill=BOTH,expand=1)
        self.show_info_in_tree()
        self.show_menu()




    #############variablesss####
    def add_std(self):
        id = self.ID_var.get()
        name = self.Name_var.get()
        address = self.Address_var.get()
        contact = self.Contact_var.get()
        gender = self.Gender_var.get()
        dob = self.DOB_var.get()
        try:
            if id=='' or name=='' or address=='' or contact=='' or gender=='' or dob=='':
                messagebox.showerror('Error','Please fill all fields')

            # elif int(id.get()):
            #     messagebox.showerror('Error','please enter number')

            else:
                 self.std.add_stds(id, name, address,contact,gender,dob)
                 messagebox.showinfo("student", "student Added")
                 self.show_info_in_tree()
                 self.reset_data()
        except Exception as e:
            print(e)



    def show_info_in_tree(self):
        all_items = self.std.show_info()
        self.Student_tree.delete(*self.Student_tree.get_children())
        for i in all_items:
            self.Student_tree.insert("", "end", text="a", values=i)
        self.Student_tree.bind("<Double-1>",self.select_details)


    def update_std(self):
        id = self.ID_var.get()
        name = self.Name_var.get()
        address = self.Address_var.get()
        contact = self.Contact_var.get()
        gender = self.Gender_var.get()
        dob = self.DOB_var.get()
        if self.std.update_details( name, address,contact,gender,dob,id):
            messagebox.showinfo("std", "Student details Updated")
            self.show_info_in_tree()
        else:
            messagebox.showerror("Error", "Student details can not be Updated")


    def select_details(self, event):
        sel_item = self.Student_tree.selection()[0]
        ind = self.Student_tree.index(sel_item)

        self.update_index = ind
        all_items = self.std.show_info()
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


        self.entry_dob.delete(0, 'end')
        self.entry_dob.insert(0, selected_data[5])


    def show_menu(self):
        my_menu = Menu(self.root)
        self.root.config(menu=my_menu)
        order_menu = Menu(my_menu)
        edit_menu = Menu(my_menu)
        view_menu = Menu(my_menu)
        help_menu = Menu(my_menu)
        my_menu.add_cascade(label="Account", menu=order_menu)
        my_menu.add_cascade(label="Setting", menu=edit_menu)
        my_menu.add_cascade(label="view", menu=view_menu)
        my_menu.add_cascade(label="Help", menu=help_menu)
        order_menu.add_command(label="make bill", )
        order_menu.add_command(label="Show")
        order_menu.add_separator()
        order_menu.add_command(label="Exit", command=self.root.quit)

    def reset_data(self):
        self.ID_var.set('')
        self.Name_var.set('')
        self.Address_var.set('')
        self.Contact_var.set('')
        self.Gender_var.set('')
        self.DOB_var.set('')

    def delete_data(self):
        id = self.ID_var.get()
        name = self.Name_var.get()
        address = self.Address_var.get()
        contact = self.Contact_var.get()

        gender = self.Gender_var.get()
        dob = self.DOB_var.get()

        if id == "":
            messagebox.showerror("Error", "Select Item first")
        elif not  id == '' or name == '' or address == '' or contact == '' or gender == ''or dob =='':
            self.std.delete_item(id)
            self.show_info_in_tree()
            messagebox.showinfo("Success", "Delete success")

    def search_item(self):

        searchopt =self.entry_search.get()
        searchval=self.combo_search.get()

        all_items = self.std.search_items_by_name(searchopt,searchval)
        self.Student_tree.delete(*self.Student_tree.get_children())
        print(searchval)
        print(searchopt)
        for i in all_items:
            self.Student_tree.insert("", "end", text=i[0], value=(i))



    def show_all(self):
        self.show_info_in_tree()



root = Tk()
Student(root)
root.mainloop()








































































