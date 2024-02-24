from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2 

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="DEVELOPER",font=("Sans Serif",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=-100,y=0,width=1500,height=45)

        img_top=Image.open(r"C:\DIGITAL ATTENDANCE MANAGEMENT SYSTEM\college_images\Developer.jpg")
        img_top = img_top.resize((1530, 600), Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=-70,y=55,width=1530,height=600)

        # Frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=835,y=0,width=500,height=500)

        img_top1=Image.open("C:\DIGITAL ATTENDANCE MANAGEMENT SYSTEM\college_images\me.jpg")
        img_top1 = img_top1.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=200)

        # Developer info 
        dev_label=Label(main_frame,text="Hello My Name is Andrew",font=("times new roman",17,"bold"),fg="blue",bg="white")
        dev_label.place(x=0,y=5)

        dep_label=Label(main_frame,text="I am a Full Stack Developer",font=("times new roman",17,"bold"),fg="blue",bg="white")
        dep_label.place(x=0,y=40)

        img2=Image.open(r"C:\DIGITAL ATTENDANCE MANAGEMENT SYSTEM\college_images\89Untitled.jpeg")
        img2 = img2.resize((500, 300), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=220,width=500,height=250)






if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()