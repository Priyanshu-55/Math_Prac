#*** THUNDERSTARK ***

# Modules
from tkinter import *
from tkinter import ttk
import random
from playsound import playsound

#Window screen
root=Tk()
root.maxsize(800,800)
root.minsize(1400,1000)
root.title("MathPrac")
root.iconbitmap(r"C:\Thunderstark\study\bekar\MathPrac\logo.ico")
#Colors
def light_color():
    light_colors=['#e6e6ff','#9999e6','#ecb3ff','#ff99cc','#ff9999','#99ffd6']
    tm=random.choice(light_colors)
    return tm
def label_color():
        ligt_clr_label=['#db70b8','#c266ff','#bbbb77','#4dffb8','#4da6ff','#ff33bb','#ff1ac6','#00ff00']
        tm=random.choice(ligt_clr_label)
        return tm
def dark_color():
    dark_colors=['#990000','#997300','#269900','#009999','#730099','#99004d','#990000','#141452','#7a0099']
    tm=random.choice(dark_colors)
    return tm

def btn_sound():
    playsound(r"C:\Thunderstark\study\bekar\MathPrac\mouse_sound.mp3",block=False)
playsound(r"C:\Thunderstark\study\bekar\MathPrac\bg_sound.mp3",block=False)


#bg 
bglbl=Label(root)
bglbl.place(x=0,y=0,height=1000,width=1400)


   
# ************************************************First Plate Labels   *************************************************
#first Plate
# frstplt=Label(root,bg="Green")
# frstplt.place(x=50,y=50,height=250,width=1300)

#type Label
typlbl=Label(root,text="TYPE",font=("Broadway",30),fg='#007399')
typlbl.place(x=50,y=50,height=80,width=300)

#type combobox
typbox=ttk.Combobox(root,font=("Broadway",30))
typbox.place(x=400,y=60,height=60,width=600)

#********************TYPE COMBOBOX DATA**************
typbox['state']='readonly'
typbox['values']=['ALL','ADDITION','SUBTRACTION','MULTIPLICATION','DIVISION']
#****************************************************

#Range Label
rnglbl=Label(root,text="RANGE ",font=("Broadway",30),bg="black",fg='#007399')
rnglbl.place(x=50,y=140,height=70,width=300)

#RANGE combobox
global rngbox
rngbox=ttk.Combobox(root,font=("Broadway",30))
rngbox.place(x=400,y=150,height=60,width=600)

#********************RANGE COMBOBOX DATA***********************************
rngbox['state']='readonly'
rngbox['values']=["2 Digit","3 Digit","4 Digit","CUSTOM"]
#**************************************************************************

#********************RANGE DATA LABEL***************************************
#             From         
frmlbl=Label(root,text="From",font=("Broadway",30),bg="black",fg='#007399')
frmlbl.place(x=50,y=220,height=80,width=300)

frmrngent=Entry(root,font=("Broadway",30),bg="black",fg='#007399',state='disable')
frmrngent.place(x=400,y=230,height=60,width=100)
#             To        
tolbl=Label(root,text="To",font=("Broadway",30),bg="black",fg='#007399')
tolbl.place(x=550,y=220,height=80,width=300)

torngent=Entry(root,font=("Broadway",30),bg="black",fg='#007399',state='disable')
torngent.place(x=900,y=230,height=60,width=100)
#*****************************************************************************
global var_rngbox_out,var_type_out
var_rngbox_out=None
var_type_out=None
def showcustom():
    global rngbox,var_rngbox_out,var_type_out
    tm=rngbox.get()
    var_type_out=typbox.get()
    if tm=="CUSTOM":
        var_rngbox_out='CUSTOM'
        frmrngent.config(state='normal')
        torngent.config(state='normal')
    elif tm=='2 Digit':
        var_rngbox_out='2 Digit'
        frmrngent.config(state='disable')
        torngent.config(state='disable')
    elif tm=='3 Digit':
        var_rngbox_out='3 Digit'
        frmrngent.config(state='disable')
        torngent.config(state='disable')
    elif tm=='4 Digit':
        var_rngbox_out='4 Digit'
        frmrngent.config(state='disable')
        torngent.config(state='disable')
    else:
        frmrngent.config(state='disable')
        torngent.config(state='disable')
    frmrngent.after(1000,showcustom)
