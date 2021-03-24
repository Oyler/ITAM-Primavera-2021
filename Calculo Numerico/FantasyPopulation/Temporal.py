import numpy as np
import pandas as pd

df = pd.read_csv('D:\Downloads\Temp.csv')
names = df['Names']
surnames = df['Surnames']

fullname = []
for name in names:
    for surname in surnames:
        new_name = name + ' ' + surname
        fullname.append(new_name)
new_df = pd.DataFrame(fullname, columns=['Fullnames'])
new_df.to_csv('MaleDragonbornNames.csv')