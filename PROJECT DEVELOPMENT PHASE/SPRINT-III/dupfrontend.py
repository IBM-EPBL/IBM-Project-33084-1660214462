from tkinter import *
import sqlite3
from PIL import ImageTk, Image
from tkinter import messagebox as ms
import pickle
from tkinter import ttk
model=pickle.load(open("heartfull.pkl",'rb'))

root=Tk()


root.title("Hear disease prediction app")

root.geometry("1000x650")
root.configure(background="#166969")
#root.iconbitmap('aa.ico')
root.resizable(False, False)
#load = Image.open('button1.png')
#button_image= ImageTk.PhotoImage(load)
print("PNT2022TMID28916 - SrishJeneJesshari")

Age=DoubleVar()
Sex=DoubleVar()
Chestpaintype=DoubleVar()
FBSover=DoubleVar()
MaxHR=DoubleVar()
Exerciseangina=DoubleVar()
Cholesterol=DoubleVar()
BP=DoubleVar()
EKGresults=DoubleVar()
Thallium=DoubleVar()
STdepression=DoubleVar()
Numberofvesselsfluro=DoubleVar()
SlopeofST=DoubleVar()


def pred():
    Age1=(Age.get())
    Sex1=(Sex.get())
    Chestpaintype1=(Chestpaintype.get())
    FBSover1=(FBSover.get())
    MaxHR1=(MaxHR.get())
    Exerciseangina1=(Exerciseangina.get())
    Cholesterol1=(Cholesterol.get())
    BP1=(BP.get())
    EKGresults1=(EKGresults.get())
    Thallium1=(Thallium.get())
    STdepression1=(STdepression.get())
    Numberofvesselsfluro1=(Numberofvesselsfluro.get())
    SlopeofST1=(SlopeofST.get())
    
    
    print(Age1,Sex1,Chestpaintype1,FBSover1,MaxHR1,Exerciseangina1,Cholesterol1 , BP1 , EKGresults1 , Thallium1, STdepression1, Numberofvesselsfluro1, SlopeofST1)
    if Age1 or Sex1 or Chestpaintype1 or FBSover or MaxHR1 or Exerciseangina1 or Cholesterol1 or BP1 or EKGresults1 or Thallium1 or STdepression1 or Numberofvesselsfluro1 or SlopeofST1 :
        p=model.predict([[Age1,Sex1,Chestpaintype1,FBSover1,MaxHR1,Exerciseangina1,Cholesterol1,BP1,EKGresults1,Thallium1,STdepression1,Numberofvesselsfluro1,SlopeofST1]])
        p2=model.predict_proba([[Age1,Sex1,Chestpaintype1,FBSover1,MaxHR1,Exerciseangina1,Cholesterol1,BP1,EKGresults1,Thallium1,STdepression1,Numberofvesselsfluro1,SlopeofST1]])
        print(p[0])
        p3=round(max(p2[0])*100,2)
        p4=str(p3)+" % "+str(p[0])
        lb6.configure(text=p4)
        
        txt1.delete(first=0,last=100)
        txt2.delete(first=0,last=100)
        txt3.delete(first=0,last=100)
        txt4.delete(first=0,last=100)
        txt5.delete(first=0,last=100)
        txt6.delete(first=0,last=100)
        txt7.delete(first=0,last=100)
        txt8.delete(first=0,last=100)
        txt9.delete(first=0,last=100)
        txt10.delete(first=0,last=100)
        txt11.delete(first=0,last=100)
        txt12.delete(first=0,last=100)
        txt13.delete(first=0,last=100)
            
        
    else:
        ms.showerror('Error!','Enter all the data')


    
    
    

    
def clear():
    txt1.delete(first=0,last=END)
    txt2.delete(first=0,last=END)
    txt3.delete(first=0,last=END)
    txt4.delete(first=0,last=END)
    txt5.delete(first=0,last=END)
    txt6.delete(first=0,last=END)
    txt7.delete(first=0,last=END)
    txt8.delete(first=0,last=END)
    txt9.delete(first=0,last=END)
    txt10.delete(first=0,last=END)
    txt11.delete(first=0,last=END)
    txt12.delete(first=0,last=END)
    txt13.delete(first=0,last=END)


    

lb1=Label(root,text="Age:",font=("Calibri",12),bg="#166969",fg="white")
lb1.grid(row=0,column=0,padx=5,pady=5)
txt1=Spinbox(root,textvariable=Age,from_=0.1, to=10.0,bd=5,font=("Calibri",12),bg="#166969",fg="white")
txt1.grid(row=0,column=1)

lb2=Label(root,text="Sex:",font=("Calibri",12),bg="#166969",fg="white")
lb2.grid(row=1,column=0,padx=5,pady=5)
txt2=Spinbox(root,textvariable=Sex,from_=0.1, to=10.0,bd=5,font=("Calibri",12),bg="#166969",fg="white")
txt2.grid(row=1,column=1)


lb3=Label(root,text="Chestpaintype:",font=("Calibri",12),bg="#166969",fg="white")
lb3.grid(row=2,column=0,padx=5,pady=5)
txt3=Spinbox(root,textvariable=Chestpaintype,from_=0.1, to=10.0,bd=5,font=("Calibri",12),bg="#166969",fg="white")
txt3.grid(row=2,column=1)


