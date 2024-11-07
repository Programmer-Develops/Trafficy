from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Traffic:
    def __init__(self,root):
        self.root = root
        self.root.title("Traffic Management  - Road Safety")
        self.root.geometry("1540x800+0+0")


        self.Nameofrule=StringVar()
        self.ref=StringVar()
        self.times=StringVar()
        self.Numberofcases=StringVar()
        self.Phonenumber=StringVar()
        self.Caughtdate=StringVar()
        self.Releasedate=StringVar()
        self.Fine=StringVar()
        self.Vehicle=StringVar()
        self.Furtherinfo=StringVar()
        self.Vehiclenumber=StringVar()
        self.Advice=StringVar()
        self.Licensename=StringVar()
        self.Rulebreakerid=StringVar()
        self.Numberoflicense=StringVar()
        self.Name=StringVar()
        self.Dateofbirth=StringVar()
        self.Address=StringVar()


        lbltitle = Label(self.root,bd=20,relief = RIDGE, text="Traffic Management System",fg="red",bg="white",font=("Comic Sans MS",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #___________________________________________Data___________________________________________#
        Dataframe = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=120,width = 1530,height=400)

        DataFrameLeft = LabelFrame(Dataframe,bd=20,relief=RIDGE,padx=10,
                                   font=("times new roman",12,"bold"),text="Rule Breaker Information")
        DataFrameLeft.place(x=0,y=5,width=980,height=350)

        DataFrameRight = LabelFrame(Dataframe,bd=20,relief=RIDGE,padx=10,
                                   font=("times new roman",12,"bold"),text="Information")
        DataFrameRight.place(x=850,y=5,width=460,height=350)

        #________________________________________Buttons Frame______________________________________#
        Buttonframe= Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)

        #________________________________________Details Frame______________________________________#
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE, bg="lightblue")  # Change background color
        Detailsframe.place(x=0, y=600, width=1530, height=220)  # Increased height to 220
 
        #________________________________________DataFrameLeft______________________________________#
        lblNamePerson= Label(DataFrameLeft,text="Name of the Rule",font=("times new Roman",12,"bold"),padx=2,pady=6)
        lblNamePerson.grid(row=0,column=0)

        comruleName= ttk.Combobox(DataFrameLeft,textvariable=self.Nameofrule,state="readonly",font=("times new Roman",12,"bold"),width=33)
        comruleName["values"] = ("Traffic lights rule","Hit and run","Road Rage","Not obeying Traffic police","theft","Lane not followed")
        comruleName.current(0)
        comruleName.grid(row=0,column=1)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Ref no:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35, textvariable=self.ref)
        txtref.grid(row=1,column=1)

        lblno=Label(DataFrameLeft,font=("arial",12,"bold"),text="Times :",padx=2,pady=4)
        lblno.grid(row=2,column=0,sticky=W)
        txtno=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35, textvariable=self.times)
        txtno.grid(row=2,column=1)

        lblnoc=Label(DataFrameLeft,font=("arial",12,"bold"),text="Number of cases :",padx=2,pady=6)
        lblnoc.grid(row=3,column=0,sticky=W)
        txtnoc=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35, textvariable=self.Numberofcases)
        txtnoc.grid(row=3,column=1)

        lbllot=Label(DataFrameLeft,font=("arial",12,"bold"),text="ph no :",padx=2,pady=6)
        lbllot.grid(row=4,column=0,sticky=W)
        txtlot=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35, textvariable=self.Phonenumber)
        txtlot.grid(row=4,column=1)
        
        lbldatecaught=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date of getting caught :",padx=2,pady=6)
        lbldatecaught.grid(row=5,column=0,sticky=W)
        txtdatecaught=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35, textvariable=self.Caughtdate)
        txtdatecaught.grid(row=5,column=1)

        lbldaterelease=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date of release :",padx=2,pady=6)
        lbldaterelease.grid(row=6,column=0,sticky=W)
        txtdaterelease=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35, textvariable=self.Releasedate)
        txtdaterelease.grid(row=6,column=1)

        lblfine=Label(DataFrameLeft,font=("arial",12,"bold"),text="fine :",padx=2,pady=6)
        lblfine.grid(row=7,column=0,sticky=W)
        txtfine=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35, textvariable=self.Fine)
        txtfine.grid(row=7,column=1)

        lblvehicle=Label(DataFrameLeft,font=("arial",12,"bold"),text="vehicle :",padx=2,pady=6)
        lblvehicle.grid(row=8,column=0,sticky=W)
        txtvehicle=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35,  textvariable=self.Vehicle)
        txtvehicle.grid(row=8,column=1)

        lblfurtherinfo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Further Info",padx=2)
        lblfurtherinfo.grid(row=0,column=2,sticky=W)
        txtfurtherinfo=Entry(DataFrameLeft,font=("arial",12,"bold"),width=35, textvariable=self.Furtherinfo)
        txtfurtherinfo.grid(row=0,column=3)

        lblvehicleno=Label(DataFrameLeft,font=("arial",12,"bold"),text="Vehicle number",padx=2,pady=6)
        lblvehicleno.grid(row=1,column=2,sticky=W)
        txtvehicleno=Entry(DataFrameLeft,font=("arial",12,"bold"),width=35, textvariable=self.Vehiclenumber)
        txtvehicleno.grid(row=1,column=3)

        lblstorage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Advice :",padx=2,pady=6)
        lblstorage.grid(row=2,column=2,sticky=W)
        txtstorage=Entry(DataFrameLeft,font=("arial",12,"bold"),width=35, textvariable=self.Advice)
        txtstorage.grid(row=2,column=3)

        lbllicense=Label(DataFrameLeft,font=("arial",12,"bold"),text="License Name",padx=2,pady=6)
        lbllicense.grid(row=3,column=2,sticky=W)
        txtlicense=Entry(DataFrameLeft,font=("arial",12,"bold"),width=35, textvariable=self.Licensename)
        txtlicense.grid(row=3,column=3)

        lblrbid=Label(DataFrameLeft,font=("arial",12,"bold"),text="Rule Breaker ID",padx=2,pady=6)
        lblrbid.grid(row=4,column=2,sticky=W)
        txtrbid=Entry(DataFrameLeft,font=("arial",12,"bold"),width=35, textvariable=self.Rulebreakerid)
        txtrbid.grid(row=4,column=3)

        lbllicenseno=Label(DataFrameLeft,font=("arial",12,"bold"),text="Number of License",padx=2,pady=6)
        lbllicenseno.grid(row=5,column=2,sticky=W)
        txtlicenseno=Entry(DataFrameLeft,font=("arial",12,"bold"),width=35, textvariable=self.Numberoflicense)
        txtlicenseno.grid(row=5,column=3)
        
        lblname=Label(DataFrameLeft,font=("arial",12,"bold"),text="Rule Breaker Name",padx=2,pady=6)
        lblname.grid(row=6,column=2,sticky=W)
        txtname=Entry(DataFrameLeft,font=("arial",12,"bold"),width=35, textvariable=self.Name)
        txtname.grid(row=6,column=3)

        lbldob=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date of Birth",padx=2,pady=6)
        lbldob.grid(row=7,column=2,sticky=W)
        txtdob=Entry(DataFrameLeft,font=("arial",12,"bold"),width=35, textvariable=self.Dateofbirth)
        txtdob.grid(row=7,column=3)

        lbladdress=Label(DataFrameLeft,font=("arial",12,"bold"),text="Rule Breaker Address",padx=2,pady=6)
        lbladdress.grid(row=8,column=2,sticky=W)
        txtaddress=Entry(DataFrameLeft,font=("arial",12,"bold"),width=35, textvariable=self.Address)
        txtaddress.grid(row=8,column=3)

        #________________________________________DataFrameRight______________________________________#
        self.txtInformation=Text(DataFrameRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtInformation.grid(row=0,column=0)

        #___________________________________________buttons_________________________________________#
        btnInformation=Button(Buttonframe,command=self.iInformation,text="Information",bg="green",fg="white",font=("arial",12,"bold"),width=15,height=2,padx=2,pady=6)
        btnInformation.grid(row=0,column=0)

        btnInformationData=Button(Buttonframe,command=self.iInformationData,text="Data",bg="green",fg="white",font=("arial",12,"bold"),width=15,height=2,padx=2,pady=6)
        btnInformationData.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,command=self.update_data,text="Update",bg="green",fg="white",font=("arial",12,"bold"),width=15,height=2,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,command=self.idelete,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=15,height=2,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=15,height=2,padx=2,pady=6,command=self.clear)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,text="Exit",bg="green",fg="white",font=("arial",12,"bold"),width=15,height=2,padx=2,pady=6)
        btnExit.grid(row=0,column=5)

        #___________________________________________Table_________________________________________#
        #___________________________________________Scrollbar_________________________________________#
        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)

        # Traffic table with larger font for visibility
        self.traffic_table = ttk.Treeview(Detailsframe, column=("Nameofrule", "ref", "times", "Numberofcases", "Phonenumber",
                                                                "Caughtdate", "Releasedate", "Fine", "Vehicle", "Vehiclenumber", 
                                                                "Name", "Dateofbirth", "Address"), 
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.traffic_table.xview)
        scroll_y.config(command=self.traffic_table.yview)

        # Adding headings with larger font size
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("arial", 12, "bold"))  # Adjust heading font size

        self.traffic_table.heading("Nameofrule", text="Name of rule")
        self.traffic_table.heading("ref", text="Ref no")
        self.traffic_table.heading("times", text="Times")
        self.traffic_table.heading("Numberofcases", text="Cases")
        self.traffic_table.heading("Phonenumber", text="Phone no")
        self.traffic_table.heading("Caughtdate", text="Caught Date")
        self.traffic_table.heading("Releasedate", text="Release Date")
        self.traffic_table.heading("Fine", text="Fine")
        self.traffic_table.heading("Vehicle", text="Vehicle")
        self.traffic_table.heading("Vehiclenumber", text="Vehicle no")
        self.traffic_table.heading("Name", text="Name")
        self.traffic_table.heading("Dateofbirth", text="Birth Date")
        self.traffic_table.heading("Address", text="Address")



        self.traffic_table["show"]="headings"



        self.traffic_table.column("Nameofrule",width=100)
        self.traffic_table.column("ref",width=100)
        self.traffic_table.column("times",width=100)
        self.traffic_table.column("Numberofcases",width=100)
        self.traffic_table.column("Phonenumber",width=100)
        self.traffic_table.column("Caughtdate",width=100)
        self.traffic_table.column("Releasedate",width=100)
        self.traffic_table.column("Fine",width=100)
        self.traffic_table.column("Vehicle",width=100)
        self.traffic_table.column("Vehiclenumber",width=100)
        self.traffic_table.column("Name",width=100)
        self.traffic_table.column("Dateofbirth",width=100)
        self.traffic_table.column("Address",width=100)

        # Set column widths and make them more visible
        for col in ("Nameofrule", "ref", "times", "Numberofcases", "Phonenumber", "Caughtdate", "Releasedate", 
                    "Fine", "Vehicle", "Vehiclenumber", "Name", "Dateofbirth", "Address"):
            self.traffic_table.column(col, width=120)

        # Adding the table to fill the frame
        self.traffic_table.pack(fill=BOTH, expand=1)
        self.traffic_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    #___________________________________________Functionality_________________________________________#
    def iInformationData(self):
        if self.Nameofrule.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn = mysql.connector.connect(host = "localhost", username="root", password="MY_PASSWORD", database="TrafficData")
            my_cursor= conn.cursor()
            my_cursor.execute("insert into traffic values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.Nameofrule.get(),
                self.ref.get(),
                self.times.get(),
                self.Numberofcases.get(),
                self.Phonenumber.get(),
                self.Caughtdate.get(),
                self.Releasedate.get(),
                self.Fine.get(),
                self.Vehicle.get(),
                self.Numberoflicense.get(),
                self.Name.get(),
                self.Dateofbirth.get(),
                self.Address.get(),
            ))
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")

    def update_data(self):
        conn = mysql.connector.connect(host = "localhost", username="root", password="MY_PASSWORD", database="TrafficData")
        my_cursor= conn.cursor()
        my_cursor.execute("update traffic set Nameofrule=%s,times=%s,Numberofcases=%s,Phonenumber=%s,Caughtdate=%s,Releasedate=%s,fine=%s,Vehicle=%s,Numberoflicense=%s,Name=%s,Dateofbirth=%s,Address=%s where ref=%s",(
            self.Nameofrule.get(),
            self.ref.get(),
            self.times.get(),
            self.Numberofcases.get(),
            self.Phonenumber.get(),
            self.Caughtdate.get(),
            self.Releasedate.get(),
            self.Fine.get(),
            self.Vehicle.get(),
            self.Numberoflicense.get(),
            self.Name.get(),
            self.Dateofbirth.get(),
            self.Address.get(),
        ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Updated successfully")


    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost", username="root", password="MY_PASSWORD", database="TrafficData")
        my_cursor= conn.cursor()
        my_cursor.execute("select * from traffic")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.traffic_table.delete(*self.traffic_table.get_children())
            for i in rows:
                self.traffic_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self,event=""):
        cursor_row=self.traffic_table.focus()
        content=self.traffic_table.item(cursor_row)
        row=content["values"]
        self.Nameofrule.set(row[0])
        self.ref.set(row[1])
        self.times.set(row[2])
        self.Numberofcases.set(row[3])
        self.Phonenumber.set(row[4])
        self.Caughtdate.set(row[5])
        self.Releasedate.set(row[6])
        self.Fine.set(row[7])
        self.Vehicle.set(row[8])
        self.Numberoflicense.set(row[9])
        self.Name.set(row[10])
        self.Dateofbirth.set(row[11])
        self.Address.set(row[12])

    def iInformation(self):
        self.txtInformation.insert(END,"Name of rule:\t\t\t"+self.Nameofrule.get()+"\n")
        self.txtInformation.insert(END,"Ref no:\t\t\t"+self.ref.get()+"\n")
        self.txtInformation.insert(END,"Times:\t\t\t"+self.times.get()+"\n")
        self.txtInformation.insert(END,"Number of cases:\t\t\t"+self.Numberofcases.get()+"\n")
        self.txtInformation.insert(END,"Phone number:\t\t\t"+self.Phonenumber.get()+"\n")
        self.txtInformation.insert(END,"Caught Date:\t\t\t"+self.Caughtdate.get()+"\n")
        self.txtInformation.insert(END,"Release Date:\t\t\t"+self.Releasedate.get()+"\n")
        self.txtInformation.insert(END,"Fine:\t\t\t"+self.Fine.get()+"\n")
        self.txtInformation.insert(END,"Vehicle:\t\t\t"+self.Vehicle.get()+"\n")
        self.txtInformation.insert(END,"Further Info:\t\t\t"+self.Furtherinfo.get()+"\n")
        self.txtInformation.insert(END,"Vechicle Number:\t\t\t"+self.Vehiclenumber.get()+"\n")
        self.txtInformation.insert(END,"Advice:\t\t\t"+self.Advice.get()+"\n")
        self.txtInformation.insert(END,"License Name:\t\t\t"+self.Licensename.get()+"\n")
        self.txtInformation.insert(END,"Rule Breaker ID:\t\t\t"+self.Rulebreakerid.get()+"\n")
        self.txtInformation.insert(END,"Number of License:\t\t\t"+self.Numberoflicense.get()+"\n")
        self.txtInformation.insert(END,"Name:\t\t\t"+self.Name.get()+"\n")
        self.txtInformation.insert(END,"Date of birth:\t\t\t"+self.Dateofbirth.get()+"\n")
        self.txtInformation.insert(END,"Address:\t\t\t"+self.Address.get()+"\n")

    def idelete(self):
        conn = mysql.connector.connect(host = "localhost", username="root", password="MY_PASSWORD", database="TrafficData")
        my_cursor= conn.cursor()
        query = "delete from traffic where ref=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Successfully deleted record")

    def clear(self):
        self.Nameofrule.set("")
        self.ref.set("")
        self.times.set("")
        self.Numberofcases.set("")
        self.Phonenumber.set("")
        self.Caughtdate.set("")
        self.Releasedate.set("")
        self.Fine.set("")
        self.Vehicle.set("")
        self.Furtherinfo.set("")
        self.Vehiclenumber.set("")
        self.Advice.set("")
        self.Licensename.set("")
        self.Rulebreakerid.set("")
        self.Numberoflicense.set("")
        self.Name.set("")
        self.Dateofbirth.set("")
        self.Address.set("")
        self.txtInformation.delete("1.0",END)

    def iExit(self):
        iExit=messagebox.askyesno("Traffic Management System","Confirm you want to exit ?")
        if iExit>0:
            root.destroy()
            return




if __name__ == "__main__":
    root=Tk()
    application=Traffic(root)
    root.mainloop()