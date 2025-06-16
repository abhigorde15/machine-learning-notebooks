import pandas as pd
data ={
  "Name" : ["Ram",None,"Ghanshyam"],
  "Age" : [10,None,30],
  "City" :["Nagpur",None,"Pune"],
  "Salary" :[50000,None,45000]
}
df = pd.DataFrame(data)
print(df)
print(df.isnull())
print("Total Missing values in  df",df.isnull().sum())
#df.dropna(inplace=True)
#print("After Removing Missing data Row",df)
#df.fillna(0,inplace= True)
#print("After Adding values to None",df)
df["Age"].fillna(df["Age"].mean(),inplace=True)
print("Filled Age with mean value \n",df)