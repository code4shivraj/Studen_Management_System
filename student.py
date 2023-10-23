from tkinter import *
from tkinter import ttk
from pymysql import *
import pymysql.cursors
from tkinter import messagebox


class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Studen Management System".center(100))
        self.root.geometry("1350x700+0+0")
 
        title = Label(self.root,text="Studen Management System",bd=10,relief="groove",font=("times new roman",30,"bold"),bg="royalblue4",fg="white")
        title.pack(side=TOP,fill=X)

        #========all variable =============

        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        #==========Manage frame=============

        Manage_Frame = Frame(self.root,bd=5,relief="ridge",bg="slategray3")
        Manage_Frame.place(x=5,y=75,width=450,height=580)

        m_title = Label(Manage_Frame,text="Manage Students",bg="slategray3",font=("times in roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=10)

        lbl_roll=Label(Manage_Frame,text="Roll Number*",bg="slategray3",font=("times in roman",15,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky=W)

        txt_roll = Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times in roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky=W)

        lbl_name=Label(Manage_Frame,text="Name*",bg="slategray3",font=("times in roman",15,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky=W)

        txt_name = Entry(Manage_Frame,textvariable=self.name_var,width=20,font=("times in roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky=W)

        lbl_Email=Label(Manage_Frame,text="Email ID",bg="slategray3",font=("times in roman",15,"bold"))
        lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky=W)

        txt_Email = Entry(Manage_Frame,textvariable=self.email_var,font=("times in roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky=W)

        lbl_Gender=Label(Manage_Frame,text="Gender*",bg="slategray3",font=("times in roman",15,"bold"))
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky=W)

        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.gender_var,width=19,font=("times in roman",15),state='readonly')
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky=W)

        lbl_contact=Label(Manage_Frame,text="Contact",bg="slategray3",font=("times in roman",15,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky=W)

        txt_contact = Entry(Manage_Frame,textvariable=self.contact_var,font=("times in roman",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky=W)

        lbl_dob=Label(Manage_Frame,text="D.O.B*",bg="slategray3",font=("times in roman",15,"bold"))
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky=W)

        txt_dob = Entry(Manage_Frame,textvariable=self.dob_var,font=("times in roman",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky=W)

        lbl_address=Label(Manage_Frame,text="Address",bg="slategray3",font=("times in roman",15,"bold"))
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky=W)

        self.txt_address=Text(Manage_Frame,width=31,height=3,font=("",10),bd=5,relief=GROOVE)
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky=W)

        #============button==========#
        btn_frame = Frame(Manage_Frame,bd=4,relief=RIDGE,bg="slategray3")
        btn_frame.place(x=10,y=495,width=410)

        add_btn = Button(btn_frame,text="ADD",width=10,bg='green',command=self.add_studens).grid(row=0,column=0,padx=10,pady=10)
        update_btn = Button(btn_frame,text="UPDATE",width=10,command=self.update_data,bg='blue').grid(row=0,column=1,padx=10,pady=10)
        delete_btn = Button(btn_frame,text="DELETE",width=10,command=self.delete_data,bg='red').grid(row=0,column=2,padx=10,pady=10)
        clear_btn = Button(btn_frame,text="CLEAR",width=10,command=self.clear,bg='yellow').grid(row=0,column=3,padx=10,pady=10)

        #========detail frame==========
        Details_Frame = Frame(self.root,bd=5,relief="ridge",bg="slategray3")
        Details_Frame.place(x=460,y=75,width=817,height=580)

        lbl_search=Label( Details_Frame,text="Search By",bg="slategray3",font=("times in roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky=W)

        combo_search = ttk.Combobox(Details_Frame,width=10,textvariable=self.search_by,font=("times in roman",14),state='readonly')
        combo_search['values']=("Roll_No","Name","Contact")
        combo_search.grid(row=0,column=1,pady=10,padx=20,sticky=W)

        txt_serch = Entry(Details_Frame,textvariable=self.search_txt,font=("times in roman",14,"bold"),bd=5,relief=GROOVE)
        txt_serch.grid(row=0,column=2,pady=10,padx=20,sticky=W)

        serch_btn = Button(Details_Frame,text="Serch",command=self.search_data,width=9,bg='green').grid(row=0,column=3,padx=10,pady=10)
        showall_btn = Button(Details_Frame,text="Show All",command=self.fetch_data,width=9,bg='blue').grid(row=0,column=4,padx=10,pady=10)

        #==========Table frame ================

        Table_Frame = Frame(Details_Frame,bd=3,relief="ridge",bg="slategray3")
        Table_Frame.place(x=5,y=60,width=788,height=495)

        scroll_x= Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y= Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll",text="Roll_No")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("address",text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("roll",width=100)
        self.Student_table.column("name",width=200)
        self.Student_table.column("email",width=200)
        self.Student_table.column("gender",width=200)
        self.Student_table.column("contact",width=200)
        self.Student_table.column("dob",width=200)
        self.Student_table.column("address",width=200)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_studens(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.dob_var.get()=="" or self.gender_var.get()=="":
            messagebox.showerror("Error","enter all field")

        else:
            con=pymysql.connect(host='localhost',user='root',password='',database='stm')
            cur = con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                    self.name_var.get(),
                                                                    self.email_var.get(),
                                                                    self.gender_var.get(),
                                                                    self.contact_var.get(),
                                                                    self.dob_var.get(),
                                                                    self.txt_address.get('1.0',END))
                        )
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("success","entry was submitted")
    
    def fetch_data(self):
        con = pymysql.connect(host='localhost',user='root',password='',database='stm')
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if rows != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0",END)

    def get_cursor(self,ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])

    def update_data(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='stm')
        cur = con.cursor()
        cur.execute("update students set name =%s,email=%s,gender=%s, contact=%s, dob=%s,address=%s where roll_no = %s",
                                                                (self.name_var.get(),
                                                                self.email_var.get(),
                                                                self.gender_var.get(),
                                                                self.contact_var.get(),
                                                                self.dob_var.get(),
                                                                self.txt_address.get('1.0',END),
                                                                self.Roll_No_var.get())
                    )
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='stm')
        cur = con.cursor()
        cur.execute("delete from students where roll_no = %s",self.Roll_No_var.get())

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def search_data(self):
        if self.search_by.get()=='':
            messagebox.showerror("Error","Select type of serch value")

        elif self.search_txt.get()=='':
            messagebox.showerror("Error","Enter any value to search") 

        else: 
            con = pymysql.connect(host='localhost',user='root',password='',database='stm')
            cur = con.cursor()
            cur.execute("select * from students where "+ str(self.search_by.get()) +" LIKE '%" + str(self.search_txt.get())+"%'")
            rows = cur.fetchall()
            if rows != 0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert('',END,values=row)
                con.commit()
            con.close()

root = Tk()
ob = Student(root)
root.mainloop()
