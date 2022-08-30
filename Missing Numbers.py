import numpy as np
import pandas as pd
q = '3 4 5 3 4 4 nan'.split()
lst = [float(x) if x != 'nan' else np.NaN for x in q]
data = {"Num":lst}
lst1 = pd.Series(lst)
m = round(np.mean(lst1),1)
df = lst1.fillna(value=m)
print(df)
# Works fine 