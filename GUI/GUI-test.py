from tkinter import *
from PIL import Image
import sys
root= Tk()
###退出
def quit():
    sys.exit()


def sysname_check_event(fp):
    areacode = ['XUC']
    brastype = 0  # 后续接口  华为0，
    if brastype == 0:
        brastype0 = '-ME60'
    else:
        brastype0 = '-M6000'

    for line in list(fp):  # 遍历每一行
        for areacode0 in areacode:
             for i in range(1,20):
                brasnumber0='%02d'%i
                sysnamecheck = 'sysname AH' + areacode0 + '-MB-CMNET-BRAS' + brasnumber0 + brastype0
                #print(sysnamecheck)
                if (sysnamecheck in line):
                    return (True)

    return (False)


    # if (error_sysname==1) :
    #     #print("sysname error")
    #     #return (False)

def time_zone_check(fp):

    check_time_zone='clock timezone beijing add 08:00:00'
    #print(fp)
    for line in list(fp):
        if(check_time_zone in line):
            return(True)
    return(False)











def print_result(check,event):####分项结果打印函数，并实现错误内容标注
    if check:
        # print('pass')
        result_data_Text.insert(INSERT, event+" check pass \n")
    else:
        # print('fault')
        result_data_Text.insert(INSERT, event+" check fault")
        #result_data_Text.mark_set(a,CURRENT +' linestart')
        result_data_Text.mark_set("a", CURRENT + ' linestart')
        result_data_Text.mark_set("b", CURRENT + ' lineend')
        result_data_Text.tag_add("tag1",'a', 'b')
        result_data_Text.tag_config("tag1", background="yellow", foreground="red")
        result_data_Text.insert(INSERT, "\n")



def check_in_line():
    file = open("testarea.log")
    fp = file.readlines()
    result_data_Text.delete('1.0','end')   #首次运行清屏
    check1=sysname_check_event(fp)
    print_result(check1, 'sysname')
    check2 = time_zone_check(fp)
    print_result(check2, 'time zone')
    file.close()






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


result_data_Text = Text(root, width=500, height=150)   ####结果文本框
result_data_Text.place(x=60,y=80,width=500, height=150)

start_button=Button(None,text='开始',command=check_in_line)
start_button.place(x=160, y=300)
quit_button=Button(None,text='退出',command=quit)
quit_button.place(x=480, y=300)
#####导出功能按钮，
######按文件夹读取文件，显示文件名






root.mainloop()    #主体循环