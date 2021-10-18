import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import seaborn as sns
pd.set_option('display.max_columns', 400)
pd.set_option('display.max_rows', 400)


#100件の対応表のcsvを読み込む
df = pd.read_csv("/Users/tomoya/Library/Mobile Documents/com~apple~CloudDocs/code/check/heatmapdf.csv")

heat_df = pd.pivot_table(df, index='Project', columns='Project')

sns.heatmap(heat_df)
