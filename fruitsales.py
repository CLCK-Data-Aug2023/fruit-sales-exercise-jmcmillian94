# add your code here
import pandas as pd
import os

fruit_sales = pd.DataFrame({'Apples': [35,41], 'Bananas': [21,34]}, index=['2017 Sales', '2018 Sales'])

file_path = 'fruit.csv'
fruit_sales.to_csv(file_path)