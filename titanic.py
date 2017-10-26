import pandas as pd
source_dir=('.\data')
df = pd.read_excel(source_dir+'\\titanic3.xls')

cols=df.columns.values.tolist()

df['survived']=df['survived'].replace(1,'Yes')
df['survived']=df['survived'].replace(0,'No')

