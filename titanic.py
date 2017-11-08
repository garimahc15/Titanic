import pandas as pd
source_dir=('.\data')
df = pd.read_excel(source_dir+'\\filtered1.xlsx')

cols=df.columns.values.tolist()

"""
df['survived']=df['survived'].replace('Yes',1)
df['survived']=df['survived'].replace('No',0)

df['pclass']=df['pclass'].replace(1,'Upper Class')
df['pclass']=df['pclass'].replace(2,'Middle Class')
df['pclass']=df['pclass'].replace(3,'Lower Class')

df['embarked']=df['embarked'].replace('C','Cherbourg')
df['embarked']=df['embarked'].replace('Q','Queenstown')
df['embarked']=df['embarked'].replace('S','Southampton')

df.rename(columns={'pclass': 'Passenger Class', 'name': 'Passenger Name','sibsp':'siblings/spouse in titanic','parch':'parents/children in titanic','boar':'lifeboat no','body':'mortuary boat no'}, inplace=True)

df.rename(columns={'home.dest':'homdes'}, inplace=True)

df['Address 1']=df['homdes'].str.split(',').str[0]
df['State / Country']= df['homdes'].str.split(',').str[-1]

df = df.drop('homdes', 1)
df.rename(columns={'Passenger Name':'passenger_name'}, inplace=True)

df[['fname','sallas']] = df.passenger_name.str.split(',', expand=True)

df['salutation'] = df.passenger_name.str.extract(r',\s*([^\.]*)\s*\.', expand=False)

salutaion=list(df['salutation'].unique())

df['lname']= df['sallas'].str.split('.').str[1]

df = df.drop('sallas', 1)
df = df.drop('passenger_name', 1)
"""
nulls=df.isnull().sum()
"""
df=df.drop(df.index[0])

df=df.drop('index',1)


ag=df['age'].tolist()

fare=df['fare'].tolist()


df=df[['salutation','fname','lname','age','sex','Address 1','State / Country','embarked','Passenger Class','siblings/spouse in titanic','parents/children in titanic','ticket','fare','cabin','survived','boat','mortuary boat no']]

df=df.sort_values('fname')

mean_age = df.groupby(['sex','Passenger Class'])['age'].mean()

def nanages(row):
    
    if pd.isnull(row['age']):
        return mean_age[row['sex'],row['Passenger Class']]
    else:
        return row['age']

df['age'] =df.apply(nanages, axis=1)


labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-80']
df['age_group'] = pd.cut(df.age, range(0, 81, 10), right=False, labels=labels)



"""
total= pd.crosstab(df['survived'],df['sex'])

total1 = pd.crosstab(df['survived'],df['Passenger Class'])

mean_survival=df.groupby('Passenger Class').survived.mean()
survival_groups=df.groupby(['age_group']).survived.mean()
survival_by_mail_female=df.groupby(['sex','age_group']).survived.mean()




df.to_excel(source_dir+'\\filtered1.xlsx') 
