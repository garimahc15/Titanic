import pandas as pd
source_dir=('.\data')
df = pd.read_excel(source_dir+'\\filtered.xls')

cols=df.columns.values.tolist()
"""
df['survived']=df['survived'].replace(1,'Yes')
df['survived']=df['survived'].replace(0,'No')

df['pclass']=df['pclass'].replace(1,'Upper Class')
df['pclass']=df['pclass'].replace(2,'Middle Class')
df['pclass']=df['pclass'].replace(3,'Lower Class')


df['embarked']=df['embarked'].replace('C','Cherbourg')
df['embarked']=df['embarked'].replace('Q','Queenstown')
df['embarked']=df['embarked'].replace('S','Southampton')


df.rename(columns={'pclass': 'Passenger Class', 'name': 'Passenger Name','sibsp':'siblings/spouse in titanic','parch':'parents/children in titanic','boar':'lifeboat no','body':'mortuary boat no','home.dest':'Destination'}, inplace=True)


df.rename(columns={'home.dest':'homdes'}, inplace=True)

df['Address 1']=df['homdes'].str.split(',').str[0]
df['Address 2']= df['homdes'].str.split(',').str[-1]


df = df.drop('homdes', 1)


df[['fname','sallas']] = df.Passenger_Name.str.split(',', expand=True)

df['salutaion'] = df.Passenger_Name.str.extract(r',\s*([^\.]*)\s*\.', expand=False)
list(df['salutaion'].unique())
df.rename(columns={'the Countess':'Countess'}, inplace=True)

"""



df.to_excel(source_dir+'\\filtered.xls') 
