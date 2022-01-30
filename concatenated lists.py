#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Import Pandas
import pandas as pd

# Load Data 

# Creating Column Names for the Table (("Energy Used #Out for Now ; Aswell as Energy Usage; Water Usage;"))
df = pd.DataFrame(columns=["Product", "Type", "Unique_Aspect", "CO2_Equivalent_per_Kilo","Score"])

# The CO2 Equivalent that is being used was measured according to the "Carbon Foot Print - Value" at a generic German supermarket checkout in 2019 by the Institute of Energy and Environmental Research in Heidelberg "ifeu"

# Adding the Data: 5 of selected types each, often with their comparable product
IFEU_study_CFP_Germany2020 = [
    ["Avocado", "Fruit", "from Peru", 0.8,"A"],
    ["Avocado", "Fruit", "from Peru Biological", 0.8,"A"],
    ["Strawberries", "Fruit", "Winter Season", 3.4, "C"],
    ["Strawberries", "Fruit", "Normal season regional", 0.3,"A"],
    ["Pineapple", "Fruit", "by Ship", 0.6, "A"],
    ["Pineapple", "Fruit", "by Plane", 15.1, "E"],
    ["Apples", "Fruit", "from New Zealand", 0.8, "A"],
    ["Apples", "Fruit", "mean Regional and Seasonal", 0.3, "A"],
    ["Peach", "Fruit", "Fresh",0.2, "A"],
    ["Peach", "Fruit", "Can", 1.6, "B"],
    ["Broccoli", "Vegetable", "Fresh", 0.3, "A"],
    ["Broccoli", "Vegetable", "Frozen",0.3, "A"],
    ["Beans", "Vegetable", "Fresh", 0.8, "A"],
    ["Beans", "Vegetable", "Can", 1.3, "B"],
    ["Champignon", "Vegetable", "Fresh", 1.3, "B"],
    ["Champignon", "Vegetable", "Can", 2.4, "B"],
    ["Tomatoes", "Vegetable", "Paste", 4.3, "C"],
    ["Tomatoes", "Vegetable", "Can", 1.8, "B"],
    ["Carrots", "Vegetable", "Fresh", 0.2, "A"],
    ["Carrots", "Vegetable", "Biological", 0.2, "A"],
    ["Butter", "Dairy", "Conventional", 9.0, "D"],
    ["Butter", "Dairy", "Biological", 11.5, "E"],
    ["Cheese", "Dairy", "mean Conventional", 5.7, "D"],
    ["Cheese", "Dairy", "mean Biological", 7.2, "D"],
    ["Milk", "Dairy", "Biological", 1.7, "B"],
    ["Oat Milk", "Dairy ", "Substitute", 0.3, "A"],
    ["Cream", "Dairy", "Biological", 5.3, "D"],
    ["Oat Cream", "Dairy", "Substitute", 0.6, "A"],
    ["Curd", "Dairy", "Biological", 4.1, "C"],
    ["Soja Curd", "Dairy", "Substitute", 0.7, "A"],
    ["Shrimp", "Fish", "Frozen", 12.5, "E"],
    ["Salmon", "Fish", "Aquaculture", 5.1, "D"],
    ["Beef", "Meat", "mean Conventional", 13.6, "E"],
    ["Beef", "Meat", "Biological", 15.1, "E"],
    ["Pork", "Meat", "mean Conventional", 4.6, "C"],
    ["Pork", "Meat", "Biological", 5.2, "D"],
    ["Tofu", "Meat", "Substitute", 1.0, "A"],
    ["Tempeh", "Meat", "Substitue", 0.7, "A"],
    ["Venison", "Meat", "From Deer", 11.5, "E"],
    ["Veggie Patties", "Meat", "mean Substitutes", 1.45, "B"],
    ["Brown Bread", "Pastries", "Conventional", 0.6, "A"],
    ["Brown Bread", "Pastries", "Biological", 0.6, "A"],
    ["Honey", "Sweets", "Glas", 2.0, "B"],
    ["Olive Oil", "Ingredient", "Glas", 3.2, "C"],
    ["Coconut Oil", "Ingredient", "Glas", 2.3, "B"],
    ["Beet Sugar", "Ingredient", "Conventional", 0.7, "A"],
    ["Beet Sugar", "Ingredient", "Biological", 0.5, "A"],
    ["Peanuts with Shell", "Ingredient", "Conventional", 0.8, "A"],
    ["Peanutbutter", "Sweets", "Glas", 2.0, "B"],
    ["Beer 0.5L", "Drinks", "Glas", 0.9, "A"],
    ["Beer 0.5L", "Drinks", "Can", 1.0, "A"],
    ["Lemonade 0.75L", "Drinks", "Plastic", 0.4, "A"],
    ["Sparkling Water 0.7L", "Drinks", "Glas", 0.2, "A"],
    ["Tap Water", "Drinks", "Sink", 0.0, "A"],
    ["Wine 0.75L", "Drinks", "Glas", 1.0, "A"],
    ["Coffee Powder", "Drinks", "Conventional", 5.6, "D"],
    ["Apple Juice 1L", "Drinks", "Glas", 0.4, "A"],
    ["Orange Juice 1L", "Drinks", "Carton", 0.7, "A"],

]

