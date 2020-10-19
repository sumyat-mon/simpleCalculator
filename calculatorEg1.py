from tkinter import *
x=Tk()

# text editor
w=StringVar(x)
e=Entry(x,width='25',fg='white',bg='grey',textvariable=w)
e.pack(pady=50)


'''
# Button
oneBtn=Button(f,text='1',fg='white',bg='grey',borderwidth='6',width='2',command=lambda w=w:w.set(w.get()+'1'))
oneBtn.pack(side='left',pady=5)
twoBtn=Button(f,text='2',fg='white',bg='grey',borderwidth='6',width='2',command=lambda w=w:w.set(w.get()+'2'))
twoBtn.pack(side='left',pady=5)

plusBtn=Button(f2,text='+',fg='white',bg='grey',borderwidth='6',width='2',command=lambda w=w:w.set(w.get()+'+'))
plusBtn.pack(side='left',pady=5)

equalBtn=Button(f2,text='=',fg='white',bg='grey',borderwidth='6',width='2',command=lambda w=w:w.set(eval(w.get())))
equalBtn.pack(side='left',pady=5)
'''

for i in ('789/','456*','123-','0.+%'):
    f=Frame(x)
    f.pack()
    for j in i:    
        w.set('')
        Button(f,text=j,fg='white',bg='grey',borderwidth=6,width=2,command=lambda w=w,j=j:w.set(w.get()+j)).pack(side='left',pady=5)


# frame
f=Frame(x)
f.pack()
Button(f,text='cls',width=7,borderwidth=6,fg='white',bg='grey',command=lambda w=w:w.set('')).pack(side='left',pady=5)
Button(f,text='Ans',width=7,borderwidth=6,fg='white',bg='grey',command=lambda w=w:w.set(eval(w.get()))).pack(side='left',pady=5)

x.mainloop()