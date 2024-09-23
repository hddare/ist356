import numpy as np
import pandas as pd
s1 = pd.Series(data=[1,2,3,4], index=['a','b','c','d'])
s2 = pd.Series(data=[2.2,np.nan,3.0,1.5], index=['a','b','c','d'])
s3 = pd.Series(data=['q','q','z','z'], index=['a','b','c','d'])
df = pd.DataFrame( {'s1': s1, 's2': s2, 's3': s3})
df

grade = df.loc['c', 's2']
print(grade)
twoqs = df.loc['a':'b', 's3']
print(twoqs)
print(df.loc['c':'d', 's2':'s3'])