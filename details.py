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


class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1205x515+154+179")

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
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman",12,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=425,height=460)

        #==floor==
        lbl_floor=Label(labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W,padx=20)

        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20,font=("arial",13,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)

        #==Room no==
        lbl_roomno=Label(labelframeleft,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_roomno.grid(row=1,column=0,sticky=W,padx=20)

        self.var_roomno=StringVar()
        entry_roomno=ttk.Entry(labelframeleft,textvariable=self.var_roomno,width=20,font=("arial",13,"bold"))
        entry_roomno.grid(row=1,column=1,sticky=W)

        #==Room Type==
        lbl_roomtype=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_roomtype.grid(row=2,column=0,sticky=W,padx=20)

        self.var_roomtype=StringVar()
        entry_roomtype=ttk.Entry(labelframeleft,textvariable=self.var_roomtype,width=20,font=("arial",13,"bold"))
        entry_roomtype.grid(row=2,column=1,sticky=W)

        #===================================buttons===============================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=395,width=412,height=35)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnreset.grid(row=0,column=3,padx=1)

         #======================table frame ============================================
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("times new roman",12,"bold"),padx=2,)
        Table_frame.place(x=500,y=55,width=600,height=350)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_frame,columns=("floor","roomno","roomtype"),
        xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room No")
        self.room_table.heading("roomtype",text="Room Type")
       
    
        self.room_table["show"]="headings"
        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomtype",width=100)
   
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomtype.get()=="":
            messagebox.showerror("Error","All Feilds Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",
                (
                self.var_floor.get(),
                self.var_roomno.get(),
                self.var_roomtype.get(),
                
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some Thing went Wrong:{str(es)}",parent=self.root)

    #===============fetch all data=====================================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
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

        self.var_floor.set(row[0]),
        self.var_roomno.set(row[1]),
        self.var_roomtype.set(row[2]),

     # ============update============================
    def update(self):
        if self.var_floor.get=="":
            messagebox.showerror("Error","Please enter Floor number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set floor=%s,Roomtype=%s where roomno=%s",
            (

                self.var_floor.get(),
                self.var_roomtype.get(),
                self.var_roomno.get(),
               
                
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","New Room detailed has been updated successfully",parent=self.root)

      #===================delete===================================
    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want delete this Room Details",parent=self.root)
        if delete > 0:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
            my_cursor=conn.cursor()
            query="delete from details where roomno=%s"
            value=(self.var_roomno.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    
     #================reset ==============================================
    def reset(self):
        self.var_floor.set(""),
        self.var_roomno.set(""),
        self.var_roomtype.set(""),
        
                
        





if __name__ == "__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()
