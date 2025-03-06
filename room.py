from os import stat
from tkinter import*
from PIL import  ImageTk,Image
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
from mysql.connector import cursor

class roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1205x515+154+179")

        #======================variables================================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()



         #======================Title====================================
        lbl_title=Label(self.root,text="ROOMBOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1205,height=50)

        #====================== logo ==================================
        img2=Image.open(r"C:\Users\HP\Desktop\Hotel Management System\images\logo.jpg")
        img2=img2.resize((50,50),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimage2,bd=2,relief=RIDGE)
        lblimg.place(x=0,y=0,height=50,width=50)

        #==================label frame =======================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="RoomBooking Details",font=("times new roman",12,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=425,height=460)

        #==================labels and entrys====================================
        #custcontact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("arial",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        #fetch data btn
        btnfetchdata=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",font=("arial",9,"bold"),bg="black",fg="gold",width=9)
        btnfetchdata.place(x=340,y=4)

        #check_in_date
        check_in_date=Label(labelframeleft,text="Check in Date:",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=29,font=("arial",13,"bold"))
        txtcheck_in_date.grid(row=1,column=1) 

        #check_out_date
        lbl_check_out_date=Label(labelframeleft,text="Check out Date:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_check_out_date.grid(row=2,column=0,sticky=W)
        txtcheck_out_date=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=29,font=("arial",13,"bold"))
        txtcheck_out_date.grid(row=2,column=1) 

        #room_type
        label_roomtype=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        label_roomtype.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select roomtype from details")
        ide=my_cursor.fetchall()

        combo_roomtype=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_roomtype,width=27,state="readonly")
        combo_roomtype["value"]=ide
        combo_roomtype.current(0)
        combo_roomtype.grid(row=3,column=1) 

        #Available Room
        lblavailabale=Label(labelframeleft,text="Available Room:",font=("arial",12,"bold"),padx=2,pady=6)
        lblavailabale.grid(row=4,column=0,sticky=W)
         #txtpostcode=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=29,font=("arial",13,"bold"))
         #txtpostcode.grid(row=4,column=1)

        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select roomno from details")
        rows=my_cursor.fetchall()
        combo_roomno=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_roomavailable,width=27,state="readonly")
        combo_roomno["value"]=rows
        combo_roomno.current(0)
        combo_roomno.grid(row=4,column=1)

        #meal
        lblmeal=Label(labelframeleft,text="Meal:",font=("arial",12,"bold"),padx=2,pady=6)
        lblmeal.grid(row=5,column=0,sticky=W)
        txtmeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,width=29,font=("arial",13,"bold"))
        txtmeal.grid(row=5,column=1)

        #no of days
        lblNoOfDays=Label(labelframeleft,text="No of Days:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,width=29,font=("arial",13,"bold"))
        txtNoOfDays.grid(row=6,column=1)

        #Paid Tax 
        lblNoOfDays=Label(labelframeleft,text="Paid Tax:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=7,column=0,sticky=W)

        txtNoOfDays=ttk.Entry(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_paidtax,width=29,state="readonly")
        txtNoOfDays.grid(row=7,column=1)
        
        #sub total
        lblNoOfDays=Label(labelframeleft,text="Sub Total:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=8,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_actualtotal,width=29)
        txtNoOfDays.grid(row=8,column=1)

        #Total
        lblIdnumber=Label(labelframeleft,text="Total Cost:",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdnumber.grid(row=9,column=0,sticky=W)
        txtIdnumber=ttk.Entry(labelframeleft,textvariable=self.var_total,width=29,font=("arial",13,"bold"))
        txtIdnumber.grid(row=9,column=1)

        #============================billbutton=================================
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

        #===================================buttons===============================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=395,width=412,height=35)

        btnAdd=Button(btn_frame,command=self.add_data,text="Add",font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnreset.grid(row=0,column=3,padx=1)

        #============================Right side Image==============================================
        img3=Image.open(r"C:\Users\HP\Desktop\Hotel Management System\images\hotel5.jpg")
        img3=img3.resize((500,340),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimage3,bd=2,relief=RIDGE)
        lblimg.place(x=700,y=55,height=225,width=500)


        #======================table frame ============================================
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details ",font=("times new roman",12,"bold"),padx=2,)
        Table_frame.place(x=435,y=250,width=765,height=260)

        #======================= show data table ============================================
        details_table=Frame(Table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=20,width=755,height=200)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,columns=("contact","checkin","checkout","roomtype","roomavailable","meal",
        "noofdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-In")
        self.room_table.heading("checkout",text="Check-Out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noofdays",text="NoOfDays")
        

        self.room_table["show"]="headings"
        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noofdays",width=100)
        
       
        self.room_table.pack(fill=BOTH,expand=1)
        
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #=========================add data ======================
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All Feilds Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",
                (
                self.var_contact.get(),
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_noofdays.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some Thing went Wrong:{str(es)}",parent=self.root)
  
     # ============update============================
    def update(self):
        if self.var_contact.get=="":
            messagebox.showerror("Error","Please enter Mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set Check_in=%s,Check_out=%s,Roomtype=%s,Roomavailable=%s,Meal=%s,Noofdays=%s where Contact=%s",
            (

                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_noofdays.get(),
                self.var_contact.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room detailed has been updated successfully",parent=self.root)

    #===================delete===================================
    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent=self.root)
        if delete > 0:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    #================reset ==============================================
    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set("")
        self.var_paidtax.set(""),
        self.var_actualtotal.set(""),
        self.var_total.set("")
    

    #===============fetch all data=====================================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #=============get cursor=======================================
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])
    


    #==================all data fetch================================
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This Number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=2,relief=RIDGE,padx=2)
                showDataframe.place(x=435,y=56,width=260,height=225)

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)    

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=70,y=0)
                 
                #=====gender===============
                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=40)    

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=70,y=40)

                #=========emial=========================
                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblemail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                lblemail.place(x=0,y=80)    

                lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=70,y=80)

                #=============Nationality======================
                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblNationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                lblNationality.place(x=0,y=120)    

                lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl4.place(x=100,y=120)

                #=================Address==============================
                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblAddress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                lblAddress.place(x=0,y=160)    

                lbl5=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl5.place(x=100,y=160)


       #============== serch system ======================================
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room where"+str(self.search_var.get())+"LIKE'%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commite()
        conn.close()

    def  total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%y")
        outDate=datetime.strptime(outDate,"%d/%m/%y")     
        self.var_noofdays.set(abs(outDate-inDate).days)

        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(600)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
            q1=float(300)
            q2=float(600)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="lunch" and self.var_roomtype.get()=="Duplex"):
            q1=float(500)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)






if __name__ == "__main__":
    root=Tk()
    obj=roombooking(root)
    root.mainloop()
