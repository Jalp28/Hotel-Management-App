from tkinter import*
from tkinter import ttk
from tkinter import font
from  PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import random
from Hotel import HotelManagementSystem
from register import Register

def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1500x800+0+0")

        self.var_pass=StringVar()
        self.var_email=StringVar()

    
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\HP\Desktop\Hotel Management System\images\hotel1.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0)

        frame=Frame(self.root,bg="black")
        frame.place(x=500,y=140,width=340,height=450)

        img1=Image.open(r"C:\Users\HP\Desktop\Hotel Management System\images\user.png")
        img1=img1.resize((70,70),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        lblimg1=Label(image=self.photoimage1,bd=2,relief=RIDGE,bg="black")
        lblimg1.place(x=639,y=150,height=80,width=80)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=100,y=100)

        #==========================label==============================
        username=lbl=Label(frame,text="Username :",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=20,y=150)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=20,y=180,width=280)

        password=lbl=Label(frame,text="Password :",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=20,y=220)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=20,y=250,width=280)
         
        #==================loginbtn================================
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        #==============registrationbtn===============================
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=7,y=350,width=150)
        
      
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):

        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","ALL Fields required")

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
            
            self.var_email.get(),
            self.var_pass.get(),
            ))
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Invalid Username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
                
            conn.commit()
            conn.close()



                
           






        



        

if __name__ == "__main__":
    main()