import pandas as pd
data ={
  "Name" : ["Ram","Shyam","Ghanshyam"],
  "Age" : [10,20,30],
  "City" :["Nagpur","Mumbai","Pune"],
  "Salary" :[50000,60000,45000]
}
df = pd.DataFrame(data)
print(df)

df.drop(columns=["City"],inplace=True)# if we want multiple cols to remove then use , and give all cols in columns=["Salary","Age"] this way
print("After droping City")
print(df)