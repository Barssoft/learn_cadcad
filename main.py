import pandas as pd
from model.run import df

df1 = df.copy(deep=True)
print(df1)
last_row = df1.iloc[-1]
print(last_row)
print(len(last_row["agents"]))
print(last_row["agents"].shape[0])

columns = [f"col{i}" for i in range(10)]
df4 = pd.DataFrame(last_row["agents"], columns=columns)

# Выводим DataFrame
print(df4)
