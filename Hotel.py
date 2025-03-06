from tkinter import*
from PIL import  ImageTk,Image
from customer import cust_win
from room import roombooking
from details import DetailsRoom
from devloper_details import DevloperDetails






class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1500x800+0+0")
 
        #=========================img 1===============================
        img1=Image.open(r"C:\Users\HP\Desktop\Hotel Management System\images\hotel1.jpg")
        img1=img1.resize((1550,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimage1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,height=100,width=1550)

        #====================== logo ==================================
        img2=Image.open(r"C:\Users\HP\Desktop\Hotel Management System\images\logo.jpg")
        img2=img2.resize((100,100),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimage2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,height=100,width=100)

        #======================Title====================================
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=100,width=1460,height=50)

        #====================== main frame ==============================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=150,width=1550,height=620)
        
        #====================menu========================================
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=155)

        #====================== btn frame ==============================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=38,width=155,height=300)
        
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=11,font=("times new roman",17,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,width=11,font=("times new roman",17,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",command=self.DetailsRoom,width=11,font=("times new roman",17,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        DevloperDetails_btn=Button(btn_frame,text="Developer",command=self.DevloperDetails,width=11,font=("times new roman",17,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        DevloperDetails_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=11,font=("times new roman",17,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)

        #=================================right side img=========================================
        img3=Image.open(r"C:\Users\HP\Desktop\Hotel Management System\images\hotel2.jpg")
        img3=img3.resize((1260,550),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimage3,bd=2,relief=RIDGE)
        lblimg1.place(x=155,y=0,height=550,width=1260)
        
        #==========================down img ======================================================
        img4=Image.open(r"C:\Users\HP\Desktop\Hotel Management System\images\hotel3.jpg")
        img4=img4.resize((250,300),Image.ANTIALIAS)
        self.photoimage4=ImageTk.PhotoImage(img4)

        lblimg1=Label(main_frame,image=self.photoimage4,bd=2,relief=RIDGE)
        lblimg1.place(x=0,y=400,height=150,width=155)

        img5=Image.open(r"C:\Users\HP\Desktop\Hotel Management System\images\hotel4.jpg")
        img5=img5.resize((252,300),Image.ANTIALIAS)
        self.photoimage5=ImageTk.PhotoImage(img5)

        lblimg1=Label(main_frame,image=self.photoimage5,bd=2,relief=RIDGE)
        lblimg1.place(x=0,y=252,height=150,width=155)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_win(self.new_window)
    
    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=roombooking(self.new_window)

    def DetailsRoom(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)

    def DevloperDetails(self):
         self.new_window=Toplevel(self.root)
         self.app=DevloperDetails(self.new_window)

    def logout(self):
    
        self.root.destroy()


       



if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
