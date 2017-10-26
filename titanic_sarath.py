import numpy as np
import pandas as pd

source_dir=('.\Data')
df = pd.read_excel(source_dir+'\\titanic3.xls')

df1=df[df['pclass'].isin(['1'])]
df2=df[df['pclass'].isin(['2'])]
df3=df[df['pclass'].isin(['3'])]

dfr=df.copy()
df4 = pd.concat([df['home.dest'], df[13].str.split(',', expand=True)], axis=1)
