import pandas as pd
import numpy as np

# 基本配置:设备名称配置  sysname AH***-MB-CMNET-BRAS**-***
def sysname_check_event(fp):
    areacode = ['XUC','WUH','HF','BOZ']
    brastype = 0  # 后续接口  华为0，
    if brastype == 0:
        brastype0 = '-ME60'
    else:
        brastype0 = '-M6000'

    for line in fp.readlines():  # 遍历每一行
        for areacode0 in areacode:
             for i in range(0,20):
                brasnumber0='%02d'%i
                sysnamecheck = 'sysname AH' + areacode0 + '-MB-CMNET-BRAS' + brasnumber0 + brastype0
                print(sysnamecheck)
                if (sysnamecheck in line):
                    error_sysname= 0
                    #print(line)
                    return(True)
                else:
                    #print('123456')
                    error_sysname= 1

    if (error_sysname==1) :
        #print("sysname error")
        return (False)

#基本配置：时区配置
def time_zone_check(fp):
    check_time_zone='clock timezone beijing add 08:00:00'
    for line in fp.readlines():
        if(check_time_zone in line):
            #print('right')
            error_check_timezone=0
            return(True)
        else:
            #print('time zone fault')
            error_check_timezone=1

    if (error_check_timezone==1):
        return(False)







fp = open("testarea.log")
#check1=sysname_check_event(fp)
#check2=time_zone_check(fp)
print(check1)
fp.close()


