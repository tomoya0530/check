import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import csv
import xml.etree.ElementTree as ET
pd.set_option('display.max_columns', 200)
pd.set_option('display.max_rows', 200)

#ルール名がまとめられているCSVの読み込み
df_rule = pd.read_csv("/Users/tomoya/Library/Mobile Documents/com~apple~CloudDocs/code/check/rulecsv.csv")

#プロジェクト名がまとめられているCSVの読み込み
df_pro = pd.read_csv("/Users/tomoya/Library/Mobile Documents/com~apple~CloudDocs/code/check/project.csv")

df_heat =pd.read_csv("/Users/tomoya/Library/Mobile Documents/com~apple~CloudDocs/code/check/heatmap.csv")
#出力用のrule名のリスト
rulelists =[] 

for i in range(0,184):
    rulelists.insert(i, df_rule.iloc[i,1])


df_outrule = pd.DataFrame(rulelists, columns = ['ruleName / ProjectName'])

#ルールを検出する一連の処理
#横方向の処理プロジェクトA→B→C......
for i in range(0,103):#101

    #存在するルール名を格納するためのリスト
    checklist = []

    #project.csvからプロジェクト名を抽出する
    Project_Name = df_pro.iloc[i,0]
    #スラッシュがあると読み込み時にパスがおかしくなるのでアンダーバーに置換

    #縦方向にルールを検出する処理
    #プロジェクト名のxmlファイルを読み込む
    tree = ET.parse('/Users/tomoya/Library/Mobile Documents/com~apple~CloudDocs/code/xml/'+Project_Name+'.xml')
    root = tree.getroot()

    #出力確認用
    print ('"'+Project_Name+'のルール一覧を出力"')
    for module in root.iter('module'):
        tmp1 = str(module.attrib)
        #空白の削除とチェック名の文字列の整形
        tmp2 = tmp1.replace(' ', '')
        tmp3 = tmp2[9:]
        check_name = tmp3[:-2]
        
        #ルール名のcsvと比較して, 検出したチェック名をリストに入れる
        for i in range(0,184):
        
            if (df_rule.iloc[i,1] == check_name) : checklist.insert(i,check_name)

    #重複しているルール名を削除        
    check_unique = list(set(checklist))
    
    #ルール名が存在→1、ない→0としたリストを作成
    output=[]
    for i in range(0,184):
        if (df_rule.iloc[i,1] in check_unique) :output.insert(i,df_rule.iloc[i,1])
        else:output.insert(i,0)

    #出力用のデータフレームに追加していく
    df_outrule[Project_Name] = output
    #print(output)
    #df_heat[Project_Name] = check_unique

#print(df_outrule)
df_outrule.to_csv('/Users/tomoya/Library/Mobile Documents/com~apple~CloudDocs/code/check/shugo.csv')

