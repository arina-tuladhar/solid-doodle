import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    student_info = students.loc[students['student_id'] == 101, ['name', 'age']]
    return student_info

data = {'student_id': [101  ,53, 128, 3 ], 'name': ['Ulysses', 'William', 'Henry', 'Henry'], 'age': [13, 10, 6, 11] }

df = pd.DataFrame(data)

print(selectData(df))