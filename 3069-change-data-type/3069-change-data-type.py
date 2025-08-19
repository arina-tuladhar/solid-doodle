import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students

data = pd.DataFrame({'student_id':[1, 2], 'name':['Ava', 'Kate'], 'age':[6, 15], 'grade':[73.0, 87.0]})
print(changeDatatype(data))