import pandas as pd
# an array is a a sequence of value
from pandas import Series, DataFrame
import numpy as np

# a serie is a one dimentional array-like object containing a sequence of values.
# the most simple for of serie can be seen below.
# the index in the serie is seen to the left and the value to the right

ser=pd.Series()
# creating an empty series

data=np.array(['g', 'e', 'e', 'k', 's'])

ser=pd.Series(data)

testing_indexing=pd.Series(['g', 'e', 'e', 'k', 's'], index=['a', 'b', 'c', 'd', 'e']

print(testing_indexing)

df=pd.DataFrame()

lst=["Geeks", "for", "geeks", "is", "portal", "for", "geeks"]

df=pd.DataFrame(lst)
print(df)
