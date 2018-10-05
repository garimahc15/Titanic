import numpy as np
import pandas as pd


source_dir=('.\Data')
df = pd.read_excel(source_dir+'\\titanic3.xls')

df1=df[df['pclass'].isin(['1'])]
df2=df[df['pclass'].isin(['2'])]
df3=df[df['pclass'].isin(['3'])]
df3=df[df['pclass'].isin(['4'])]


dfr=df.copy()

df.info()

df.rename(columns={'home.dest':'homdes'}, inplace=True)

df[['Home','destination']] = df.homdes.str.split(',', expand=True)

df7 = df['homdes'].str.split(',').str[-1]

dflb=df7.copy()
#df7.ver = df7.homdes.replace({'MO:','ON:','NY:','NI:','PQ:','MN:','CA:','MI:','DC:','NJ:','OH:','MB:','WA:','NE:','PA:','CO:','MA:','ND:','BC:','IN:','WI:','AB:','IA:','CT:','IL:','VT:','RI:','WV:','ME:','NS:','FL:','NM:','ID:','UT:'})




a=list(df7.unique())

df8=df.pivot(index='index', columns='embarked', values='embarked')

df=df.reset_index()


df.columns=['nan','Cherbourg','queensland','Southampton']


result.drop('male', axis=1, inplace=True)

#df8['Q']=df['Q'].replace(3,'Lower Class')




df.info()


#

a=df.isnull().sum()
a
g = df.groupby(("name"),["name", "age"])


g.groups


df2=df.groupby(pd.cut(df["age"], np.arange(0,18))).count()






g = df.groupby('age')
g.count()

dfn = (df['age'].value_counts(dropna=False))
dfc=df.copy()

dfc["age"] = dfc.groupby("Passenger Name").transform(lambda x: x.fillna(x.mean()))




df[['fname','sallas']] = df.name.str.split(',', expand=True)





df['salu'] = df.name.str.extract(r',\s*([^\.]*)\s*\.', expand=False)


list(df['salu'].unique())





df1=df.pivot(index='index', columns='salu', values='salu')


result = pd.concat([df, df1], axis=1)



df.rename(columns={'the Countess':'Countess'}, inplace=True)

result=result.reset_index()

result=result['level_0']
df3=df[['Countesss']].sum()


result.to_csv('titanic_resulto.csv')

list(result.columns.values)

result.reindex(columns=['index','pclass','survived','name','sex','age','sibsp','parch',
 'ticket','fare','cabin','embarked','boat','body','home.dest','fname','sallas','salu',
 'Capt','Col','Don','Dona','Dr','Jonkheer','Lady','Major','Master','Miss','Mlle','Mme',
 'Mr','Mrs','Ms','Rev','Sir','the Countess'])




df3=result[['the Countesss']].sum()



rc=result.copy()


df[ticket].unique()

df4=df.groupby(['pclass','sex'])['age'].mean()

dfc=df.copy()
df4=df4.reset_index()

result=rc.copy()

round(df4.iloc[1,2],2)#male 1
round(df4.iloc[0,2],2)#female 1

round(df4.iloc[2,2],2)#male2
round(df4.iloc[3,2],2)#female2

round(df4.iloc[5,2],2)#male3
round(df4.iloc[4,2],2)#female 3

result['age'] = result['age'].replace(result[(result['pclass']==1) & (result['sex']=='male') & (result['age'].isnull())]['age'],round(df4.iloc[1,2],2))
result['age'] = result['age'].replace(result[(result['pclass']==1) & (result['sex']=='female') & (result['age'].isnull())]['age'],round(df4.iloc[0,2],2))


result['age'] = result['age'].replace(result[(result['pclass']==2) & (result['sex']=='male') & (result['age'].isnull())]['age'],round(df4.iloc[2,2],2))
result['age'] = result['age'].replace(result[(result['pclass']==2) & (result['sex']=='female') & (result['age'].isnull())]['age'],round(df4.iloc[3,2],2))

result['age'] = result['age'].replace(result[(result['pclass']==3) & (result['sex']=='male') & (result['age'].isnull())]['age'],round(df4.iloc[5,2],2))
result['age'] = result['age'].replace(result[(result['pclass']==3) & (result['sex']=='female') & (result['age'].isnull())]['age'],round(df4.iloc[4,2],2))

result.info()


list(result['ticket'].unique())





df0=df.groupby(['cabin','fare'])['fare'].count()

df0=df0.reset_index()
df0 = df0.to_frame()
df0.columns=['mfare']
result.info()

















































