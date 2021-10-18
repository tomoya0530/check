import pandas as pd
import csv
#from pathlib import Path
import xml.etree.ElementTree as ET
pd.set_option('display.max_columns', 200)
pd.set_option('display.max_rows', 200)

#ルール名がまとめられているCSVの読み込み
df_rule = pd.read_csv("/Users/tomoya/Library/Mobile Documents/com~apple~CloudDocs/code/check/rulecsv.csv")

#プロジェクト名がまとめられているCSVの読み込み
df_pro = pd.read_csv("/Users/tomoya/Library/Mobile Documents/com~apple~CloudDocs/code/check/project.csv")


#ルールを検出する一連の処理
#横方向の処理プロジェクトA→B→C......
for i in range(0,101):
    Project = df_pro.iloc[i,0]
    #スラッシュがあるとパスがおかしくなるのでアンダーバーに置換
    Project_Name = Project.replace('/', '_')

    #縦方向にルールを検出する処理
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
        
        #ルール名のcsvと比較して, チェックの検出
        for i in range(0,185):
            sum =0 
            if (df_rule.iloc[i,1] == check_name) : print(check_name)
    
    print('')
    print('--------------------------------------------------------------------------------------------------------------------')
