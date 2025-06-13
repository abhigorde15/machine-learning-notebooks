import pandas as pd 
#read data from csv file 
#df = pd.read_csv("Pandas/sales_data_sample.csv", encoding="latin1")
#df = pd.read_excel("Pandas/SampleSuperstore.xlsx", engine="openpyxl")
df = pd.read_json("Pandas/sample_Data.json")
print(df)