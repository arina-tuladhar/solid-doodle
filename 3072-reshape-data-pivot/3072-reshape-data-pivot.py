import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    pivoted = weather.pivot_table(index='month', columns='city', values='temperature')
    return pivoted

data = pd.DataFrame({'city':['Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'Elpaso', 'Elpaso', 'Elpaso', 'Elpaso', 'Elpaso'], 'month':['January', 'February', 'March', 'April', 'May', 'January', 'February', 'March', 'April', 'May'], 'temperature':[13, 23, 38, 5, 34, 20, 6, 26, 2, 43]})

print(pivotTable(data))