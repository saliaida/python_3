from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry('600x400+400+100')
bg1 = '#D2D2DB'
win.configure(bg=bg1)
win.title('content management')
#========functions===============
def insert():
    fname = ent_fname.get()
    lname = ent_lname.get()
    city = ent_city.get()
    tel = ent_tel.get()
    lst_manage.insert(END,f'{fname}-{lname}-{city}-{tel}')
    clear()
    
def clear():
    ent_city.delete(0,END)
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_tel.delete(0,END)
    ent_fname.focus_set()
    
def delete():
    select = lst_manage.curselection()
    messagebox.askquestion('Delete',f'Do you want to delete?'+str(select))
    lst_manage.delete(select)
    
def fetch():
    clear()
    index= lst_manage.curselection()
    data = lst_manage.get(index)
    ldata= data.split('-')    
    ent_fname.insert(0,ldata[0])
    ent_lname.insert(0,ldata[1])
    ent_city.insert(0,ldata[2])
    ent_tel.insert(0,ldata[3])
    
def exit1():
    result = messagebox.askquestion('Exit','Do you want to exit?')
    if result == 'yes':
        win.destroy()
    else:
        messagebox.showinfo('Thanks','so lets continue')
        
#==========main====================
lbl_fname = Label(win,text='Fname:',font='arial 14',bg=bg1 ,fg = 'red')
lbl_fname.place(x= 20 , y=50)
ent_fname = Entry(win,font='arial 14')
ent_fname.place(x= 100 , y=50,width=150)
lbl_lname = Label(win,text='Lname:',font='arial 14',bg=bg1 ,fg = 'red')
lbl_lname.place(x= 300 , y=50)
ent_lname = Entry(win,font='arial 14')
ent_lname.place(x= 380 , y=50,width=150)
lbl_city = Label(win,text='City:',font='arial 14',bg=bg1 ,fg = 'red')
lbl_city.place(x= 45 , y=100)
ent_city = Entry(win,font='arial 14')
ent_city.place(x= 100 , y=100,width=150)
lbl_tel = Label(win,text='Tel:',font='arial 14',bg=bg1 ,fg = 'red')
lbl_tel.place(x= 330 , y=100)
ent_tel = Entry(win,font='arial 14')
ent_tel.place(x= 380 , y=100,width=150)
lst_manage = Listbox(win,font='arial 14')
lst_manage.place(x= 45 , y=150,width=320)
btn_insert = Button(win,text='Insert',font='arial 14',fg = 'blue',command=insert)
btn_insert.place(x = 400 , y=150,width=100)
btn_clear = Button(win,text='Clear',font='arial 14',fg = 'blue',command=clear)
btn_clear.place(x = 400 , y=200,width=100)
btn_delete = Button(win,text='Delete',font='arial 14',fg = 'blue',command=delete)
btn_delete.place(x = 400 , y=250,width=100)
btn_fetch = Button(win,text='Fetch',font='arial 14',fg = 'blue',command=fetch)
btn_fetch.place(x = 400 , y=300,width=100)
btn_exit = Button(win,text='Exit',font='arial 12',fg = 'yellow',bg = '#BB9EF3',command=exit1)
btn_exit.place(x = 550 , y=350)

















win.mainloop()