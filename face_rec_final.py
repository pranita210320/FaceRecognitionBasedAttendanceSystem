#face recognition
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from tkinter import messagebox
#from student import Student
import mysql.connector
import numpy as np
from time import strftime
from datetime import datetime
import cv2 
import os

class Face_rec_final:
	def __init__(self,root):
		self.root=root;
		self.root.geometry("2500x750+0+0")
		self.root.title("facerecognition")

		face_lbl=Label(self.root,bg="lightgreen")
		face_lbl.place(x=250,y=150,width=1000,height=600)
		#Title label
		title_lbl=Label(self.root,text="Face detection",font=("times and roman",35,"bold"),bg="black",fg="white")
		title_lbl.place(x=250,y=0,width=1000,height=150)

		#face detection
		img5=Image.open(r"C:\Users\Dell\Desktop\face_recognition\collegeimages\face.jpeg")
		img5=img5.resize((250,250),Image.Resampling.LANCZOS)
		self.photoimg5=ImageTk.PhotoImage(img5)

		faceB=Button(self.root,image=self.photoimg5,cursor="hand2",command=self.recognition,font=("times and roman",15,"bold"),bg="darkGreen",fg="white")
		faceB.place(x=600,y=200,width=250,height=250)

		att_lbl=Label(self.root,text="Click on button for Face detection and marking attendance",font=("times and roman",15,"bold"),bg="lightgreen",fg="black")
		att_lbl.place(x=250,y=500,width=1000,height=150)


		#exit button
		bexit=Button(self.root,command=self.exit,text="back",cursor="hand2",font=("times and roman",10,"bold"),bg="red",fg="black")
		bexit.place(x=250,y=600,width=100,height=100)

	#attendance
	def attendance(self,i):
		with open("attend.csv","r+",newline="\n") as f:
			myDataList=f.readlines()
			name_list=[]
			for line in myDataList:
				entry=line.split((","))
				name_list.append(entry[0])
			if((i not in name_list)):
				now=datetime.now()
				d1=now.strftime("%d/%m/%y")
				dtString=now.strftime("%H:%M:%S")
				f.writelines(f"\n{i},{dtString},{d1},Preset")

	def recognition(self):
		def draw_boundry(img,classifier,scalefactor,minNeighbors,color,text,clf):
			gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
			features=classifier.detectMultiScale(gray_img,scalefactor,minNeighbors)

			coord=[]

			for (x,y,w,h) in features:
				cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
				id1,predict=clf.predict(gray_img[y:y+h,x:x+w])
				confidence=int((100*(1-predict/300)))

				conn=mysql.connector.connect(host="localhost",username="root",password="pranitakb@2001",database="facesdata")
				my_cursor=conn.cursor()
				my_cursor.execute("select name from studentinfo where id="+str(id1))
				i=my_cursor.fetchone()
				i="+".join(i)

				if confidence>77:
					cv2.putText(img,f"Name:{i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
					self.attendance(i)
				else:
					cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),3)
					cv2.putText(img,"Your are not registered",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

				coord=[x,y,w,h]

			return coord

		def rec(img,clf,faceCascade):
			coord=draw_boundry(img,faceCascade,1.1,10,(255,25,255),"face",clf)
			return img

		faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
		clf=cv2.face.LBPHFaceRecognizer_create()
		clf.read("classifier.xml")

		video_cap=cv2.VideoCapture(0)


		while True:
			ret,img=video_cap.read()
			img=rec(img,clf,faceCascade)
			cv2.imshow("face recognition",img)

			if cv2.waitKey(1)==13:
				break
		video_cap.release()
		cv2.destroyAllWindows()
		
		#exit
	def exit(self):
		self.iexit=tkinter.messagebox.askyesno("Face Recognition","Return to main window? ",parent=self.root)
		if self.iexit>0:
			self.root.destroy()
		else:
			return 
	

if __name__ =="__main__":
	root=Tk()
	obj=Face_rec_final(root)
	root.mainloop()


