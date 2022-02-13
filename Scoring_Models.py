# Steps:
# 1.Import Moduls
# 2.Display Settings
# 3.Import CSV File
# 4.Checking Missing datapoints
# 5.Split Data in Training and Test Sets
# 6.Using RandomForestClassifier as algorithm
# 7.Testing the Model with kFold


# 1.Import Moduls
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

# 2.Display Settings
desired_width = 320
pd.set_option("display.width", desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

# 3.Import CSV File
url = "https://drive.google.com/file/d/1gjFX5lsuap1rlJkNcKBRmGi6tPA-57t1/view?usp=sharing"
url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]
food_data = pd.read_csv(url)

#print(food_data)

# 4.Checking missing datapoints
print(food_data.isnull().sum())
#CAUTION! Fillna just because otherwise the model doesn't work! Should be changed later!
food_data = food_data.fillna(0)
#CAUTION! Limiting data for testing/performance, will be changed later!
food_data = food_data[:30]
print(food_data)

# 5.Split Data in Training and Test Sets
# X_all=all emission columns minus CO2_Equivalent_per_Kilo
# y_all=Predict Columns, which is CO2_Equivalent_per_Kilo

X_all = food_data[["food_emissions_land_use", "food_emissions_farm", "food_emissions_animal_feed", "food_emissions_processing",
     "food_emissions_transport", "food_emissions_retail", "food_emissions_packaging"]]

#Changing Predict Column to 0 and 1
y_all = np.where(food_data["CO2_Equivalent_per_Kilo"]=='M', 1,0).astype(int)

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
print(accuracy_score(y_test, predictions))


# 7.Testing the Model with kFold
def run_kfold(clf):
    kf = KFold(n_splits=10)
    outcomes = []
    fold = 0
    for train_index, test_index in kf:
        fold += 1
        X_train, X_test = X_all.values[train_index], X_all.values[test_index]
        y_train, y_test = y_all.values[train_index], y_all.values[test_index]
        clf.fit(X_train, y_train)
        predictions = clf.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        outcomes.append(accuracy)
        print("Fold {0} accuracy: {1}".format(fold, accuracy))
    mean_outcome = np.mean(outcomes)
    print("Mean Accuracy: {0}".format(mean_outcome))

run_kfold(clf)