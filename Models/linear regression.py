# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 17:15:24 2022

@author: carol

Linear regression models for descriptors
"""
#import modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

#import file

url = "https://drive.google.com/file/d/1RgVDovPm_AuNKmGIikFyHeS0vZDBMlww/view?usp=sharing"
url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]
df = pd.read_csv(url)
array = df.to_numpy()

#define variables as numpy arrays
total_emissions = array[:, 9]
y = array[:,11:]
processing = array[:,11]
animal_feed = array[:,12]
land_use = array[:,13]
farm = array[:,14]
transport = array[:,15]
retail = array[:,16]
packaging = array[:,17]
X = total_emissions.reshape(-1,1)

#creating the pipeline
lr = LinearRegression()
scaler = StandardScaler()
pipe = make_pipeline(scaler, lr)

##########################################################
#processing
#seperate training and testing data
y1 = processing
X_train, X_test, y1_train, y1_test = train_test_split(
     X, y1, test_size=0.33, random_state=42)
# apply scaling and regression on training data
pipe.fit(X_train, y1_train)  
# apply scaling on testing data, without leaking training data
pipe.score(X_test, y1_test)
y1_pred = pipe.predict(X_test)

#plot the fits
plt.figure()
plt.scatter(X_test, y1_test)
plt.plot(X, pipe.predict(X))
plt.title("Linear regression processing emissions")
plt.xlabel("Total emissions [kg CO_2/kg]")
plt.ylabel("Emissions processing")

#Regression  metrics
print("Regression metrics for linear regression model processing:")
#Mean Absolute Error
print("Mean absolute error: ", mean_absolute_error(y1_test, y1_pred))
#Mean Squared Error
print("Mean squared error: ", mean_squared_error(y1_test, y1_pred))
#R^2 Score
print("R^2 score: ", r2_score(y1_test, y1_pred))

##########################################################
#animal_feed
#seperate training and testing data
y2 = animal_feed
X_train, X_test, y2_train, y2_test = train_test_split(
     X, y2, test_size=0.33, random_state=42)
# apply scaling and regression on training data
pipe.fit(X_train, y2_train)  
# apply scaling on testing data, without leaking training data
pipe.score(X_test, y2_test)
y2_pred = pipe.predict(X_test)

#plot the fits
plt.figure()
plt.scatter(X_test, y2_test)
plt.plot(X, pipe.predict(X))
plt.title("Linear regression animal feed emissions")
plt.xlabel("Total emissions [kg CO_2/kg]")
plt.ylabel("Emissions animal feed")

#Regression  metrics
print("Regression metrics for linear regression model animal feed:")
#Mean Absolute Error
print("Mean absolute error: ", mean_absolute_error(y2_test, y2_pred))
#Mean Squared Error
print("Mean squared error: ", mean_squared_error(y2_test, y2_pred))
#R^2 Score
print("R^2 score: ", r2_score(y2_test, y2_pred))

##########################################################
#land_use
#seperate training and testing data
y3 = land_use
X_train, X_test, y3_train, y3_test = train_test_split(
     X, y3, test_size=0.33, random_state=42)
# apply scaling and regression on training data
pipe.fit(X_train, y3_train)  
# apply scaling on testing data, without leaking training data
pipe.score(X_test, y3_test)
y3_pred = pipe.predict(X_test)

#plot the fits
plt.figure()
plt.scatter(X_test, y3_test)
plt.plot(X, pipe.predict(X))
plt.title("Linear regression land use emissions")
plt.xlabel("Total emissions [kg CO_2/kg]")
plt.ylabel("Emissions land use")

#Regression  metrics
print("Regression metrics for linear regression model land use:")
#Mean Absolute Error
print("Mean absolute error: ", mean_absolute_error(y3_test, y3_pred))
#Mean Squared Error
print("Mean squared error: ", mean_squared_error(y3_test, y3_pred))
#R^2 Score
print("R^2 score: ", r2_score(y3_test, y3_pred))

##########################################################
#farm
#seperate training and testing data
y4 = farm
X_train, X_test, y4_train, y4_test = train_test_split(
     X, y4, test_size=0.33, random_state=42)
# apply scaling and regression on training data
pipe.fit(X_train, y4_train)  
# apply scaling on testing data, without leaking training data
pipe.score(X_test, y4_test)
y4_pred = pipe.predict(X_test)

#plot the fits
plt.figure()
plt.scatter(X_test, y4_test)
plt.plot(X, pipe.predict(X))
plt.title("Linear regression farm emissions")
plt.xlabel("Total emissions [kg CO_2/kg]")
plt.ylabel("Emissions farm")

#Regression  metrics
print("Regression metrics for linear regression model farm:")
#Mean Absolute Error
print("Mean absolute error: ", mean_absolute_error(y4_test, y4_pred))
#Mean Squared Error
print("Mean squared error: ", mean_squared_error(y4_test, y4_pred))
#R^2 Score
print("R^2 score: ", r2_score(y4_test, y4_pred))

##########################################################
#transport
#seperate training and testing data
y5 = transport
X_train, X_test, y5_train, y5_test = train_test_split(
     X, y5, test_size=0.33, random_state=42)
# apply scaling and regression on training data
pipe.fit(X_train, y5_train)  
# apply scaling on testing data, without leaking training data
pipe.score(X_test, y5_test)
y5_pred = pipe.predict(X_test)

#plot the fits
plt.figure()
plt.scatter(X_test, y5_test)
plt.plot(X, pipe.predict(X))
plt.title("Linear regression transport emissions")
plt.xlabel("Total emissions [kg CO_2/kg]")
plt.ylabel("Emissions transport")

#Regression  metrics
print("Regression metrics for linear regression model farm:")
#Mean Absolute Error
print("Mean absolute error: ", mean_absolute_error(y5_test, y5_pred))
#Mean Squared Error
print("Mean squared error: ", mean_squared_error(y5_test, y5_pred))
#R^2 Score
print("R^2 score: ", r2_score(y5_test, y5_pred))


##########################################################
#retail
#seperate training and testing data
y6 = retail
X_train, X_test, y6_train, y6_test = train_test_split(
     X, y6, test_size=0.33, random_state=42)
# apply scaling and regression on training data
pipe.fit(X_train, y6_train)  
# apply scaling on testing data, without leaking training data
pipe.score(X_test, y6_test)
y6_pred = pipe.predict(X_test)

#plot the fits
plt.figure()
plt.scatter(X_test, y6_test)
plt.plot(X, pipe.predict(X))
plt.title("Linear regression retail emissions")
plt.xlabel("Total emissions [kg CO_2/kg]")
plt.ylabel("Emissions retail")

#Regression  metrics
print("Regression metrics for linear regression model farm:")
#Mean Absolute Error
print("Mean absolute error: ", mean_absolute_error(y6_test, y6_pred))
#Mean Squared Error
print("Mean squared error: ", mean_squared_error(y6_test, y6_pred))
#R^2 Score
print("R^2 score: ", r2_score(y6_test, y6_pred))

##########################################################
#packaging
#seperate training and testing data
y7 = packaging
X_train, X_test, y7_train, y7_test = train_test_split(
     X, y7, test_size=0.33, random_state=42)
# apply scaling and regression on training data
pipe.fit(X_train, y7_train)  
# apply scaling on testing data, without leaking training data
pipe.score(X_test, y7_test)
y7_pred = pipe.predict(X_test)

#plot the fits
plt.figure()
plt.scatter(X_test, y7_test)
plt.plot(X, pipe.predict(X))
plt.title("Linear regression packaging emissions")
plt.xlabel("Total emissions [kg CO_2/kg]")
plt.ylabel("Emissions packaging")

#Regression  metrics
print("Regression metrics for linear regression model farm:")
#Mean Absolute Error
print("Mean absolute error: ", mean_absolute_error(y7_test, y7_pred))
#Mean Squared Error
print("Mean squared error: ", mean_squared_error(y7_test, y7_pred))
#R^2 Score
print("R^2 score: ", r2_score(y7_test, y7_pred))

######################################################
#comparison of regression metrics
Metrics = [
    ["Processing", mean_absolute_error(y1_test, y1_pred), mean_squared_error(y1_test, y1_pred), r2_score(y1_test, y1_pred)],
    ["Animal feed", mean_absolute_error(y2_test, y2_pred), mean_squared_error(y2_test, y2_pred), r2_score(y2_test, y2_pred)],
    ["Land use", mean_absolute_error(y3_test, y3_pred), mean_squared_error(y3_test, y3_pred), r2_score(y3_test, y3_pred)],
    ["Farm", mean_absolute_error(y4_test, y4_pred), mean_squared_error(y4_test, y4_pred), r2_score(y4_test, y4_pred)],
    ["Transport", mean_absolute_error(y5_test, y5_pred), mean_squared_error(y5_test, y5_pred), r2_score(y5_test, y5_pred)],
    ["Retail", mean_absolute_error(y6_test, y6_pred), mean_squared_error(y6_test, y6_pred), r2_score(y6_test, y6_pred)],
    ["Packaging", mean_absolute_error(y7_test, y7_pred), mean_squared_error(y7_test, y7_pred), r2_score(y7_test, y7_pred)],
    ]
df_metrics = pd.DataFrame(columns=["Independent variable", "Mean absolute error", "Mean squared error", "R^2 score"], data=Metrics)
print(df_metrics)