lb4=Label(root,text="FBSover",font=("Calibri",12),bg="#166969",fg="white")
lb4.grid(row=3,column=0,padx=5,pady=5)
txt4=Spinbox(root,textvariable=FBSover,from_=0, to=10.0,bd=5,font=("Calibri",12),bg="#166969",fg="white")
txt4.grid(row=3,column=1)


lb5=Label(root,text="MaxHR",font=("Calibri",12),bg="#166969",fg="white")
lb5.grid(row=4,column=0,padx=5,pady=5)
txt5=Spinbox(root,textvariable=MaxHR,from_=0.1, to=10.0,bd=5,font=("Calibri",12),bg="#166969",fg="white")
txt5.grid(row=4,column=1)

lb6=Label(root,text="Exerciseangina",font=("Calibri",12),bg="#166969",fg="white")
lb6.grid(row=5,column=0,padx=5,pady=5)
txt6=Spinbox(root,textvariable=Exerciseangina,from_=0, to=10.0,bd=5,font=("Calibri",12),bg="#166969",fg="white")
txt6.grid(row=5,column=1)

lb7=Label(root,text="Cholesterol",font=("Calibri",12),bg="#166969",fg="white")
lb7.grid(row=6,column=0,padx=5,pady=5)
txt7=Spinbox(root,textvariable=Cholesterol,from_=0.1, to=10.0,bd=5,font=("Calibri",12),bg="#166969",fg="white")
txt7.grid(row=6,column=1)

lb8=Label(root,text="BP",font=("Calibri",12),bg="#166969",fg="white")
lb8.grid(row=7,column=0,padx=5,pady=5)
txt8=Spinbox(root,textvariable=BP,from_=0.1, to=10.0,bd=5,font=("Calibri",12),bg="#166969",fg="white")
txt8.grid(row=7,column=1)

lb9=Label(root,text="EKGresults",font=("Calibri",12),bg="#166969",fg="white")
lb9.grid(row=8,column=0,padx=5,pady=5)
txt9=Spinbox(root,textvariable=EKGresults,from_=0.1, to=10.0,bd=5,font=("Calibri",12),bg="#166969",fg="white")
txt9.grid(row=8,column=1)

lb10=Label(root,text=" Thallium",font=("Calibri",12),bg="#166969",fg="white")
lb10.grid(row=9,column=0,padx=5,pady=5)
txt10=Spinbox(root,textvariable= Thallium,from_=0.1, to=10.0,bd=5,font=("Calibri",12),bg="#166969",fg="white")
txt10.grid(row=9,column=1)

lb11=Label(root,text="STdepression",font=("Calibri",12),bg="#166969",fg="white")
lb11.grid(row=10,column=0,padx=5,pady=5)
txt11=Spinbox(root,textvariable=STdepression,from_=0.1, to=10.0,bd=5,font=("Calibri",12),bg="#166969",fg="white")
txt11.grid(row=10,column=1)

lb12=Label(root,text="Numberofvesselsfluro",font=("Calibri",12),bg="#166969",fg="white")
lb12.grid(row=11,column=0,padx=5,pady=5)
txt12=Spinbox(root,textvariable=Numberofvesselsfluro,from_=0, to=10.0,bd=5,font=("Calibri",12),bg="#166969",fg="white")
txt12.grid(row=11,column=1)

lb13=Label(root,text=" SlopeofST",font=("Calibri",12),bg="#166969",fg="white")
lb13.grid(row=12,column=0,padx=5,pady=5)
txt13=Spinbox(root,textvariable= SlopeofST,from_=0.1, to=10.0,bd=5,font=("Calibri",12),bg="#166969",fg="white")
txt13.grid(row=12,column=1)







#btn1=Button(root,image=button_image,command=submit,bd=5)
#btn1.grid(row=5,column=1,padx=(0,0),pady=(30,30))
btn1=Button(root,text="predict",command=pred,bd=5,font=("Calibri",15),width=5,bg="green",activebackground="red")
btn1.grid(row=13,column=1,padx=(0,0),pady=(30,30))

btn2=Button(root,text="clear",command=clear,bd=5,font=("Calibri",15),width=5,bg="green",activebackground="red")
btn2.grid(row=13,column=2,padx=(0,0),pady=(30,30))


lb5=Label(root,text="The Prediction of heart disease is:",font=("Calibri",15),bg="#166969",fg="white")
lb5.grid(row=14,column=0,padx=15,pady=15)
lb6=Label(root,text="",bd=5,font=("Calibri",15),bg="#166969",fg="white")
lb6.grid(row=14,column=1)

print("PNT2022TMID28916 - SrishJeneJesshari")



#btn3=Button(root,text="Search",command=search,bd=5,font=("Calibri",24),width=10,bg="green",activebackground="red")
#btn3.grid(row=7,column=1,padx=(0,0),pady=(30,30))
##btn4=Button(root,text="Clear",command=clear2,bd=5,font=("Calibri",24),width=10,bg="green",activebackground="red")
#btn4.grid(row=7,column=2,padx=(0,0),pady=(30,30))

root.mainloop()
