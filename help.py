from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2 

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="HELP DESK",font=("Sans Serif",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=-100,y=0,width=1500,height=45)

        img_top=Image.open(r"C:\DIGITAL ATTENDANCE MANAGEMENT SYSTEM\college_images\farzad-p-xSl33Wxyc-unsplash.jpg")
        img_top = img_top.resize((1530, 600), Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=-70,y=55,width=1530,height=600)

        dev_label=Label(f_lbl,text="Email:kingandrewmark@gmail.com",font=("times new roman",15,"bold"),fg="blue",bg="white")
        dev_label.place(x=760,y=250)


if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()