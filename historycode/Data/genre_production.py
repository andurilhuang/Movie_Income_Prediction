import pandas as pd

df = pd.read_csv("FinalMerge.csv", encoding="latin1")
#df.shape 2384, 19
df['Production'] = df['Production'].str.split(' ').str.get(0)
#df.groupby('Production')['Production'].count()
#prod = df.Production.unique()
#len(prod)
# 312 Production companies

df = pd.concat([df, df['Genre'].str.get_dummies(sep=', ')], axis=1) 
#df.shape  2384, 42
#list(df[df.columns[19:42]])

df['Thriller'] = df[['Thriller', 'Horror']].sum(axis=1)
df['Fantasy'] = df[['Fantasy', 'Sci-Fi']].sum(axis=1)
df['Other'] = df[['Music', 'History', 'Sport', 'War', 'Western', 'Musical', 'Documentary', 'News', 'Short']].sum(axis=1)
df.drop(['Music', 'History', 'Sport', 'War', 'Western', 'Musical', 'Documentary', 'News', 'Short', 'Horror', 'Sci-Fi'], axis=1, inplace=True)
#df.shape 2384 32
#df

variables = list(df)[19:32]
for x in variables:
    #print(x)
    df.loc[df['%s' % x] > 1, '%s' % x] = 1
    #print(df['%s' % x].value_counts())