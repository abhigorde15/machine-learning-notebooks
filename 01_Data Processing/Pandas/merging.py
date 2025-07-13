import pandas as pd 
df_customer = {
  "Cust_id" : [1,2,4],
  "Name" :["Abhishek","Pavan","Ayush"],
}
df_order = {
  "Cust_id" : [1,2,3],
  "Amount" : [250,500,450]
}
df1 = pd.DataFrame(df_customer)
df2 = pd.DataFrame(df_order)
print(pd.merge(df1,df2,how="inner"))

df_region1 = {
  "Cust_id" : [1,2,4],
  "Name" :["Abhishek","Pavan","Ayush"],
}
df_region2 = {
  "Cust_id" : [3,5],
  "Name" : ["Gupta","Aditya"]
}
df3 = pd.DataFrame(df_region1)
df4 = pd.DataFrame(df_region2)
df_concat = pd.concat([df3,df4],axis=0,ignore_index=True)
print(df_concat)

