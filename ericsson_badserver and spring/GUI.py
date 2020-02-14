from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):  # 从Frame派生出Application类，它是所有widget的父容器
    def __init__(self, master=None):  # master即是窗口管理器，用于管理窗口部件，如按钮标签等，顶级窗口master是None，即自己管理自己
        Frame.__init__(self, master)
        self.pack()  # 将widget加入到父容器中并实现布局
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='hi')  # 创建一个标签显示内容到窗口
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)  # 创建一个Quit按钮，实现点击即退出窗口
        self.quitButton.pack()
        self.input = Entry(self)  # 创建一个输入框，以输入内容
        self.input.pack()
        self.nameButton = Button(self, text='hello', command=self.hello)  # 创建一个hello按钮，点击调用hello方法，实现输出

        self.nameButton.pack()

    def hello(self):
        name = self.input.get()  # 获取输入的内容
        messagebox.showinfo('Message', 'hello,%s' % name)  # 显示输出


app = Application()
app.master.title("hello")  # 窗口标题

app.mainloop()  # 主消息循环