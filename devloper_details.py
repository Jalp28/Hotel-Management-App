from tkinter import*
from tkinter import ttk

class DevloperDetails:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1205x515+154+179")
    
        lbl_title=Label(self.root,text="DEVELOPER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1205,height=50)

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Developer Contact Details",font=("times new roman",12,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=1190,height=460)

        contact=Label(labelframeleft,text="Devloper Contact   :",font=("arial",12,"bold"),padx=2,pady=6)
        contact.grid(row=0,column=0,sticky=W)

        contact=Label(labelframeleft,text="+91 9624623868 / +91 7623863126",font=("arial",12,"bold"),padx=2,pady=6)
        contact.grid(row=0,column=1,sticky=W)

        email=Label(labelframeleft,text="Email                          :",font=("arial",12,"bold"),padx=2,pady=6)
        email.grid(row=1,column=0,sticky=W)

        email=Label(labelframeleft,text="jalpkumarpatel18@gnu.ac.in",font=("arial",12,"bold"),padx=2,pady=6)
        email.grid(row=1,column=1,sticky=W)
        
        



if __name__ == "__main__":
    root=Tk()
    obj=DevloperDetails(root)
    root.mainloop()


