import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

data = {'employee_id' : [3, 90, 9, 60, 49, 43], 'name' : ['Bob', 'Alice', 'Tatiana', 'Annabelle',         'Jonathan', 'Khaled'], 'department' : ['Operations', 'Sales', 'Engineering', 'Information Technology', 'Human Resources', 'Administration'], 'salary': [48675, 11096, 33805, 37678, 23793, 40454]}

df = pd.DataFrame(data)
print(selectFirstRows(df))
