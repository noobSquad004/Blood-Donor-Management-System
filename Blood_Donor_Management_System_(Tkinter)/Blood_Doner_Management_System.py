import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from PIL import  ImageTk
import pymysql

class Donor:
    def __init__(self, root):
        self.root = root
        self.root.title("Blood Donor Management System")
        self.root.geometry("1370x700+0+0")

        title = Label(self.root, text="Blood Donor Management System", font=("times new roman", 30, "bold"), bd=10, relief=GROOVE,
                      bg="white", fg="red")
        title.pack(side=TOP, fill=X)

        # Variables--------------------------------------------------------------------
        self.fname_var = StringVar()
        self.lname_var = StringVar()
        self.gender_var = StringVar()
        self.blood_group_var = StringVar()
        self.age_var = StringVar()
        self.ldd_var = StringVar()
        self.contact_var = StringVar()
        self.search_txt = StringVar()

        # Frame_________________________________________________________________________
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="red")
        Manage_Frame.place(x=30, y=70, width=450, height=530)

        m_title = Label(Manage_Frame, text="   Donor Information", bg="red", fg="white",
                        font=("times new roman", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_fname = Label(Manage_Frame, text="First Name", bg="white", fg="black", font=("times new roman", 15, "bold"))
        lbl_fname.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        txt_fname = Entry(Manage_Frame, textvariable=self.fname_var, font=("times new roman", 12, "bold"), bd=5,
                          relief=GROOVE)
        txt_fname.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_lname = Label(Manage_Frame, text="Last Name", bg="white", fg="black", font=("times new roman", 15, "bold"))
        lbl_lname.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_lname = Entry(Manage_Frame, textvariable=self.lname_var, font=("times new roman", 12, "bold"), bd=5,
                          relief=GROOVE)
        txt_lname.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender", bg="white", fg="black", font=("times new roman", 15, "bold"))
        lbl_gender.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font=("times new roman", 13, "bold"),
                                    state='readonly')
        combo_gender['values'] = ("Male", "Female")
        combo_gender.grid(row=3, column=1, pady=10, padx=20)

        lbl_blood_group = Label(Manage_Frame, text="Blood Group", bg="white", fg="black",
                                font=("times new roman", 15, "bold"))
        lbl_blood_group.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        combo_blood_group = ttk.Combobox(Manage_Frame, textvariable=self.blood_group_var,
                                         font=("times new roman", 13, "bold"), state='readonly')
        combo_blood_group['values'] = ("O+", "A+", "B+", "AB+", "O-", "A-", "B-", "AB-")
        combo_blood_group.grid(row=4, column=1, pady=10, padx=20)

        lbl_age = Label(Manage_Frame, text="Age", bg="white", fg="black", font=("times new roman", 15, "bold"))
        lbl_age.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_age = Entry(Manage_Frame, textvariable=self.age_var, font=("times new roman", 12, "bold"), bd=5,
                        relief=GROOVE)
        txt_age.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_ldd = Label(Manage_Frame, text="L.D.D:", bg="white", fg="black", font=("times new roman", 15, "bold"))
        lbl_ldd.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txt_ldd = Entry(Manage_Frame, textvariable=self.ldd_var, font=("times new roman", 12, "bold"), bd=5,
                        relief=GROOVE)
        txt_ldd.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_contact = Label(Manage_Frame, text="Contact No:", bg="white", fg="black",
                            font=("times new roman", 15, "bold"))
        lbl_contact.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        txt_contact = Entry(Manage_Frame, textvariable=self.contact_var, font=("times new roman", 12, "bold"), bd=5,
                            relief=GROOVE)
        txt_contact.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        lbl_address = Label(Manage_Frame, text="Address", bg="white", fg="black", font=("times new roman", 15, "bold"))
        lbl_address.grid(row=8, column=0, pady=10, padx=20, sticky="w")
        self.txt_address = Text(Manage_Frame, width=30, height=4, font=("", 10))
        self.txt_address.grid(row=8, column=1, pady=10, padx=20, sticky="w")

        ##Create a new frame ...........................................................
        Manage_Frame_1 = Frame(self.root, bd=4, relief=RIDGE, bg="red")
        Manage_Frame_1.place(x=3, y=610, width=1350, height=80)

        btn_frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        btn_frame.place(x=460, y=625, width=430)

        Addbtn = Button(btn_frame, text="Add", width=15, bg="red", fg="white", relief=GROOVE,
                        font=("times of roman", 9, "bold"), command=self.add).grid(row=0, column=1, padx=10, pady=10)
        Updatebtn = Button(btn_frame, text="Update", width=15, bg="red", fg="white", relief=GROOVE,
                           font=("times of roman", 9, "bold"), command=self.update_data).grid(row=0, column=2, padx=10,
                                                                                              pady=10)

        clearbtn = Button(btn_frame, text="Clear", width=15, bg="red", fg="white", relief=GROOVE,
                          font=("times of roman", 9, "bold"), command=self.clear).grid(row=0, column=3, padx=10,
                                                                                       pady=10)





        ##Create a new frame ...........................................................
        details_frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        details_frame.place(x=500, y=70, width=800, height=530)

        lbl_search = Label(details_frame, text="Search By Blood Group", bg="red", fg="white",
                           font=("times new roman", 15, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        lbl_search = Label(details_frame, text="Enter:", bg="red", fg="white", font=("times new roman", 15, "bold"))
        lbl_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        txt_search = Entry(details_frame, textvariable=self.search_txt, font=("times new roman", 15, "bold"), bd=5,
                           relief=GROOVE, bg="white")
        txt_search.grid(row=0, column=3, pady=10, padx=20, sticky="w")
        Searchbtn = Button(details_frame, text="Search", width=10, bg="red", fg="white", relief=GROOVE,
                           font=("times of roman", 9, "bold"), command=self.search_data).grid(row=0, column=4, padx=10,
                                                                                              pady=10)


        # Create Table frame.................................................................

        table_frame = Frame(details_frame, bd=4, relief=RIDGE, bg="red")
        table_frame.place(x=10, y=70, width=760, height=400)


        ###Creating Scrollbar..................................................................
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.information = ttk.Treeview(table_frame, column=(
        "First Name", "Last Name", "Gender","Blood Group", "Age", "L.D.D", "Contact No", "Address"),
                                          xscrollcommand=scroll_y, yscrollcommand=scroll_x)
        scroll_x.pack(side="bottom", fill="x")
        scroll_y.pack(side="right", fill="y")

        scroll_x.config(command=self.information.xview())
        scroll_y.config(command=self.information.yview())

        self.information.heading("First Name", text="First Name")
        self.information.heading("Last Name", text="last Name")
        self.information.heading("Blood Group", text="Blood Group")
        self.information.heading("Gender", text="Gender")
        self.information.heading("Age", text="Age")
        self.information.heading("L.D.D", text="L.D.D")
        self.information.heading("Contact No", text="Contact No")
        self.information.heading("Address", text="Address")

        self.information['show'] = 'headings'

        self.information.column("First Name", width=80)
        self.information.column("Last Name", width=80)
        self.information.column("Blood Group", width=80)
        self.information.column("Gender", width=80)
        self.information.column("Age", width=40)
        self.information.column("L.D.D", width=80)
        self.information.column("Contact No", width=80)
        self.information.column("Address", width=80)

        self.information.pack(fill="both", expand=1)
        self.information.bind('<ButtonRelease-1>', self.get_cursor)
        self.fetch_data()

    def add(self):
        if self.fname_var.get() == "" or self.blood_group_var.get() == "" or self.contact_var.get() == "":
            messagebox.showerror("Error", "All fields are required to fill")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="blood")
            cursor = con.cursor()
            cursor.execute("insert into donor_information values(%s,%s,%s,%s,%s,%s,%s,%s)", (self.fname_var.get(),
                                                                                             self.lname_var.get(),
                                                                                             self.gender_var.get(),
                                                                                             self.blood_group_var.get(),
                                                                                             self.age_var.get(),
                                                                                             self.ldd_var.get(),
                                                                                             self.contact_var.get(),
                                                                                             self.txt_address.get('1.0',
                                                                                                                  END)))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Record has been inserted")

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="blood")
        cursor = con.cursor()
        cursor.execute('select *from donor_information')
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.information.delete(*self.information.get_children())
            for row in rows:
                self.information.insert('', END, values=row)
            con.commit()
        con.close()

    def get_cursor(self, ev):
        curosor_row = self.information.focus()
        contents = self.information.item(curosor_row)
        row = contents['values']
        self.fname_var.set(row[0])
        self.lname_var.set(row[1])
        self.gender_var.set(row[2])
        self.blood_group_var.set(row[3])
        self.age_var.set(row[4])
        self.ldd_var.set(row[5])
        self.contact_var.set(row[6])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, row[7])

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="blood")
        cursor = con.cursor()
        cursor.execute(
            "update donor_information set fname= %s,lname= %s,gender= %s,blood_group= %s,age= %s,ldd= %s,address= %s where contact= %s",
            (self.fname_var.get(),
             self.lname_var.get(),
             self.gender_var.get(),
             self.blood_group_var.get(),
             self.age_var.get(),
             self.ldd_var.get(),
             self.txt_address.get('1.0', END),
             self.contact_var.get()))

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Success", "Record has been updated")

    def clear(self):
        self.fname_var.set("")
        self.lname_var.set("")
        self.gender_var.set("")
        self.blood_group_var.set("")
        self.age_var.set("")
        self.ldd_var.set("")
        self.contact_var.set("")
        self.txt_address.delete('1.0', END)

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="blood")
        cursor = con.cursor()
        cursor.execute("select *from donor_information where blood_group LIKE '%" + str(self.search_txt.get()) + "%'")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.information.delete(*self.information.get_children())
            for row in rows:
                self.information.insert('', END, values=row)
            con.commit()
        con.close()

        messagebox.showinfo("Search", "Data was successfully found out ")