showcustom()
#use after function in tkinter to change color 
#Points 
pntslbl=Label(root,text="POINTS",font=("Stencil",40),bg="black",fg="red")
pntslbl.place(x=1050,y=50,height=90,width=300)
#points
global points
points=0

relpntslbl=Label(root,text=points,font=("Vivaldi",60),bg="black",fg="red")
relpntslbl.place(x=1050,y=140,height=150,width=300)


# ************************************************END OF FIRST PLATE******************************************************



#************************************************Variables ****************************************************************

#Num1 and Num2 variables
global num1,num2,oprt,fnresult,resultlst,rng_to,rng_from
num1=None
num2=None
oprt=None

#Range
rng_from=0
rng_to=0
#**************
#range for num1 and num2
def rangenums():
    global var_rngbox_out,rng_from,rng_to
    if var_rngbox_out=='2 Digit':
        rng_from=0
        rng_to=99
    elif var_rngbox_out=='3 Digit':
        rng_from=100
        rng_to=999
    elif var_rngbox_out=='4 Digit':
        rng_from=1000
        rng_to=9999
    else:
        tm1=frmrngent.get()
        tm2=torngent.get()
        rng_from=int(tm1)
        rng_to=int(tm2)
def newoprt():
    global oprt,var_type_out
    if var_type_out=='DIVISION':
        tm='/'
    elif var_type_out=="ADDITION":
        tm="+"
    elif var_type_out=='SUBTRACTION':
        tm='-'
    elif var_type_out=='MULTIPLICATION':
        tm='*'
    else:
        tm=random.choice(["+","-","*","/"])
    oprt=tm
fnresult=0
resultlst=[None,None,None,None]

#Random no. and operator generator
#random no. for num1
def rangen1():
    global num1,rng_from,rng_to
    a=random.randint(rng_from,rng_to)
    num1=a
    return a
#random no. for num2
def rangen2():
    global num2,rng_from,rng_to
    b=random.randint(rng_from,rng_to)
    num2=b
    return b

#random no.
def randnum():
    a=random.randint(1,99)
    return a

#calculation for +-*/
def calculation(a,op,b):
    if op=="+":
        return a+b
    elif op=="-":
        return a-b
    elif op=="*":
        return a*b
    elif op=="/":
        return round(a/b,2)

#result
def reslt():
    global fnresult,oprt
    fnresult=calculation(num1,oprt,num2)
    return fnresult

# ************************************************SECOND Plate Labels   **************************************************

#Question Label plate
#size (x=50) (y=350) (height=150) (width=1300)

#Num1 Label
num1lbl=Label(root,text=num1,font=("Algerian",65),bg="black",fg="red")
num1lbl.place(x=50,y=350,width=400,height=150)

#operator
oprtlbl=Label(root,text=oprt,font=("Algerian",70),bg="black",fg='red')
oprtlbl.place(x=450,y=350,width=200,height=150)

#Num2 Label
num2lbl=Label(root,text=num2,font=("Algerian",65),bg="black",fg="red")
num2lbl.place(x=650,y=350,width=400,height=150)

# ? = label
extralbl=Label(root,text="=    ?",font=("Algerian",65),bg="black",fg="red")
extralbl.place(x=1050,y=350,width=300,height=150)

# ***********************************************END OF SECOND PLATE*************************************************************

#config shorthand command
def conshrt(a,b):
    a.config(text=b)

#function to fill the list with real and fake results
def fill_lst():
    global fnresult
    def gnrt():
        a=random.randint(1,20)
        op=random.choice(['+','-','/'])
        temp=calculation(fnresult,op,a)
        return temp
    for i in range(0,4):
        tmp=gnrt()
        if type(tmp)==float:
            tmp=round(tmp,2)
        resultlst[i]=tmp
    tm=random.randint(0,3)
    resultlst[tm]=fnresult
#All config command
def allconfig():
    newoprt()
    conshrt(oprtlbl,oprt)
    rangenums()
    print("operator ",oprt)

    rangen1()
    conshrt(num1lbl,num1)
    rangen2()
    conshrt(num2lbl,num2)

    reslt()#perform calculation and give output
    fill_lst()#Create a rondom list with fake and real

    print(num1,oprt,num2,"=",fnresult)
    print('lst',resultlst)
    print(rng_from,rng_to)
    print(user_btn_choice)
    btn_sound()#to play mouse sound

    conshrt(res1btn,resultlst[0])
    conshrt(res2btn,resultlst[1])
    conshrt(res3btn,resultlst[2])
    conshrt(res4btn,resultlst[3])
