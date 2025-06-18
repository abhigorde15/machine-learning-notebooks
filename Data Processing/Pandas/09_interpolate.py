"""
1.preserve data integrity 
2. smooth trends 
3.avoid data loss
4. used mostly in :- time series data,numeric data with trends,avoid dropping data
10,20,30,Nan,50,60 
by interpolation Nan will be filled with 40
"""
import pandas as pd
data ={
  "Name" : ["Ram","Shyam","Ghanshyam"],
  "Age" : [10,None,30],
  "City" :["Nagpur","Nashik","Pune"],
  "Salary" :[50000,60000,45000]
}
df = pd.DataFrame(data)
print(df)
df.interpolate(method="linear",axis=0,inplace=True)