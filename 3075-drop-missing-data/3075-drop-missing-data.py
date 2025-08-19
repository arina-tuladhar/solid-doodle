import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    data_cleaned = students.dropna(axis=0, subset='name')
    return data_cleaned

data = {'student_id': [355, 951, 470, 977, 300], 'name': [None, None, 'Quincy', 'Sophia', 'Liam'], 'age': [9, 8, 20, None, 15]}

df = pd.DataFrame(data)

print(dropMissingData(df))