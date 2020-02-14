import pandas as pd
import numpy as np
from numpy import set_printoptions
pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)


#####   MME 用户数统计

locareast=pd.read_csv('LOCAREAST.csv')
local_area2={'OBJECTID':[4600021904,4600021905,4600021906,4600021908,4600021911,4600021912,4600021913,4600021914,4600021915,4600021916,4600021917,4600021918,4600021919,4600022160,4600022161,4600022162,4600022164,4600022167,4600054769,4600054770,4600054771,4600054772,4600054773,4600054774],'市县':['宣城','宣城','宣城','宁国','广德','广德','郎溪','广德','宁国','宁国','旌德','绩溪','泾县','郎溪','广德','宣城','泾县','宣城','广德','泾县','宁国','郎溪','宣城','绩溪']}
local_area = pd.DataFrame(data=local_area2)
locareast.EXCHID = locareast.EXCHID.replace(np.nan,"XUCGS6")
g1=locareast.reset_index().groupby(['OBJECTID','EXCHID'])['NLASATSGS'].idxmax()
g2=locareast.iloc[g1]
#print(g2)
g3 = pd.merge(g2, local_area, on="OBJECTID", how="left")
#print(g3)
g4=pd.pivot_table(g3,index=["市县"],values=["NLASATSGS"],aggfunc=[np.sum])
g4.columns=['MME用户数']
#print(g4)


######   VLR用户数统计


locareast1=pd.read_csv('LOCAREAST1.csv')
locareast1.EXCHID = locareast1.EXCHID.replace(np.nan,"XUCGS6")
j1=locareast1.reset_index().groupby(['OBJECTID','EXCHID'])['NLASUBREG'].idxmax()
j2=locareast1.iloc[j1]
#print(j2)
j3 = pd.merge(j2, local_area, on="OBJECTID", how="left")
#print(j3)
j4=pd.pivot_table(j3,index=["市县"],values=["NLASUBREG"],aggfunc=[np.sum])
j4.columns=['VLR用户数']
#print(j4)


#####             聚合显示


kkk1=pd.merge(g4, j4, on="市县", how="left")
#print(kkk1)
order2={'序号':[1,2,3,4,5,6,7],'市县':['广德','绩溪','泾县','旌德','郎溪','宁国','宣城']}
order1 = pd.DataFrame(data=order2)
kkk2=pd.merge(order1, kkk1, on="市县", how="left")
kkk2 = kkk2.loc[:, ['序号', '市县', 'VLR用户数', 'MME用户数']]
print(kkk2)
kkk2.to_csv("result.csv",encoding="ANSI",index=False)





