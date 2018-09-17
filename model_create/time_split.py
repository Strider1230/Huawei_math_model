# -*- coding: utf-8 -*-
'''
Created on 2018年9月17日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
import pandas as pd
import random
import sys
sys.setrecursionlimit(1000000)
# S1=[]#存储按时间到达停机位的航班
s_time=pd.read_csv('../dataset/pucks_2_4.csv')
port=pd.read_csv('../dataset/可停靠登机口.csv')
s1_time=s_time.sort_index(by=['到达序列号'])#按到达顺序排序
s2_time=s_time.sort_index(by=['出发序列号'])#按出发顺序排序
# print(s2_time)
# time_dict=[]
# for i in range(-287,236):
#     list=[]
#     for j in s_time.iterrows():
#         if j[1]['到达序列号']<=i & i<=j[1]['到达序列号']:
#             list.append(j)
#     if len(list)>0:
#         time_dict.append({i:list})  
# print(time_dict)
#给登机口一个初始化开启时间
    
#每个航班可停靠登机口,pk01,pk02
D={}     
for i in s1_time['飞机转场记录号']:
    list_D=[]  
    for j in port.iterrows():
        if(str(i)==j[1]['飞机转场记录号']):
            list_D.append(j[1]['登机口'])
    list_D.append('t70')
    D.setdefault(str(i),list_D)
print(D)
G={}#所有停机位初始化时间，包括G1,G2,G3
port=port.drop_duplicates(subset=['登机口'],keep='first')
for i in port['登机口']:
    G.setdefault(str(i),-350)  
G.setdefault('t70',-350)
def init():
    i1=0
    s=''
    G1=G
    D1=D
    for i  in  s1_time.iterrows():
        Di=D1[str(i[1]['飞机转场记录号'])]#获取航班i的可停靠集合
        if len(Di)==0:
            init()
        else:
            bi=random.randint(0,len(Di)-1)
            if int(i[1]['到达序列号'])>(int(G1[Di[bi]])+int(9)):
                if str(Di[bi])!='t70':
                    up={Di[bi]:int(i[1]['出发序列号'])}
                    G1.update(up)
                    for k,v in D1.items():
                        if len(v)==0:
                            init()
                        else:
                                if str(Di[bi])!='t70':
                                    if str(Di[bi]) in list(v):                            
                                        D1[k].remove(str(Di[bi]))
                    for k1,v1 in D1.items():
                        if len(list(v1))==0:
                            #print(D1)
                            init()
            s+=str(i[1]['飞机转场记录号'])+':'+str(Di[bi])+','+str(bi)+'\n'                            
        
    return s                       
                            
if __name__ == '__main__':
    
    f= open('initial_sequnce.csv','a')
    D2=init()
    f.write(D2)
#     for i in s1_time['飞机转场记录号']:
#         f.write(i+':'+str(D2[i])+'\n')
    #print(D2)                    
                    
            
        
    
 
        



