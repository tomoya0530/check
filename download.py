#GitHubからxmlファイルをダウンロード
import wget as wg
import pandas as pd
import os
import time

df = pd.read_csv("/Users/tomoya/Library/Mobile Documents/com~apple~CloudDocs/code/check/project.csv")

for i in range(0,104):
    Project = df.iloc[i,0]
    #ファイルのダウンロード時に/があると上手くいかないのでアンダーバーに置換
    Project_Name = Project.replace('/', '_')
    print(Project_Name)
    URL = df.iloc[i,2]
    # xmlをダウンロードする
    wg.download(URL, '/Users/tomoya/Library/Mobile Documents/com~apple~CloudDocs/code/xml/'+Project_Name+'.xml')




    