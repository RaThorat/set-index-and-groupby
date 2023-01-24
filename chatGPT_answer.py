import pandas as pd

data={'Application number':[0,1,2,3,4,5,6,7,8,9],
      'Physics':[1,0,1,0,1,0,0,1,1,0],
     'Chemistry':[1,0,0,0,1,0,0,0,0,1],
     'Biology':[0,1,0,1,1,0,1,0,0,0],
     'Mathematics':[0,0,0,0,1,1,0,0,1,0]}

df=pd.DataFrame(data)
df = df.set_index('Application number')

out = (
    df[df==1]
    .stack()
    .reset_index()
    .drop(0, axis=1)
    .rename(columns={'level_1': 'Discipline_list'})
    .groupby('Application number', as_index=False)
    .agg(Discipline_list=('Discipline_list', lambda x: ', '.join(x)))
)

out.to_csv('out.csv')
