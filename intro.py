# with open('sales_data.csv', 'r', encoding='utf-8') as file:
# 	data = file.read()
# 	print(data)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load dataset
sales = pd.read_csv('sales_data.csv',
	parse_dates=['Date'])

# print(sales)

# print(sales.head())

# print(sales.info())

# print(sales.describe())

# print(sales['Unit_Cost'].describe())

# print(sales['Unit_Cost'].mean())

# print(sales['Unit_Cost'].median())

# sales['Unit_Cost'].plot(kind='box', vert=False, figsize=(14,6))

# sales['Unit_Cost'].plot(kind='density', figsize=(14,6))

# ax = sales['Unit_Cost'].plot(kind='density', figsize=(14,6))
# ax.axvline(sales['Unit_Cost'].mean(), color='red')
# ax.axvline(sales['Unit_Cost'].median(), color='green')

# ax = sales['Unit_Cost'].plot(kind='hist', figsize=(14,6))
# ax.set_ylabel('Number of Sales')
# ax.set_xlabel('dollars')

# print(sales['Age_Group'].value_counts())

# sales['Age_Group'].value_counts().plot(kind='pie', figsize=(6,6))

# ax = sales['Age_Group'].value_counts().plot(kind='bar', figsize=(14,6))
# ax.set_ylabel('Number of Sales')

plt.figure(figsize=(14,6))
sns.barplot(x='Product', y='Revenue', data=sales, estimator=sum, errorbar=None)
plt.title('Total Revenue by Products')
plt.xlabel('Product Names')
plt.ylabel('Total Revenue')
plt.tight_layout()
# plt.show()

# Step 1: Data Cleaning
# Check for missing values
# print(sales.isnull().sum())
# print(sales.dtypes)


# Fill missing values
numeric_columns = sales.select_dtypes(include=[float, int])
numeric_columns.fillna(numeric_columns.mean(), inplace=True)
sales[numeric_columns.columns] = numeric_columns
# print(sales.head())

# Removing Duplicates
sales['Month'] = sales['Month'].str.title()
sales['Age_Group'] = sales['Age_Group'].str.title()
sales['Customer_Gender'] = sales['Customer_Gender'].str.title()
sales['Country'] = sales['Country'].str.title()
sales['State'] = sales['State'].str.title()
sales['Sub_Category'] = sales['Sub_Category'].str.title()
sales['Product_Category'] = sales['Product_Category'].str.title()
sales['Product'] = sales['Product'].str.title()

# Standardize capitalization
sales.drop_duplicates(inplace=True)

# Removing Outliers
sales = sales[sales['Customer_Age'] <= 100]

# Data Categorization: Create a new column
def categorize_sales(revenue):
	if revenue < 1000:
		return 'Low'
	elif 1000 <= revenue < 5000:
		return 'Medium'
	else:
		return 'High'

sales['Sales_Category'] = sales['Revenue'].apply(categorize_sales)

def categorize_order(order_quantity):
	if order_quantity < 10:
		return 'Small'
	elif 10 <= order_quantity < 20:
		return 'Medium'
	else:
		return 'Large'
sales['Order_Category'] = sales['Order_Quantity'].apply(categorize_order)




# Standardizing Data
# Strip leading/trailing spaces from strings
sales['Month'] = sales['Month'].str.strip()
sales['Age_Group'] = sales['Age_Group'].str.strip()
sales['Customer_Gender'] = sales['Customer_Gender'].str.strip()
sales['Country'] = sales['Country'].str.strip()
sales['State'] = sales['State'].str.strip()
sales['Sub_Category'] = sales['Sub_Category'].str.strip()
sales['Product_Category'] = sales['Product_Category'].str.strip()
sales['Product'] = sales['Product'].str.strip()

# Final CLeaned Data
column_names_list = list(sales.columns)
print('Column Names as List:', column_names_list)

# Save cleaned and categorized data to a new file
# sales.to_csv('cleaned_data.csv', index=False)



