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
#
def jaccard_similarity(x, y):
    intersection = len(set.intersection(*[set(x), set(y)]))
    union = len(set.union(*[set(x), set(y)]))
    return intersection / float(union)

for i in range(0,103):#100
    
    Project_NameA = df_pro.iloc[i,0]
    ArrayA = df_hyo[Project_NameA].to_list()
    #print(ArrayA)
    ArrayA1 = [n for n in ArrayA if n!='0']
    #NumArrayA = ArrayA.np.
    
    lists = [] 
    for j in range(0,103):#100
        Project_NameB = df_pro.iloc[j,0]
        ArrayB = df_hyo[Project_NameB].to_list()
        ArrayB1 = [n for n in ArrayB if n!='0']
        print(Project_NameA+'と'+Project_NameB+'のジャッカード距離')
        print(jaccard_similarity(ArrayA1,ArrayB1))
        lists.insert(j,jaccard_similarity(ArrayA1,ArrayB1))
        listNum = np.array(lists)    
    
    df_heat[Project_NameA] = listNum
    #print(lists)
    #print(listNum)

print(df_heat)

df_heat.to_csv('/Users/tomoya/Library/Mobile Documents/com~apple~CloudDocs/code/check/jaccad.csv')



