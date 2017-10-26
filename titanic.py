import pandas as pd
source_dir=('.\data')
df = pd.read_excel(source_dir+'\\titanic3.xls')

cols=df.columns.values.tolist()

df['survived']=df['survived'].replace(1,'Yes')
df['survived']=df['survived'].replace(0,'No')

df['pclass']=df['pclass'].replace(1,'Upper Class')
df['pclass']=df['pclass'].replace(2,'Middle Class')
df['pclass']=df['pclass'].replace(3,'Lower Class')

df.rename(columns={'pclass': 'Passenger Class', 'name': 'Passenger Name','sibsp':'siblings/spouse in titanic','parch':'parents/children in titanic','boar':'lifeboat no','body':'mortuary boat no','home.dest':'destination'}, inplace=True)











df.to_excel(source_dir+'\\filtered.xls')