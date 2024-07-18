import pandas as pd
import numpy as np

# Question 1

data1 = {
    'customer_id': [1, 2, 3, 4, 5],
    'age': [25, np.nan, 35, np.nan, 45],
    'gender': ['Male', 'Female', np.nan, 'Female', np.nan],
    'Income': [50000, 60000, 70000, np.nan, np.nan],
    'purchase_amount': [200, 200, np.nan, 400, 500]
}
df1 = pd.DataFrame(data1)

def function1(dataframe):
    # Part 1
    # This is to find Sum of NA in each row, Take out Axis = 1 to get by column
    nan_count = dataframe.isna().sum(axis=1)
    print(nan_count)
    print(len(dataframe.index))
    dataframe.rm(nan_count >= 2)

    # Part 2
    dataframe.fillna().mean().isnull().sum()

    # Part 3


    return

function1(df1)

# Question 2

data2 = {
    'customer_id': [1, 1, 2, 2, 3],
    'purchase_amount': [100, 200, 150, 300, 400],
    'purchase_date': ['2024-07-14', '2024-07-15', '2024-07-16', '2024-07-17', '2024-07-18']
}

df2 = pd.DataFrame(data2)

# Day of the Week
df2['day_of_week'] = df2['purchase_date'].apply() # Some Calendar Function

# We need to change this
# Is Weekend
if df2['day_of_week'] == 'Saturday' or 'Sunday' or 'Friday':
    df2['Is_Weekend'] = True
else:
    df2['Is_Weekend'] = False

# Question 3

data3 = {
    'product_id': [1, 1, 1, 1, 2, 2, 2, 2],
    'store_id': [101, 101, 101, 101, 202, 202, 202, 202],
    'sales': [10, 20, 30, 40, 5, 15, 25, 35],
    'date': ['2024-07-01', '2024-07-02', '2024-07-03', '2024-07-04', '2024-07-01', '2024-07-02', '2024-07-03', '2024-07-04']
}

df3 = pd.DataFrame(data3)
