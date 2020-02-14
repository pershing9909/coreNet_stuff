# coding=gbk
import pandas as pd
import numpy as np
from numpy import set_printoptions
pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

locareast=pd.read_csv('LOCAREAST.csv')
locareast1=pd.read_csv('LOCAREAST1.csv')
locareast.EXCHID = locareast.EXCHID.replace(np.nan,"XUCGS6")
locareast1.EXCHID = locareast.EXCHID.replace(np.nan,"XUCGS6")
g1=locareast.reset_index().groupby(['OBJECTID','EXCHID'])['NLASATSGS'].idxmax
g2=locareast.iloc[g1]
j1=locareast1.reset_index().groupby(['OBJECTID','EXCHID'])['NLASUBREG'].idxmax
j2=locareast1.iloc[j1]
#print(g2)
#print(j2)


#注册用户数
zhuceyonghushu=pd.pivot_table(j2,index=["EXCHID"],values=["NLASUBREG"],aggfunc=[np.sum])
zhuceyonghushu.columns=['注册用户数']
#开机用户数
fuzhuoyonghushu=pd.pivot_table(j2,index=["EXCHID"],values=["NLASUBATTACH"],aggfunc=[np.sum])
fuzhuoyonghushu.columns=['开机用户数']
#开机用户比
kkk1=pd.merge(zhuceyonghushu, fuzhuoyonghushu, on="EXCHID", how="left")
kkk1['开机用户比'] = kkk1.apply(lambda x:x['开机用户数']/x['注册用户数']*100, axis=1)
#print(kkk1)

### EPC用户数
EPCyonghushu=pd.pivot_table(g2,index=["EXCHID"],values=["NLASATSGS"],aggfunc=[np.sum])
EPCyonghushu.columns=['EPC用户数']
kkk1=pd.merge(kkk1, EPCyonghushu, on="EXCHID", how="left")
#寻呼次数
xunhucishu=pd.pivot_table(g2,index=["EXCHID"],values=["NLAPAG1LOTOT"],aggfunc=[np.sum])
xunhucishu.columns=['寻呼次数']
kkk1=pd.merge(kkk1, xunhucishu, on="EXCHID", how="left")

###print(kkk1)

####寻呼成功次数
NLAPAG1RESUCC=pd.pivot_table(g2,index=["EXCHID"],values=["NLAPAG1RESUCC"],aggfunc=[np.sum])
NLAPAG1RESUCC.columns=['NLAPAG1RESUCC']
NLAPAG2RESUCC=pd.pivot_table(g2,index=["EXCHID"],values=["NLAPAG2RESUCC"],aggfunc=[np.sum])
NLAPAG2RESUCC.columns=['NLAPAG2RESUCC']
print(NLAPAG1RESUCC)
print(NLAPAG2RESUCC)
succ=pd.merge(NLAPAG1RESUCC, NLAPAG2RESUCC, on="EXCHID", how="left")

succ['寻呼成功次数'] = succ.apply(lambda x: x.sum(), axis=1)
#print(succ)
succ.drop(["NLAPAG1RESUCC","NLAPAG2RESUCC"],axis=1,inplace=True)
#print(succ)

####   寻呼成功率
kkk1=pd.merge(kkk1, succ, on="EXCHID", how="left")
#print(kkk1)
kkk1['寻呼成功率'] = kkk1.apply(lambda x:x['寻呼成功次数']/x['寻呼次数']*100, axis=1)
#print(kkk1)

'''
### ############################################################### CSFB寻呼成功率
csfb=pd.read_csv('CSFB.csv')
csfb.EXCHID = csfb.EXCHID.replace(np.nan,"XUCGS6")
f1=csfb.reset_index().groupby(['OBJECTID','EXCHID'])['NLASATSGS'].idxmax
f2=csfb.iloc[f1]
'''

#注册用户数
zhuceyonghushu_lac=pd.pivot_table(j2,index=["OBJECTID","EXCHID"],values=["NLASUBREG"],aggfunc=[np.sum])
zhuceyonghushu_lac.columns=['注册用户数']
#print(zhuceyonghushu_lac)
#开机用户数


fuzhuoyonghushu_lac=pd.pivot_table(j2,index=["OBJECTID","EXCHID"],values=["NLASUBATTACH"],aggfunc=[np.sum])
fuzhuoyonghushu_lac.columns=['开机用户数']
#开机用户比
kkk2=pd.merge(zhuceyonghushu_lac, fuzhuoyonghushu_lac, on=["OBJECTID","EXCHID"], how="left")
kkk2['开机用户比'] = kkk2.apply(lambda x:x['开机用户数']/x['注册用户数']*100, axis=1)
print(kkk2)

### EPC用户数
EPCyonghushu_lac=pd.pivot_table(g2,index=["OBJECTID","EXCHID"],values=["NLASATSGS"],aggfunc=[np.sum])
EPCyonghushu_lac.columns=['EPC用户数']
kkk2=pd.merge(kkk2, EPCyonghushu_lac, on=["OBJECTID","EXCHID"], how="left")

#寻呼次数
xunhucishu_lac=pd.pivot_table(g2,index=["OBJECTID","EXCHID"],values=["NLAPAG1LOTOT"],aggfunc=[np.sum])
xunhucishu_lac.columns=['寻呼次数']
kkk2=pd.merge(kkk2, xunhucishu_lac, on=["OBJECTID","EXCHID"], how="left")

###print(kkk1)

####寻呼成功次数
NLAPAG1RESUCC_lac=pd.pivot_table(g2,index=["OBJECTID","EXCHID"],values=["NLAPAG1RESUCC"],aggfunc=[np.sum])
NLAPAG1RESUCC_lac.columns=['NLAPAG1RESUCC']
NLAPAG2RESUCC_lac=pd.pivot_table(g2,index=["OBJECTID","EXCHID"],values=["NLAPAG2RESUCC"],aggfunc=[np.sum])
NLAPAG2RESUCC_lac.columns=['NLAPAG2RESUCC']
#print(NLAPAG1RESUCC_lac)
#print(NLAPAG2RESUCC_lac)

succ_lac=pd.merge(NLAPAG1RESUCC_lac, NLAPAG2RESUCC_lac, on=["OBJECTID","EXCHID"], how="left")

succ_lac['寻呼成功次数'] = succ_lac.apply(lambda x: x.sum(), axis=1)
print(succ_lac)
succ_lac.drop(["NLAPAG1RESUCC","NLAPAG2RESUCC"],axis=1,inplace=True)
#print(succ_lac)

####   寻呼成功率
kkk2=pd.merge(kkk2, succ_lac, on=["OBJECTID","EXCHID"], how="left")
#print(kkk1)
kkk2['寻呼成功率'] = kkk2.apply(lambda x:x['寻呼成功次数']/x['寻呼次数']*100, axis=1)
#print(kkk2)

kkk1.to_csv("result_bad_server.csv",encoding="ANSI",index=True)
kkk2.to_csv("result_bad_server.csv",mode='a',encoding="ANSI",index=True)
