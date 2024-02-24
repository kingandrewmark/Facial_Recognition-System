from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        # first image
        img=Image.open(r"C:\DIGITAL ATTENDANCE MANAGEMENT SYSTEM\college_images\vadim-sherbakov-d6ebY-faOO0-unsplash.jpg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # second image 
        img1=Image.open(r"C:\DIGITAL ATTENDANCE MANAGEMENT SYSTEM\college_images\download.jpeg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        # third image 
        img2=Image.open(r"C:\DIGITAL ATTENDANCE MANAGEMENT SYSTEM\college_images\sandip-roy-eiUlzMiiin8-unsplash.jpg")
        img2 = img2.resize((530, 130), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=900,y=0,width=530,height=130)


        # bg image
        img3=Image.open(r"C:\DIGITAL ATTENDANCE MANAGEMENT SYSTEM\college_images\cx-insight-YloghyfD7e8-unsplash.jpg")
        img3 = img3.resize((1500, 700), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1500,height=700)   

        title_lbl=Label(text="DIGITAL ATTENDANCE MANAGEMENT SYSTEM",font=("Sans Serif",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=-100,y=0,width=1500,height=45)

        #=======================Time===========================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text= string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font = ('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=100,y=0,width=110,height=50)
        time()

        # student button 
        img4=Image.open(r"C:\DIGITAL ATTENDANCE MANAGEMENT SYSTEM\college_images\mimi-thian-vdXMSiX-n6M-unsplash.jpg")
        img4 = img4.resize((1500, 700), Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        aspect_ratio = img4.width / img4.height
        new_height = 220
        new_width = int(new_height * aspect_ratio)

        img4 = img4.resize((new_width, new_height), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)


        b1 = Button(self.root, image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=150,width=220,height=220)

        b1_1= Button(self.root,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=350,width=220,height=40)


        # Detect face button 
        img5=Image.open(r"C:\DIGITAL ATTENDANCE MANAGEMENT SYSTEM\college_images\download.jpeg")
        img5 = img5.resize((1500, 700), Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        aspect_ratio = img5.width / img5.height
        new_height = 220
        new_width = int(new_height * aspect_ratio)

        img5 = img5.resize((new_width, new_height), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)


        b2 = Button(self.root, image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=400,y=150,width=220,height=220)

        b2_2= Button(self.root,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_2.place(x=400,y=350,width=220,height=40)


        # Attendance Face button  
        img6=Image.open(r"C:\DIGITAL ATTENDANCE MANAGEMENT SYSTEM\college_images\download (1).jpeg")
        img6 = img6.resize((1500, 700), Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        aspect_ratio = img6.width / img6.height
        new_height = 220
        new_width = int(new_height * aspect_ratio)

        img6 = img6.resize((new_width, new_height), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)


        b3 = Button(self.root, image=self.photoimg6,cursor="hand2",command=self.attendance_data,)
        b3.place(x=700,y=150,width=220,height=220)

        b3_3= Button(self.root,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_3.place(x=700,y=350,width=220,height=40)

        # Help desk  
        img7=Image.open(r"C:\DIGITAL ATTENDANCE MANAGEMENT SYSTEM\college_images\th.jpeg")
        img7 = img7.resize((1500, 700), Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        aspect_ratio = img7.width / img7.height
        new_height = 220
        new_width = int(new_height * aspect_ratio)

        img7 = img7.resize((new_width, new_height), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)


        b4 = Button(self.root, image=self.photoimg7,cursor="hand2",command=self.help_data)
        b4.place(x=1000,y=150,width=220,height=220)

        b4_4= Button(self.root,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_4.place(x=1000,y=350,width=220,height=40)


        # Train face button    
        img8=Image.open(r"C:\DIGITAL ATTENDANCE MANAGEMENT SYSTEM\college_images\Untitled.jpeg")
        img8 = img8.resize((1500, 700), Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        aspect_ratio = img8.width / img8.height
        new_height = 220
        new_width = int(new_height * aspect_ratio)

        img8 = img8.resize((new_width, new_height), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)


        b5 = Button(self.root, image=self.photoimg8,cursor="hand2",command=self.train_data)
        b5.place(x=100,y=400,width=220,height=220)

        b5_5= Button(self.root,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5_5.place(x=100,y=600,width=220,height=40)


        # Photos face button    
        img9=Image.open(r"C:\DIGITAL ATTENDANCE MANAGEMENT SYSTEM\college_images\1Untitled.jpeg")
        img9 = img9.resize((1500, 700), Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        aspect_ratio = img9.width / img9.height
        new_height = 220
        new_width = int(new_height * aspect_ratio)

        img9 = img9.resize((new_width, new_height), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)


        b6 = Button(self.root, image=self.photoimg9,cursor="hand2",command=self.open_img)
        b6.place(x=400,y=400,width=220,height=220)

        b6_6= Button(self.root,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_6.place(x=400,y=600,width=220,height=40)


        # Developer face button    
        img10=Image.open(r"C:\DIGITAL ATTENDANCE MANAGEMENT SYSTEM\college_images\2Untitled.jpeg")
        img10 = img10.resize((1500, 700), Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        aspect_ratio = img10.width / img10.height
        new_height = 220
        new_width = int(new_height * aspect_ratio)

        img10 = img10.resize((new_width, new_height), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)


        b7 = Button(self.root, image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b7.place(x=700,y=400,width=220,height=220)

        b7_7= Button(self.root,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7_7.place(x=700,y=600,width=220,height=40)

        # Exit face button    
        img11=Image.open(r"C:\DIGITAL ATTENDANCE MANAGEMENT SYSTEM\college_images\3Untitled.jpeg")
        img11 = img11.resize((1500, 700), Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        aspect_ratio = img11.width / img11.height
        new_height = 220
        new_width = int(new_height * aspect_ratio)

        img11 = img11.resize((new_width, new_height), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)


        b8 = Button(self.root, image=self.photoimg11,cursor="hand2",command=self.iExit)
        b8.place(x=1000,y=400,width=220,height=220)

        b8_8= Button(self.root,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b8_8.place(x=1000,y=600,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return 

    # ========Functions buttons=======

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()