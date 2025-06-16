import pandas as pd 
data ={
  "Name" : ["Arun","Varun","Karun","Narun","Tarun"],
  "Age" :[20,15,30,34,28],
  "Salary" :[50000,60000,45000,52000,40000]
}
df = pd.DataFrame(data)
avg_salary = df["Salary"].mean()
print(avg_salary)

grouped = df.groupby("Age")["Salary"].sum()
#grouped = df.groupby(["Age","Name"])["Salary"].sum()
print(grouped)
