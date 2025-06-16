import pandas as pd 
data ={
  "Name" : ["Ram","Shyam","Ghanshyam"],
  "Age" : [10,20,30],
  "City" :["Nagpur","Mumbai","Pune"],
  "Salary" :[50000,60000,45000]
}
df = pd.DataFrame(data)
print(df)
#df["Bonus"] = df["Salary"]*0.1
#print(df)

# df.insert(loc,"Col_name",data)
df.insert(0,"Emp_id",[10,20,30])
print(df)