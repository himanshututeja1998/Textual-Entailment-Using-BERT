import pandas as pd
import numpy as np

data=pd.read_csv("entail.csv")
data2=data.values

entail=np.chararray((734,734), itemsize=15, unicode=False)
for ii in range(len(data2)):
    jj=(int)(data2[ii][0])
    kk=(int)(data2[ii][1])
    labels11=["contradiction", "entailment", "neutral"]
    result = np.where(data2[ii] == np.amax(data2[ii][2:5]))
    ans=result[0][0]
    ans1=ans-2
    print()
    entail[jj][kk]=labels11[ans1]
preds1=pd.DataFrame(entail)
preds1.to_csv("matrix.csv",index=False)