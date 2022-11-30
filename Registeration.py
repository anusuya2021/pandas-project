import tkinter as tk  
from functools import partial
from tkinter import messagebox
import csv
def clear():
    e1.delete(0,tk.END)
    e3.delete(0,tk.END)
def register(n1,n2):
    check1=-2
    check2=-2
    us=(n1.get())
    pa=(n2.get())
    if len(us)==0 :
        tk.messagebox.showinfo("Login/Register","user id is empty")
    else:
        check1=valid_us(us)
    if len(pa)==0:
        tk.messagebox.showinfo("Login/Register","Password is empty")
    else:
        check2=valid_pa(pa)
    
    if check1==0 and check2==0:
        file_append(us,pa)
    clear()
    return
def valid_us(us):
    va=0
    ats=-1
    dos=-1
    if '@' in us:
        ats=us.index('@')
        dos=us.index('.')
    else:
        tk.messagebox.showinfo("Username","@ is missing")
        va=-1
    if ats>dos and va==0:
        tk.messagebox.showinfo("Username","Invalid Email")
        va=-1
    if ats==0 and va==0:
        tk.messagebox.showinfo("Username",". is missing")
        va=-1
    if ats+1 == dos and va==0:
        tk.messagebox.showinfo("Validation","Invalid Email")
        va=-1
    asc = ord(us[0])
    if asc >= 65 and asc <= 90:
        pass
    elif asc >=97 and asc <=122:
        pass
    else:
        tk.messagebox.showinfo("Validation","Invalid Email")
        va=-1
    return va
def valid_pa(pa):
    va=0
    upp =0
    low =0
    spe = 0
    dig=0
    inv=0
    if (len(pa)<=5 or len(pa)>=16):
        tk.messagebox.showinfo("Password","Password length:6-15")
        va1=-1
    else:
        for i in pa:
            if ord(i)>=32 and ord(i)<=126:
                if ord(i)>=95 and ord(i)<=122:
                    low=low+1
                elif ord(i) >=65 and ord(i) <=90:
                    upp = upp+1
                elif ord(i) >=48 and ord(i)<=57:
                    dig=dig+1
                else:
                    spe = spe+1
            else:
                    inv=inv+1
    
    if low==0:
         tk.messagebox.showinfo("Password","Lower case alphabet missing")
         va=-1
    if upp==0:
         tk.messagebox.showinfo("Password","Missing-uppercase alphabet")
         va=-1
         
    if dig==0:
         tk.messagebox.showinfo("Password","Missing-digit")
         va=-1
    if spe ==0:
         tk.messagebox.showinfo("Paasword","Missing-special character")
         va=-1
    if inv>0 :
         tk.messagebox.showinfo("Validation","Invalid Password")
         va = -1
    return va
        
def login(n1,n2):
    check1=-2
    check2=-2
    us=(n1.get())
    pa=(n2.get())
    if len(us)==0 :
        tk.messagebox.showinfo("Login/Register","user id is empty")
    elif len(pa)==0:
        tk.messagebox.showinfo("Login/Register","Password is empty")
    else:
        check_entry(us,pa)
    clear()
    return
def forget(n1,n2):
    flag =-1
    us=(n1.get())
    pa=(n2.get())
    if len(us)==0 :
        tk.messagebox.showinfo("Login/Register","user id is empty")
    else:
        with open("id_data.csv",'r') as F:
            reader = csv.reader(F)
            user=[]
            pawo=[]
            for row in reader:
                if us == row[0]:
                   pas = row[1] 
                   flag=1
                   break
    F.close()
    if flag ==1:
           tk.messagebox.showinfo("Login","Password="+pas)
    else:
           tk.messagebox.showinfo("Login","Id is not found. Register your id")
    clear()
    return
def file_append(us,pa):
    with open("id_data.csv",'a',newline='') as F:
        writer = csv.writer(F)
        writer.writerow([us,pa])
        tk.messagebox.showinfo("Registration","Registeration is successful")
        
    F.close()
def check_entry(us,pa):
       flag =-1
       with open("id_data.csv",'r') as F:
            reader = csv.reader(F)
            user=[]
            pawo=[]
            for row in reader:
                if us == row[0] and pa == row[1] :
                   flag=1
                   break
       F.close()
       if flag ==1:
           tk.messagebox.showinfo("Login","Login successful")
       else:
           tk.messagebox.showinfo("Login","Id is not found. Register your id")
           
   
top=tk.Tk()
top.geometry("400x250")
top.title("Login form")
n1 = tk.StringVar()  
n2 = tk.StringVar()
tit=tk.Label(top,text="LOGIN",font=("Arial Bold",15) ).place(x=150,y=20)
name = tk.Label(top, text = "User Name/Email",font=("Arial Bold",13)).place(x = 30,y = 50)  
password = tk.Label(top, text = "Password",font=("Arial Bold",13)).place(x = 30, y = 100)  
e1 = tk.Entry(top,width=20,font=("Arial Bold",13),textvariable=n1)
e1.place(x = 200, y = 50)  
e3 = tk.Entry(top,width=20,font=("Arial Bold",13),textvariable=n2)
e3.place(x = 200, y = 100)
labelResult = tk.Label(top)  
labelResult.grid(row=7, column=2)  
register=partial(register,n1,n2)
login=partial(login,n1,n2)
forget=partial(forget,n1,n2)
b1=tk.Button(top,text="Register",font=("Arial Bold",13),command=register).place(x=50,y=140)
b2=tk.Button(top,text="Login",font=("Arial Bold",13),command=login).place(x=250,y=140)
b3=tk.Button(top,text="Forget Password",font=("Arial Bold",13),command=forget).place(x=115,y=200)
top.mainloop()  
