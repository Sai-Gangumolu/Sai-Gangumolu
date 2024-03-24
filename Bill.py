from tkinter import *

root = Tk()
root.geometry("1000x500")
root.title("Grocery e-Bill Generator")
root.resizable(False,False)

#9.Reset

def Reset():
    entry_tomatoes.delete(0,END)
    
    entry_brinjals.delete(0,END)
    
    entry_onions.delete(0,END)
    
    entry_carrots.delete(0,END)
    
    entry_chillies.delete(0,END)
    
    entry_cucumbers.delete(0,END)
    entry_mushrooms.delete(0,END)

#6.Total

def Total():
    try:a1=int(tomatoes.get())
    except: a1=0

    try:a2=int(brinjals.get())
    except: a2=0

    try:a3=int(onions.get())
    except: a3=0

    try:a4=int(carrots.get())
    except: a4=0

    try:a5=int(chillies.get())
    except: a5=0

    try:a6=int(cucumbers.get())
    except: a6=0

    try:a7=int(mushrooms.get())
    except: a7=0

#7.Define cost of each item per quantity
    c1 = 300*a1
    c2 = 250*a2
    c3 = 200*a3
    c4 = 150*a4
    c5 = 100*a5
    c6 = 80*a6
    c7 = 80*a7

    lbl_total = Label(f2,font=('aria',20,'bold'),text="Total Bill",width=16,fg="black",bg="red")
    lbl_total.place(x=0,y=50)

    entry_total=Entry(f2,font=('aria',20,'bold'),textvariable=Total_bill,bd=6,width=15,bg="red")
    entry_total.place(x=20,y=100)

    totalcost=c1+c2+c3+c4+c5+c6+c7
    string_bill="₹",str('%.2f' %totalcost)
    Total_bill.set(string_bill)


Label(text = "Grocery e-Bill Generator",bg = "red", fg = "black", font = ("calibri", 33), width="300", height="2").pack()

#2.MENU CARD
f = Frame(root,bg = "skyblue",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)

Label(f,text="Menu", font=("Gabriola",40,"bold"),fg="black",bg="skyblue").place(x=80,y=0)

Label(f,font=("Lucida Calligraphy",15,'bold'),text="tomatoes.....Rs.300/kilo",fg="black",bg="skyblue").place(x=10,y=80)

Label(f,font=("Lucida Calligraphy",15,'bold'),text="brinjals.....Rs.250/kilo",fg="black",bg="skyblue").place(x=10,y=110)

Label(f,font=("Lucida Calligraphy",15,'bold'),text="onions.....Rs.200/kilo",fg="black",bg="skyblue").place(x=10,y=140)

Label(f,font=("Lucida Calligraphy",15,'bold'),text="carrots.....Rs.150/kilo",fg="black",bg="skyblue").place(x=10,y=170)

Label(f,font=("Lucida Calligraphy",15,'bold'),text="chillies.....Rs.100/kilo",fg="black",bg="skyblue").place(x=10,y=200)

Label(f,font=("Lucida Calligraphy",15,'bold'),text="cucumbers.....Rs.80/kilo",fg="black",bg="skyblue").place(x=10,y=230)

Label(f,font=("Lucida Calligraphy",15,'bold'),text="mushrooms.....Rs.80/kilo",fg="black",bg="skyblue").place(x=10,y=260)

#8.BILL
f2=Frame(root,bg="skyblue",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill=Label(f2,text="Checkout",font=('calibri',20),bg="red")
Bill.place(x=120,y=10)

#3.ENTRY WORK
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

tomatoes=StringVar()
brinjals=StringVar()
onions=StringVar()
carrots=StringVar()
chillies=StringVar()
cucumbers=StringVar()
mushrooms=StringVar()

Total_bill = StringVar()

#1.Label

lbl_tomatoes=Label(f1,font=("aria",20,"bold"),text = "tomatoes",width=12,fg="black")
lbl_brinjals=Label(f1,font=("aria",20,"bold"),text = "brinjals",width=12,fg="black")
lbl_onions=Label(f1,font=("aria",20,"bold"),text = "onions",width=12,fg="black")
lbl_carrots=Label(f1,font=("aria",20,"bold"),text = "carrots",width=12,fg="black")
lbl_chillies=Label(f1,font=("aria",20,"bold"),text = "chillies",width=12,fg="black")
lbl_cucumbers=Label(f1,font=("aria",20,"bold"),text = "cucumbers",width=12,fg="black")
lbl_mushrooms=Label(f1,font=("aria",20,"bold"),text = "mushrooms",width=12,fg="black")
lbl_tomatoes.grid(row=1,column=0)
lbl_brinjals.grid(row=2,column=0)
lbl_onions.grid(row=3,column=0)
lbl_carrots.grid(row=4,column=0)
lbl_chillies.grid(row=5,column=0)
lbl_cucumbers.grid(row=6,column=0)
lbl_mushrooms.grid(row=7,column=0)

#4.Entry

entry_tomatoes=Entry(f1,font=("aria",20,"bold"),textvariable=tomatoes,bd=6,width=8,bg="white")
entry_brinjals=Entry(f1,font=("aria",20,"bold"),textvariable=brinjals,bd=6,width=8,bg="white")
entry_onions=Entry(f1,font=("aria",20,"bold"),textvariable=onions,bd=6,width=8,bg="white")
entry_carrots=Entry(f1,font=("aria",20,"bold"),textvariable=carrots,bd=6,width=8,bg="white")
entry_chillies=Entry(f1,font=("aria",20,"bold"),textvariable=chillies,bd=6,width=8,bg="white")
entry_cucumbers=Entry(f1,font=("aria",20,"bold"),textvariable=cucumbers,bd=6,width=8,bg="white")
entry_mushrooms=Entry(f1,font=("aria",20,"bold"),textvariable=mushrooms,bd=6,width=8,bg="white")

entry_tomatoes.grid(row=1,column=1)
entry_brinjals.grid(row=2,column=1)
entry_onions.grid(row=3,column=1)
entry_carrots.grid(row=4,column=1)
entry_chillies.grid(row=5,column=1)
entry_cucumbers.grid(row=6,column=1)
entry_mushrooms.grid(row=7,column=1)

#5.Buttons

btn_reset=Button(f1,bd=5,fg="black",bg="red",font=("ariel",16,'bold'),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="red",font=("ariel",16,"bold"),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)

root.mainloop()