df = pd.DataFrame(columns=["Product", "Type", "Unique_Aspect", "CO2_Equivalent_per_Kilo","Score"],data=IFEU_study_CFP_Germany2020)
df
df = df.drop(["Score"],axis=1)
df

#Information on Tomatoes (source: https://www.umweltdialog.de/de/verbraucher/lebensmittel/2015/Klimakiller-Tomaten-.php)
tomatoe_values = [
    ["Tomatoes", "Vegetable", "Conventional production in heated greenhouse, local, out of season", 9.3, "nan"],
    ["Tomatoes", "Vegetable", "Organic production in heated greenhouse, local, out of season", 9.2, "nan"],
    ["Tomatoes", "Vegetable", "From Canaries, transport by flight", 7.2, "nan"],
    ["Tomatoes", "Vegetable", "Conventional production in non-heated greenhouse, local, out of season", 2.3, "nan"],
    ["Tomatoes", "Vegetable", "From Spain, open air production", 0.6, "nan"],
    ["Tomatoes", "Vegetable", "Conventional regional production during season", 0.085, "nan"],
    ["Tomatoes", "Vegetable", "Organic regional production during season", 0.035, "nan"]
    ]

tomatoes = pd.DataFrame(columns=["Product", "Type", "Unique_Aspect", "CO2_Equivalent_per_Kilo","Score"],data=tomatoe_values)

#Adding the information from Our World in Data
#open the data:
data2 = "C:/Users/carol/Documents/TechLabs/Sources on CO2 footprint/Our World in Data/OurWorldInData_food-footprints.csv"
df2 = pd.read_csv(data2)

#delete unneccessary columns and rename "Entity" to "Product"
df_no_year = df2.drop("Year", axis = 1)
df_OWID = df_no_year.drop("Code", axis = 1)
df_OWID["Product"] = df_OWID["Entity"]

#adding total CO2-eq
df_OWID["CO2_Equivalent_per_Kilo"] = df_OWID.sum(axis=1)

#Adding data from supporting information of Drewnoski et al., Am. J. of Clinical Nutrition, 2015
#open data
data3 = "C:/Users/carol/Documents/TechLabs/Sources on CO2 footprint/Drewnowski_AmJClinicalNutrition_2015/Extracted Table.xlsx"
df3 = pd.read_excel(data3)

#adjusting the DataFrame
df3["CO2_Equivalent_per_Kilo"] = df3["GHGEs per 100g (Median)"] / 100
df3["Product"] = df3["Food group"]
df_Drewnowski = df3.drop(["GHGEs per 100g (Median)"], axis=1)




#concatenating the datasets
concatenated = pd.concat([df, tomatoes, df_OWID, df3])

# In[19]:


# The Score is devided in 5 categories : A , B , C , D , E
# A is True if "CO2/kg" <= 1
# B is True if "CO2/kg" >= {3,1}
# C is True if "CO2/kg" >= {5,3}
# D is True if "CO2/kg" >= {10,5}
# E is True if "CO2/kg" >  10

def scoring(CO2):
    if CO2 <= 1:
        score = "A"
    elif CO2 <= 3:
        score = "B"   
    elif CO2 <= 5:
        score = "C"
    elif CO2 <= 10:
        score = "D"
    else: 
        score = "E"
    return score


# In[20]:


concatenated["Score"] = [
    scoring(CO2)
    for CO2 in concatenated.CO2_Equivalent_per_Kilo
    ]
df


#saving the concatenated data for further use
filename = "C:/Users/carol/Documents/TechLabs/group/group-5-carbon-food-print/concatenated lists.csv"
concatenated.to_csv(filename)