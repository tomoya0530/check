import pandas as pd
from pandas import Series, DataFrame,plotting
import numpy as np
import csv
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
#from sklearn.cluster import KMeans
from scipy.spatial import distance

pd.set_option('display.max_columns', 200)
pd.set_option('display.max_rows', 200)

#対応表CSVの読み込み
df_hyo = pd.read_csv("/Users/tomoya/Library/Mobile Documents/com~apple~CloudDocs/code/check/shugo.csv")
#データフレームの転置
#df_hyoT = df_hyo.T


#ルール名がまとめられているCSVの読み込み
df_rule = pd.read_csv("/Users/tomoya/Library/Mobile Documents/com~apple~CloudDocs/code/check/rulecsv.csv")
#プロジェクト名がまとめられているCSVの読み込み
df_pro = pd.read_csv("/Users/tomoya/Library/Mobile Documents/com~apple~CloudDocs/code/check/project.csv")


df_heat =pd.read_csv("/Users/tomoya/Library/Mobile Documents/com~apple~CloudDocs/code/check/heatmap.csv")
#print(df_heat.head())
#ユークリッド距離の計算
def euclid(x, y):
    suma =0
    sumb =0
    naiseki =0
    for i in range(0, len(x)):
        suma = suma + x[i] ** 2
        sumb = sumb + y[i] ** 2
        naiseki = naiseki + x[i]*y[i]
        #t = t + (x[i] - y[i]) ** 2
    #    distance = 
    #return t ** (0.5)
    #return np.sqrt(np.sum((x - y) ** 2))
    return naiseki/((suma * sumb)**0.5)
    

for i in range(0,101):#100
    
    ProjectA = df_pro.iloc[i,0]
    Project_NameA = ProjectA.replace('/', '_')
    ArrayA = df_hyo[Project_NameA].to_list()
    #NumArrayA = ArrayA.np.
    
    lists = [] 
    for j in range(0,101):#100
        ProjectB = df_pro.iloc[j,0]
        Project_NameB = ProjectB.replace('/', '_')
        ArrayB = df_hyo[Project_NameB].to_list()
        print(Project_NameA+'と'+Project_NameB+'の類似度')
        print(euclid(ArrayA,ArrayB))
        lists.insert(j,euclid(ArrayA,ArrayB))
        listNum = np.array(lists)    
    
    df_heat[Project_NameA] = listNum
    #print(lists)
    #print(listNum)

print(df_heat)

df_heat.to_csv('/Users/tomoya/Library/Mobile Documents/com~apple~CloudDocs/code/check/heatmapout.csv')

#print(df)

#print(df_hyoT)




