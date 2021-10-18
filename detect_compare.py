import numpy as np

def jaccard_similarity(x, y):
    intersection = len(set.intersection(*[set(x), set(y)]))
    union = len(set.union(*[set(x), set(y)]))
    return intersection / float(union)

MY = ["FileTabCharacterCheck","IndentationCheck:'method def'","LocalVariableNameCheck","WhitespaceAroundCheck","WhitespaceBefore","IndentationCheck:'for'","WhitespaceAroundCheck:'='","WhitespaceAfterCheck:'for'","WhitespaceAroundCheck:'<='","WhitespaceAroundCheck:'='","WhitespaceAroundCheck:'<='",".IndentationCheck:'method def rcurly"]
COPY = ["IndentationCheck:'for'","FileTabCharacterCheck","WhitespaceAfterCheck:'for' " , "WhitespaceAroundCheck:'{'"]

ruiji = jaccard_similarity(MY,COPY)
print("類似度は"+str(ruiji*100)+"%")

