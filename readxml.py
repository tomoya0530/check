import xml.etree.ElementTree as ET
import pandas as pd

#xmlをElementTreeに読み込む
tree = ET.parse('/Users/tomoya/Library/Mobile Documents/com~apple~CloudDocs/code/check/zxingcheck.xml')

df = pd.read_csv("/Users/tomoya/Library/Mobile Documents/com~apple~CloudDocs/code/check/rulecsv.csv")
root = tree.getroot()
pd.set_option('display.max_columns', 200)
pd.set_option('display.max_rows', 200)


for module in root.iter('module'):
    tmp1 = str(module.attrib)
    #空白の削除とチェック名の文字列の整形
    tmp2 = tmp1.replace(' ', '')
    tmp3 = tmp2[9:]
    
    check_name = tmp3[:-2]
    #ルール名のcsvと比較して, チェックの検出
    for i in range(0,185):
        sum =0 
        if (df.iloc[i,1] == check_name) : print(check_name)