# reslt()
# fill_lst()

#**********************************************************GENERATE AND COLOR BUTTON***********************************
#GENERATE BUTTON
gnrtbtn=Button(root,text="GENERATE",font=("Mistral",40),bg="blue",fg="red",command=allconfig)
gnrtbtn.place(x=50,y=525,height=70,width=300)



#************************************************************************************************************************
#****************Checking answer is right or not
global user_btn_choice
user_btn_choice=None
def check_answer():
    global points
    global user_btn_choice,resultlst,fnresult
    if resultlst[user_btn_choice]==fnresult:
        points+=1
        relpntslbl.config(bg="#196619",fg='#dfff80')
        pntslbl.config(bg="#196619",fg='#dfff80')
    else:
        points-=1
        relpntslbl.config(bg="#b32400",fg='#4d1919')
        pntslbl.config(bg="#b32400",fg='#4d1919')

    conshrt(relpntslbl,points)

def agnblk():
    relpntslbl.config(bg="black",fg="red")
    pntslbl.config(bg="black",fg="red")
    relpntslbl.after(500,agnblk)
agnblk()


#*******************ALL BUTTONS COMMANDS*****************
def btn1com():
    global user_btn_choice
    user_btn_choice=0
    check_answer()
    allconfig()
def btn2com():
    global user_btn_choice
    user_btn_choice=1
    check_answer()
    allconfig()
def btn3com():
    global user_btn_choice
    user_btn_choice=2
    check_answer()
    allconfig()
def btn4com():
    global user_btn_choice
    user_btn_choice=3
    check_answer()
    allconfig()



#**********************************************************PLATE THIRD ***********************************************
# plt=Label(root,bg="black")
# plt.place(x=50,y=600,height=350,width=1300)

#Button1
res1btn=Button(root,text=resultlst[0],font=("Snap ITC",60),bg="blue",fg="red",command=btn1com)
res1btn.place(x=150,y=625,height=150,width=500)

#Button2
res2btn=Button(root,text=resultlst[1],font=("Snap ITC",65),bg="blue",fg="red",command=btn2com)
res2btn.place(x=700,y=625,height=150,width=500)

#Button3
res3btn=Button(root,text=resultlst[2],font=("Snap ITC",65),bg="blue",fg="red",command=btn3com)
res3btn.place(x=150,y=825,height=150,width=500)

#Button4
res4btn=Button(root,text=resultlst[3],font=("Snap ITC",65),bg="blue",fg="red",command=btn4com)
res4btn.place(x=700,y=825,height=150,width=500)
#************************************************************************************************************************

#Colors
def light_color():
    light_colors=['#e6e6ff','#9999e6','#ecb3ff','#ff99cc','#ff9999','#99ffd6']
    tm=random.choice(light_colors)
    return tm
def label_color():
        ligt_clr_label=['#db70b8','#ff1aff','#c266ff','#bbbb77','#4dffb8','#4da6ff','#ff33bb','#ff1ac6','#00ff00']
        tm=random.choice(ligt_clr_label)
        return tm
def dark_color():
    dark_colors=['#990000','#997300','#269900','#009999','#730099','#99004d','#990000','#141452','#7a0099']
    tm=random.choice(dark_colors)
    return tm

#short hand config for bg
def bgclr(a,b):
    a.config(bg=b)
def clrchng():
    btn_sound()
    elemnents1=[bglbl]
    elemnents2=[typlbl,rnglbl,frmlbl,frmrngent,tolbl,torngent]
    elements3=[res1btn,res2btn,res3btn,res4btn]
    elements4=[gnrtbtn]
    clr1=light_color()
    clr2=label_color()
    clr3=label_color()
    clr4=dark_color()
    for i in elemnents1:
        bgclr(i,clr1)
    for i in elemnents2:
        bgclr(i,clr2)
    for i in elements3:
        bgclr(i,clr3)
    for i in elements4:
        bgclr(i,clr4)
clrchng()
#COLOR BUTTON
clrtbtn=Button(root,text="COLOR",font=("Mistral",40),bg="white",fg="red",command=clrchng)
clrtbtn.place(x=1150,y=525,height=70,width=200)

root.mainloop()


#*****************************End**********************************************************