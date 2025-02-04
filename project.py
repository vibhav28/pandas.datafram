import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv",sep="\t") 

##this will tell the total entries in a file
entries=len(df)
print(f"no. of entries in the file is:{entries}")
#
##this will print the columns names in a list format  
df.columns=df.columns.str.strip()  
print(df.columns)

##this will print the most selling order
most_ordered_item = df['item_name'].value_counts().iloc[0]
print(f"the most ordered item is chicken bowl which is ordered : {most_ordered_item}times" )
#
##this will convert the item price from string to float
s = df["item_price"]= df["item_price"].str.replace('$','').astype(float)
print(s)
#
##this will print the total revenue sale 
a=df["item_price"].sum()
print(f"the total revenue for the period given in the dataset is {a}")
#
#this will print the average total revenue sale
b=df.groupby("item_name")["item_price"].sum().mean()
print(f"the average revenue amount per order is {b}")


#
# orders greater than 10$
grouped_items = df[df['item_price'] > 10]
print("Items greater than $10:")
print(grouped_items[['order_id','item_name','item_price']])

##this will tell the name of items in the menu or  item_name column
print(df["item_name"].unique().tolist())


#to print the items which are more than 10$
top_10 = df[df['item_price'] > 10]
print(top_10)

#to print the graph the top 5 revenue generating items using a bar chart with item label on X-axis and total revenue on Y-axis.

top_5 = df.groupby('item_name')['item_price'].sum().nlargest(5)
plt.bar(top_5.index, top_5.values)
plt.xticks(rotation=45)
plt.show()

