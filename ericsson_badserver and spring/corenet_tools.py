# -*- coding: gbk -*-
import pymysql

from sshtunnel import SSHTunnelForwarder

# with SSHTunnelForwarder(
#         ('103.46.128.49', 15882),# B����������
#         ssh_username="pi",
#         ssh_password="px999",
#         remote_bind_address=('127.0.0.1', 3306)) as server:# A����������
#
#     conn = pymysql.connect(host='127.0.0.1',  # �˴���������127.0.0.1
#                            port=3306,
#                            user='root',
#                            passwd='px999',
#                            db='CoreNet',
#                            charset="utf8")

db = pymysql.connect(host='103.46.128.49',port=28639, user='root',passwd='px999',db='CoreNet',charset="utf8")
cursor = db.cursor()
cursor.execute('Show tables;')
print(cursor.fetchall())
db.close()
