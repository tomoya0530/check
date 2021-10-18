import pandas as pd


#csvをデータフレームに読み込む
df = pd.read_csv("/Users/tomoya/Library/Mobile Documents/com~apple~CloudDocs/code/check/rulecsv.csv")

#対象のcheckstyleをtextにしたものを開く
f = open('/Users/tomoya/Library/Mobile Documents/com~apple~CloudDocs/code/check/zxingcheck.txt', 'r', encoding='UTF-8')
data = f.read()



def rule_find():
 #検出されたルールの数をカウントする変数
 sum=0
 print("   注釈のチェック")
 for i in range(0,8):
    rule = df.iloc[i,1]
    test = '<module name="'+rule+'"/>'
    if test in data : 
        print(rule) 
        sum +=1

 print("   ブロックチェック")
 for i in range(8,14):
    rule = df.iloc[i,1]
    test = '<module name="'+rule+'"/>'
    if test in data :
        print(rule) 
        sum +=1

 print("   クラスデザイン")
 for i in range(14,23):
    rule = df.iloc[i,1]
    test = '<module name="'+rule+'"/>'
    if test in data :
        print(rule) 
        sum +=1

 print("   コーディング")
 for i in range(23,75):
    rule = df.iloc[i,1]
    test = '<module name="'+rule+'"/>'
    if test in data :
        print(rule) 
        sum +=1

 print("   ヘッダー")
 for i in range(75,77):
    rule = df.iloc[i,1]
    test = '<module name="'+rule+'"/>'
    if test in data :
        print(rule) 
        sum +=1

 print("   インポート")
 for i in range(77,85):
    rule = df.iloc[i,1]
    test = '<module name="'+rule+'"/>'
    if test in data :
        print(rule) 
        sum +=1

 print("   ジャバDocコメント")
 for i in range(85,106):
    rule = df.iloc[i,1]
    test = '<module name="'+rule+'"/>'
    if test in data :
        print(rule) 
        sum +=1

 print("   メトリクス")
 for i in range(106,112):
    rule = df.iloc[i,1]
    test = '<module name="'+rule+'"/>'
    if test in data :
        print(rule) 
        sum +=1

 print("   その他")
 for i in range(112,128):
    rule = df.iloc[i,1]
    test = '<module name="'+rule+'"/>'
    if test in data :
        print(rule) 
        sum +=1

 print("   修飾子")
 for i in range(128,132):
    rule = df.iloc[i,1]
    test = '<module name="'+rule+'"/>'
    if test in data :
        print(rule) 
        sum +=1

 print("   命名規則")
 for i in range(132,153):
    rule = df.iloc[i,1]
    test = '<module name="'+rule+'"/>'
    if test in data :
        print(rule) 
        sum +=1

 print("   正規表現")
 for i in range(153,158):
    rule = df.iloc[i,1]
    test = '<module name="'+rule+'"/>'
    if test in data :
        print(rule) 
        sum +=1

 print("   サイズ")
 for i in range(158,168):
    rule = df.iloc[i,1]
    test = '<module name="'+rule+'"/>'
    if test in data :
        print(rule) 
        sum +=1

 print("   空白")
 for i in range(168,185):
    rule = df.iloc[i,1]
    test = '<module name="'+rule+'"/>'
    if test in data :
        print(rule) 
        sum +=1
 print("合計のルール数は"+str(sum))

rule_find()