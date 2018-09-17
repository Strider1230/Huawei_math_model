# -*- coding: utf-8 -*-
'''
Created on 2018年9月15日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
import pandas as pd
# xlsx=pd.read_excel('../InputData.xlsx',sheetname='Gates')
# print(xlsx)
# xlsx.to_csv('../Gates.csv')
pucks=pd.read_csv('../dataset/pucks_1_3.csv')
# list_w=['332','333','33E','33H','33L','773']
# list_n=['319','320','321','323','325','738','73A','73E','73H','73L']
# air_type=[]
# #print(pucks['飞机型号'])
# for i in pucks['飞机型号']:
#     if str(i)in list_n:
#         air_type.append('W')
#     else:
#         air_type.append('N')
# # print(len(air_type),air_type)
# pucks['机体类别']=air_type
# pucks.to_csv('../dataset/pucks_1.csv')
# pucks=pucks.dropna(axis=0)
# pucks.to_csv('../dataset/pucks_2.csv')
# pucks=pucks[pucks['出发日期']=='2018/1/20']
# pucks.to_csv('../dataset/pucks_1_3.csv')
# pucks['精确到达时间']=pucks['到达日期']+[' ']+pucks['到达时刻'] 
# pucks['精确出发时间']=pucks['出发日期']+[' ']+pucks['出发时刻']  
# pucks.to_csv('../dataset/pucks_2_1.csv')
start_label=[]
stop_label=[]
for i in pucks.iterrows():
   start_time=i[1]['出发时刻'].split(':')
   time=int(start_time[0])
   min=int(start_time[1])
   start_label.append((time*60+min)/5)
pucks['出发序列号']=start_label
for j in pucks.iterrows():
    if j[1]['到达日期']=='2018/1/19':
        stop_time=j[1]['到达时刻'].split(':')
        time=int(stop_time[0])
        min=int(stop_time[1])
        stop_label.append(-(time*60+min)/5)
    else:
        stop_time=j[1]['到达时刻'].split(':')
        time=int(stop_time[0])
        min=int(stop_time[1])
        stop_label.append((time*60+min)/5)
pucks['到达序列号']=stop_label
pucks.to_csv('../dataset/pucks_2_4.csv')#对第二十天的数据按5min对数据进行分片

    
    
        

        
    




        
