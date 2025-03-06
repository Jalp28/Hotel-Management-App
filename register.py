from tkinter import*
from tkinter import ttk
from tkinter import font
from  PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1500x800+0+0")

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityq=StringVar()
        self.var_securitya=StringVar()
        self.var_pass=StringVar()
        self.var_confirmpass=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\HP\Desktop\Hotel Management System\images\hotel1.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relheight=1,relwidth=1)

        frame1=Frame(self.root,bg="white")
        frame1.place(x=300,y=100,width=800,height=550)
           
        register_lbl=Label(frame1,text="Register Here",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        #==========labels and entry=====================================
        fname=Label(frame1,text="First Name:",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame1,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)
        
        l_name=Label(frame1,text="Last Name:",font=("times new roman",15,"bold"),bg="white")
        l_name.place(x=400,y=100)

        self.txt_lname_entry=ttk.Entry(frame1,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname_entry.place(x=400,y=130,width=250)

        contact=Label(frame1,text="Contact:",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame1,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame1,text="Email:",font=("times new roman",15,"bold"),bg="white")
        email.place(x=400,y=170)

        self.txt_email=ttk.Entry(frame1,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=400,y=200,width=250)

        security_q=Label(frame1,text="Select Security Quetions:",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_q.place(x=50,y=240)

        self.combo_security_q=ttk.Combobox(frame1,font=("times new roman",15,"bold"),textvariable=self.var_securityq,state="readonly")
        self.combo_security_q["values"]=("Select","your birth place","your friend name","your pet name")
        self.combo_security_q.place(x=50,y=270,width=250)
        self.combo_security_q.current(0)

        security_a=Label(frame1,text="Security Answer:",font=("times new roman",15,"bold"),bg="white")
        security_a.place(x=400,y=240)

        self.txt_security=ttk.Entry(frame1,textvariable=self.var_securitya,font=("times new roman",15,"bold"))
        self.txt_security.place(x=400,y=270,width=250)

        pswd=Label(frame1,text="Password:",font=("times new roman",15,"bold"),bg="white")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame1,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame1,text="Confirm Password:",font=("times new roman",15,"bold"),bg="white")
        confirm_pswd.place(x=400,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame1,textvariable=self.var_confirmpass,font=("times new roman",15,"bold"))
        self.txt_confirm_pswd.place(x=400,y=340,width=250)


        img=Image.open(r"C:\Users\HP\Desktop\Hotel Management System\images\register.png")
        img=img.resize((150,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame1,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=100,y=400,width=150)
        
       

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityq.get()=="Select":
            messagebox.showerror("Error","All Feilds are Required")
        elif self.var_pass.get()!=self.var_confirmpass.get():
            messagebox.showerror("Error","confirm password and password must be same")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityq.get(),
                    self.var_securitya.get(),
                    self.var_pass.get()
                                                        ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")










if __name__ == "__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()

