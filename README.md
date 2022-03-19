# group-5-carbon-food-print
Repository of the TechLabs Group 5: Carbon FoodPrint

Contributors: Johanna van Betteray, Luca Bochnia, Carolin Borbeck, Mike Müller, Anastasia Yablokova

Mentor: Amine Jebari

The objective of the project was to predict the carbon footprint of several food items based on different input factors. The data used consists of the dependent variable "CO2 equivalent per Kilo" and seven independent variables: food emissions for processing, animal feed, land use, farm, transport, retail, and packaging.

The repository contains the following folders:

1. Archive:
    Files not used for the final data and models. The folder contains first programs to generate datafiles and also discarded modeling approaches. 
    The files in the folder have been kept to keep an overview of how the project progressed, especially at the beginning of the project phase.
2. Data:
    The folder contains the program to compile the data which could be found as well as the final dataset that is used for the modeling. 
    As most datasets available contained very little information, the values for different emission factors were averaged for certain food groups (see file "average emission factors calculations.xlsx). The basis for the calculation is given by the following source: 
    https://ourworldindata.org/food-choice-vs-eating-local
3. Models:
    There are two relevant programs for the models used:
    
    linear regression.py: 
      Linear regressions for the impact of each of the seven identified variables on the total CO2 emission of the food product.
      
    Classification_Models.py: 
      The program uses the following models: k-nearest neighbors, Logistic Regression, C-Support Vector Classification - Linear,
      C-Support Vector Classification, RandomForest, Decision Tree, Gaussian Naive Bayes
      
The programs call on data stored in a google drive ("complete dataset.csv") to make the programs not depend on local paths:
https://drive.google.com/drive/folders/1GIv8S7_wsJHCpfwIDiA96caf2_4DDvM7

Python modules needed to run the programs:

-pandas

-numpy

-matplotlib

-seaborn

-time

-sklearn

