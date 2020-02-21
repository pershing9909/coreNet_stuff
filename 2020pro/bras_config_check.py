import pandas as pd
import numpy as np

error_sysname=0


def sysname_check_event(fp,error_sysname):   # 基本配置:设备名称配置  sysname AH***-MB-CMNET-BRAS**-***

    areacode = ['XUC']
    brasnumber = ['10']
    brastype = 0  # 后续接口  华为0，
    if brastype == 0:
        brastype0 = '-ME60'
    else:
        brastype0 = '-M6000'

    for line in fp.readlines():  # 遍历每一行
        for areacode0 in areacode:
            for brasnumber0 in brasnumber:
                sysnamecheck = 'sysname AH' + areacode0 + '-MB-CMNET-BRAS' + brasnumber0 + brastype0
                # print(sysnamecheck)
                if (sysnamecheck in line):
                    print(line)
                else:
                    print('123456')
                    error_sysname= 1

    if (error_sysname==1) :print("sysname error")

123124123123


fp = open("BRAS10_cu.log")
sysname_check_event(fp,error_sysname)
fp.close()




