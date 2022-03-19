
# import the data
import pandas as pd
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import missingno as msno
import os

root_dir = os.path.abspath(os.curdir)
df = pd.read_csv(root_dir + "\Data\complete_dataset.csv")

df.info()
df.describe()

print(df.head())

#missing values
df.isna()
df.isna().sum()

#visualize missingness
msno.matrix(df)
plt.show()

dropped_df = df.dropna(axis="columns")
msno.matrix(dropped_df)
plt.show()

#Distribution Analysis using df.hist()
num_cols_df = df.select_dtypes("float64")
num_cols_df.hist(figsize=(10, 10), bins=100)
plt.show()

fig, ax = plt.subplots(figsize=(15, 10))
df.drop(["Unnamed: 0.1", "Unnamed: 0"], axis = 1).plot(x="Product", kind="bar", stacked=True, ax=ax)
plt.xlabel("Product")
plt.show()


sns.countplot(x="Product", data=df.drop(["Unnamed: 0.1", "Unnamed: 0"], axis = 1))
plt.xticks(rotation=90, fontsize=5)
plt.grid(True)
plt.show()

#Data processing (X - features, y- target variable)
X = df.drop(["CO2_Equivalent_per_Kilo",
             "Product",
             "Type",
             "Country of Origin",
             "Method of Transportation",
             "Organic",
             "Seasonal",
             "Type of Packaging",
             "Processed",
             "Source"], axis = 1)

y = df["CO2_Equivalent_per_Kilo"]

#Data splitting
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#normalization is a scaling technique in which values are shifted and rescaled so that they end up ranging between 0 and 1
#fit scaler on training data
norm = MinMaxScaler().fit(X_train)

#transform training data
X_train_norm = norm.transform(X_train)
print("Scaled Train Data: \n\n")
print(X_train_norm)

#transform testing data
X_test_norm = norm.transform(X_test)
print("Scaled Test Data with Normalization: \n\n")
print(X_test_norm)

#standardization is a scaling technique where the values are centered around the mean with a unit standard deviation
#copy datasets
X_train_stand = X_train.copy()
X_test_stand = X_test.copy()

#apply standardization on numerical features
for i in X.select_dtypes("float64").columns:

    #fit on training data column
    scale = StandardScaler().fit(X_train_stand[[i]])
    #transform the training data column
    X_train_stand[i] = scale.transform(X_train_stand[[i]])
    #transform the testing data column
    X_test_stand[i] = scale.transform(X_test_stand[[i]])
print("Scaled Train Data")

#Model building
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

y_lr_train_pred = lin_reg.predict(X_train)
y_lr_test_pred = lin_reg.predict(X_test)

lr_train_mse = mean_squared_error(y_train, y_lr_train_pred)
lr_train_r2 = r2_score(y_train, y_lr_train_pred)

lr_test_mse = mean_squared_error(y_test, y_lr_test_pred)
lr_test_r2 = r2_score(y_test, y_lr_test_pred)


lr_results = pd.DataFrame(['Linear regression',lr_train_mse, lr_train_r2, lr_test_mse, lr_test_r2]).transpose()
lr_results.columns = ["Method", "Training MSE", "Training R2", "Test MSE", "Test R2"]
print(lr_results)

