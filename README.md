Just trying to do some Github Practice.

Question 1.

You have a dataset in the form of a pandas data frame that contains information about customer transaction. Some columns have missing values. Write a function to clean the dataset by:
1. Removing any rows where more than 50% of the columns have missing values
2. Imputing missing values in numerical columns with the median value of the column
3. Imputing missing values in categorical   columns with the most frequent value of the column

Question 2.

Given a dataset of customer purchases with the following columns: `customer_id`, `purchase_amount`, `purchase_date`, write a function that:
1. Creates a new column `day_of_week` that indicates the day of the week that purchase was made.
2. Creates a new column `is_weekend` that is True if the purchase was made on a weekend and False otherwise
3. Aggregates the total `purchase_amount` for each `customer_id` and returns a data frame with `customer_id` and the total `purchase_amount`

Question 3.

You are given a dataset in a pandas data frame containing historical sales data with the following columns: `product_id`, `store_id`, `sales`, `date`. Your task is to: 
1. Create a time series model to predict the sales for each product at each store for the next month.
2. Explain the steps you would take to preprocess the data and build the model
3. Implement the function to generate sales predictions using a simple forecasting method such as a moving average or exponential smoothing

