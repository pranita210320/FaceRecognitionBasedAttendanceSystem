#student details
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from tkinter import messagebox
#from student import Student
import mysql.connector
import cv2
import os
import numpy as np

class Student:
	def __init__(self,root):
		self.root=root;
		self.root.geometry("2500x750+0+0")
		self.root.title("facerecognition")
		
		#variabels
		self.var_dep=StringVar()
		self.var_sem=StringVar()
		self.var_year=StringVar()
		self.var_name=StringVar()
		self.var_id=StringVar()
		self.var_radio1=StringVar()
		self.var_radio2=StringVar()

		#Title label
		f_lbl=Label(self.root)
		f_lbl.place(x=0,y=0,width=500,height=130)
		title_lbl=Label(self.root,text="Student Information",font=("times and roman",35,"bold"),bg="black",fg="white")
		title_lbl.place(x=250,y=0,width=1000,height=150)

		#Main Frame
		main_frame=Frame(self.root,bd=2,bg="lightgreen")
		main_frame.place(x=250,y=150,width=1000,height=600)
		
		
		#left label frame
		left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,font=("times and roman",12,"bold"),bg="white",fg="black")
		left_frame.place(x=30,y=70,width=450,height=500)
		#right label frame
		right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,font=("times and roman",12,"bold"),bg="white",fg="black")
		right_frame.place(x=525,y=70,width=450,height=500)
		#Details
		current_course_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,font=("times and roman",12,"bold"),bg="white",fg="black")
		current_course_frame.place(x=15,y=15,width=400,height=150)
		#department
		dep_label=Label(current_course_frame,text="Department",font=("times and roman",12,"bold"))
		dep_label.grid(row=0,column=0)
		dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times and roman",12,"bold"),state="readonly")
		dep_combo["values"]=("select department","electronics","computer","it")
		dep_combo.current(0)
		dep_combo.grid(row=0,column=1,padx=2,sticky=W)
		#year
		year_label=Label(current_course_frame,text="Year",font=("times and roman",12,"bold"))
		year_label.grid(row=2,column=0)
		year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times and roman",12,"bold"),state="readonly")
		year_combo["values"]=("select year","fy","sy","ty")
		year_combo.current(0)
		year_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)
		#sem
		sem_label=Label(current_course_frame,text="Semester",font=("times and roman",12,"bold"))
		sem_label.grid(row=3,column=0)
		sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times and roman",12,"bold"),state="readonly")
		sem_combo["values"]=("select semester","1st","2nd")
		sem_combo.current(0)
		sem_combo.grid(row=3,column=1,padx=2,pady=10,sticky=W)
		
		course_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,font=("times and roman",12,"bold"),bg="white",fg="black")
		course_frame.place(x=15,y=175,width=400,height=150)
		#name and id input
		id_label=Label(course_frame,text="Student Id",font=("times and roman",12,"bold"))
		id_label.grid(row=0,column=0,padx=2,stick=W)
		
		id_entry=ttk.Entry(course_frame,width=20,textvariable=self.var_id,font=("times and roman",12,"bold"))
		id_entry.grid(row=0,column=1,padx=0,stick=W)
		
		name_label=Label(course_frame,text="Student Name",font=("times and roman",12,"bold"))
		name_label.grid(row=3,column=0,padx=3,stick=W)
		
		name_entry=ttk.Entry(course_frame,width=20,textvariable=self.var_name,font=("times and roman",12,"bold"))
		name_entry.grid(row=3,column=1,padx=3,stick=W)
		
		#buttons
		but_frame=LabelFrame(left_frame,bd=2,relief=RIDGE)
		but_frame.place(x=15,y=375,width=425,height=70)
		#Save button
		saveb=Button(but_frame,text="save",command=self.add_data,width=20,font=("times and roman",12,"bold"),bg="white",fg="blue")
		saveb.grid(row=0,column=0)
		#Reset button
		saver=Button(but_frame,text="reset",command=self.reset_data,width=20,font=("times and roman",12,"bold"),bg="white",fg="blue")
		saver.grid(row=0,column=1)
		#Delete button
		saved=Button(but_frame,text="delete",command=self.delete_data,width=20,font=("times and roman",12,"bold"),bg="white",fg="blue")
		saved.grid(row=1,column=1)
		#Photo sampel button
		saveps=Button(but_frame,text="Photo Sample",command=self.generate_dataset,width=20,font=("times and roman",12,"bold"),bg="white",fg="blue")
		saveps.grid(row=1,column=0)
		#Train data
		btrain=Button(left_frame,command=self.train_classifier,text="Train Data",cursor="hand2",font=("times and roman",10,"bold"),bg="darkgreen",fg="black")
		btrain.place(x=300,y=450,width=100,height=30)
		#exit button
		bexit=Button(left_frame,command=self.exit,text="back",cursor="hand2",font=("times and roman",10,"bold"),bg="red",fg="black")
		bexit.place(x=20,y=450,width=100,height=30)

		#Tabel of Student Details
		sea_frame=LabelFrame(right_frame,bd=2,relief=RIDGE)
		sea_frame.place(x=15,y=15,width=400,height=100)

		mlabel=Label(sea_frame,text="Student Details",font=("times and roman",25,"bold"))
		mlabel.place(x=50,y=15,width=300,height=70)
		tabel_frame=Frame(right_frame,bd=2,relief=RIDGE)
		tabel_frame.place(x=15,y=115,width=400,height=330)
		#scrollbar
		scroll_x=ttk.Scrollbar(tabel_frame,orient=HORIZONTAL)
		self.studentinfo_table=ttk.Treeview(tabel_frame,column=("rollno","name","dep","year","sem"),xscrollcommand=scroll_x.set)
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_x.config(command=self.studentinfo_table.xview)


		self.studentinfo_table.heading("dep",text="Department")
		self.studentinfo_table.heading("sem",text="semester")
		self.studentinfo_table.heading("year",text="year")
		self.studentinfo_table.heading("name",text="Name")
		self.studentinfo_table.heading("rollno",text="Roll No")
		self.studentinfo_table["show"]="headings"
		self.studentinfo_table.pack(fill=BOTH,expand=1)
		self.studentinfo_table.bind("<ButtonRelease>",self.get_cursor)
		self.fetch_data()

	
		#Function declarations 
	def add_data(self):
		if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
			messagebox.showerror("Error","all fields are required",parent=self.root)
		else:
			try:
				#messagebox.showinfo("success","welcome",parent=self.root)
				conn=mysql.connector.connect(host="localhost",username="root",password="pranitakb@2001",database="facesdata")
				my_cursor=conn.cursor()
				my_cursor.execute("insert into studentinfo values(%s,%s,%s,%s,%s)",(
																						self.var_id.get(),
																						self.var_name.get(),
																						self.var_dep.get(),
																						self.var_year.get(),
																						self.var_sem.get()
																						))
				conn.commit()
				self.fetch_data()
				conn.close()
				messagebox.showinfo("success","student details added succesfully",parent=self.root)
			except Exception as es:
				messagebox.showerror("Error",f"due to :{str(es)}",parent=self.root)
	#fetch data
	def fetch_data(self):
		conn=mysql.connector.connect(host="localhost",username="root",password="pranitakb@2001",database="facesdata")
		my_cursor=conn.cursor()
		my_cursor.execute("select * from studentinfo")
		data=my_cursor.fetchall()

		if len(data)!=0:
			self.studentinfo_table.delete(*self.studentinfo_table.get_children())
			for i in data:
				self.studentinfo_table.insert("",END,values=i)
			conn.commit()
		conn.close()

	#get cursor
	def get_cursor(self,event=""):
		cursor_focus=self.studentinfo_table.focus()
		content=self.studentinfo_table.item(cursor_focus)
		data=content["values"]

		self.var_id.set(data[1]),
		self.var_name.set(data[2]),
		self.var_dep.set(data[3]),
		self.var_year.set(data[4]),
		self.var_sem.set(data[5])

	#update function
	def update_data(self):
		if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
			messagebox.showerror("Error","all fields are required",parent=self.root)
		else:
			try:
				Update=messagebox.askyesno("update","do you want to update",parent=self.root)
				if Update>0:
					conn=mysql.connector.connect(host="localhost",username="root",password="pranitakb@2001",database="facesdata")
					my_cursor=conn.cursor()
					my_cursor.execute("Update studentinfo set id=%s,name=%s,dept=%s,year=%s,seml=%s where id=%s",(
																						#self.var_id.get(),
																						self.var_name.get(),
																						self.var_dep.get(),
																						self.var_year.get(),
																						self.var_sem.get(),
																						self.var_id.get()
																						))
				else:
					if not Update:
						return
				messagebox.showinfo("success","info succesfully updated",parent=self.root)
				conn.commit()
				self.fetch_data()
				conn.close()
			except Exception as es:
				messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
	#delete data
	def delete_data(self):
		if self.var_id.get()=="":
			messagebox.showerror("Error","student id is required",parent=self.root)
		else:
			try:
				delete=messagebox.askyesno("student delete page","Do you want to delete",parent=self.root)
				if delete>0:
					conn=mysql.connector.connect(host="localhost",username="root",password="pranitakb@2001",database="facesdata")
					my_cursor=conn.cursor()
					sql="delete from studentinfo where id=%s"
					val=(self.var_id.get(),)
					my_cursor.execute(sql,val)
				else:
					if not delete:
						return
				conn.commit()
				self.fetch_data()
				conn.close()
				messagebox.showinfo("delete","succesfully deleted info",parent=self.root)
			except Exception  as es:
				messagebox.showerror("error",f"Due To{str(es)}",parent=self.root)


		#reset 
	def reset_data(self):
		self.var_id.set("")
		self.var_name.set("")
		self.var_dep.set("select department")
		self.var_year.set("select year")
		self.var_sem.set("select sem")

		#creating dataset
	def generate_dataset(self):
		if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
			messagebox.showerror("Error","all fields are required",parent=self.root)
		else:
			try:
				conn=mysql.connector.connect(host="localhost",username="root",password="pranitakb@2001",database="facesdata")
				my_cursor=conn.cursor()
				my_cursor.execute("select * from studentinfo")
				myresult=my_cursor.fetchall()
				id=0
				for x in myresult:
					id+=1
				my_cursor.execute("update studentinfo set id=%s,name=%s,dept=%s,year=%s,seml=%s where id=%s",(
																						self.var_id.get(),
																						self.var_name.get(),
																						self.var_dep.get(),
																						self.var_year.get(),
																						self.var_sem.get(),
																						self.var_id.get()==id+1
																						))
				conn.commit();
				self.fetch_data()
				self.reset_data()
				conn.close()
				#load data face
				face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
				def face_cropped(img):
					gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
					faces=face_classifier.detectMultiScale(gray,1.3,5)
					#scaling factor 1.3
					#minimum neighbour 5
					for(x,y,w,h) in faces:
						face_cropped=img[y:y+h,x:x+w]
						return face_cropped
				cap=cv2.VideoCapture(0)
				img_id=0
				while True:
					ret,myframe=cap.read()
					if face_cropped(myframe) is not None:
						img_id+=1
						face=cv2.resize(face_cropped(myframe),(450,450))
						face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
						file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
						cv2.imwrite(file_name_path,face)
						cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)	
						cv2.imshow("Croped face",face)
					
					if cv2.waitKey(1)==13 or int(img_id)==100:
						break
				cap.release()
				cv2.destroyAllWindows()
				messagebox.showinfo("result","generating data set compeleted succesfully")
			except Exception as es:
				messagebox.showerror("error"f"due to :{str(es)}",parent=self.root)

	def train_classifier(self):
		data_dir=(r"C:\Users\Dell\Desktop\face_recognition\data")
		path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

		faces=[]
		ids=[]

		for image in path:
			img=Image.open(image).convert('L')  
			imageNp=np.array(img,'uint8') 
			id1=int(os.path.split(image)[1].split('.')[1])
			faces.append(imageNp)
			ids.append(id1)
			cv2.imshow("training",imageNp)
			cv2.waitKey(1)==13
		ids=np.array(ids)

		#train
		clf=cv2.face.LBPHFaceRecognizer_create()
		clf.train(faces,ids)
		clf.write("classifier.xml")
		cv2.destroyAllWindows()
		messagebox.showinfo("Result","Training complete")

	


				#exit
	def exit(self):
		self.iexit=tkinter.messagebox.askyesno("Face Recognition","Return to main window? ",parent=self.root)
		if self.iexit>0:
			self.root.destroy()
		else:
			return 
	

if __name__ =="__main__":
	root=Tk()
	obj=Student(root)
	root.mainloop()
	
