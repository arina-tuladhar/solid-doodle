import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
   melted = report.melt(id_vars='product', var_name='quarter', value_name='sales')
   # melted = pd.melt(report,id_vars='product', var_name='quarter', value_name='sales') 
   return melted

data = pd.DataFrame({'product':['Umbrella', 'SleepingBag'], 'quarter_1':[417, 800], 'quarter_2':[224, 936], 'quarter_3':[397, 93], 'quarter_4':[611, 875]})

print(meltTable(data))