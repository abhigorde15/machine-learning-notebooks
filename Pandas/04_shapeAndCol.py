"""
1. how big is dataset 
2.what are the names of cols 

"""
import pandas as pd 
data ={
  "Name" : ["Ram","Shyam","Ghanshyam"],
  "Age" : [10,20,30],
  "City" :["Nagpur","Mumbai","Pune"]
}
df = pd.DataFrame(data)
print("Shape",df.shape)
print("Column Names",df.columns)

"""
1.select specific col  (use square brackets)
2. filter rows (boolean conditions)
3. combine multiple conditions
"""

print("Name Column Content:- \n",df["Name"])
filter_row = df[df["Age"]>= 20]
print("Age Greater than equal to 20 ",filter_row)

filtered = df[(df["Age"] >20) & (df["Age"]<=30)]
print("Age Greater than 20 and less than equal to 30",filter_row)
subset = df[[ "Name", "Age"]]
print(subset)