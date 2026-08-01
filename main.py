import pandas as pd 

data1 = pd.read_csv("data/daily_sales_data_0.csv")
data2 = pd.read_csv("data/daily_sales_data_1.csv")
data3 = pd.read_csv("data/daily_sales_data_2.csv")

all_data = pd.concat([data1, data2, data3], ignore_index=True)         # all products 

pink_data = all_data[all_data["product"] == "pink morsel"]     

pink_data["Sales"] = (pink_data["quantity"] * pink_data["price"].str.replace("$", "", regex=False).astype(float))

final_data = pink_data[["Sales", "date", "region"]]

final_data.to_csv("output.csv", index=False)

