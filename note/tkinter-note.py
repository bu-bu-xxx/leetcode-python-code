# tkinter python自带的gui
# B站: https://www.bilibili.com/video/BV1jW411Y7dL
# web: https://www.runoob.com/python/python-gui-tkinter.html


"""
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('my window')
window.geometry('500x300')

# Label
var = tk.StringVar()
var0 = '123'
l1 = tk.Label(master=window, textvariable=var, font=('仿宋', 30), width=10, height=5)
l1.pack()
var.set('123')

# Entry
e = tk.Entry(window)

# Text
t = tk.Text(window, height=2)


# Button
def insert_point():
    str_var = e.get()
    t.insert('insert', str_var)
b1 = tk.Button(master=window, text='insert', width=5, height=5, command=insert_point)


# Frame
frm = tk.Frame(window)
frm.pack()
frm.pack()
frm_l = tk.Frame(frm)
frm_r = tk.Frame(frm)
frm_l.pack(side='left')
frm_r.pack(side='right')
tk.Label(frm_l, text='left').pack()
tk.Label(frm_r, text='right').pack()


# messagebox
# 必须 from tkinter import messagebox
def hit_me():
    messagebox.showerror(title='hi', message='error')
    messagebox.showwarning(title='hi', message='warning')
    messagebox.showinfo(title='hi', message='info')


tk.Button(window, text='hit me', command=hit_me).pack()

# pack
# e.pack()
# b1.pack()
# t.pack()

# mainloop
window.mainloop()
"""





