import pandas as pd
from datetime import datetime

# Equivalent to Users table
users_df = pd.DataFrame(columns=['user_id', 'name', 'email', 'password', 'city'])
users_df = users_df.astype({
    'user_id': 'int64',
    'name': 'string',
    'email': 'string',
    'password': 'string',
    'city': 'string'
})

# Equivalent to Products table
products_df = pd.DataFrame(columns=['product_id', 'name', 'category', 'price', 'stock'])
products_df = products_df.astype({
    'product_id': 'int64',
    'name': 'string',
    'category': 'string',
    'price': 'float64',
    'stock': 'int64'
})

# Equivalent to Orders table
orders_df = pd.DataFrame(columns=['order_id', 'user_id', 'product_id', 'quantity', 'order_date'])
orders_df = orders_df.astype({
    'order_id': 'int64',
    'user_id': 'int64',
    'product_id': 'int64',
    'quantity': 'int64',
    'order_date': 'datetime64[ns]'
})

# Example usage: Adding sample data
users_df.loc[0] = [1, 'John Doe', 'john@example.com', 'password123', 'Warangal']
products_df.loc[0] = [1, 'Laptop', 'Electronics', 999.99, 10]
orders_df.loc[0] = [1, 1, 1, 1, datetime(2023, 1, 1)]

print("Users DataFrame:")
print(users_df)
print("\nProducts DataFrame:")
print(products_df)
print("\nOrders DataFrame:")
print(orders_df)