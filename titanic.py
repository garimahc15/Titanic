import pandas as pd
source_dir=('.\data')
df = pd.read_excel(source_dir+'\\titanic3.xls')

cols=df.columns.values.tolist()



