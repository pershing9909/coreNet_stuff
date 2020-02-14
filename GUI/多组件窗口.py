from  tkinter import  *
#import tkinter
def greeting():
    print('Hello,123')

win = Frame()
win.pack()
Label(win, text="hello,container world!").pack(side = TOP)
Button(win, text='hello',command=greeting).pack(side=LEFT)
Button(win, text='quit',command=win.quit).pack(side=RIGHT)

win.mainloop()