from tkinter import *
from PIL import Image
import sys
root= Tk()
###退出
def quit():
    print('感谢您的使用')
    sys.exit()

###开始



####界面

#--------------------------------------------------------- 主界面
root.title('欢迎使用BRAS局数据检查工具')
#win.geometry('320x180')
root.resizable(0,0)
sw = root.winfo_screenwidth() #得到屏幕宽度
sh = root.winfo_screenheight() #得到屏幕高度
x = (sw-640) / 2
y = (sh-360) / 2
root.geometry('640x360+%d+%d' %(x,y))
photo = PhotoImage(file="ffdfds.gif")
can=Canvas(root,width=129, height=45)
can.place(x=10,y=3)
can.create_image(65, 0, image=photo, anchor='n')
welcomewords=Label(root,text='自研BRAS局数据检查工具',font=("黑体", 30, "bold"))
welcomewords.place(x=160,y=12,width=450,height=40)

start_button=Button(None,text='开始',command=quit)

quit_button=Button(None,text='退出',command=quit)




root.mainloop()    #主体循环