from tkinter import *
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
#win.geometry("%dx%d+%d+%d" %(ww,wh,x,y))
                               #主体循环

top_welcome= Frame(root,height = 90,width = 320)
top_welcome.pack(side=TOP,fill=BOTH)

#photo = PhotoImage(file="/Users/pershing9909/PycharmProjects/coreNet_stuff/2020pro/adjust_img.gif")
#can=Canvas(top_welcome)
#can.pack(fill=BOTH,side =LEFT)
#can.create_image(2, 2, image=photo, anchor= W)
Label(top_welcome,text='安徽移动自研BRAS局数据检查工具',bg='green').pack(side=LEFT)
# start_button=Button(None,text='开始',command=quit)
# quit_button=Button(None,text='退出',command=quit)
# start_button.pack()
# quit_button.pack()
root.mainloop()