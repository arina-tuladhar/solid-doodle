import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    data = pd.concat([df1, df2], ignore_index = True)
    return data

data1 = pd.DataFrame({'student_id':[1, 2, 3, 4], 'name':['Mason', 'Ava', 'Taylor', 'Georgia'], 'age':[8, 6, 15, 17]})
data2 = pd.DataFrame({'student_id':[5, 6], 'name':['Leo', 'Alex'], 'age':[7, 7]})
print(concatenateTables(data1, data2))