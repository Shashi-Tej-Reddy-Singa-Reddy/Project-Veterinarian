from tkinter import *
import tkinter.font as tkFont
import tkinter.messagebox as tkMessageBox
from tkinter import filedialog
import tkinter.ttk as ttk
import csv
import os
from turtle import left, width
from importlib.resources import path
from pickle import TRUE
from turtle import update
import pandas  as pd
import numpy as np
import xlwings as xw
import cv2

root = Tk()
root.title("Veternian")
root.geometry('720x480')
arr=[]
MyFont = tkFont.Font(family="Times New Roman", size=35, weight="bold")
devfont= tkFont.Font(family="Times New Roman", size=23, weight="bold")

data = [['animal ID','food','temp','atm temp','ww','medicine','injuries','budget']]

fd = open('report.csv', 'w',newline='')
# try:
writer = csv.writer(fd, dialect='excel')
writer.writerows(data)

# finally:
fd.close()

lbl = Label(root, text = "ZOO")
lbl.configure(font = MyFont)
lbl.place(relx = 0.5, rely = 0.1, anchor = CENTER)

# lbl1 = Label(root, text = "x")
# lbl1.configure(font = devfont)
# lbl1.place(relx = 0.5, rely = 0.2, anchor = CENTER)


lbluser = Label(root, text = "Organisation Name")
lbluser.place(rely=0.35,relx=0.4,anchor=CENTER)
lblpass = Label(root, text = "Location ")
lblpass.place(rely=0.4,relx=0.4,anchor=CENTER)

username = Entry(root,width=20)
username.place(rely=0.35,relx=0.57,anchor=CENTER)
pasword= Entry(root,width=20)
pasword.place(rely=0.4,relx=0.57,anchor=CENTER)
def isChecked():
    if cb.get() == 1:
        btn['state'] = NORMAL
        btn.configure(text='Sign in')
    elif cb.get() == 0:
        btn['state'] = DISABLED
        btn.configure(text='Sign in')
    else:
        tkMessageBox.showerror('PythonGuides', 'Something went wrong!')

cb = IntVar()
us1=StringVar
us2=StringVar
def poty():
    us1=username.get()
    us2=pasword.get()
    if us1=="" and us2=="":
        prowin= Toplevel(root)
        prowin.title("Admin")
        prowin.geometry("720x480")
        
        lbl = Label(prowin, text = "SARDAR'S ZOO")
        lbl.configure(font = MyFont)
        lbl.place(relx = 0.5, rely = 0.1, anchor = CENTER)

        lbl1 = Label(prowin, text = "Administrator")
        lbl1.configure(font = devfont)
        lbl1.place(relx = 0.5, rely = 0.2, anchor = CENTER)
        loadbtn=Button(prowin,font=devfont,text ="upload",width=15,command = uploadwindow)
        loadbtn.place(relx = 0.5, rely = 0.35, anchor = CENTER)

        upbtn = Button(prowin,font=devfont,text ="Update details",width=15,command = updatewindow)
        upbtn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        cambtn = Button(prowin,font=devfont,text ="View camera",width=15,command = camwindow)
        cambtn.place(relx = 0.5, rely = 0.65, anchor = CENTER)

        dbtn = Button(prowin,font=devfont,text ="know develepers",width=15,command = developerwindow)
        dbtn.place(relx = 0.5, rely = 0.80, anchor = CENTER)
    else:
        lblpas1 = Label(root, text = "Invalid org. name or address",fg='red')
        lblpas1.place(rely=0.6,relx=0.48,anchor=CENTER)
tempo=StringVar()
Checkbutton(root,text="accept T&C",variable=cb,onvalue=1,offvalue=0,command=isChecked).place(rely=0.5,relx=0.5,anchor=CENTER)
btn = Button(root,text='Sign in',state=DISABLED,command=poty)
btn.place(rely=0.55,relx=0.5,anchor=CENTER)

def uploadwindow():
    file1=filedialog.askopenfilename()
    tempo=file1.get()
    file1.close()
    
