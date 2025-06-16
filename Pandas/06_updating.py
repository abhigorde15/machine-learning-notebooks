import pandas as pd 
data ={
  "Name" : ["Ram","Shyam","Ghanshyam"],
  "Age" : [10,20,30],
  "City" :["Nagpur","Mumbai","Pune"],
  "Salary" :[50000,60000,45000]
}
df = pd.DataFrame(data)
print(df)
# .loc[row_idx,"Col_name"] = new_value 
df.loc[0,"Salary"] = 70000
print("After changing 0th row of salary")
print(df)
#increase salary by 5% 
print("After 5% increse in all salaries")
df["Salary"] = df["Salary"]*1.05 
print(df)