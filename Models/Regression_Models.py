#------------------------Regression Models TechLabs Group 5---------------------

# Steps:
# 1.Import Moduls
# 2.Settings
# 3.Import CSV File
# 4.Checking Missing datapoints

#BASIC STATISTICS
# 5.Getting Basic Statistics data as count, mean, std, min, max and the inter-quartile range
# 6.Examine correlation coefficient (Independent Values)

#REGRESSION
# 7.Linear Regression + Root Mean Squared Error
#

# 1.Import Moduls
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

# 2.Settings
#Start Time for Script Running time
start = time.time()

#Settings for displaying tables
desired_width = 320
pd.set_option("display.width", desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

# 3.Import CSV File"
url = "https://drive.google.com/file/d/1RgVDovPm_AuNKmGIikFyHeS0vZDBMlww/view?usp=sharing"
url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]
food_data = pd.read_csv(url)

#print(food_data)

# 4.Checking missing datapoints
print("Missing Values for each column:")
print(food_data.isnull().sum())
#Fillna in case there is missing data
food_data = food_data.fillna(0)
#Data can be limited here, if needed for testing purposes, just delete hashtag:
#food_data = food_data[:30]
print(food_data)


#BASIC STATISTICS:

# 5.Getting Basic Statistics data as count, mean, std, min, max and the inter-quartile range

#Define independent and dependent values
# X_all=all emission columns minus CO2_Equivalent_per_Kilo
# y_all=Predict Columns, which is CO2_Equivalent_per_Kilo

X_all = food_data[["food_emissions_land_use", "food_emissions_farm", "food_emissions_animal_feed", "food_emissions_processing",
     "food_emissions_transport", "food_emissions_retail", "food_emissions_packaging"]]

y_all = food_data["CO2_Equivalent_per_Kilo"]


num_test = 0.20
X_train, X_test, y_train, y_test = train_test_split(X_all, y_all, test_size=num_test, random_state=23)

print(X_all.describe().T)
print("Statistics for the column CO2_Equivalent_per_Kilo:")
print(y_all.describe().T)


# 6.Examine correlation coefficient (Independent Values)
plt.figure(figsize=(10,6))
corr = X_all.corr()
heatmap = sns.heatmap(corr, annot=True, cmap="Blues")
plt.show(block=False)


#REGRESSION:

# 7.Linear Regression + Root Mean Squared Error

#Fitting the regression model
regr = linear_model.LinearRegression()
regr.fit(X_all, y_all)

#Predicting the Total CO2 Emission

#For just random numbers for the independent values
predictedCO2 = regr.predict([[3,7,4,3,9,2,1]])
print("Predicted Total CO2 Equivalent for given numbers:")
print(predictedCO2)

#Regression with the X_test data
predictedCO2_2 = regr.predict(X_test)
print("List of outcomes for Total CO2 Equivalent for X_test:")
print(predictedCO2_2)

#Calculating the Root Mean Squared Error (RMSE)
print("RMSE: ", np.sqrt(mean_squared_error(y_test, predictedCO2_2)))



print(20*"-", "END", 20*"-")
#plt.show() at the end to get the graphs last
plt.show()
#Timer Script
print("Running Script took", time.time()-start, "seconds.")
