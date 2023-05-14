# ======================= بسم الله الرحمن الرحيم =======================
# ============ Management Student Program => برنامج ادارة الطلاب =========

# ============ Import Modules ==========

from tkinter import *
# === For  ComboBox ===
from tkinter import ttk

# ===== Main Class ========

class Student:
    # ===== Initialize Program Function ====
    def __init__(self,root):
        self.root = root
        self.root.geometry('1270x950+0+0')
        self.root.title('Student Management [System]')
        self.root.config(background='silver')
        self.root.resizable(False,False)

        # ====== Main Title Of Program ======
        p_title = Label(root,text='[Student Management System]',bg='#2874A6',fg='white',font=('System',15))
        p_title.pack(fill=X)
        # Student Information Frame
        SI = Frame (root,width='318',height='500')
        SI.place(x=950,y='25')
        # Labels And Entrys
        idS = Entry(SI,justify='center',bd=2)
        idS.place(x=100,y=30)
        idS_lbl = Label (SI,text='Student ID',fg='Black',font=('Arial',12))
        idS_lbl.place(x=120,y=5)
        nameS = Entry(SI,justify='center',bd=2)
        nameS.place(x=100,y=80)
        nameS_lbl = Label (SI,text='Student Name',fg='Black',font=('Arial',12))
        nameS_lbl.place(x=110,y=55)
        emailS = Entry(SI,justify='center',bd=2)
        emailS.place(x=100,y=140)
        emailS_lbl = Label (SI,text='Student Email',fg='Black',font=('Arial',12))
        emailS_lbl.place(x=110,y=110)
        PhoneS = Entry(SI,justify='center',bd=2)
        PhoneS.place(x=100,y=190)
        PhoneS_lbl = Label (SI,text='Student Phone',fg='Black',font=('Arial',12))
        PhoneS_lbl.place(x=110,y=160)
        LevelS = Entry(SI,justify='center',bd=2)
        LevelS.place(x=100,y=250)
        LevelS_lbl = Label (SI,text='Student Level',fg='Black',font=('Arial',12))
        LevelS_lbl.place(x=110,y=220)
        GenderS = ttk.Combobox(SI,values = ['Male','Female'],width='17')
        GenderS.place(x=100,y=310)
        GenderS_lbl = Label (SI,text='Student Gender',fg='Black',font=('Arial',12))
        GenderS_lbl.place(x=105,y=280)
        AdressS = Entry(SI,justify='center',bd=2)
        AdressS.place(x=100,y=370)
        AdressS_lbl = Label (SI,text='Student Address',fg='Black',font=('Arial',12))
        AdressS_lbl.place(x=110,y=340)
        DeleteSByName = Entry(SI,width='30',justify='center',bd=2)
        DeleteSByName.place(x=100,y=420)
        DeleteSByName_lbl = Label (SI,text='Delete Student By Name',fg='red',font=('Arial',13))
        DeleteSByName_lbl.place(x=100,y=395)

        # Frame Admin Title Label
        AF = Label(root,text='Control Panel',width='37',bg='#3498DB',fg='White',font=('System'),bd=5)
        AF.place(x=957,y=529)

        # Admin Frame [Controlling Buttons]
        ACB = Frame (root,width='318',height='395',bg='white')
        ACB.place(x=950,y='560')

        ADDS = Button(ACB,text='Add Student',width=40,background='#273746',foreground='White',bd=5)
        ADDS.place(x=15,y=15)

        ADDS = Button(ACB,text='Delete Student',width=40,background='#273746',foreground='White',bd=5)
        ADDS.place(x=15,y=100)

        ADDS = Button(ACB,text='Student Information Edit',width=40,background='#273746',foreground='White',bd=5)
        ADDS.place(x=15,y=150)

        ADDS = Button(ACB,text='Clear Entrys',width=40,background='#273746',foreground='White',bd=5)
        ADDS.place(x=15,y=200)

        ADDS = Button(ACB,text='About',width=40,background='#273746',foreground='White',bd=5)
        ADDS.place(x=15,y=250)

        ADDS = Button(ACB,text='Exit Program <3',width=40,background='#273746',foreground='White',bd=5)
        ADDS.place(x=15,y=340)


root = Tk()
object = Student(root)
root.mainloop()