# coding=utf-8-sig
from ftplib import FTP
import datetime
import re


def ftpconnect():
    ftp_server = '10.225.84.74'  ###FTP 地址
    username = 'xc_px'     ###FTP 账号
    password = 'Ericsson#1'   ###FTP密码
    ftp = FTP()
    ftp.connect(ftp_server, 21)
    ftp.set_debuglevel(3)
    ftp.set_pasv(True)
    #ftp.encoding = 'GB18030'  #ISO-8859-1
    #ftp.encoding = 'ISO-8859-1'
    ftp.login(username, password)
    return ftp


def downloadfile():
    # # 格式化取到昨天的日期
    # # d = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y%m%d')
    # #d = 'C20200131.2200-20200131.2300_XUCGS1:1002' ###文件名称
    # remotepath = '/var/opt/ericsson/sgw/outputfiles/apgfiles/sts_bk'   #远程FTP服务器目录
    # # 调用ftp连接函数
    # ftp = ftpconnect()
    # ftp.cwd(remotepath)  #进入FTP目录
    # list = ftp.nlst()
    # for name in list:
    #     # 正则过滤掉其他日期
    #     L = re.match(d, name)
    #     if L:
    #         path = 'E:/2020PRo/download/' + name
    #         #f = open(path, 'wb')
    #         file_handle = open(name, "wb").write
    #         filename = 'RETR ' + name
    #         ftps.retrbinary(filename, file_handle, blocksize=1024)
    #         #ftp.retrlines(filename, file_handle)
    # ftp.quit()

    ftp = ftpconnect()
    ftp.cwd('/var/opt/ericsson/sgw/outputfiles/apgfiles/sts_bk')
    sever_filename = 'C20200131.2200-20200131.2300_XUCGS1:1002'
    filename = 'RETR ' + sever_filename
    local_filename = 'D:/'
    bufsize = 10240  # 缓冲区大小
    with open(sever_filename, "wb") as  f:
        ftp.retrbinary(filename, f.write, bufsize)
        f.close()
    ftp.quit  # 退出ftp


downloadfile()
