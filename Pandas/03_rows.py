#head(n) and tail(n)
import pandas as pd
df = pd.read_csv("Pandas/sales_data_sample.csv", encoding="latin1")
df.head(6)
print(df)#display starting 6 
print("Displaying Information of df")
print(df.info())