# Steps:
# 1.Import Moduls
# 2.Settings
# 3.Import CSV File
# 4.Checking Missing datapoints
# 5.Split Data in Training and Test Sets
# 6.Using RandomForestClassifier as algorithm
# 7.Testing the Model with kFold
# 8.Getting Basic Statistics data as count, mean, std, min, max and the inter-quartile range
# 9.Examine correlation coefficient (Independent Values)
# 10.Linear Regression + Root Mean Squared Error


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
url = "https://drive.google.com/file/d/1gq-pD4aSLdp48GGM6fTHzCeJGkz_qFiN/view?usp=sharing"
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

# 5.Split Data in Training and Test Sets
# X_all=all emission columns minus CO2_Equivalent_per_Kilo
# y_all=Predict Columns, which is CO2_Equivalent_per_Kilo

X_all = food_data[["food_emissions_land_use", "food_emissions_farm", "food_emissions_animal_feed", "food_emissions_processing",
     "food_emissions_transport", "food_emissions_retail", "food_emissions_packaging"]]

#Changing Predict Column to 0 and 1
y_all = np.where(food_data["CO2_Equivalent_per_Kilo"]> 5, 1,0).astype(int)
print("CO2_Equivalent_per_Kilo over 5:")
print(y_all)

num_test = 0.20
X_train, X_test, y_train, y_test = train_test_split(X_all, y_all, test_size=num_test, random_state=23)


#6. Using RandomForestClassifier as algorithm
clf = RandomForestClassifier()
#Combination Parameter
parameters = {'n_estimators': [4, 6, 9],
              'max_features': ['log2', 'sqrt', 'auto'],
              'criterion': ['entropy', 'gini'],
              'max_depth': [2, 3, 5, 10],
              'min_samples_split': [2, 3, 5],
              'min_samples_leaf': [1, 5, 8]
              }

#Type of scoring
acc_scorer = make_scorer(accuracy_score)

#GridsearchCV
grid_obj = GridSearchCV(clf, parameters, scoring=acc_scorer)
grid_obj = grid_obj.fit(X_train, y_train)

#Finding the best combination of parameters
clf = grid_obj.best_estimator_

#Fit best algoritm
clf.fit(X_train, y_train)

#Printing the accuracy score
predictions = clf.predict(X_test)
print("Accuracy Score for test:")
print(accuracy_score(y_test, predictions))


# 7.Testing the Model with kFold
def run_kfold(X_all, y_all, clf):
    kf = KFold(n_splits=10)
    outcomes = []
    fold = 0
    for train_index, test_index in kf.split(X_all):
        fold += 1
        X_train, X_test = X_all.values[train_index], X_all.values[test_index]
        y_train, y_test = y_all[train_index], y_all[test_index]
        clf.fit(X_train, y_train)
        predictions = clf.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        outcomes.append(accuracy)
        print("Fold {0} accuracy: {1}".format(fold, accuracy))
    mean_outcome = np.mean(outcomes)
    print("Mean Accuracy: {0}".format(mean_outcome))

run_kfold(X_all, y_all, clf)


# 8.Getting Basic Statistics data as count, mean, std, min, max and the inter-quartile range

#Define independent and dependent values
independent = food_data[["food_emissions_land_use", "food_emissions_farm", "food_emissions_animal_feed", "food_emissions_processing",
     "food_emissions_transport", "food_emissions_retail", "food_emissions_packaging"]]

dependent = food_data["CO2_Equivalent_per_Kilo"]

print(independent.describe().T)
print("Statistics for the column CO2_Equivalent_per_Kilo:")
print(dependent.describe().T)


# 9.Examine correlation coefficient (Independent Values)
plt.figure(figsize=(10,6))
corr = independent.corr()
heatmap = sns.heatmap(corr, annot=True, cmap="Blues")
plt.show(block=False)


# 10.Linear Regression + Root Mean Squared Error

#Fitting the regression model
regr = linear_model.LinearRegression()
regr.fit(independent,dependent)

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
