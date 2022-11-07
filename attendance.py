#attendance
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from tkinter import messagebox
#from student import Student
import mysql.connector
#import cv2
import csv
from tkinter import filedialog
import os

mydata=[]

class Attendance:
	def __init__(self,root):
		self.root=root;
		self.root.geometry("2500x750+0+0")
		self.root.title("Attendance")

		a_lbl=Label(self.root)
		a_lbl.place(x=0,y=0,width=500,height=130)
		att_lbl=Label(self.root,text="Attendance",font=("times and roman",35,"bold"),bg="black",fg="white")
		att_lbl.place(x=250,y=0,width=1000,height=150)

		mainframe=Frame(self.root,bd=2,bg="lightgreen")
		mainframe.place(x=250,y=150,width=1000,height=600)

		t_frame=Frame(mainframe,bd=2,relief=RIDGE)
		t_frame.place(x=200,y=30,width=600,height=500)

		importb=Button(mainframe,text="Import Data",command=self.importCsv,width=20,font=("times and roman",12,"bold"),bg="white",fg="blue")
		importb.place(x=200,y=530,width=200,height=50)

		#exit button
		bexit=Button(mainframe,command=self.exit,text="back",cursor="hand2",font=("times and roman",10,"bold"),bg="red",fg="black")
		bexit.place(x=600,y=530,width=200,height=50)

		
		exportb=Button(mainframe,text="Export Data",command=self.exportCsv,width=20,font=("times and roman",12,"bold"),bg="white",fg="blue")
		exportb.place(x=400,y=530,width=200,height=50)
		
		scroll_x=ttk.Scrollbar(t_frame,orient=HORIZONTAL)
		scroll_y=ttk.Scrollbar(t_frame,orient=VERTICAL)
		self.attend_table=ttk.Treeview(t_frame,column=("name","t","d"),xscrollcommand=scroll_y.set,yscrollcommand=scroll_y.set)

		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)
		scroll_x.config(command=self.attend_table.xview)
		scroll_y.config(command=self.attend_table.yview)

		self.attend_table.heading("name",text="Name")
		self.attend_table.heading("t",text="Time")
		self.attend_table.heading("d",text="Date")
		self.attend_table["show"]="headings"
		self.attend_table.pack(fill=BOTH,expand=1)
	
		#fetch data
	def fetchdata(self,row):
		self.attend_table.delete(*self.attend_table.get_children())
		for i in row:
			self.attend_table.insert("",END,values=i)

	def importCsv(self):
		global mydata
		mydata.clear()
		filen=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open",filetypes=(("CSV file","*csv"),("All File","*.*")),parent=self.root)
		with open(filen) as myfile:
			csvread=csv.reader(myfile,delimiter=",")
			for i in csvread:
				mydata.append(i)
			self.fetchdata(mydata)
	def exportCsv(self):
		try:
			if len(mydata)<1:
				messagebox.showerror("No data","No data found",parent=self.root)
				return False
			filen=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open",filetypes=(("CSV file","*csv"),("All File","*.*")),parent=self.root)
			with open(filen,mode="w",newline="") as myfile:
				exp_write=csv.writer(myfile,delimiter=",")
				for i in mydata:
					exp_write.writerow(i)
				messagebox.showinfo("Data export","Data exported to "+os.path.basename(filen)+"succesful")
		except Exception as es:
			messagebox("Error"f"Due To :{str(es)}",parent=self.root)
		
			
#exit
	def exit(self):
		self.iexit=tkinter.messagebox.askyesno("Face Recognition","Return to main window? ",parent=self.root)
		if self.iexit>0:
			self.root.destroy()
		else:
			return 
	


if __name__ =="__main__":
	root=Tk()
	obj=Attendance(root)
	root.mainloop()




