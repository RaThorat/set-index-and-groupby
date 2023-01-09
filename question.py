# Is there a better way to summerize a table information instead of using iloc and append method with nested loops in pandas?
# I have a table of grant application numbers and their corresponding disciplines given by cell value 1.
import pandas as pd
import numpy as np
data={'Application number':[0,1,2,3,4,5,6,7,8,9],
      'Physics':[1,0,1,0,1,0,0,1,1,0],
     'Chemistry':[1,0,0,0,1,0,0,0,0,1],
     'Biology':[0,1,0,1,1,0,1,0,0,0],
     'Mathematics':[0,0,0,0,1,1,0,0,1,0]}

#creation of dataframe
df=pd.DataFrame(data)

#column counting all disciplines per grant
df['All_Discipline_count']=df.loc[:,'Physics' : 'Mathematics'].sum(axis=1)

df.head(10)
# I would like to summarize discipline list and discipline count per grant application. I do that using iloc and multiple nested loops.
# Creation of resulting dataframe
dfA = pd.DataFrame(columns = ['Application number', 'Discipline_list', 'All_Discipline_count'])

# Pay attention to how iloc a cell selects. 'Application number' is zeroth column. 
i=0 #starts from oth row
j=1 #starts from 1st column
Aanvraag_nummer=0
k=df.columns.get_loc("All_Discipline_count") #column number where the All_Discipline_count is
l=len(df.index)#number of rows
for i in range (0,l):
    Discipline_count=0 #introducing zero discipline count
    Discipline_list=" " #introducing empty discipline list
    for j in range (1,k): #counting columns of disciplines
        if (df.iloc[i,j]==1) & (Discipline_count<df.iloc[i,k]): #if the given cell has 1 as value
            Discipline_list=Discipline_list+ df.columns[j] #adds a column name to discipline list
            Discipline_count+=1 #counts the number of disciplines with 1 as value
            if Discipline_count==df.iloc[i,k]:#if all disciplines are counted
                Aanvraag_nummer=df.iloc[i,0]
                new_row = {'Application number':Aanvraag_nummer, 'Discipline_list':Discipline_list, 'All_Discipline_count':df.iloc[i,k]}
                dfA = dfA.append(new_row, ignore_index=True)
dfA.head(10)
# The script works for 10 to 100 applications and 20 disciplines as columns. It also works when there are multiple disciplines are given per grant application.

# However, I notice that I get warning while running the code.
#/tmp/ipykernel_26718/1290491379.py:19: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

#The code is also slow..Any better method to get the same results?

