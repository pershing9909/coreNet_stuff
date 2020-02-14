from tkinter import *
import sys
root= Tk()

# widget = Label(text='hello GUI world!')
# widget.pack(expand=YES, fill=BOTH)#打包可扩展
#Label(text='hello GUI world!').pack(expand=YES, fill=BOTH)
# widget=Button(None,text='hello GUI world!',command=sys.exit)

def quit():
    print('Hello,I must going...')
    sys.exit()



widget=Button(None,text='hello GUI world!',command=quit)
widget.pack(expand=YES,fill=Y)
root.title('hahahaha')
root.mainloop()                                 #主体循环