class Blood_Requester:
    def __init__(self, root):
        self.root = root
        self.root.title("Blood Donor Management System")
        self.root.geometry("1370x700+0+0")

        title = Label(self.root, text="Blood Donor Management System", font=("times new roman", 30, "bold"), bd=10, relief=GROOVE,
                      bg="white", fg="red")
        title.pack(side=TOP, fill=X)

        # Variables--------------------------------------------------------------------
        self.fname_var = StringVar()
        self.lname_var = StringVar()
        self.gender_var = StringVar()
        self.blood_group_var = StringVar()
        self.age_var = StringVar()
        #self.ldd_var = StringVar()
        self.dob_var = StringVar()
        self.contact_var = StringVar()
        self.search_txt = StringVar()

        # Frame_________________________________________________________________________
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="red")
        Manage_Frame.place(x=30, y=70, width=450, height=530)

        m_title = Label(Manage_Frame, text="   Patient's Information", bg="red", fg="white",
                        font=("times new roman", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_fname = Label(Manage_Frame, text="First Name", bg="white", fg="black", font=("times new roman", 15, "bold"))
        lbl_fname.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        txt_fname = Entry(Manage_Frame, textvariable=self.fname_var, font=("times new roman", 12, "bold"), bd=5,
                          relief=GROOVE)
        txt_fname.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_lname = Label(Manage_Frame, text="Last Name", bg="white", fg="black", font=("times new roman", 15, "bold"))
        lbl_lname.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_lname = Entry(Manage_Frame, textvariable=self.lname_var, font=("times new roman", 12, "bold"), bd=5,
                          relief=GROOVE)
        txt_lname.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender", bg="white", fg="black", font=("times new roman", 15, "bold"))
        lbl_gender.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font=("times new roman", 13, "bold"),
                                    state='readonly')
        combo_gender['values'] = ("Male", "Female")
        combo_gender.grid(row=3, column=1, pady=10, padx=20)

        lbl_blood_group = Label(Manage_Frame, text="Blood Group", bg="white", fg="black",
                                font=("times new roman", 15, "bold"))
        lbl_blood_group.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        combo_blood_group = ttk.Combobox(Manage_Frame, textvariable=self.blood_group_var,
                                         font=("times new roman", 13, "bold"), state='readonly')
        combo_blood_group['values'] = ("O+", "A+", "B+", "AB+", "O-", "A-", "B-", "AB-")
        combo_blood_group.grid(row=4, column=1, pady=10, padx=20)

        lbl_age = Label(Manage_Frame, text="Age", bg="white", fg="black", font=("times new roman", 15, "bold"))
        lbl_age.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_age = Entry(Manage_Frame, textvariable=self.age_var, font=("times new roman", 12, "bold"), bd=5,
                        relief=GROOVE)
        txt_age.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_dob = Label(Manage_Frame, text="Blood Needed Date:", bg="white", fg="black", font=("times new roman", 15, "bold"))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txt_dob = Entry(Manage_Frame, textvariable=self.dob_var, font=("times new roman", 12, "bold"), bd=5,
                        relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_contact = Label(Manage_Frame, text="Contact No:", bg="white", fg="black",
                            font=("times new roman", 15, "bold"))
        lbl_contact.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        txt_contact = Entry(Manage_Frame, textvariable=self.contact_var, font=("times new roman", 12, "bold"), bd=5,
                            relief=GROOVE)
        txt_contact.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        lbl_address = Label(Manage_Frame, text="Hospital", bg="white", fg="black", font=("times new roman", 15, "bold"))
        lbl_address.grid(row=8, column=0, pady=10, padx=20, sticky="w")
        self.txt_address = Text(Manage_Frame, width=30, height=4, font=("", 10))
        self.txt_address.grid(row=8, column=1, pady=10, padx=20, sticky="w")

        ##Create a new frame ...........................................................
        Manage_Frame_1 = Frame(self.root, bd=4, relief=RIDGE, bg="red")
        Manage_Frame_1.place(x=3, y=610, width=1350, height=80)

        btn_frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        btn_frame.place(x=460, y=625, width=430)

        Reqbtn = Button(btn_frame, text="Request", width=25, bg="red", fg="white", relief=GROOVE,
                        font=("times of roman", 9, "bold"), command=self.add).grid(row=0, column=1, padx=10, pady=10)

        clearbtn = Button(btn_frame, text="Clear", width=25, bg="red", fg="white", relief=GROOVE,
                          font=("times of roman", 9, "bold"), command=self.clear).grid(row=0, column=2, padx=10,
                                                                                       pady=10)





        ##Create a new frame ...........................................................
        details_frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        details_frame.place(x=500, y=70, width=800, height=530)

        lbl_search = Label(details_frame, text="Search By Blood Group", bg="red", fg="white",
                           font=("times new roman", 15, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        lbl_search = Label(details_frame, text="Enter:", bg="red", fg="white", font=("times new roman", 15, "bold"))
        lbl_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        txt_search = Entry(details_frame, textvariable=self.search_txt, font=("times new roman", 15, "bold"), bd=5,
                           relief=GROOVE, bg="white")
        txt_search.grid(row=0, column=3, pady=10, padx=20, sticky="w")
        Searchbtn = Button(details_frame, text="Search", width=10, bg="red", fg="white", relief=GROOVE,
                           font=("times of roman", 9, "bold"), command=self.search_data).grid(row=0, column=4, padx=10,
                                                                                              pady=10)


        # Create Table frame.................................................................

        table_frame = Frame(details_frame, bd=4, relief=RIDGE, bg="red")
        table_frame.place(x=10, y=70, width=760, height=400)


        ###Creating Scrollbar..................................................................
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.information = ttk.Treeview(table_frame, column=(
        "First Name", "Last Name", "Gender","Blood Group", "Age", "dob", "Contact No", "Address"),
                                          xscrollcommand=scroll_y, yscrollcommand=scroll_x)
        scroll_x.pack(side="bottom", fill="x")
        scroll_y.pack(side="right", fill="y")

        scroll_x.config(command=self.information.xview())
        scroll_y.config(command=self.information.yview())

        self.information.heading("First Name", text="First Name")
        self.information.heading("Last Name", text="last Name")
        self.information.heading("Blood Group", text="Blood Group")
        self.information.heading("Gender", text="Gender")
        self.information.heading("Age", text="Age")
        self.information.heading("dob", text="BND")
        self.information.heading("Contact No", text="Contact No")
        self.information.heading("Address", text="Hospital")

        self.information['show'] = 'headings'

        self.information.column("First Name", width=80)
        self.information.column("Last Name", width=80)
        self.information.column("Blood Group", width=80)
        self.information.column("Gender", width=80)
        self.information.column("Age", width=40)
        self.information.column("dob", width=80)
        self.information.column("Contact No", width=80)
        self.information.column("Address", width=80)

        self.information.pack(fill="both", expand=1)
        self.information.bind('<ButtonRelease-1>', self.get_cursor)
        self.fetch_data()


    def add(self):
        if self.fname_var.get() == "" or self.blood_group_var.get() == "" or self.contact_var.get() == "":
            messagebox.showerror("Error", "All fields are required to fill")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="blood")
            cursor = con.cursor()
            cursor.execute("insert into blood_requester values(%s,%s,%s,%s,%s,%s,%s,%s)", (self.fname_var.get(),
                                                                                             self.lname_var.get(),
                                                                                             self.gender_var.get(),
                                                                                             self.blood_group_var.get(),
                                                                                             self.age_var.get(),
                                                                                             self.dob_var.get(),
                                                                                             self.contact_var.get(),
                                                                                             self.txt_address.get('1.0',
                                                                                                                  END)))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Record has been inserted")

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="blood")
        cursor = con.cursor()
        cursor.execute('select *from blood_requester')
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.information.delete(*self.information.get_children())
            for row in rows:
                self.information.insert('', END, values=row)
            con.commit()
        con.close()

    def get_cursor(self, ev):
        curosor_row = self.information.focus()
        contents = self.information.item(curosor_row)
        row = contents['values']
        self.fname_var.set(row[0])
        self.lname_var.set(row[1])
        self.gender_var.set(row[2])
        self.blood_group_var.set(row[3])
        self.age_var.set(row[4])
        #self.ldd_var.set(row[5])
        self.dob_var.set(row[5])
        self.contact_var.set(row[6])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, row[7])

    def clear(self):
        self.fname_var.set("")
        self.lname_var.set("")
        self.gender_var.set("")
        self.blood_group_var.set("")
        self.age_var.set("")
        self.dob_var.set("")
        self.contact_var.set("")
        self.txt_address.delete('1.0', END)

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="blood")
        cursor = con.cursor()
        cursor.execute("select *from blood_requester where blood_group LIKE '%" + str(self.search_txt.get()) + "%'")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.information.delete(*self.information.get_children())
            for row in rows:
                self.information.insert('', END, values=row)
            con.commit()
        con.close()

        messagebox.showinfo("Search", "Data was successfully found out ")
