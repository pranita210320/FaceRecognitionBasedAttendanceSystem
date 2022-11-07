from tkinter import*
from tkinter import ttk
import tkinter

from PIL import Image,ImageTk
from student import Student
from time import strftime
from datetime import datetime
from face_rec_final import Face_rec_final
from attendance import Attendance
import cv2
import os

class Face_Recognition:
	def __init__(self,root):
		self.root=root;
		self.root.geometry("2500x750+0+0")
		self.root.title("facerecognition")

		#College image in starting
		img=Image.open(r"C:\Users\Dell\Desktop\face_recognition\collegeimages\collegeimg.jpg")
		img=img.resize((1300,200),Image.Resampling.LANCZOS)
		self.photoimg=ImageTk.PhotoImage(img)
		
		f_lbl=Label(self.root,image=self.photoimg)
		f_lbl.place(x=-80,y=0,width=1700,height=200)

		#title
		title_lbl=Label(self.root,text="Welcome to Attendance System ",font=("times and roman",30,"bold"),bg="black",fg="white")
		title_lbl.place(x=120,y=200,width=1300,height=100)
		
		#show time on main frame
		def time():
			string=strftime('%H:%M:%S %p')
			lbl.config(text=string)
			lbl.after(1000,time)

		lbl=Label(title_lbl,font=("times and roman",17,"bold"),bg="white",fg="black")
		lbl.place(x=30,y=30,width=150,height=50)
		time()

		#background
		bg_lbl=Label(self.root,bg="lightgreen")
		bg_lbl.place(x=120,y=300,width=1300,height=1000)

		bg_lbl1=Label(self.root,text="  New Registration       Mark Attendance    	Attendance               Exit          ",font=("times and roman",18,"bold"),bg="lightgreen",fg="black")
		bg_lbl1.place(x=300,y=570,width=880,height=100)
		
		#Button student registration
		img1=Image.open(r"C:\Users\Dell\Desktop\face_recognition\collegeimages\student.jpeg")
		img1=img1.resize((220,220),Image.Resampling.LANCZOS)
		self.photoimg1=ImageTk.PhotoImage(img1)
		b1=Button(self.root,image=self.photoimg1,command=self.student_details,cursor="hand2",font=("times and roman",10,"bold"))
		b1.place(x=330,y=370,width=220,height=220)
	

		#Button mark attendance
		img2=Image.open(r"C:\Users\Dell\Desktop\face_recognition\collegeimages\face.jpeg")
		img2=img2.resize((220,220),Image.Resampling.LANCZOS)
		self.photoimg2=ImageTk.PhotoImage(img2)
		b2=Button(self.root,image=self.photoimg2,command=self.student_faces,cursor="hand2",font=("times and roman",10,"bold"))
		b2.place(x=550,y=370,width=220,height=220)
		
		#Button Attendace
		img3=Image.open(r"C:\Users\Dell\Desktop\face_recognition\collegeimages\attendance.jpeg")
		img3=img3.resize((220,220),Image.Resampling.LANCZOS)
		self.photoimg3=ImageTk.PhotoImage(img3)
		b3=Button(self.root,image=self.photoimg3,command=self.attenddata,cursor="hand2",font=("times and roman",10,"bold"),bg="black",fg="white")
		b3.place(x=770,y=370,width=220,height=220)
		
		#Button Exit
		img4=Image.open(r"C:\Users\Dell\Desktop\face_recognition\collegeimages\exit.jpeg")
		img4=img4.resize((220,220),Image.Resampling.LANCZOS)
		self.photoimg4=ImageTk.PhotoImage(img4)
		b4=Button(self.root,image=self.photoimg4,command=self.exit,cursor="hand2",font=("times and roman",10,"bold"))
		b4.place(x=990,y=370,width=220,height=220)

		#Function for Buutons
		#Student details
	def student_details(self):
		self.new_window=Toplevel(self.root)
		self.app=Student(self.new_window)
	
		#Face Recognition 
	def student_faces(self):
		self.new_window=Toplevel(self.root)
		self.app=Face_rec_final(self.new_window)
		
		#Attendance
	def attenddata(self):
		self.new_window=Toplevel(self.root)
		self.app=Attendance(self.new_window)

	    #exit
	def exit(self):
		self.iexit=tkinter.messagebox.askyesno("Face Recognition","Do you want to exit ? ",parent=self.root)
		if self.iexit>0:
			self.root.destroy()
		else:
			return 
	

if __name__ =="__main__":
	root=Tk()
	obj=Face_Recognition(root)
	root.mainloop()


