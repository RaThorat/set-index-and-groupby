#Answer by User Rabinzel — Stack Overflow (https://stackoverflow.com/users/15521392/rabinzel)
data={'Application number':[0,1,2,3,4,5,6,7,8,9],
      'Physics':[1,0,1,0,1,0,0,1,1,0],
     'Chemistry':[1,0,0,0,1,0,0,0,0,1],
     'Biology':[0,1,0,1,1,0,1,0,0,0],
     'Mathematics':[0,0,0,0,1,1,0,0,1,0]}

df=pd.DataFrame(data)
print(df)
df = df.set_index('Application number')

out = (
    df[df==1]
    .stack()
    .reset_index()
    .drop(0, axis=1)
    .rename(columns={'level_1': 'Discipline_list'})
    .groupby('Application number', as_index=False)
    .agg(Discipline_list=('Discipline_list', lambda x: ', '.join(x)),
 All_Discipline_count=('Discipline_list', 'count'))
)

print(out)