def developerwindow():
    devwin = Toplevel(root)
    devwin.title("GG")
    devwin.geometry("720x480")
    Label(devwin,font=MyFont,text ="<<-----DEVELOPERS----->>").place(relx = 0.5, rely = 0.1,anchor=CENTER)
    Label(devwin,font=MyFont,text ="Vishnu Dath").place(relx = 0.5, rely = 0.3,anchor=CENTER)
    Label(devwin,font=MyFont,text ="Shashi Tej Reddy").place(relx = 0.5, rely = 0.4,anchor=CENTER)

def updatewindow():
    
    upwin=Toplevel(root)
    upwin.title("Update Portal")
    upwin.geometry("1920x1080")
    MyFonter= tkFont.Font(family="Times New Roman", size=50, weight="bold")
    

    def updateitem():
    
        e1=combox.get()
        e2=entry2.get()
        e3=entry3.get()
        e4=entry4.get()
        e5=entry5.get()
        e6=entry6.get()
        e7=M7.get()
        e8=entry8.get()
        if combox.get()=="" and entry2.get()=="" and entry3.get()=="" and entry4.get()=="" and entry5.get()=="" and entry6.get()=="" and entry8.get()=="" :

            print("Error") 
            tkMessageBox.showerror("error","there is issue with some information")

        else:
                result=tkMessageBox.askquestion("Submit","You are about to update details\n" )
        if(result =="yes"):
            print("here")
            with open("report.csv","r") as f1 ,open("report1.csv", "w") as working:
                for line in f1:
                    if str(e1) not in line:
                        working.write(line)
                    else:
                        working.write(('{0},{1},{2},{3},{4},{5},{6},{7}\n'.format(str(e1),e2,e3,str(e4),str(e5),e6,e7,e8)))
            os.remove("report.csv")
            os.rename("report1.csv", "report.csv")
            combox.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry6.delete(0, END)
            M7.set("")
            entry8.delete(0, END)
        p='report.csv'
        c=open(p)
        d=csv.reader(c,delimiter=',')
        l2=[]
        for i in d:
            l2.append(i)
        del l2[0]
        tv = ttk.Treeview(upwin, columns=(1, 2, 3,4,5,6,7,8), show='headings' ,height=8)
        tv.place(relx=0.7,rely=0.5,anchor=CENTER)

            

        for i in range(len(l2)):
            tv.insert(parent='', index=i, iid=i, values=(l2[i][0],l2[i][1],l2[i][2],l2[i][3],l2[i][4],l2[i][5],l2[i][6],l2[i][7]))
        tv.column("# 1",anchor=CENTER, stretch=NO, width=130)
        tv.column("# 2",anchor=CENTER, stretch=NO, width=130)
        tv.column("# 3",anchor=CENTER, stretch=NO, width=130)
        tv.column("# 4",anchor=CENTER, stretch=NO, width=130)
        tv.column("# 5",anchor=CENTER, stretch=NO, width=130)
        tv.column("# 6",anchor=CENTER, stretch=NO, width=130)
        tv.column("# 7",anchor=CENTER, stretch=NO, width=130)
        tv.column("# 8",anchor=CENTER, stretch=NO, width=130)
        tv.heading(1, text="Name")
        tv.heading(2, text="Food")
        tv.heading(3, text="Tmp")
        tv.heading(4, text="Atm T")
        tv.heading(5, text="Water(w)")
        tv.heading(6, text="medicine taken")
        tv.heading(7, text="Injuries")
        tv.heading(8, text="Bugdet Spent")
    
    
    def deleteitem():
        e1=combox.get()
        e2=entry2.get()
        e3=entry3.get()
        e4=entry4.get()
        e5=entry5.get()
        e6=entry6.get()
        e7=M7.get()
        e8=entry8.get()
        if combox.get()=="" and entry2.get()=="" and entry3.get()=="" and entry4.get()=="" and entry5.get()=="" and entry6.get()=="" and entry8.get()=="" :
            print("Error")
            tkMessageBox.showerror("error","there is issue with some information")
        else:
            result=tkMessageBox.askquestion("Submit","You are about to delete \n" + e1 )

            if(result =="yes"):
                print("here")
                with open("report.csv", 'r') as f, open("report1.csv",  "w") as w1:
                    for line in f:
                        if e1 not in line:
                            w1.write(line)
                os.remove("report.csv")
                os.rename("report1.csv", "report.csv")
                f.close()
                w1.close()
                combox.delete(0, END)
        p='report.csv'
        c=open(p)
        d=csv.reader(c,delimiter=',')
        l2=[]
        for i in d:
            l2.append(i)
        del l2[0]
        tv = ttk.Treeview(upwin, columns=(1, 2, 3,4,5,6,7,8), show='headings' ,height=8)
        tv.place(relx=0.7,rely=0.5,anchor=CENTER)

        for i in range(len(l2)):
            tv.insert(parent='', index=i, iid=i, values=(l2[i][0],l2[i][1],l2[i][2],l2[i][3],l2[i][4],l2[i][5],l2[i][6],l2[i][7]))

        # for i in range(len(l2)-2):
        #     tv.insert(parent='', index=i, iid=i, values=(l2[i+2][0],l2[i+2][1],l2[i+2][2],l2[i+2][3],l2[i+2][4],l2[i+2][5],l2[i+2][6],l2[i+2][7]))
        tv.column("# 1",anchor=CENTER, stretch=NO, width=130)
        tv.column("# 2",anchor=CENTER, stretch=NO, width=130)
        tv.column("# 3",anchor=CENTER, stretch=NO, width=130)
        tv.column("# 4",anchor=CENTER, stretch=NO, width=130)
        tv.column("# 5",anchor=CENTER, stretch=NO, width=130)
        tv.column("# 6",anchor=CENTER, stretch=NO, width=130)
        tv.column("# 7",anchor=CENTER, stretch=NO, width=130)
        tv.column("# 8",anchor=CENTER, stretch=NO, width=130)
        tv.heading(1, text="Name")
        tv.heading(2, text="Food")
        tv.heading(3, text="Tmp")
        tv.heading(4, text="Atm T")
        tv.heading(5, text="Water(w)")
        tv.heading(6, text="medicine taken")
        tv.heading(7, text="Injuries")
        tv.heading(8, text="Bugdet Spent")
        
    
    
    def clearitem():
        combox.delete(0, END)
        entry2.get()
        entry3.get()
        entry4.get()
        entry5.get()
        entry6.get()
        M7.get()
        entry8.get()
        
    def additem():
        e1=combox.get()
        e2=entry2.get()
        e3=entry3.get()
        e4=entry4.get()
        e5=entry5.get()
        e6=entry5.get()
        e7=M7.get()
        e8=entry8.get()
        if combox.get()=="" and entry2.get()=="" and entry3.get()=="" and entry4.get()=="" and entry5.get()=="" and entry6.get()=="" and  entry8.get()=="":

            print("Error")
            tkMessageBox.showerror("error","there is issue with some information")

        else:
            result=tkMessageBox.askquestion("Submit","You are about to enter following details\n" )
            combox.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry6.delete(0, END)
            entry8.delete(0, END)
            if(result =="yes"):
                print("here")
                with open("report.csv", 'a',newline='') as csvfile:
                    csvfile.write('{0},{1},{2},{3},{4},{5},{6},{7}\n'.format(str(e1),e2,e3,str(e4),str(e5),e6,e7,e8))   
                csvfile.close()
            else:
                combox.set("")
                entry2.set("")
                entry3.set("")
                entry4.set("")
                entry5.set("")
                entry6.set("")
                entry8.set("")
                

        p='report.csv'
        c=open(p)
        d=csv.reader(c,delimiter=',')
        l2=[]
        for i in d:
            l2.append(i)
        del l2[0]
        tv = ttk.Treeview(upwin, columns=(1, 2, 3,4,5,6,7,8), show='headings' ,height=8)
        tv.place(relx=0.7,rely=0.5,anchor=CENTER)

            
        for i in range(len(l2)):
            tv.insert(parent='', index=i, iid=i, values=(l2[i][0],l2[i][1],l2[i][2],l2[i][3],l2[i][4],l2[i][5],l2[i][6],l2[i][7]))
        # for i in range(len(l2)-2):
        #     tv.insert(parent='', index=i, iid=i, values=(l2[i+2][0],l2[i+2][1],l2[i+2][2],l2[i+2][3],l2[i+2][4],l2[i+2][5],l2[i+2][6],l2[i+2][7]))
            
        tv.column("# 1",anchor=CENTER, stretch=NO, width=130)
        tv.column("# 2",anchor=CENTER, stretch=NO, width=130)
        tv.column("# 3",anchor=CENTER, stretch=NO, width=130)
        tv.column("# 4",anchor=CENTER, stretch=NO, width=130)
        tv.column("# 5",anchor=CENTER, stretch=NO, width=130)
        tv.column("# 6",anchor=CENTER, stretch=NO, width=130)
        tv.column("# 7",anchor=CENTER, stretch=NO, width=130)
        tv.column("# 8",anchor=CENTER, stretch=NO, width=130)
        tv.heading(1, text="Name")
        tv.heading(2, text="Food")
        tv.heading(3, text="Tmp")
        tv.heading(4, text="Atm T")
        tv.heading(5, text="Water(w)")
        tv.heading(6, text="medicine taken")
        tv.heading(7, text="Injuries")
        tv.heading(8, text="Bugdet Spent")


    M1 = StringVar()
    M2 = StringVar()
    M3 = StringVar()
    M4= StringVar()
    M5=StringVar()
    M6= StringVar()
    M7 = StringVar()
    M8 = StringVar()

    

    txt_title = Label(upwin,width=10,text = "ZOO")
    txt_title.configure(font = MyFonter)
    txt_title.place(relx=0.5,rely=0.07,anchor=CENTER)
    label0 = Label(upwin, text="Name of the animal:", bd=15)
    label0.place(relx=0.12,rely=0.2,anchor=CENTER)
    label2 = Label(upwin, text="Food taken:", bd=15)
    label2.place(relx=0.12,rely=0.24,anchor=CENTER)
    label4 = Label(upwin, text="Temperature of animal(°C):", bd=15)
    label4.place(relx=0.12,rely=0.28,anchor=CENTER)
    label5 = Label(upwin, text="Atmospheric temperature(°C):", bd=15)
    label5.place(relx=0.12,rely=0.32,anchor=CENTER)
    label6 = Label(upwin, text="Water weight:", bd=15)
    label6.place(relx=0.12,rely=0.36,anchor=CENTER)
    label8 = Label(upwin, text="Medicine:", bd=15)
    label8.place(relx=0.12,rely=0.40,anchor=CENTER)
    label9 = Label(upwin, text="Injuries(if any):", bd=15)
    label9.place(relx=0.12,rely=0.44,anchor=CENTER)
    labe21 = Label(upwin, text="Bugdet Spent:", bd=15)
    labe21.place(relx=0.12,rely=0.48,anchor=CENTER)
    
    
    
        

    combox = ttk.Combobox(upwin, width = 27,textvariable = M1)
    combox['values'] = ('tigNT1','lioNL2','eleVE3','girVG4','spaBS5')
    combox.place(relx=0.26,rely=0.2,anchor=CENTER)
    
    
    
    entry2 = ttk.Combobox(upwin, textvariable=M2, width=27)
    entry2['values']=('red meat','carcass','fruits','grass','nuts')
    entry2.place(relx=0.26,rely=0.24,anchor=CENTER)
    entry3 = ttk.Combobox(upwin, textvariable=M3, width=27)
    entry3['values']=tuple(int(x) for x in range(30,130))
    entry3.place(relx=0.26,rely=0.28,anchor=CENTER)
    entry4 = ttk.Combobox(upwin, textvariable=M4, width=27)
    entry4['values']=tuple(int(x) for x in range(12,100))
    entry4.place(relx=0.26,rely=0.32,anchor=CENTER)
    entry5 = ttk.Combobox(upwin, textvariable=M5, width=27)
    entry5['values']=tuple(int(x) for x in range(1,40))
    entry5.place(relx=0.26,rely=0.36,anchor=CENTER)
    entry6 = ttk.Combobox(upwin, textvariable=M6, width=27)
    entry6['values']=('protozoal','protimal','cartozoal','setatie','costin')
    entry6.place(relx=0.26,rely=0.40,anchor=CENTER)
    
    r1=Radiobutton(upwin,text="yes",value="YES",variable=M7).place(relx=0.26,rely=0.44,anchor=CENTER)
    r2=Radiobutton(upwin,text="no",value="NO",variable=M7).place(relx=0.29,rely=0.44,anchor=CENTER)
    
    entry8 = Entry(upwin, textvariable=M8, width=30)
    entry8.place(relx=0.26,rely=0.48,anchor=CENTER)

    def resulter():
        label08= Label(upwin, text="Result Generated",fg='red')
        label08.place(relx=0.18,rely=0.75,anchor=CENTER)
        book1_path = "C:\\Users\\uvrao\\OneDrive\\Desktop\\finaldance\\doctor.csv"
        book2_path = "C:\\Users\\uvrao\\OneDrive\\Desktop\\finaldance\\report.csv"
        df_initial = pd.read_csv(book1_path)
        df_final = pd.read_csv(book2_path)
        # difference = df_final.compare(df_initial, align_axis=0)
        # difference = df_final.compare(df_initial, align_axis=1)
        difference = df_final.compare(df_initial, keep_shape=True, keep_equal=False)
        # difference = df_final.compare(df_initial, keep_shape=True,keep_equal=True)
        difference.to_csv("C:\\Users\\uvrao\\OneDrive\\Desktop\\finaldance\\final.csv")
        difference=difference[difference.columns[2::]]
        difference[difference.columns[0]]=df_initial[df_initial.columns[0]]
        difference[difference.columns[1]]=df_initial[df_initial.columns[1]]
        a=list(difference.columns)
        b=list(df_initial.columns)
        a[0],a[1]=b[0],b[1]
        for i in range(len(difference.columns)):
            difference.columns.values[i]=a[i]
        difference.replace(np.nan,'ok')
        difference.to_csv("C:\\Users\\uvrao\\OneDrive\\Desktop\\finaldance\\final.csv")
        print(difference)


    
  
    
    def newbox():
        newwin=Toplevel(root)
        newwin.title("Exit portal")
        newwin.geometry("1080x720")
        def certcloser():
            newwin.destroy()
            newwin.update()
        Label(newwin,font=MyFont,text ="....DONE SUBMITTING.....").pack()
        btn = Button(newwin,width=15,font=devfont,text='Exit on logout',command=closer)
        btn.place(rely=0.6,relx=0.5,anchor=CENTER)
        btn1 = Button(newwin,width=15,font=devfont,text='<--BACK',command=certcloser)
        btn1.place(rely=0.4,relx=0.5,anchor=CENTER)
    
    btnadd = Button(upwin, width=10, text="ADD", command=additem)
    btnadd.place(relx=0.12,rely=0.56,anchor=CENTER)  
    btnadd2 = Button(upwin, width=10, text="UPDATE", command=updateitem)
    btnadd2.place(relx=0.18,rely=0.56,anchor=CENTER)
    btnadd4 = Button(upwin, width=10, text="CLEAR", command=clearitem)
    btnadd4.place(relx=0.24,rely=0.56,anchor=CENTER)
    btnadd3 = Button(upwin, width=10, text="RESULT", command=resulter)
    btnadd3.place(relx=0.18,rely=0.63,anchor=CENTER) 
    btnadd4 = Button(upwin, width=10, text="DELETE", command=deleteitem)
    btnadd4.place(relx=0.12,rely=0.63,anchor=CENTER) 
    btnadd1 = Button(upwin, width=10, text="EXIT", command=newbox)
    btnadd1.place(relx=0.24,rely=0.63,anchor=CENTER)
    

def closer():
    root.destroy()

def camwindow():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)
    while True:
        _, img = cap.read()


        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray,1.1,4)

        for (x,y,w,h)in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h) , (255,0,0))

        cv2.imshow('img',img)
        k = cv2.waitKey()
        if k==5:
            break

    
    

root.mainloop()