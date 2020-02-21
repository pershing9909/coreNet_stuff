import pandas as pd
import numpy as np

fp = open("BRAS10_cu.log")
sysname_check_event(fp)
fp.close()

'''
基本配置; 设备名称配置  sysname AH***-MB-CMNET-BRAS**-***
'''
def sysname_check_event(fp):
    areacode = ['XUC', 'WUH']
    brasnumber = ['01', '02', '03', '10']
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
                    global  error_sysname
                    error_sysname=1

    if (error_sysname==1) :print("sysname error")




