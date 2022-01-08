import tkinter as tk    # Standard Python interface to the Tcl/Tk GUI toolkit
from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox as ms
import sqlite3    # sqlite3 is a relational database management system contained in a C library
Item1 =0
Item2 =0
Item3 =0
Item4 =0
Item5 =0


# make database and users (if not exists already) table at programme start up
with sqlite3.connect('Users.db') as db:
    c = db.cursor()   #cursur() allows Python code to execute PostgreSQL command in a database session.

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEXT NOT NULL)')
db.commit()  # commit() method is used to confirm the changes made by the user to the database
db.close()    # close() function shall deallocate the file descriptor indicated by fildes

#main Class
class user:
    def __init__(self,master):    # __init__ method initializes the object's state
        # Window 
        self.master = master   # self: the instance of the class, master:gives access to the root window (Tk)
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        #Create Widgets
        self.widgets()

    #Login Function
    def login(self):
        #Establish Connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()   # it fetches all rows of a query result set and returns a list of tuples
        if result:
            self.logf.pack_forget()  # pack_forget: Unmap any widget from the screen
            self.head['text'] = "Welcome " + self.username.get()
            self.head.configure(fg="black")
            self.head.pack(fill=X)  # pack:organizes the widgets in blocks before placing in the parent widget
            application = Home(root)
            
        else:
            ms.showerror('Oops!','Username Not Found.')
            
    def new_user(self):
        #Establish Connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user,[(self.username.get())])        
        if c.fetchall():
            ms.showerror('Error!','Username Already Taken!')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log()
        #Create New Account 
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()

        #Frame Packing Methords
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'Login'
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
        
    #Draw Widgets
    def widgets(self):
        self.head = Label(self.master,text = 'Login Panel',font = ('imprint mt shadow',20),pady = 10)
        self.head.pack()
        self.logf = Frame(self.master,padx =10,pady = 10)
        Label(self.logf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.login).grid()
        Button(self.logf,text = ' Create Account ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.cr).grid(row=2,column=1)
        self.logf.pack()
        
        self.crf = Frame(self.master,padx =10,pady = 10)
        Label(self.crf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.new_user).grid()
        Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.log).grid(row=2,column=1)
        # command:to call a function// bd:to set the border width in pixels// grid:organizes the widgets in grid before placing in the parent widget

class train:

    def __init__(self,root):
        self.root = root  # Self.root: to tell the interpreter to look at a "root" of the objects being processed
        
        DateofOrder=StringVar()  # StringVar:holds a string
        DateofOrder.set(time.strftime(" %d / %m / %Y "))
        Receipt_Ref=StringVar()
        PaidTax=StringVar()
        SubTotal=StringVar()
        TotalCost=StringVar()

        var1=IntVar()    #IntVar: holds an integer
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        journeyType=IntVar()
        trainType=IntVar()
        
        varl1=StringVar()
        varl2=StringVar()
        varl3=StringVar()
        reset_counter=0

        Firstname=StringVar()
        Surname=StringVar()
        Address=StringVar()
        Postcode=StringVar()
        Mobile=StringVar()
        Telephone=StringVar()
        Email=StringVar()

        
        Km=StringVar()
        Travel_Ins=StringVar()
        Luggage=StringVar()
        Receipt=StringVar()

        Standard=StringVar()
        Express=StringVar()
       
        Km.set("0")
        Travel_Ins.set("0")
        Luggage.set("0")
        
        Standard.set("0")
        Express.set("0")
