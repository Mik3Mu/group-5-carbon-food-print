
# import the data
import pandas as pd
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

root_dir = os.path.abspath(os.curdir)
df = pd.read_csv(os.path.join(root_dir, "..", "food_production.csv"))

df.info()
print(df.head())

#Distribution Analysis using df.hist()
num_cols_df = df.select_dtypes("float64")
num_cols_df.hist(figsize=(10, 10), bins=100)
plt.show()

#Data processing (X - features, y- target variable)
X = df.drop(["total_emissions", "food_product"], axis = 1)

y = df["total_emissions"]

#Data splitting
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

#Model building
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

y_lr_train_pred = lin_reg.predict(X_train)
y_lr_test_pred = lin_reg.predict(X_test)

lr_train_mse = mean_squared_error(y_train, y_lr_train_pred)
lr_train_r2 = r2_score(y_train, y_lr_train_pred)

lr_test_mse = mean_squared_error(y_test, y_lr_test_pred)
lr_test_r2 = r2_score(y_test, y_lr_test_pred)

print(lr_train_mse)
print(lr_train_r2)
print(lr_test_mse)
print(lr_test_r2)

lr_results = pd.DataFrame(['Linear regression',lr_train_mse, lr_train_r2, lr_test_mse, lr_test_r2]).transpose()
lr_results.columns = ["Method", "Training MSE", "Training R2", "Test MSE", "Test R2"]

