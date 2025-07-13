#head(n) and tail(n)
import pandas as pd
df = pd.read_csv(r"D:\AIML\AIML\01_Data Processing\Pandas\sales_data_sample.csv", encoding="latin1")
# df.head(6)#display starting 6 
# print(df)

# print("Information of data:")
# df.info()# class,entries,column ,nonnull count,dtype, xx rows * yy cols

data ={
  "Name" : ["Ram","Shyam","Ghanshyam","Jagdish"],
  "Age" : [28,34,30,40],
  "salary" :[50000,60000,45000,57000],
  "City" :["Nagpur","Mumbai","Pune","Nashik"]
}
df = pd.DataFrame(data)
print("Sample Data ")
#print(df)
print("\n Descriptive Statistic")
print(df.describe())
