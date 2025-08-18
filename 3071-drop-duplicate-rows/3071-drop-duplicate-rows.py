import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    data_cleaned = customers.drop_duplicates(subset='email', keep='first')
    return data_cleaned

data = {'customer_id':[1, 2, 3, 4, 5, 6], 'name':['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'], 'email':['emily@example.com', 'michael@example.com', 'sarah@example.com', 'john@example.com', 'john@example.com', 'alice@example.com']}

df = pd.DataFrame(data)

print(dropDuplicateEmails(df))