class Record:
    def __init__(self, root):
        self.root = root
        self.root.title("Blood Donor Management System")
        self.root.geometry("1370x700+0+0")

        title = Label(self.root, text="Blood Donor Management System", font=("times new roman", 30, "bold"), bd=10, relief=GROOVE,
                      bg="white", fg="red")
        title.pack(side=TOP, fill=X)

        # Variables--------------------------------------------------------------------
        self.donation_date = StringVar()
        self.dob_var = StringVar()
        self.contact_var = StringVar()
        self.donor_contact_var = StringVar()


        # Frame_________________________________________________________________________
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="red")
        Manage_Frame.place(x=30, y=70, width=450, height=600)

        m_title = Label(Manage_Frame, text="   Accept Blood Request", bg="red", fg="white",
                        font=("times new roman", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_donation_date = Label(Manage_Frame, text="Donation Date:", bg="white", fg="black",
                            font=("times new roman", 15, "bold"))
        lbl_donation_date.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        txt_donation_date = Entry(Manage_Frame, textvariable=self.donation_date, font=("times new roman", 12, "bold"), bd=5,
                            relief=GROOVE)
        txt_donation_date.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_contact = Label(Manage_Frame, text="Requester Contact No:", bg="white", fg="black",
                            font=("times new roman", 15, "bold"))
        lbl_contact.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_contact = Entry(Manage_Frame, textvariable=self.contact_var, font=("times new roman", 12, "bold"), bd=5,
                            relief=GROOVE)
        txt_contact.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_donor_contact = Label(Manage_Frame, text="Donor Contact No:", bg="white", fg="black",
                            font=("times new roman", 15, "bold"))
        lbl_donor_contact.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_donor_contact = Entry(Manage_Frame, textvariable=self.donor_contact_var, font=("times new roman", 12, "bold"), bd=5,
                            relief=GROOVE)
        txt_donor_contact.grid(row=3, column=1, pady=10, padx=20, sticky="w")





        Addbtn = Button(Manage_Frame, text="Accept", width=10, bg="white", fg="red", relief=GROOVE,
                        font=("times of roman", 9, "bold"), command=self.add).grid(row=4, column=1, padx=10, pady=10)






        ##Create a new frame ...........................................................
        details_frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        details_frame.place(x=500, y=70, width=800, height=600)

        lbl_search = Label(details_frame, text="Patients information ", bg="red", fg="white",
                           font=("times new roman", 25, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")




        # Create Table frame.................................................................

        table_frame = Frame(details_frame, bd=4, relief=RIDGE, bg="red")
        table_frame.place(x=10, y=80, width=760, height=500)


        ###Creating Scrollbar..................................................................
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.information = ttk.Treeview(table_frame, column=(
        "First Name", "Last Name", "Gender","Blood Group", "Age", "dob", "Contact No", "Address"),
                                          xscrollcommand=scroll_y, yscrollcommand=scroll_x)
        scroll_x.pack(side="bottom", fill="x")
        scroll_y.pack(side="right", fill="y")

        scroll_x.config(command=self.information.xview())
        scroll_y.config(command=self.information.yview())

        self.information.heading("First Name", text="First Name")
        self.information.heading("Last Name", text="last Name")
        self.information.heading("Blood Group", text="Blood Group")
        self.information.heading("Gender", text="Gender")
        self.information.heading("Age", text="Age")
        self.information.heading("dob", text="BND")
        self.information.heading("Contact No", text="Contact No")
        self.information.heading("Address", text="Hospital")

        self.information['show'] = 'headings'

        self.information.column("First Name", width=80)
        self.information.column("Last Name", width=80)
        self.information.column("Blood Group", width=80)
        self.information.column("Gender", width=80)
        self.information.column("Age", width=40)
        self.information.column("dob", width=80)
        self.information.column("Contact No", width=80)
        self.information.column("Address", width=80)

        self.information.pack(fill="both", expand=1)
        self.information.bind('<ButtonRelease-1>', self.get_cursor)
        self.fetch_data()


    def add(self):
        if self.contact_var.get() == ""  or self.donor_contact_var.get() == "":
            messagebox.showerror("Error", "All fields are required to fill")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="blood")
            cursor = con.cursor()

            cursor.execute("insert into record values(%s,%s,%s)", (self.donation_date.get(),
                                                                   self.contact_var.get(),
                                                                   self.donor_contact_var.get()))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Record has been inserted")

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="blood")
        cursor = con.cursor()
        cursor.execute('select *from blood_requester')
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.information.delete(*self.information.get_children())
            for row in rows:
                self.information.insert('', END, values=row)
            con.commit()
        con.close()

    def get_cursor(self, ev):
        curosor_row = self.information.focus()
        contents = self.information.item(curosor_row)
        row = contents['values']
        self.contact_var.set(row[6])

    def clear(self):
        self.donation_date.set("")
        self.donor_contact_var.set("")
        self.contact_var.set("")
class Search:
    def __init__(self, root):
        self.root = root
        self.root.title("Blood Donor Management System")
        self.root.geometry("870x500+0+0")

        # Variables--------------------------------------------------------------------
        self.fname_var = StringVar()
        self.lname_var = StringVar()
        self.gender_var = StringVar()
        self.blood_group_var = StringVar()
        self.age_var = StringVar()
        self.ldd_var = StringVar()
        self.contact_var = StringVar()
        self.search_txt = StringVar()

        # Frame_________________________________________________________________________





        ##Create a new frame ...........................................................
        details_frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        details_frame.pack(fill='both',expand='yes')

        lbl_search = Label(details_frame, text="Search By Blood Group", bg="red", fg="white",
                           font=("times new roman", 15, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        lbl_search = Label(details_frame, text="Enter:", bg="red", fg="white", font=("times new roman", 15, "bold"))
        lbl_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        txt_search = Entry(details_frame, textvariable=self.search_txt, font=("times new roman", 15, "bold"), bd=5,
                           relief=GROOVE, bg="white")
        txt_search.grid(row=0, column=3, pady=10, padx=20, sticky="w")
        Searchbtn = Button(details_frame, text="Search", width=10, bg="red", fg="white", relief=GROOVE,
                           font=("times of roman", 9, "bold"), command=self.search_data).grid(row=0, column=4, padx=10,
                                                                                              pady=10)


        # Create Table frame.................................................................

        table_frame = Frame(details_frame, bd=4, relief=RIDGE, bg="red")
        table_frame.place(x=10, y=70, width=760, height=400)

        ###Creating Scrollbar..................................................................
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.information = ttk.Treeview(table_frame, column=(
        "First Name", "Last Name", "Gender","Blood Group", "Age", "L.D.D", "Contact No", "Address"),
                                          xscrollcommand=scroll_y, yscrollcommand=scroll_x)
        scroll_x.pack(side="bottom", fill="x")
        scroll_y.pack(side="right", fill="y")

        scroll_x.config(command=self.information.xview())
        scroll_y.config(command=self.information.yview())

        self.information.heading("First Name", text="First Name")
        self.information.heading("Last Name", text="last Name")
        self.information.heading("Blood Group", text="Blood Group")
        self.information.heading("Gender", text="Gender")
        self.information.heading("Age", text="Age")
        self.information.heading("L.D.D", text="L.D.D")
        self.information.heading("Contact No", text="Contact No")
        self.information.heading("Address", text="Address")

        self.information['show'] = 'headings'

        self.information.column("First Name", width=80)
        self.information.column("Last Name", width=80)
        self.information.column("Blood Group", width=80)
        self.information.column("Gender", width=80)
        self.information.column("Age", width=40)
        self.information.column("L.D.D", width=80)
        self.information.column("Contact No", width=80)
        self.information.column("Address", width=80)

        self.information.pack(fill="both", expand=1)
        self.information.bind('<ButtonRelease-1>', self.get_cursor)
        self.fetch_data()
        root.mainloop()


    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="blood")
        cursor = con.cursor()
        cursor.execute('select *from donor_information')
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.information.delete(*self.information.get_children())
            for row in rows:
                self.information.insert('', END, values=row)
            con.commit()
        con.close()

    def get_cursor(self, ev):
        curosor_row = self.information.focus()
        contents = self.information.item(curosor_row)
        row = contents['values']
        self.fname_var.set(row[0])
        self.lname_var.set(row[1])
        self.gender_var.set(row[2])
        self.blood_group_var.set(row[3])
        self.age_var.set(row[4])
        self.ldd_var.set(row[5])
        self.contact_var.set(row[6])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, row[7])


    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="blood")
        cursor = con.cursor()
        cursor.execute("select *from donor_information where blood_group LIKE '%" + str(self.search_txt.get()) + "%'")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.information.delete(*self.information.get_children())
            for row in rows:
                self.information.insert('', END, values=row)
            con.commit()
        con.close()

        messagebox.showinfo("Search", "Data was successfully found out ")
def Donor_window():
    root = Toplevel()
    obj = Donor(root)
    root.mainloop()
def Blood_Requester_window():
    root = Toplevel()
    obj = Blood_Requester(root)
    root.mainloop()
def Accept_Blood_Request():
    root = Toplevel()
    obj = Record(root)
    root.mainloop()
def Search_window():
    root = Toplevel()
    obj = Search(root)
    root.mainloop()
root = Tk()
root.geometry("1370x700+0+0")
root.title("Blood Donor Management System")

title = Label(root, text="Blood Donor Management System", font=("times new roman", 30, "bold"), bd=10, relief=GROOVE,
                      bg="white", fg="DarkRed")
title.pack(side=TOP, fill=X)


btn_frame = Frame(root, bd=3, relief=RIDGE, bg="white")
btn_frame.pack(fill='both',expand='yes')


image_bg = ImageTk.PhotoImage(master= root,file='C://Users//DCL//Desktop//hp2.jpg')
label = Label(btn_frame)
label.place(x=0,y=0)
label.config(image=image_bg)

Doner_Button = Button(btn_frame, text="Donor Registration", width=45, bg="DarkRed", fg="white", relief=GROOVE,
                font=("times of roman", 9, "bold"),command=lambda: Donor_window()).grid(row=0, column=1, padx=10, pady=10)

Request_for_Blood_Button = Button(btn_frame, text="Request for Blood", width=45, bg="DarkRed", fg="white", relief=GROOVE,
                font=("times of roman", 9, "bold"),command=lambda: Blood_Requester_window()).grid(row=0, column=2, padx=10, pady=10)

Search_Button = Button(btn_frame, text="Search", width=45, bg="DarkRed", fg="white", relief=GROOVE,
                font=("times of roman", 9, "bold"),command=lambda: Search_window()).grid(row=0, column=3, padx=1, pady=10)

Ac_Req_Button = Button(btn_frame, text="Accept Blood Request", width=45, bg="DarkRed", fg="white", relief=GROOVE,
                font=("times of roman", 9, "bold"),command=lambda: Accept_Blood_Request()).grid(row=0, column=4, padx=10, pady=10)


root.mainloop()

