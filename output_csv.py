# -*- coding: utf-8 -*-

import pandas as pd
import pymongo
import time
query = input("输出查询 search_criteri :")
# 连接mongodb数据库
client = pymongo.MongoClient("mongodb://root:123456@127.0.0.1:27017/")
# 连接数据库
db = client["taobao"]
# 数据表
fangyuan = db["product"]
# 将mongodb中的数据读出
quer_data = list(fangyuan.find())
print(len(quer_data))
data = pd.DataFrame(quer_data)
data.head()
# 保存为csv格式
now_tiem = time.strftime('%Y-%m-%d',time.localtime(time.time()))
data.to_csv('./storage/csv/'+now_tiem+"_"+query,encoding='utf-8')
# 读取csv数据
df = pd.read_csv('./storage/csv/'+now_tiem+"_"+query,low_memory=False,index_col=0)
# 查看数据大小(行列)
print( data.shape)
# 查看数据行号
print (data.columns)