#==========================================Define Functiom==================================================

        def Reset():
            Km.set("0")
            Travel_Ins.set("0")
            Luggage.set("0")

            Firstname.set("")
            Surname.set("")
            Address.set("")
            Postcode.set("")
            Mobile.set("")
            Telephone.set("")
            Email.set("")

            
            TotalCost.set("")
            self.txtReceipt1.delete("1.0",END)  # .delete('1.0', END): delete the text
            self.txtReceipt2.delete("1.0",END)
            
            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            journeyType.set(0)
            trainType.set(0)
            varl1.set("0")
            varl2.set("0")
            varl3.set("0")
            
            Standard.set(0)
            Express.set(0)

            self.cboPickup.current(0)
            self.cboDrop.current(0)
           
            self.txtKm.configure(state=DISABLED)
            self.txtTravel_Ins.configure(state=DISABLED)
            self.txtLuggage.configure(state=DISABLED)
        
            self.txtStandard.configure(state=DISABLED)
            self.txtExpress.configure(state=DISABLED)
            self.reset_counter=1

        def Receiptt():
            if reset_counter == 0 and Firstname.get()!="" and Surname.get()!="" and Address.get()!="" and Postcode.get()!="" and Mobile.get()!="" and Telephone.get()!="" and Email.get()!="":
                self.txtReceipt1.delete("1.0",END)
                self.txtReceipt2.delete("1.0",END)
                x=random.randint(10853,500831)
                randomRef = str(x)
                Receipt_Ref.set(randomRef)

                self.txtReceipt1.insert(END,"Receipt Ref:\n")
                self.txtReceipt2.insert(END, Receipt_Ref.get() + "\n")
                self.txtReceipt1.insert(END,'Date:\n')
                self.txtReceipt2.insert(END, DateofOrder.get() + "\n")
                self.txtReceipt1.insert(END,'Train No:\n')
                self.txtReceipt2.insert(END, 'TR ' + Receipt_Ref.get() + " BW\n")
                self.txtReceipt1.insert(END,'Firstname:\n')
                self.txtReceipt2.insert(END, Firstname.get() + "\n")
                self.txtReceipt1.insert(END,'Surname:\n')
                self.txtReceipt2.insert(END, Surname.get() + "\n")
                self.txtReceipt1.insert(END,'Address:\n')
                self.txtReceipt2.insert(END, Address.get() + "\n")
                self.txtReceipt1.insert(END,'Postal Code:\n')
                self.txtReceipt2.insert(END, Postcode.get() + "\n")
                self.txtReceipt1.insert(END,'Telephone:\n')
                self.txtReceipt2.insert(END, Telephone.get() + "\n")
                self.txtReceipt1.insert(END,'Mobile:\n')
                self.txtReceipt2.insert(END, Mobile.get() + "\n")
                self.txtReceipt1.insert(END,'Email:\n')
                self.txtReceipt2.insert(END, Email.get() + "\n")
                self.txtReceipt1.insert(END,'From:\n')
                self.txtReceipt2.insert(END, varl1.get() + "\n")
                self.txtReceipt1.insert(END,'To:\n')
                self.txtReceipt2.insert(END, varl2.get() + "\n")
                self.txtReceipt1.insert(END,'Local:\n')
                self.txtReceipt2.insert(END, Standard.get() + "\n")
                self.txtReceipt1.insert(END,'Express:\n')
                self.txtReceipt2.insert(END, Express.get() + "\n")
                self.txtReceipt1.insert(END,'Total Cost:\n')
                self.txtReceipt2.insert(END, str(TotalCost.get()))
                
            else:
                self.txtReceipt1.delete("1.0",END)
                self.txtReceipt2.delete("1.0",END)
                self.txtReceipt1.insert(END,"\nNo Input")
                

        

        
        def Kilo():
            if var2.get() == 0:
                self.txtKm.configure(state=DISABLED)
                Km.set("0")
            elif var2.get() == 1 and varl1.get() != "" and varl2.get() != "":
                self.txtKm.configure(state=NORMAL)
                if varl1.get() == "Diamond Harbour":
                    switch ={"Sealdah": 20,"Sonarpur": 15,"Baruipur":10,"Diamond Harbour ": 0}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "Baruipur":
                    switch ={"Sealdah": 10,"Diamond Harbour": 10,"Sonarpur":5,"Baruipur": 0}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "Sonarpur":
                    switch ={"Sealdah": 5,"Diamond Harbour": 15,"Baruipur":10,"Sonarpur": 0}
                elif varl1.get() == "Sealdah":
                    switch ={"Diamond Harbour": 20,"Baruipur": 10,"Sonarpur":5,"Sealdah": 0}
                    Km.set(switch[varl2.get()])        

        
        def Travelling():
            global Item3
            if var3.get() == 1:
                self.txtTravel_Ins.configure(state = NORMAL)
                Item3=float(10)
                Travel_Ins.set("Rs " + str(Item3))
            
            else:
                self.txtTravel_Ins.configure(state = DISABLED)
                Travel_Ins.set("0")
                Item3=float(0)

        
        def Lug():
            global Item4
            if (var4.get()==1):
                self.txtLuggage.configure(state = NORMAL)
                Item4=float(30)
                Luggage.set("Rs "+ str(Item4))
            else:
                self.txtLuggage.configure(state = DISABLED)
                Luggage.set("0")
                Item4=float(0)
         
        def selectCar():
            global Item5
            if trainType.get() == 1:
                self.txtExpress.configure(state = DISABLED)
                Express.set("0") 
                self.txtStandard.configure(state = NORMAL)
                Item5 = float(1)
                Standard.set("Rs "+ str(Item5))
            
            else:
                self.txtStandard.configure(state =DISABLED)
                Standard.set("0")
                self.txtExpress.configure(state = NORMAL)
                Item5 = float(2)
                Express.set("Rs "+ str(Item5))
        
                       
        def Total_Paid():
            if ((var1.get() == 1 and var2.get() == 1 and var4.get() == 1 or var3.get() == 1) and trainType.get() != 0 and journeyType.get() != 0 and (varl1.get() != "" and varl2.get() !="")):
                if journeyType.get()==1:
                    Item2=Km.get()
                    Cost_of_fare = ((float(Item2)*Item5)+Item3+Item4)
                    TT = "Rs " + str('%.2f'%(Cost_of_fare))
                if journeyType.get()==2:
                    Item2=Km.get()
                    Cost_of_fare = ((float(Item2)*Item5)*2+Item3+Item4)
                    TT = "Rs " + str('%.2f'%(Cost_of_fare))
                TotalCost.set(TT)
            else:
                w = ms.showwarning("Error !","Invalid Input\nPlease try again !!!")
   #================================================mainframe========================================================================

        MainFrame=Frame(self.root)
        MainFrame.pack(fill=BOTH,expand=True)
        
        Tops = Frame(MainFrame, bd=5, width=1000,relief=RIDGE) # relief:simulate 3-D effects around the outside of the widget
        Tops.pack(side=TOP,fill=BOTH)

        self.lblTitle=Label(Tops,font=('arial',20,'bold'),text="\t                             Train Booking System ")
        self.lblTitle.grid()  # lbl:label

    #================================================customerframedetail=============================================================
        CustomerDetailsFrame=LabelFrame(MainFrame, width=1000,height=300,bd=20, pady=5, relief=RIDGE)
        CustomerDetailsFrame.pack(side=BOTTOM,fill=BOTH,expand=True)

        FrameDetails=Frame(CustomerDetailsFrame, width=880,height=300,bd=10, relief=RIDGE)
        FrameDetails.pack(side=LEFT,fill=BOTH,expand=True)

        CustomerName=LabelFrame(FrameDetails, width=150,height=250,bd=10, font=('arial',12,'bold'),text="Customer Info", relief=RIDGE)
        CustomerName.grid(row=0,column=0)

        TravelFrame = LabelFrame(FrameDetails,bd=10, width=300,height=250, font=('arial',12,'bold'),text="Booking Detail", relief=RIDGE)
        TravelFrame.grid(row=0,column=1)

        Book_Frame=LabelFrame(FrameDetails,width=300,height=150,relief=FLAT)
        Book_Frame.grid(row=1,column=0)

        CostFrame = LabelFrame(FrameDetails,width=150,height=150,bd=5,relief=FLAT)
        CostFrame.grid(row=1,column=1)


    #===============================================recipt======================================================================
        Receipt_BottonFrame=LabelFrame(CustomerDetailsFrame,bd=10, width=450,height=400, relief=RIDGE)
        Receipt_BottonFrame.pack(side=RIGHT,fill=BOTH,expand=True)

        ReceiptFrame=LabelFrame(Receipt_BottonFrame, width=350,height=300, font=('arial',12,'bold'),text="Receipt", relief=RIDGE)
        ReceiptFrame.grid(row=0,column=0)

        ButtonFrame=LabelFrame(Receipt_BottonFrame, width=350,height=100, relief=RIDGE)
        ButtonFrame.grid(row=1,column=0)
    #=========================================================CustomerName====================================================

        self.lblFirstname=Label(CustomerName,font=('arial',14,'bold'),text="Firstname",bd=7)
        self.lblFirstname.grid(row=0,column=0,sticky=W)
        self.txtFirstname=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Firstname,bd=7,insertwidth=2,justify=RIGHT)
        self.txtFirstname.grid(row=0,column=1)  #txt:text


        self.lblSurname=Label(CustomerName,font=('arial',14,'bold'),text="Surname",bd=7)
        self.lblSurname.grid(row=1,column=0,sticky=W)
        self.txtSurname=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Surname,bd=7,insertwidth=2,justify=RIGHT)
        self.txtSurname.grid(row=1,column=1,sticky=W)


        self.lblAddress=Label(CustomerName,font=('arial',14,'bold'),text="Address",bd=7)
        self.lblAddress.grid(row=2,column=0,sticky=W)
        self.txtAddress=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Address,bd=7,insertwidth=2,justify=RIGHT)
        self.txtAddress.grid(row=2,column=1)


        self.lblPostcode=Label(CustomerName,font=('arial',14,'bold'),text="Postcode",bd=7)
        self.lblPostcode.grid(row=3,column=0,sticky=W)
        self.txtPostcode=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Postcode,bd=7,insertwidth=2,justify=RIGHT)
        self.txtPostcode.grid(row=3,column=1)


        self.lblTelephone=Label(CustomerName,font=('arial',14,'bold'),text="Telephone",bd=7)
        self.lblTelephone.grid(row=4,column=0,sticky=W)
        self.txtTelephone=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Telephone,bd=7,insertwidth=2,justify=RIGHT)
        self.txtTelephone.grid(row=4,column=1)

        self.lblMobile=Label(CustomerName,font=('arial',14,'bold'),text="Mobile",bd=7)
        self.lblMobile.grid(row=5,column=0,sticky=W)
        self.txtMobile=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Mobile,bd=7,insertwidth=2,justify=RIGHT)
        self.txtMobile.grid(row=5,column=1)

        self.lblEmail=Label(CustomerName,font=('arial',14,'bold'),text="Email",bd=7)
        self.lblEmail.grid(row=6,column=0,sticky=W)
        self.txtEmail=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Email,bd=7,insertwidth=2,justify=RIGHT)
        self.txtEmail.grid(row=6,column=1)

 
    #===============================================Train Information==============================================================
        self.lblPickup=Label(TravelFrame,font=('arial',14,'bold'),text="Pickup",bd=7)
        self.lblPickup.grid(row=0,column=0,sticky=W)

        self.cboPickup =ttk.Combobox(TravelFrame, textvariable = varl1 , state='readonly', font=('arial',20,'bold'), width=14)
        self.cboPickup['value']=('','Diamond Harbour','Baruipur','Sonarpur','Sealdah')
        self.cboPickup.current(0)
        self.cboPickup.grid(row=0,column=1)   #cbo: combo boxes


        self.lblDrop=Label(TravelFrame,font=('arial',14,'bold'),text="Drop",bd=7)
        self.lblDrop.grid(row=1,column=0,sticky=W)

        self.cboDrop =ttk.Combobox(TravelFrame, textvariable = varl2 , state='readonly', font=('arial',20,'bold'), width=14)
        self.cboDrop['value']=('','Diamond Harbour','Baruipur','Sonarpur','Sealdah')
        self.cboDrop.current(0)
        self.cboDrop.grid(row=1,column=1)

    #===============================================Train Information==============================================================


        self.chkKm=Checkbutton(TravelFrame,text="Distance(KMs) *",variable = var2, onvalue=1, offvalue=0,font=('arial',16,'bold'),command=Kilo).grid(row=4, column=0, sticky=W)
        self.txtKm=Label(TravelFrame,font=('arial',14,'bold'),textvariable=Km,bd=6,width=18,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN,highlightthickness=0)
        self.txtKm.grid(row=4,column=1)   # chk:check box

        self.chkTravel_Ins=Checkbutton(TravelFrame,text="Travelling Insurance *",variable = var3, onvalue=1, offvalue=0,font=('arial',16,'bold'),command=Travelling).grid(row=5, column=0, sticky=W)
        self.txtTravel_Ins=Label(TravelFrame,font=('arial',14,'bold'),textvariable=Travel_Ins,bd=6,width=18,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN)
        self.txtTravel_Ins.grid(row=5,column=1)

      
        self.chkLuggage=Checkbutton(TravelFrame,text="Extra Luggage",variable = var4, onvalue=1, offvalue=0,font=('arial',16,'bold'),command=Lug).grid(row=6, column=0, sticky=W)
        self.txtLuggage=Label(TravelFrame,font=('arial',14,'bold'),textvariable=Luggage,bd=6,width=18,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN)
        self.txtLuggage.grid(row=6,column=1)
    
    #=================================payment information ===========================================================================
         

        self.lblTotalCost=Label(CostFrame,font=('arial',14,'bold'),text="Total Cost",bd=7)
        self.lblTotalCost.grid(row=2,column=2,sticky=W)
        self.txtTotalCost = Label(CostFrame,font=('arial',14,'bold'),textvariable=TotalCost,bd=7, width=10, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtTotalCost.grid(row=2,column=3)

    #==========================================================Train select=======================================================================

        self.chkStandard=Radiobutton(Book_Frame,text="Local",value=1,variable = trainType,font=('arial',14,'bold'),command=selectCar).grid(row=0, column=0, sticky=W)
        self.txtStandard = Label(Book_Frame,font=('arial',14,'bold'),width =7,textvariable=Standard,bd=5, state= DISABLED, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtStandard.grid(row=0,column=1)
    
       
        self.chkExpress = Radiobutton(Book_Frame,text="Express",value=3,variable = trainType,font=('arial',14,'bold'),command=selectCar).grid(row=2, column=0)
        self.txtExpress = Label(Book_Frame,font=('arial',14,'bold'),width =7,textvariable=Express,bd=5, state= DISABLED, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtExpress.grid(row=2,column=1)

        self.chkSingle =Radiobutton(Book_Frame,text="Single",value=1,variable = journeyType,font=('arial',14,'bold')).grid(row=0, column=2, sticky=W)
        self.chkReturn =Radiobutton(Book_Frame,text="Return",value=2,variable = journeyType,font=('arial',14,'bold')).grid(row=2, column=2, sticky=W)
        
    
    #=======================================Receipt====================================================================================

        self.txtReceipt1 = Text(ReceiptFrame,width = 22, height = 21,font=('arial',10,'bold'),borderwidth=0)
        self.txtReceipt1.grid(row=0,column=0,columnspan=2)
        self.txtReceipt2 = Text(ReceiptFrame,width = 22, height = 21,font=('arial',10,'bold'),borderwidth=0)
        self.txtReceipt2.grid(row=0,column=2,columnspan=2)


    #======================================Button========================================================================================
        
        self.btnTotal = Button(ButtonFrame,padx=10,bd=7,font=('arial',7,'bold'),width = 2,text='Total',command=Total_Paid).grid(row=0,column=0)
        self.btnReceipt = Button(ButtonFrame,padx=10,bd=7,font=('arial',7,'bold'),width = 2,text='Receipt',command=Receiptt).grid(row=0,column=1)
        self.btnReset = Button(ButtonFrame,padx=10,bd=7,font=('arial',7,'bold'),width = 2,text='Reset',command=Reset).grid(row=0,column=2)
        self.btnExit = Button(ButtonFrame,padx=10,bd=7,font=('arial',7,'bold'),width = 2,text='Exit', command=root.quit).grid(row=0,column=3)
        
    #====================================================================================================================================
class cab:

    def __init__(self,root):
        self.root = root

        DateofOrder=StringVar()
        DateofOrder.set(time.strftime(" %d / %m / %Y "))
        Receipt_Ref=StringVar()
        PaidTax=StringVar()
        SubTotal=StringVar()
        TotalCost=StringVar()

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        journeyType=IntVar()
        carType=IntVar()
        
        varl1=StringVar()
        varl2=StringVar()
        varl3=StringVar()
        reset_counter=0


        Firstname=StringVar()
        Surname=StringVar()
        Address=StringVar()
        Postcode=StringVar()
        Mobile=StringVar()
        Telephone=StringVar()
        Email=StringVar()

        CabTax=StringVar()
        Km=StringVar()
        Travel_Ins=StringVar()
        Luggage=StringVar()
        Receipt=StringVar()

        Standard=StringVar()
        FordGalaxy=StringVar()
        FordMondeo=StringVar()

        CabTax.set("0")
        Km.set("0")
        Travel_Ins.set("0")
        Luggage.set("0")

        Standard.set("0")
        FordGalaxy.set("0")
        FordMondeo.set("0")
    
    #==========================================Define Functiom==================================================

        def Reset():
            CabTax.set("0")
            Km.set("0")
            Travel_Ins.set("0")
            Luggage.set("0")

            Standard.set("0")
            FordGalaxy.set("0")
            FordMondeo.set("0")

            Firstname.set("")
            Surname.set("")
            Address.set("")
            Postcode.set("")
            Mobile.set("")
            Telephone.set("")
            Email.set("")

            PaidTax.set("")
            SubTotal.set("")
            TotalCost.set("")
            self.txtReceipt1.delete("1.0",END)
            self.txtReceipt2.delete("1.0",END)
            
            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            journeyType.set(0)
            carType.set(0)
            varl1.set("0")
            varl2.set("0")
            varl3.set("0")

            self.cboPickup.current(0)
            self.cboDrop.current(0)
            self.cboPooling.current(0)

            self.txtCabTax.configure(state=DISABLED)
            self.txtKm.configure(state=DISABLED)
            self.txtTravel_Ins.configure(state=DISABLED)
            self.txtLuggage.configure(state=DISABLED)
        
            self.txtStandard.configure(state=DISABLED)
            self.txtFordGalaxy.configure(state=DISABLED)
            self.txtFordMondeo.configure(state=DISABLED)
            self.reset_counter=1

        def Receiptt():
            if reset_counter == 0 and Firstname.get()!="" and Surname.get()!="" and Address.get()!="" and Postcode.get()!="" and Mobile.get()!="" and Telephone.get()!="" and Email.get()!="":
                self.txtReceipt1.delete("1.0",END)
                self.txtReceipt2.delete("1.0",END)
                x=random.randint(10853,500831)
                randomRef = str(x)
                Receipt_Ref.set(randomRef)

                self.txtReceipt1.insert(END,"Receipt Ref:\n")
                self.txtReceipt2.insert(END, Receipt_Ref.get() + "\n")
                self.txtReceipt1.insert(END,'Date:\n')
                self.txtReceipt2.insert(END, DateofOrder.get() + "\n")
                self.txtReceipt1.insert(END,'Cab No:\n')
                self.txtReceipt2.insert(END, 'TR ' + Receipt_Ref.get() + " BW\n")
                self.txtReceipt1.insert(END,'Firstname:\n')
                self.txtReceipt2.insert(END, Firstname.get() + "\n")
                self.txtReceipt1.insert(END,'Surname:\n')
                self.txtReceipt2.insert(END, Surname.get() + "\n")
                self.txtReceipt1.insert(END,'Address:\n')
                self.txtReceipt2.insert(END, Address.get() + "\n")
                self.txtReceipt1.insert(END,'Postal Code:\n')
                self.txtReceipt2.insert(END, Postcode.get() + "\n")
                self.txtReceipt1.insert(END,'Telephone:\n')
                self.txtReceipt2.insert(END, Telephone.get() + "\n")
                self.txtReceipt1.insert(END,'Mobile:\n')
                self.txtReceipt2.insert(END, Mobile.get() + "\n")
                self.txtReceipt1.insert(END,'Email:\n')
                self.txtReceipt2.insert(END, Email.get() + "\n")
                self.txtReceipt1.insert(END,'From:\n')
                self.txtReceipt2.insert(END, varl1.get() + "\n")
                self.txtReceipt1.insert(END,'To:\n')
                self.txtReceipt2.insert(END, varl2.get() + "\n")
                self.txtReceipt1.insert(END,'Pooling:\n')
                self.txtReceipt2.insert(END, varl3.get() + "\n")
                self.txtReceipt1.insert(END,'Standard:\n')
                self.txtReceipt2.insert(END, Standard.get() + "\n")
                self.txtReceipt1.insert(END,'Prime Sedan:\n')
                self.txtReceipt2.insert(END, FordGalaxy.get() + "\n")
                self.txtReceipt1.insert(END,'Premium Sedan:\n')
                self.txtReceipt2.insert(END, FordMondeo.get() + "\n")
                self.txtReceipt1.insert(END,'Paid:\n')
                self.txtReceipt2.insert(END, PaidTax.get() + "\n")
                self.txtReceipt1.insert(END,'SubTotal:\n')
                self.txtReceipt2.insert(END, str(SubTotal.get()) + "\n")
                self.txtReceipt1.insert(END,'Total Cost:\n')
                self.txtReceipt2.insert(END, str(TotalCost.get()))
                
            else:
                self.txtReceipt1.delete("1.0",END)
                self.txtReceipt2.delete("1.0",END)
                self.txtReceipt1.insert(END,"\nNo Input")
                

        def Cab_Tax():
            global Item1
            if var1.get() == 1:
                self.txtCabTax.configure(state = NORMAL)
                Item1=float(50)
                CabTax.set("Rs " + str(Item1))
            elif var1.get() == 0:
                self.txtCabTax.configure(state=DISABLED)
                CabTax.set("0")
                Item1=0

        
        def Kilo():
            if var2.get() == 0:
                self.txtKm.configure(state=DISABLED)
                Km.set("0")
            elif var2.get() == 1 and varl1.get() != "" and varl2.get() != "":
                self.txtKm.configure(state=NORMAL)
                if varl1.get() == "VIP road":
                    switch ={"Salt Lake": 10,"Park street": 8,"New Town":6,"VIP road ": 0}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "Park street":
                    switch ={"Salt Lake": 10,"VIP road": 8,"New Town":6,"Park street ": 0}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "Salt Lake":
                    switch ={"VIP road": 10,"Park street": 8,"New Town":6,"Salt Lake ": 0}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "New Town":
                    switch ={"Salt Lake": 10,"Park street": 8,"VIP road":6,"New Town ": 0}
                    Km.set(switch[varl2.get()])        

        
        def Travelling():
            global Item3
            if var3.get() == 1:
                self.txtTravel_Ins.configure(state = NORMAL)
                Item3=float(10)
                Travel_Ins.set("Rs " + str(Item3))
            elif var3.get() == 0:
                self.txtTravel_Ins.configure(state = DISABLED)
                Travel_Ins.set("0")
                Item3=0

        
        def Lug():
            global Item4
            if (var4.get()==1):
                self.txtLuggage.configure(state = NORMAL)
                Item4=float(30)
                Luggage.set("Rs "+ str(Item4))
            elif var4.get()== 0:
                self.txtLuggage.configure(state = DISABLED)
                Luggage.set("0")
                Item4=0

        
        def selectCar():
            global Item5
            if carType.get() == 1:
                self.txtFordGalaxy.configure(state = DISABLED)
                FordGalaxy.set("0") 
                self.txtFordMondeo.configure(state = DISABLED)
                FordMondeo.set("0")
                self.txtStandard.configure(state = NORMAL)
                Item5 = float(8)
                Standard.set("Rs "+ str(Item5))
            elif carType.get() == 2:
                self.txtStandard.configure(state =DISABLED)
                Standard.set("0")
                self.txtFordMondeo.configure(state = DISABLED)
                FordMondeo.set("0")
                self.txtFordGalaxy.configure(state = NORMAL)
                Item5 = float(15)
                FordGalaxy.set("Rs "+ str(Item5))
            else:
                self.txtStandard.configure(state =DISABLED)
                Standard.set("0")
                self.txtFordGalaxy.configure(state = DISABLED)
                FordGalaxy.set("0")
                self.txtFordMondeo.configure(state = NORMAL)
                Item5 = float(22)
                FordMondeo.set("Rs "+ str(Item5))
                
                       
        def Total_Paid():
            if ((var1.get() == 1 and var2.get() == 1 and var3.get() == 1 or var4.get() == 1) and carType.get() != 0 and journeyType.get() != 0 and (varl1.get() != "" and varl2.get() !="")):
                if journeyType.get()==1:
                    Item2=Km.get()
                    Cost_of_fare = (Item1+(float(Item2)*Item5)+Item3+Item4)

                    Tax = "Rs " + str('%.2f'%((Cost_of_fare) *0.09))
                    ST = "Rs " + str('%.2f'%((Cost_of_fare)))
                    TT = "Rs " + str('%.2f'%(Cost_of_fare+((Cost_of_fare)*0.9)))
                elif journeyType.get()==2:
                    Item2=Km.get()
                    Cost_of_fare = (Item1+(float(Item2)*Item5)*1.5+Item3+Item4)

                    Tax = "Rs " + str('%.2f'%((Cost_of_fare) *0.09))
                    ST = "Rs " + str('%.2f'%((Cost_of_fare)))
                    TT = "Rs " + str('%.2f'%(Cost_of_fare+((Cost_of_fare)*0.9)))
                else:
                    Item2=Km.get()
                    Cost_of_fare = (Item1+(float(Item2)*Item5)*2+Item3+Item4)

                    Tax = "Rs " + str('%.2f'%((Cost_of_fare) *0.09))
                    ST = "Rs " + str('%.2f'%((Cost_of_fare)))
                    TT = "Rs " + str('%.2f'%(Cost_of_fare+((Cost_of_fare)*0.9)))

                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)
            else:
                w = ms.showwarning("Error !","Invalid Input\nPlease try again !!!")

            

   #================================================mainframe========================================================================

        MainFrame=Frame(self.root)
        MainFrame.pack(fill=BOTH,expand=True)
        
        Tops = Frame(MainFrame, bd=10,height=20, width=500,relief=RIDGE)
        Tops.pack(side=TOP,fill=BOTH)

        self.lblTitle=Label(Tops,font=('arial',15,'bold'),text="\t                                       Cab Booking System ")
        self.lblTitle.grid()

    #================================================customerframedetail=============================================================
        CustomerDetailsFrame=LabelFrame(MainFrame, width=1000,height=300,bd=20, pady=5, relief=RIDGE)
        CustomerDetailsFrame.pack(side=BOTTOM,fill=BOTH,expand=True)

        FrameDetails=Frame(CustomerDetailsFrame, width=800,height=300,bd=10, relief=RIDGE)
        FrameDetails.pack(side=LEFT,fill=BOTH,expand=True)

        CustomerName=LabelFrame(FrameDetails, width=150,height=250,bd=10, font=('arial',12,'bold'),text="Customer Info", relief=RIDGE)
        CustomerName.grid(row=0,column=0)

        TravelFrame = LabelFrame(FrameDetails,bd=10, width=300,height=250, font=('arial',12,'bold'),text="Booking Detail", relief=RIDGE)
        TravelFrame.grid(row=0,column=1)

        Book_Frame=LabelFrame(FrameDetails,width=300,height=150,relief=FLAT)
        Book_Frame.grid(row=1,column=0)

        CostFrame = LabelFrame(FrameDetails,width=150,height=150,bd=5,relief=FLAT)
        CostFrame.grid(row=1,column=1)


    #===============================================recipt======================================================================
        Receipt_BottonFrame=LabelFrame(CustomerDetailsFrame,bd=10, width=450,height=400, relief=RIDGE)
        Receipt_BottonFrame.pack(side=RIGHT,fill=BOTH,expand=True)

        ReceiptFrame=LabelFrame(Receipt_BottonFrame, width=350,height=300, font=('arial',12,'bold'),text="Receipt", relief=RIDGE)
        ReceiptFrame.grid(row=0,column=0)

        ButtonFrame=LabelFrame(Receipt_BottonFrame, width=350,height=100, relief=RIDGE)
        ButtonFrame.grid(row=1,column=0)
    #=========================================================CustomerName====================================================

        self.lblFirstname=Label(CustomerName,font=('arial',14,'bold'),text="Firstname",bd=7)
        self.lblFirstname.grid(row=0,column=0,sticky=W)
        self.txtFirstname=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Firstname,bd=7,insertwidth=2,justify=RIGHT)
        self.txtFirstname.grid(row=0,column=1)


        self.lblSurname=Label(CustomerName,font=('arial',14,'bold'),text="Surname",bd=7)
        self.lblSurname.grid(row=1,column=0,sticky=W)
        self.txtSurname=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Surname,bd=7,insertwidth=2,justify=RIGHT)
        self.txtSurname.grid(row=1,column=1,sticky=W)


        self.lblAddress=Label(CustomerName,font=('arial',14,'bold'),text="Address",bd=7)
        self.lblAddress.grid(row=2,column=0,sticky=W)
        self.txtAddress=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Address,bd=7,insertwidth=2,justify=RIGHT)
        self.txtAddress.grid(row=2,column=1)


        self.lblPostcode=Label(CustomerName,font=('arial',14,'bold'),text="Postcode",bd=7)
        self.lblPostcode.grid(row=3,column=0,sticky=W)
        self.txtPostcode=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Postcode,bd=7,insertwidth=2,justify=RIGHT)
        self.txtPostcode.grid(row=3,column=1)


        self.lblTelephone=Label(CustomerName,font=('arial',14,'bold'),text="Telephone",bd=7)
        self.lblTelephone.grid(row=4,column=0,sticky=W)
        self.txtTelephone=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Telephone,bd=7,insertwidth=2,justify=RIGHT)
        self.txtTelephone.grid(row=4,column=1)

        self.lblMobile=Label(CustomerName,font=('arial',14,'bold'),text="Mobile",bd=7)
        self.lblMobile.grid(row=5,column=0,sticky=W)
        self.txtMobile=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Mobile,bd=7,insertwidth=2,justify=RIGHT)
        self.txtMobile.grid(row=5,column=1)

        self.lblEmail=Label(CustomerName,font=('arial',14,'bold'),text="Email",bd=7)
        self.lblEmail.grid(row=6,column=0,sticky=W)
        self.txtEmail=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Email,bd=7,insertwidth=2,justify=RIGHT)
        self.txtEmail.grid(row=6,column=1)

 
    #===============================================Cab Information==============================================================
        self.lblPickup=Label(TravelFrame,font=('arial',14,'bold'),text="Pickup",bd=7)
        self.lblPickup.grid(row=0,column=0,sticky=W)

        self.cboPickup =ttk.Combobox(TravelFrame, textvariable = varl1 , state='readonly', font=('arial',20,'bold'), width=14)
        self.cboPickup['value']=('','VIP road','Park street','Salt Lake','New Town')
        self.cboPickup.current(0)
        self.cboPickup.grid(row=0,column=1)


        self.lblDrop=Label(TravelFrame,font=('arial',14,'bold'),text="Drop",bd=7)
        self.lblDrop.grid(row=1,column=0,sticky=W)

        self.cboDrop =ttk.Combobox(TravelFrame, textvariable = varl2 , state='readonly', font=('arial',20,'bold'), width=14)
        self.cboDrop['value']=('','VIP road','Park street','Salt Lake','New Town')
        self.cboDrop.current(0)
        self.cboDrop.grid(row=1,column=1)

        self.lblPooling=Label(TravelFrame,font=('arial',14,'bold'),text="Pooling",bd=7)
        self.lblPooling.grid(row=2,column=0,sticky=W)

        self.cboPooling =ttk.Combobox(TravelFrame, textvariable = varl3 , state='readonly', font=('arial',20,'bold'), width=14)
        self.cboPooling['value']=('','1','2','3','4')
        self.cboPooling.current(1)
        self.cboPooling.grid(row=2,column=1)

    #===============================================Cab Information==============================================================

        self.chkCabTax=Checkbutton(TravelFrame,text="Base Charge *",variable = var1, onvalue=1, offvalue=0,font=('arial',16,'bold'),command=Cab_Tax).grid(row=3, column=0, sticky=W)
        self.txtCabTax=Label(TravelFrame,font=('arial',14,'bold'),textvariable=CabTax,bd=6,width=18,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN)
        self.txtCabTax.grid(row=3,column=1)


        self.chkKm=Checkbutton(TravelFrame,text="Distance(KMs) *",variable = var2, onvalue=1, offvalue=0,font=('arial',16,'bold'),command=Kilo).grid(row=4, column=0, sticky=W)
        self.txtKm=Label(TravelFrame,font=('arial',14,'bold'),textvariable=Km,bd=6,width=18,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN,highlightthickness=0)
        self.txtKm.grid(row=4,column=1)

        self.chkTravel_Ins=Checkbutton(TravelFrame,text="Travelling Insurance *",variable = var3, onvalue=1, offvalue=0,font=('arial',16,'bold'),command=Travelling).grid(row=5, column=0, sticky=W)
        self.txtTravel_Ins=Label(TravelFrame,font=('arial',14,'bold'),textvariable=Travel_Ins,bd=6,width=18,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN)
        self.txtTravel_Ins.grid(row=5,column=1)

      
        self.chkLuggage=Checkbutton(TravelFrame,text="Extra Luggage",variable = var4, onvalue=1, offvalue=0,font=('arial',16,'bold'),command=Lug).grid(row=6, column=0, sticky=W)
        self.txtLuggage=Label(TravelFrame,font=('arial',14,'bold'),textvariable=Luggage,bd=6,width=18,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN)
        self.txtLuggage.grid(row=6,column=1)
    
    #=================================payment information ===========================================================================
         
        self.lblPaidTax=Label(CostFrame,font=('arial',14,'bold'),text="Paid Tax\t\t",bd=7)
        self.lblPaidTax.grid(row=0,column=2,sticky=W)
        self.txtPaidTax = Label(CostFrame,font=('arial',14,'bold'),textvariable=PaidTax,bd=7, width=10, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtPaidTax.grid(row=0,column=3)
            

        
        self.lblSubTotal=Label(CostFrame,font=('arial',14,'bold'),text="Sub Total",bd=7)
        self.lblSubTotal.grid(row=1,column=2,sticky=W)
        self.txtSubTotal = Label(CostFrame,font=('arial',14,'bold'),textvariable=SubTotal,bd=7, width=10, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtSubTotal.grid(row=1,column=3)



        self.lblTotalCost=Label(CostFrame,font=('arial',14,'bold'),text="Total Cost",bd=7)
        self.lblTotalCost.grid(row=2,column=2,sticky=W)
        self.txtTotalCost = Label(CostFrame,font=('arial',14,'bold'),textvariable=TotalCost,bd=7, width=10, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtTotalCost.grid(row=2,column=3)

    #==========================================================Cabselect=======================================================================

        self.chkStandard=Radiobutton(Book_Frame,text="Maruti Van",value=1,variable = carType,font=('arial',14,'bold'),command=selectCar).grid(row=0, column=0, sticky=W)
        self.txtStandard = Label(Book_Frame,font=('arial',14,'bold'),width =7,textvariable=Standard,bd=5, state= DISABLED, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtStandard.grid(row=0,column=1)
        

        self.chkFordGalaxyd=Radiobutton(Book_Frame,text="Scropio",value=2,variable = carType,font=('arial',14,'bold'),command=selectCar).grid(row=1, column=0, sticky=W)
        self.txtFordGalaxy= Label(Book_Frame,font=('arial',14,'bold'),width =7,textvariable=FordGalaxy,bd=5, state= DISABLED, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtFordGalaxy.grid(row=1,column=1)
             
       
        self.chkFordMondeo = Radiobutton(Book_Frame,text="Inova",value=3,variable = carType,font=('arial',14,'bold'),command=selectCar).grid(row=2, column=0, sticky=W)
        self.txtFordMondeo = Label(Book_Frame,font=('arial',14,'bold'),width =7,textvariable=FordMondeo,bd=5, state= DISABLED, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtFordMondeo.grid(row=2,column=1)

        self.chkSingle =Radiobutton(Book_Frame,text="Single",value=1,variable = journeyType,font=('arial',14,'bold')).grid(row=0, column=2, sticky=W)
        self.chkReturn =Radiobutton(Book_Frame,text="Return",value=2,variable = journeyType,font=('arial',14,'bold')).grid(row=1, column=2, sticky=W)
        self.chkSpecialsNeeds =Radiobutton(Book_Frame,text="SpecialNeeds",value=3,variable = journeyType,font=('arial',14,'bold')).grid(row=2, column=2, sticky=W)
    
    
    #=======================================Receipt====================================================================================

        self.txtReceipt1 = Text(ReceiptFrame,width = 22, height = 21,font=('arial',10,'bold'),borderwidth=0)
        self.txtReceipt1.grid(row=0,column=0,columnspan=2)
        self.txtReceipt2 = Text(ReceiptFrame,width = 22, height = 21,font=('arial',10,'bold'),borderwidth=0)
        self.txtReceipt2.grid(row=0,column=2,columnspan=2)


    #======================================Button========================================================================================
        
        self.btnTotal = Button(ButtonFrame,padx=18,bd=7,font=('arial',11,'bold'),width = 2,text='Total',command=Total_Paid).grid(row=0,column=0)
        self.btnReceipt = Button(ButtonFrame,padx=18,bd=7,font=('arial',11,'bold'),width = 2,text='Receipt',command=Receiptt).grid(row=0,column=1)
        self.btnReset = Button(ButtonFrame,padx=18,bd=7,font=('arial',11,'bold'),width = 2,text='Reset',command=Reset).grid(row=0,column=2)
        self.btnExit = Button(ButtonFrame,padx=18,bd=7,font=('arial',11,'bold'),width = 2,text='Exit', command=root.quit).grid(row=0,column=3)
        
    #====================================================================================================================================
class flight:

    def __init__(self,root):
        self.root = root
        
        DateofOrder=StringVar()
        DateofOrder.set(time.strftime(" %d / %m / %Y "))
        Receipt_Ref=StringVar()
        PaidTax=StringVar()
        SubTotal=StringVar()
        TotalCost=StringVar()

        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        travelType=IntVar()
        
        
        varl1=StringVar()
        varl2=StringVar()
        varl3=StringVar()
        reset_counter=0

        Firstname=StringVar()
        Surname=StringVar()
        Address=StringVar()
        Postcode=StringVar()
        Mobile=StringVar()
        Telephone=StringVar()
        Email=StringVar()

        
        Km=StringVar()
        Travel_Ins=StringVar()
        Luggage=StringVar()
        Receipt=StringVar()


        st_class=StringVar()
        nd_class=StringVar()
        economy_class=StringVar()

        Km.set("0")
        Travel_Ins.set("0")
        Luggage.set("0")


        st_class.set("0")
        nd_class.set("0")
        economy_class.set("0")
#==========================================Define Functiom==================================================

        def Reset():
            Km.set("0")
            Travel_Ins.set("0")
            Luggage.set("0")
            
            st_class.set("0")
            nd_class.set("0")
            economy_class.set("0")

            Firstname.set("")
            Surname.set("")
            Address.set("")
            Postcode.set("")
            Mobile.set("")
            Telephone.set("")
            Email.set("")

            PaidTax.set("")
            SubTotal.set("")
            TotalCost.set("")
            self.txtReceipt1.delete("1.0",END)
            self.txtReceipt2.delete("1.0",END)
            
            var2.set(0)
            var3.set(0)
            var4.set(0)
            travelType.set(0)
            varl1.set("0")
            varl2.set("0")
            varl3.set("0")

            self.cboPickup.current(0)
            self.cboDrop.current(0)

            self.txtKm.configure(state=DISABLED)
            self.txtTravel_Ins.configure(state=DISABLED)
            self.txtLuggage.configure(state=DISABLED)
        
            self.txtst_class.configure(state=DISABLED)
            self.txtnd_class.configure(state=DISABLED)
            self.txteconomy_class.configure(state=DISABLED)
            self.reset_counter=1

        def Receiptt():
            if reset_counter == 0 and Firstname.get()!="" and Surname.get()!="" and Address.get()!="" and Postcode.get()!="" and Mobile.get()!="" and Telephone.get()!="" and Email.get()!="":
                self.txtReceipt1.delete("1.0",END)
                self.txtReceipt2.delete("1.0",END)
                x=random.randint(10853,500831)
                randomRef = str(x)
                Receipt_Ref.set(randomRef)

                self.txtReceipt1.insert(END,"Receipt Ref:\n")
                self.txtReceipt2.insert(END, Receipt_Ref.get() + "\n")
                self.txtReceipt1.insert(END,'Date:\n')
                self.txtReceipt2.insert(END, DateofOrder.get() + "\n")
                self.txtReceipt1.insert(END,'Train No:\n')
                self.txtReceipt2.insert(END, 'TR ' + Receipt_Ref.get() + " BW\n")
                self.txtReceipt1.insert(END,'Firstname:\n')
                self.txtReceipt2.insert(END, Firstname.get() + "\n")
                self.txtReceipt1.insert(END,'Surname:\n')
                self.txtReceipt2.insert(END, Surname.get() + "\n")
                self.txtReceipt1.insert(END,'Address:\n')
                self.txtReceipt2.insert(END, Address.get() + "\n")
                self.txtReceipt1.insert(END,'Postal Code:\n')
                self.txtReceipt2.insert(END, Postcode.get() + "\n")
                self.txtReceipt1.insert(END,'Telephone:\n')
                self.txtReceipt2.insert(END, Telephone.get() + "\n")
                self.txtReceipt1.insert(END,'Mobile:\n')
                self.txtReceipt2.insert(END, Mobile.get() + "\n")
                self.txtReceipt1.insert(END,'Email:\n')
                self.txtReceipt2.insert(END, Email.get() + "\n")
                self.txtReceipt1.insert(END,'From:\n')
                self.txtReceipt2.insert(END, varl1.get() + "\n")
                self.txtReceipt1.insert(END,'To:\n')
                self.txtReceipt2.insert(END, varl2.get() + "\n")
                self.txtReceipt1.insert(END,'1st Class:\n')
                self.txtReceipt2.insert(END, st_class.get() + "\n")
                self.txtReceipt1.insert(END,'2nd Class:\n')
                self.txtReceipt2.insert(END, nd_class.get() + "\n")
                self.txtReceipt1.insert(END,'Economy Class:\n')
                self.txtReceipt2.insert(END, economy_class.get() + "\n")
                self.txtReceipt1.insert(END,'Total Cost:\n')
                self.txtReceipt2.insert(END, str(TotalCost.get()))
                
            else:
                self.txtReceipt1.delete("1.0",END)
                self.txtReceipt2.delete("1.0",END)
                self.txtReceipt1.insert(END,"\nNo Input")
                

        

        
        def Kilo():
            if var2.get() == 0:
                self.txtKm.configure(state=DISABLED)
                Km.set("0")
            elif var2.get() == 1 and varl1.get() != "" and varl2.get() != "":
                self.txtKm.configure(state=NORMAL)
                if varl1.get() == "Kolkata":
                    switch ={"Chennai": 20,"Delhi": 15,"Mumbai":10,"Kolkata ": 0}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "Mumbai":
                    switch ={"Kolkata": 10,"Delhi": 10,"Chennai":25,"Mumbai": 0}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "Delhi":
                    switch ={"Kolkata": 15,"Mumbai": 15,"Chennai":10,"Delhi": 0}
                elif varl1.get() == "Chennai":
                    switch ={"Delhi": 20,"Mumbai": 25,"Kolkata":20,"Chennai": 0}
                    Km.set(switch[varl2.get()])        

        
        def Travelling():
            global Item3
            if var3.get() == 1:
                self.txtTravel_Ins.configure(state = NORMAL)
                Item3=float(300)
                Travel_Ins.set("Rs " + str(Item3))
            else:
                self.txtTravel_Ins.configure(state = DISABLED)
                Travel_Ins.set("0")
                Item3=float(0)

        
        def Lug():
            global Item4
            if (var4.get()==1):
                self.txtLuggage.configure(state = NORMAL)
                Item4=float(800)
                Luggage.set("Rs "+ str(Item4))
            else:
                self.txtLuggage.configure(state = DISABLED)
                Luggage.set("0")
                Item4=float(0)
         
        def selectCar():
            global Item5
            if travelType.get() == 1:
                self.txteconomy_class.configure(state = DISABLED)
                economy_class.set("0")
                self.txtnd_class.configure(state = DISABLED)
                nd_class.set("0")
                self.txtst_class.configure(state = NORMAL)
                Item5 = float(300)
                st_class.set("Rs "+ str(Item5))
            
            elif travelType.get() == 2:
                self.txtst_class.configure(state =DISABLED)
                st_class.set("0")
                self.txteconomy_class.configure(state =DISABLED)
                economy_class.set("0")
                self.txtnd_class.configure(state = NORMAL)
                Item5 = float(200)
                nd_class.set("Rs "+ str(Item5))
            else:
                self.txtnd_class.configure(state =DISABLED)
                nd_class.set("0")
                self.txtst_class.configure(state =DISABLED)
                st_class.set("0")
                self.txteconomy_class.configure(state = NORMAL)
                Item5 = float(100)
                economy_class.set("Rs "+ str(Item5))
        
                       
        def Total_Paid():
            if ((var2.get()==1 and var3.get() == 1 or var4.get() == 1) and travelType.get() != 0 and (varl1.get() != "" and varl2.get() !="")):
                if travelType.get()==1:
                    Item2=Km.get()
                    Cost_of_fare = ((float(Item2)*Item5)+Item3+Item4)
                    TT = "Rs " + str('%.2f'%(Cost_of_fare))
                if travelType.get()==2:
                    Item2=Km.get()
                    Cost_of_fare = ((float(Item2)*Item5)+Item3+Item4)
                    TT = "Rs " + str('%.2f'%(Cost_of_fare))
                if travelType.get()==3:
                    Item2=Km.get()
                    Cost_of_fare = ((float(Item2)*Item5)+Item3+Item4)
                    TT = "Rs " + str('%.2f'%(Cost_of_fare))
                TotalCost.set(TT)
            else:
                w = ms.showwarning("Error !","Invalid Input\nPlease try again !!!")
   #================================================mainframe========================================================================

        MainFrame=Frame(self.root)
        MainFrame.pack(fill=X,expand=True)
        
        Tops = Frame(MainFrame, bd=10, width=1350,relief=RIDGE)
        Tops.pack(side=TOP,fill=BOTH)

        self.lblTitle=Label(Tops,font=('arial',20,'bold'),text="\t                               Flight Booking System ")
        self.lblTitle.grid()

    #================================================customerframedetail=============================================================
        CustomerDetailsFrame=LabelFrame(MainFrame, width=1000,height=300,bd=20, pady=5, relief=RIDGE)
        CustomerDetailsFrame.pack(side=BOTTOM,fill=BOTH,expand=True)

        FrameDetails=Frame(CustomerDetailsFrame, width=880,height=300,bd=10, relief=RIDGE)
        FrameDetails.pack(side=LEFT,fill=BOTH,expand=True)

        CustomerName=LabelFrame(FrameDetails, width=150,height=250,bd=10, font=('arial',12,'bold'),text="Customer Info", relief=RIDGE)
        CustomerName.grid(row=0,column=0)

        TravelFrame = LabelFrame(FrameDetails,bd=10, width=300,height=250, font=('arial',12,'bold'),text="Booking Detail", relief=RIDGE)
        TravelFrame.grid(row=0,column=1)

        Book_Frame=LabelFrame(FrameDetails,width=300,height=150,relief=FLAT)
        Book_Frame.grid(row=1,column=0)

        CostFrame = LabelFrame(FrameDetails,width=150,height=150,bd=5,relief=FLAT)
        CostFrame.grid(row=1,column=1)


    #===============================================recipt======================================================================
        Receipt_BottonFrame=LabelFrame(CustomerDetailsFrame,bd=10, width=450,height=400, relief=RIDGE)
        Receipt_BottonFrame.pack(side=RIGHT,fill=BOTH,expand=True)

        ReceiptFrame=LabelFrame(Receipt_BottonFrame, width=350,height=300, font=('arial',12,'bold'),text="Receipt", relief=RIDGE)
        ReceiptFrame.grid(row=0,column=0)

        ButtonFrame=LabelFrame(Receipt_BottonFrame, width=350,height=100, relief=RIDGE)
        ButtonFrame.grid(row=1,column=0)
    #=========================================================CustomerName====================================================

        self.lblFirstname=Label(CustomerName,font=('arial',14,'bold'),text="Firstname",bd=7)
        self.lblFirstname.grid(row=0,column=0,sticky=W)
        self.txtFirstname=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Firstname,bd=7,insertwidth=2,justify=RIGHT)
        self.txtFirstname.grid(row=0,column=1)


        self.lblSurname=Label(CustomerName,font=('arial',14,'bold'),text="Surname",bd=7)
        self.lblSurname.grid(row=1,column=0,sticky=W)
        self.txtSurname=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Surname,bd=7,insertwidth=2,justify=RIGHT)
        self.txtSurname.grid(row=1,column=1,sticky=W)


        self.lblAddress=Label(CustomerName,font=('arial',14,'bold'),text="Address",bd=7)
        self.lblAddress.grid(row=2,column=0,sticky=W)
        self.txtAddress=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Address,bd=7,insertwidth=2,justify=RIGHT)
        self.txtAddress.grid(row=2,column=1)


        self.lblPostcode=Label(CustomerName,font=('arial',14,'bold'),text="Postcode",bd=7)
        self.lblPostcode.grid(row=3,column=0,sticky=W)
        self.txtPostcode=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Postcode,bd=7,insertwidth=2,justify=RIGHT)
        self.txtPostcode.grid(row=3,column=1)


        self.lblTelephone=Label(CustomerName,font=('arial',14,'bold'),text="Telephone",bd=7)
        self.lblTelephone.grid(row=4,column=0,sticky=W)
        self.txtTelephone=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Telephone,bd=7,insertwidth=2,justify=RIGHT)
        self.txtTelephone.grid(row=4,column=1)

        self.lblMobile=Label(CustomerName,font=('arial',14,'bold'),text="Mobile",bd=7)
        self.lblMobile.grid(row=5,column=0,sticky=W)
        self.txtMobile=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Mobile,bd=7,insertwidth=2,justify=RIGHT)
        self.txtMobile.grid(row=5,column=1)

        self.lblEmail=Label(CustomerName,font=('arial',14,'bold'),text="Email",bd=7)
        self.lblEmail.grid(row=6,column=0,sticky=W)
        self.txtEmail=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Email,bd=7,insertwidth=2,justify=RIGHT)
        self.txtEmail.grid(row=6,column=1)

 
    #===============================================Flight Information==============================================================
        self.lblPickup=Label(TravelFrame,font=('arial',14,'bold'),text="Departure",bd=7)
        self.lblPickup.grid(row=0,column=0,sticky=W)

        self.cboPickup =ttk.Combobox(TravelFrame, textvariable = varl1 , state='readonly', font=('arial',20,'bold'), width=14)
        self.cboPickup['value']=('','Kolkata','Mumbai','Delhi','Chennai')
        self.cboPickup.current(0)
        self.cboPickup.grid(row=0,column=1)


        self.lblDrop=Label(TravelFrame,font=('arial',14,'bold'),text="Destination",bd=7)
        self.lblDrop.grid(row=1,column=0,sticky=W)

        self.cboDrop =ttk.Combobox(TravelFrame, textvariable = varl2 , state='readonly', font=('arial',20,'bold'), width=14)
        self.cboDrop['value']=('','Kolkata','Mumbai','Delhi','Chennai')
        self.cboDrop.current(0)
        self.cboDrop.grid(row=1,column=1)

        

    #===============================================Flight Information==============================================================


        self.chkKm=Checkbutton(TravelFrame,text="Distance(KMs) *",variable = var2, onvalue=1, offvalue=0,font=('arial',16,'bold'),command=Kilo).grid(row=4, column=0, sticky=W)
        self.txtKm=Label(TravelFrame,font=('arial',14,'bold'),textvariable=Km,bd=6,width=18,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN,highlightthickness=0)
        self.txtKm.grid(row=4,column=1)

        self.chkTravel_Ins=Checkbutton(TravelFrame,text="Travelling Insurance *",variable = var3, onvalue=1, offvalue=0,font=('arial',16,'bold'),command=Travelling).grid(row=5, column=0, sticky=W)
        self.txtTravel_Ins=Label(TravelFrame,font=('arial',14,'bold'),textvariable=Travel_Ins,bd=6,width=18,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN)
        self.txtTravel_Ins.grid(row=5,column=1)

      
        self.chkLuggage=Checkbutton(TravelFrame,text="Extra Luggage",variable = var4, onvalue=1, offvalue=0,font=('arial',16,'bold'),command=Lug).grid(row=6, column=0, sticky=W)
        self.txtLuggage=Label(TravelFrame,font=('arial',14,'bold'),textvariable=Luggage,bd=6,width=18,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN)
        self.txtLuggage.grid(row=6,column=1)
    
    #=================================Payment information ===========================================================================
         

        self.lblTotalCost=Label(CostFrame,font=('arial',14,'bold'),text="Total Cost",bd=7)
        self.lblTotalCost.grid(row=2,column=2,sticky=W)
        self.txtTotalCost = Label(CostFrame,font=('arial',14,'bold'),textvariable=TotalCost,bd=7, width=10, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtTotalCost.grid(row=2,column=3)

    #==========================================================Flight select=======================================================================

        self.chkst_class=Radiobutton(Book_Frame,text="1st Class",value=1,variable = travelType,font=('arial',14,'bold'),command=selectCar).grid(row=0, column=0, sticky=W)
        self.txtst_class = Label(Book_Frame,font=('arial',14,'bold'),width =7,textvariable=st_class,bd=5, state= DISABLED, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtst_class.grid(row=0,column=1)
    
       
        self.chknd_class = Radiobutton(Book_Frame,text="2nd Class",value=2,variable = travelType,font=('arial',14,'bold'),command=selectCar).grid(row=1, column=0, sticky=W)
        self.txtnd_class = Label(Book_Frame,font=('arial',14,'bold'),width =7,textvariable=nd_class,bd=5, state= DISABLED, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtnd_class.grid(row=1,column=1)

        
        self.chkeconomy_class = Radiobutton(Book_Frame,text="Economy Class",value=3,variable = travelType,font=('arial',14,'bold'),command=selectCar).grid(row=2, column=0, sticky=W)
        self.txteconomy_class = Label(Book_Frame,font=('arial',14,'bold'),width =7,textvariable=economy_class,bd=5, state= DISABLED, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txteconomy_class.grid(row=2,column=1)

    #=======================================Receipt====================================================================================

        self.txtReceipt1 = Text(ReceiptFrame,width = 22, height = 21,font=('arial',10,'bold'),borderwidth=0)
        self.txtReceipt1.grid(row=0,column=0,columnspan=2)
        self.txtReceipt2 = Text(ReceiptFrame,width = 22, height = 21,font=('arial',10,'bold'),borderwidth=0)
        self.txtReceipt2.grid(row=0,column=2,columnspan=2)


    #======================================Button========================================================================================
        
        self.btnTotal = Button(ButtonFrame,padx=10,bd=5,font=('arial',7,'bold'),width = 2,text='Total',command=Total_Paid).grid(row=0,column=0)
        self.btnReceipt = Button(ButtonFrame,padx=10,bd=5,font=('arial',7,'bold'),width = 2,text='Receipt',command=Receiptt).grid(row=0,column=1)
        self.btnReset = Button(ButtonFrame,padx=10,bd=5,font=('arial',7,'bold'),width = 2,text='Reset',command=Reset).grid(row=0,column=2)
        self.btnExit = Button(ButtonFrame,padx=10,bd=5,font=('arial',7,'bold'),width = 2,text='Exit', command=root.quit).grid(row=0,column=3)
        
    #====================================================================================================================================
class hotel:
    def __init__(self,root):
        self.root = root

        DateofOrder=StringVar()
        DateofOrder.set(time.strftime(" %d / %m / %Y "))
        Receipt_Ref=StringVar()
        PaidTax=StringVar()
        SubTotal=StringVar()
        TotalCost=StringVar()

        
        var1=IntVar()
        var4=IntVar()
        roomType=IntVar()
        bedType=IntVar()
        
        varl1=StringVar()
        varl2=StringVar()
        varl3=StringVar()
        reset_counter=0

        Firstname=StringVar()
        Surname=StringVar()
        Address=StringVar()
        Postcode=StringVar()
        Mobile=StringVar()
        Telephone=StringVar()
        Email=StringVar()

        
        day=IntVar()
        food=StringVar()
        Receipt=StringVar()
        total=StringVar()

        room_service=IntVar()
        s_bed=StringVar()
        d_bed=StringVar()
        normal=StringVar()
        ac=StringVar()
        
        day.set("0")
        food.set("0")
        var1.set(0)
        var4.set(0)

        s_bed.set("0")
        d_bed.set("0")
        normal.set("0")
        ac.set("0")

#==========================================Define Functiom==================================================
                            
        def Reset():
            total.set("0")

            Firstname.set("")
            Surname.set("")
            Address.set("")
            Postcode.set("")
            Mobile.set("")
            Telephone.set("")
            Email.set("")
            
            PaidTax.set("")
            self.txtReceipt1.delete("1.0",END)
            self.txtReceipt2.delete("1.0",END)
            
            day.set(0)
            food.set(0)
            total.set(0)
            var1.set(0)
            var4.set(0)

            s_bed.set(0)
            d_bed.set(0)
            normal.set(0)
            ac.set(0)
            TotalCost.set(0)
            room_service.set(0) 
            s_bed.set("0")
            d_bed.set("0")
            normal.set("0")
            ac.set("0")
            TotalCost.set("0")
            room_service.set("0") 
            self.txtroom_service.configure(state=DISABLED)
            self.txtfood.configure(state=DISABLED)
            self.txts_bed.configure(state=DISABLED)
            self.txtd_bed.configure(state=DISABLED)
            self.txtnormal.configure(state=DISABLED)
            self.txtac.configure(state=DISABLED)
            
            self.reset_counter=1
            
        def Receiptt():
            if reset_counter == 0 and Firstname.get()!="" and Surname.get()!="" and Address.get()!="" and Postcode.get()!="" and Mobile.get()!="" and Telephone.get()!="" and Email.get()!="":
                self.txtReceipt1.delete("1.0",END)
                self.txtReceipt2.delete("1.0",END)
                x=random.randint(10853,500831)
                randomRef = str(x)
                Receipt_Ref.set(randomRef)

                self.txtReceipt1.insert(END,"Receipt Ref:\n")
                self.txtReceipt2.insert(END, Receipt_Ref.get() + "\n")
                self.txtReceipt1.insert(END,'Date:\n')
                self.txtReceipt2.insert(END, DateofOrder.get() + "\n")
                self.txtReceipt1.insert(END,'Firstname:\n')
                self.txtReceipt2.insert(END, Firstname.get() + "\n")
                self.txtReceipt1.insert(END,'Surname:\n')
                self.txtReceipt2.insert(END, Surname.get() + "\n")
                self.txtReceipt1.insert(END,'Address:\n')
                self.txtReceipt2.insert(END, Address.get() + "\n")
                self.txtReceipt1.insert(END,'Postal Code:\n')
                self.txtReceipt2.insert(END, Postcode.get() + "\n")
                self.txtReceipt1.insert(END,'Telephone:\n')
                self.txtReceipt2.insert(END, Telephone.get() + "\n")
                self.txtReceipt1.insert(END,'Mobile:\n')
                self.txtReceipt2.insert(END, Mobile.get() + "\n")
                self.txtReceipt1.insert(END,'Email:\n')
                self.txtReceipt2.insert(END, Email.get() + "\n")
                self.txtReceipt1.insert(END,'Total Cost:\n')
                self.txtReceipt2.insert(END, str(TotalCost.get()))
                
            else:
                self.txtReceipt1.delete("1.0",END)
                self.txtReceipt2.delete("1.0",END)
                self.txtReceipt1.insert(END,"\nNo Input")
                
        
                
        def R_Service():
            global Item3
            if var4.get()==1:
                self.txtroom_service.configure(state= NORMAL)
                Item3=float(100)
                room_service.set("Rs "+ str(Item3)) 
            else:
                self.txtroom_service.configure(state = DISABLED)
                room_service.set("0")
                Item3=float(0)
                
                
        def selectBed():
            global Item4
            if bedType.get() == 1:
                self.txts_bed.configure(state = DISABLED)
                s_bed.set("0") 
                self.txtd_bed.configure(state = NORMAL)
                Item4 = float(100)
                d_bed.set("Rs "+ str(Item4))
            
            else:
                self.txtd_bed.configure(state =DISABLED)
                d_bed.set("0")
                self.txts_bed.configure(state = NORMAL)
                Item4 = float(50)
                s_bed.set("Rs "+ str(Item4))
                
        def selectRoom():
            global Item5
            if roomType.get() == 1:
                self.txtac.configure(state = DISABLED)
                ac.set("0") 
                self.txtnormal.configure(state = NORMAL)
                Item5 = float(200)
                normal.set("Rs "+ str(Item5))
            
            else:
                self.txtnormal.configure(state =DISABLED)
                normal.set("0")
                self.txtac.configure(state = NORMAL)
                Item5 = float(300)
                ac.set("Rs "+ str(Item5))
                
        def Food():
            global Item1
            if var1.get()==1:
                self.txtfood.configure(state = NORMAL)
                Item1=float(70)
                food.set("Rs "+ str(Item1))
            else:
                self.txtfood.configure(state = DISABLED)
                Item1=float(0)
                food.set("Rs "+ str(Item1))
                
        def Total_Paid():
            if (roomType.get() != 0 and bedType.get != 0 and var4.get != 0 or var1.get != 0):
                Cost_of_fare=((Item5+Item4)*day.get()+ Item3+Item1)
                TT = "Rs " + str('%.2f'%(Cost_of_fare))
                TotalCost.set(TT)
            else:
                w = ms.showwarning("Error !","Invalid Input\nPlease try again !!!")

 #================================================mainframe========================================================================

        MainFrame=Frame(self.root)
        MainFrame.pack(fill=BOTH,expand=True)
        
        Tops = Frame(MainFrame, bd=10, width=700,relief=RIDGE)
        Tops.pack(side=TOP,fill=BOTH)

        self.lblTitle=Label(Tops,font=('arial',20,'bold'),text="\t                           Hotel Booking System ")
        self.lblTitle.grid()
    #================================================customerframedetail=============================================================
        CustomerDetailsFrame=LabelFrame(MainFrame, width=700,height=300,bd=20, pady=5, relief=RIDGE)
        CustomerDetailsFrame.pack(side=BOTTOM,fill=BOTH,expand=True)

        FrameDetails=Frame(CustomerDetailsFrame, width=500,height=300,bd=10, relief=RIDGE)
        FrameDetails.pack(side=LEFT,fill=BOTH,expand=True)

        CustomerName=LabelFrame(FrameDetails, width=150,height=250,bd=10, font=('arial',12,'bold'),text="Customer Info", relief=RIDGE)
        CustomerName.grid(row=0,column=0)

        TravelFrame = LabelFrame(FrameDetails,bd=10, width=300,height=250, font=('arial',12,'bold'),text="Booking Detail", relief=RIDGE)
        TravelFrame.grid(row=0,column=1)

        Book_Frame=LabelFrame(FrameDetails,width=300,height=150,relief=FLAT)
        Book_Frame.grid(row=1,column=0)

        CostFrame = LabelFrame(FrameDetails,width=150,height=150,bd=5,relief=FLAT)
        CostFrame.grid(row=1,column=1)

    #===============================================recipt======================================================================
        Receipt_BottonFrame=LabelFrame(CustomerDetailsFrame,bd=10, width=450,height=400, relief=RIDGE)
        Receipt_BottonFrame.pack(side=RIGHT,fill=BOTH,expand=True)

        ReceiptFrame=LabelFrame(Receipt_BottonFrame, width=350,height=300, font=('arial',12,'bold'),text="Receipt", relief=RIDGE)
        ReceiptFrame.grid(row=0,column=0)

        ButtonFrame=LabelFrame(Receipt_BottonFrame, width=350,height=100, relief=RIDGE)
        ButtonFrame.grid(row=1,column=0)
    #=========================================================CustomerName====================================================

        self.lblFirstname=Label(CustomerName,font=('arial',14,'bold'),text="Firstname",bd=7)
        self.lblFirstname.grid(row=0,column=0,sticky=W)
        self.txtFirstname=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Firstname,bd=7,insertwidth=2,justify=RIGHT)
        self.txtFirstname.grid(row=0,column=1)


        self.lblSurname=Label(CustomerName,font=('arial',14,'bold'),text="Surname",bd=7)
        self.lblSurname.grid(row=1,column=0,sticky=W)
        self.txtSurname=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Surname,bd=7,insertwidth=2,justify=RIGHT)
        self.txtSurname.grid(row=1,column=1,sticky=W)


        self.lblAddress=Label(CustomerName,font=('arial',14,'bold'),text="Address",bd=7)
        self.lblAddress.grid(row=2,column=0,sticky=W)
        self.txtAddress=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Address,bd=7,insertwidth=2,justify=RIGHT)
        self.txtAddress.grid(row=2,column=1)


        self.lblPostcode=Label(CustomerName,font=('arial',14,'bold'),text="Postcode",bd=7)
        self.lblPostcode.grid(row=3,column=0,sticky=W)
        self.txtPostcode=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Postcode,bd=7,insertwidth=2,justify=RIGHT)
        self.txtPostcode.grid(row=3,column=1)


        self.lblTelephone=Label(CustomerName,font=('arial',14,'bold'),text="Telephone",bd=7)
        self.lblTelephone.grid(row=4,column=0,sticky=W)
        self.txtTelephone=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Telephone,bd=7,insertwidth=2,justify=RIGHT)
        self.txtTelephone.grid(row=4,column=1)

        self.lblMobile=Label(CustomerName,font=('arial',14,'bold'),text="Mobile",bd=7)
        self.lblMobile.grid(row=5,column=0,sticky=W)
        self.txtMobile=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Mobile,bd=7,insertwidth=2,justify=RIGHT)
        self.txtMobile.grid(row=5,column=1)

        self.lblEmail=Label(CustomerName,font=('arial',14,'bold'),text="Email",bd=7)
        self.lblEmail.grid(row=6,column=0,sticky=W)
        self.txtEmail=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Email,bd=7,insertwidth=2,justify=RIGHT)
        self.txtEmail.grid(row=6,column=1)
        
    #===============================================Hotel Information==============================================================
        self.lblday=Label(TravelFrame,font=('arial',14,'bold'),text="Day",bd=7)
        self.lblday.grid(row=0,column=0,sticky=W)

        self.cboday =ttk.Combobox(TravelFrame, textvariable = day , state='readonly', font=('arial',20,'bold'), width=14)
        self.cboday['value']=('','1','2','3','4','5')
        self.cboday.current(0)
        self.cboday.grid(row=0,column=1)
        
        self.chkroom_service=Checkbutton(TravelFrame,text="Room Service ",variable = var4, onvalue=1, offvalue=0,font=('arial',16,'bold'),command=R_Service).grid(row=1, column=0, sticky=W)
        self.txtroom_service=Label(TravelFrame,font=('arial',14,'bold'),textvariable=room_service,bd=6,width=18,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN)
        self.txtroom_service.grid(row=1,column=1)
        
        self.chkfood=Checkbutton(TravelFrame,text="Food",variable = var1, onvalue=1, offvalue=0,font=('arial',16,'bold'),command=Food).grid(row=6, column=0, sticky=W)
        self.txtfood=Label(TravelFrame,font=('arial',14,'bold'),textvariable=food,bd=6,width=18,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN)
        self.txtfood.grid(row=6,column=1)

    
    #=================================payment information ===========================================================================
         

        self.lblTotalCost=Label(CostFrame,font=('arial',14,'bold'),text="Total Cost",bd=7)
        self.lblTotalCost.grid(row=2,column=2,sticky=W)
        self.txtTotalCost = Label(CostFrame,font=('arial',14,'bold'),textvariable=TotalCost,bd=7, width=10, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtTotalCost.grid(row=2,column=3)

    #==========================================================Room select=======================================================================

        self.chknormal=Radiobutton(Book_Frame,text="Normal-Room",value=1,variable = roomType,font=('arial',14,'bold'),command=selectRoom).grid(row=0, column=0, sticky=W)
        self.txtnormal = Label(Book_Frame,font=('arial',14,'bold'),width =7,textvariable=normal,bd=5, state= DISABLED, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtnormal.grid(row=0,column=1)
    
       
        self.chkac = Radiobutton(Book_Frame,text="AC-Room",value=2,variable = roomType,font=('arial',14,'bold'),command=selectRoom).grid(row=1, column=0, sticky=W)
        self.txtac = Label(Book_Frame,font=('arial',14,'bold'),width =7,textvariable=ac,bd=5, state= DISABLED, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtac.grid(row=1,column=1)
        
        self.chks_bed=Radiobutton(Book_Frame,text="Single Bed",value=2,variable = bedType,font=('arial',14,'bold'),command=selectBed).grid(row=0, column=2, sticky=W)
        self.txts_bed = Label(Book_Frame,font=('arial',14,'bold'),width =7,textvariable=s_bed,bd=5, state= DISABLED, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txts_bed.grid(row=0,column=3)
    
       
        self.chkd_bed = Radiobutton(Book_Frame,text="Double Bed",value=1,variable = bedType,font=('arial',14,'bold'),command=selectBed).grid(row=1, column=2, sticky=W)
        self.txtd_bed = Label(Book_Frame,font=('arial',14,'bold'),width =7,textvariable=d_bed,bd=5, state= DISABLED, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtd_bed.grid(row=1,column=3)
        
        
    #=======================================Receipt====================================================================================

        self.txtReceipt1 = Text(ReceiptFrame,width = 22, height = 21,font=('arial',10,'bold'),borderwidth=0)
        self.txtReceipt1.grid(row=0,column=0,columnspan=2)
        self.txtReceipt2 = Text(ReceiptFrame,width = 22, height = 21,font=('arial',10,'bold'),borderwidth=0)
        self.txtReceipt2.grid(row=0,column=2,columnspan=2)


    #======================================Button========================================================================================
        
        self.btnTotal = Button(ButtonFrame,padx=10,bd=7,font=('arial',7,'bold'),width = 2,text='Total',command=Total_Paid).grid(row=0,column=0)
        self.btnReceipt = Button(ButtonFrame,padx=10,bd=7,font=('arial',7,'bold'),width = 2,text='Receipt',command=Receiptt).grid(row=0,column=1)
        self.btnReset = Button(ButtonFrame,padx=10,bd=7,font=('arial',7,'bold'),width = 2,text='Reset',command=Reset).grid(row=0,column=2)
        self.btnExit = Button(ButtonFrame,padx=10,bd=7,font=('arial',7,'bold'),width = 2,text='Exit', command=root.quit).grid(row=0,column=3)
        
    #====================================================================================================================================

class Home():
    def __init__(self,root):
        self.root = root
        self.root.title("Online Booking System")
        self.root.geometry(geometry) 
        self.root.configure(background='beige')
        MainFrame=Frame(self.root)
        MainFrame.pack(fill=BOTH,expand=True)
        Tops = Frame(MainFrame, bd=10, width=500,relief=RIDGE)
        Tops.pack(side=TOP,fill=BOTH)
        Button1=tk.Button(MainFrame, bd=10, height=1,width=6,text='Hotel',font=('arial',7,'bold'))
        Button1.config(command=lambda: hotel(Button1))
        Button1.place(x=0,y=90)
        Button2=Button(MainFrame, bd=10, height=1,width=6,text='Train',font=('arial',7,'bold'))
        Button2.config(command=lambda: train(Button2))
        Button2.place(x=60,y=90)
        Button3=Button(MainFrame, bd=10, height=1,width=6,text='Cab',font=('arial',7,'bold'))
        Button3.config(command=lambda: cab(Button3))
        Button3.place(x=0,y=60)
        Button4=Button(MainFrame, bd=10, height=1,width=6,text='Flight',font=('arial',7,'bold'))
        Button4.config(command=lambda: flight(Button4))
        Button4.place(x=60,y=60)
            
        self.lblTitle=Label(Tops,font=('imprint mt shadow',20,'bold'),text="\t                                  ONLINE  BOOKING  SYSTEM ")
        self.lblTitle.grid()
        
        
if __name__=='__main__':
    root = Tk()

    #=========================================== Getting Screen Width ==================================================================
    w = root.winfo_screenwidth() #Return the number of pixels of the width of the screen of this widget in pixel
    h = root.winfo_screenheight() #Return the number of pixels of the height of the screen of this widget in pixel
    geometry="%dx%d+%d+%d"%(w,h,0,0)
    root.geometry("480x280+320+200")
    root.title('Login Form')
    application = user(root)
    root.mainloop()
    exit(0)

