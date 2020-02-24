import pandas as pd
import numpy as np

# 基本配置:设备名称配置  sysname AH***-MB-CMNET-BRAS**-***
def sysname_check_event(fp):
    areacode = ['XUC']
    brastype = 0  # 后续接口  华为0，
    if brastype == 0:
        brastype0 = '-ME60'
    else:
        brastype0 = '-M6000'

    for line in list(fp):  # 遍历每一行
        for areacode0 in areacode:
             for i in range(1,3):
                brasnumber0='%02d'%i
                sysnamecheck = 'sysname AH' + areacode0 + '-MB-CMNET-BRAS' + brasnumber0 + brastype0
                #print(sysnamecheck)
                if (sysnamecheck in line):
                    return (True)

    return (False)

# #基本配置：时区配置
# def time_zone_check(fp):
#     error_check_timezone=0
#     check_time_zone='clock timezone beijing add 08:00:00'
#     for line in list(fp):
#         if(check_time_zone in line):
#             print('time zong right')
#             return(True)
#         else:
#             #print('time zone fault')
#             error_check_timezone=1
#
#     if (error_check_timezone==1):
#         return(False)



file = open("testarea.log")
fp = file.readlines()
check1=sysname_check_event(fp)
# check2=time_zone_check(fp)
print(check1)
# print(check2)
file .close()


