# Import modules
import pandas as pd
import numpy as np
#----------------------------------------------------------------------------------------------

# Adding the Data: 5 of selected types each, often with their comparable product
IFEU_study_CFP_Germany2020 = [
    ["Avocado", "Fruit", "Peru", "nan", False, "nan", "nan", False, 0.8],
    ["Avocado", "Fruit", "Peru", "nan", True, "nan", "nan", False, 0.8],
    ["Strawberries", "Fruit", "nan", "nan", "nan", False, "nan", "unprocessed", 3.4],
    ["Strawberries", "Fruit", "Germany", "nan", "nan", True, "nan", "unprocessed", 0.3],
    ["Pineapple", "Fruit", "nan", "Ship", "nan", "nan", "nan", "unprocessed", 0.6],
    ["Pineapple", "Fruit","nan", "Plane", "nan", "nan", "nan", "unprocessed", 15.1],
    ["Apples", "Fruit", "New Zealand", "nan", "nan", False, "nan", "unprocessed", 0.8],
    ["Apples", "Fruit", "Germany", "nan", "nan", True, "nan", "unprocessed", 0.3],
    ["Peach", "Fruit", "nan", "nan", "nan", "nan", "unpackaged", "unprocessed", 0.2],
    ["Peach", "Fruit", "nan", "nan", "nan", "nan", "Can", "canned", 1.6],
    ["Broccoli", "Vegetable", "nan", "nan", "nan", "nan", "unpackaged", "unprocessed",0.3],
    ["Broccoli", "Vegetable", "nan", "nan", "nan", "nan", "Plastic", "frozen",0.3],
    ["Beans", "Vegetable", "nan", "nan", "nan", "nan", "nan", "unprocessed",0.8],
    ["Beans", "Vegetable", "nan", "nan", "nan", "nan", "Can", "canned", 1.3],
    ["Champignon", "Vegetable", "nan", "nan", "nan", True, "nan", "unprocessed", 1.3],
    ["Champignon", "Vegetable", "nan", "nan", "nan", True, "Can", "canned", 2.4],
    ["Tomatoes", "Vegetable", "nan", "nan", "nan", "nan", "Metal tube", "Paste", 4.3],
    ["Tomatoes", "Vegetable", "nan", "nan", "nan", "nan",  "Can", "canned", 1.8],
    ["Carrots", "Vegetable", "nan", "nan", False, "nan", "nan", "unprocessed", 0.2],
    ["Carrots", "Vegetable", "nan", "nan", True, "nan", "nan",  "unprocessed", 0.2],
    ["Butter", "Dairy", "nan", "nan", False, "nan", "Plastic", "processed", 9.0],
    ["Butter", "Dairy", "nan", "nan", True, "nan", "Plastic", "processed", 11.5],
    ["Cheese", "Dairy", "nan", "nan", False, "nan", "nan", "processed", 5.7],
    ["Cheese", "Dairy",  "nan", "nan", True, "nan", "nan", "processed", 7.2],
    ["Milk", "Dairy", "nan", "nan", True, "nan", "Carton", "unprocessed", 1.7],
    ["Oat Milk", "Substitute", "nan", "nan", "nan", "nan", "nan", "processed", 0.3],
    ["Cream", "Dairy", "nan", "nan", True, "nan", "nan", "processed", 5.3],
    ["Oat Cream", "Substitute", "nan", "nan", "nan", "nan", "nan", "processed", 0.6],
    ["Curd", "Dairy",  "nan", "nan", True, "nan", "nan", "processed", 4.1],
    ["Soja Curd", "Substitute", "nan", "nan", "nan", "nan", "nan", "processed", 0.7],
    ["Shrimp", "Fish", "nan", "nan", "nan", "nan", "nan", "frozen", 12.5],
    ["Salmon from Aquaculture", "Fish", "nan", "nan", "nan", "nan", "nan", "unprocessed", 5.1],
    ["Beef", "Meat", "nan", "nan", False, "nan", "nan", "unprocessed", 13.6],
    ["Beef", "Meat", "nan", "nan", True, "nan", "nan", "unprocessed", 15.1],
    ["Pork", "Meat",  "nan", "nan", False, "nan", "nan", "unprocessed", 4.6],
    ["Pork", "Meat", "nan", "nan", True, "nan", "nan", "unprocessed", 5.2],
    ["Tofu", "Substitute", "nan", "nan", "nan", "nan", "Plastic", "processed", 1.0],
    ["Tempeh", "Substitute", "nan", "nan", "nan", "nan", "Plastic", "processed", 0.7],
    ["Venison from Deer", "Meat", "nan", "nan", "nan", "nan", "nan", "unprocessed", 11.5],
    ["Veggie Patties", "Substitute", "nan", "nan", "nan", "nan", "Plastic", "processed", 1.45],
    ["Brown Bread", "Pastries", "Germany", "nan", False , "nan", "nan", "unprocessed", 0.6],
    ["Brown Bread", "Pastries", "Germany", "nan", False , "nan", "nan", "unprocessed", 0.6],
    ["Honey", "Sweets", "nan", "nan", "nan", "nan", "Glas", "unprocessed", 2.0],
    ["Olive Oil", "Ingredients", "nan", "nan", "nan", "nan", "Glas", "unprocessed", 3.2],
    ["Coconut Oil", "Ingredients",  "nan", "nan", "nan", "nan", "Glas", "unprocessed", 2.3],
    ["Beet Sugar", "Ingredients",  "nan", "nan", False, "nan", "Paper", "unprocessed", 0.7],
    ["Beet Sugar", "Ingredients", "nan", "nan", True, "nan", "Paper", "unprocessed", 0.5],
    ["Peanuts with Shell", "Ingredients", "nan", "nan", False, "nan", "nan", "unprocessed",0.8],
    ["Peanutbutter", "Sweets","nan", "nan", "nan", "nan", "Glas", "processed", 2.0],
    ["Beer 0.5L", "Drinks", "nan", "nan", "nan", "nan", "Glas", "processed", 0.9],
    ["Beer 0.5L", "Drinks", "nan", "nan", "nan", "nan", "Can", "processed", 1.0],
    ["Lemonade 0.75L", "Drinks", "nan", "nan", "nan", "nan", "Plastic", "processed", 0.4],
    ["Sparkling Water 0.7L", "Drinks", "Germany", True, "nan", "nan", "Glas", "processed", 0.2],
    ["Tap Water", "Drinks", "nan", "nan", "Germany", True, "unpackaged", "unprocessed", 0.0],
    ["Wine 0.75L", "Drinks", "nan", "nan", "nan", True, "Glas", "processed", 1.0],
    ["Coffee Powder", "Drinks", "nan", "nan", False, True, "Plastic", "unprocessed", 5.6],
    ["Apple Juice 1L", "Drinks", "nan", "nan", "nan", True, "Glas", "processed", 0.4],
    ["Orange Juice 1L", "Drinks","nan", "nan", "nan", True, "Carton", "processed", 0.7]
]

df_IFEU = pd.DataFrame(columns=["Product", "Type", "Country of Origin", 
                           "Method of Transportation", 
                           "Organic", "Seasonal", 
                           "Type of Packaging", "Processed", 
                           "CO2_Equivalent_per_Kilo"],data=IFEU_study_CFP_Germany2020)
df_IFEU["Source"] ="IFEU study"


#Information on Tomatoes (source: https://www.umweltdialog.de/de/verbraucher/lebensmittel/2015/Klimakiller-Tomaten-.php)
tomatoe_values = [
    ["Tomatoes, heated greenhouse", "Vegetable", "Germany", "nan", False, False, "nan", "unprocessed", 9.3],
    ["Tomatoes, heated greenhouse", "Vegetable", "Germany", "nan", True, False, "nan", "unprocessed", 9.2],
    ["Tomatoes", "Vegetable", "Canaries", "Plane", "nan", "nan", "nan", "unprocessed", 7.2],
    ["Tomatoes, non-heated greenhouse", "Vegetable","Germany", "nan", False, False, "nan", "unprocessed", 2.3],
    ["Tomatoes, open air", "Vegetable", "Spain", "nan", "nan", "nan", "nan", "unprocessed", 0.6],
    ["Tomatoes", "Vegetable", "Germany", "nan", False, True, "nan", "unprocessed", 0.085],
    ["Tomatoes", "Vegetable", "Germany", "nan", True, True, "nan", "unprocessed", 0.035]
    ]

tomatoes = pd.DataFrame(columns=["Product", "Type", "Country of Origin", 
                           "Method of Transportation", 
                           "Organic", "Seasonal", 
                           "Type of Packaging", "Processed", 
                           "CO2_Equivalent_per_Kilo"],data=tomatoe_values)
tomatoes["Source"] = "www.umweltdialog.de"


#Adding the information from Our World in Data
#open the data:
data2 = "https://drive.google.com/file/d/1xzNgqYjhByxcYZJ36915UJtsw8OpxV-k/view?usp=sharing"
data2 = 'https://drive.google.com/uc?id=' + data2.split('/')[-2]
df_OWID = pd.read_csv(data2)

#delete unneccessary columns and rename "Entity" to "Product", dropping unneccessary columns
df_OWID.rename(columns={"Entity":"Product"}, inplace=True) 
df_OWID = df_OWID.drop(["Code"], axis =1)
df_OWID = df_OWID.drop(["Year"], axis =1)

#adding total CO2-eq
df_OWID["CO2_Equivalent_per_Kilo"] = df_OWID.sum(axis=1)
df_OWID["Type"]=("Fruit", "Fruit", "Grains", "Meat", "Meat", "Sweets", "Fruit", "Vegetable", "Sweets", 
                 "Vegetable", "Dairy", "Fruit", "Drinks", "Sweets", "Eggs", "Fish", "Ingredients", 
                 "Meat","Vegetable", "Dairy", "Ingredients", "Grains", "Ingredients", "Vegetable", 
                 "Fruit","nan", "Vegetable", "Ingredients", "Vegetable", "Meat", "Vegetable", 
                 "Meat","Ingredients", "Grains", "Vegetable", "Fish", "Ingredients", "Substitute", 
                 "Ingredients", "Substitute", "Vegetable", "Grains", "Drinks")
df_OWID["Source"] = "Our World in Data"


#Adding data from supporting information of Drewnoski et al., Am. J. of Clinical Nutrition, 2015
#open data
data3 = "https://docs.google.com/spreadsheets/d/19SAmlAQbzOAhRfrolxGM5KMrDtLWut74/edit?usp=drive_web&ouid=107291675655917561403&rtpof=true"
data3 = 'https://drive.google.com/uc?id=' + data3.split('/')[-2]
df3 = pd.read_excel(data3)

#adjusting the DataFrame
df3["CO2_Equivalent_per_Kilo"] = df3["GHGEs per 100g (Median)"] / 100
df3["Product"] = df3["Food group"]
df_Drewnowski = df3.loc[:, df3.columns.intersection(['Product','CO2_Equivalent_per_Kilo'])]
df_Drewnowski["Type"]=("Meat", "Pastries", "Dairy", "Pastries", "Drinks", "nan", "Fish", "Meat", 
                       "Pastries", "Grains", "Dish", "Sweets", "Drinks", "Sweets", "Dairy",
                       "Dish", "Vegetable", "Grains", "Sweets", "Dairy", "Vegetable", "Sweets", 
                       "Dairy", "Dairy", "Meat", "Eggs", "Pastries", "Pastries", "Fruit", "Fish",
                       "Dairy", "Dish", "Dairy", "Dish")
df_Drewnowski["Source"] = "Drewnowski et al., 2015"


#Creating a DataFrame for Data on Tomato Ketchup from the following source: 
    #Wohner, Bernhard, et al., Science of the Total Environment 738 (2020): 139846.
ketchup_data = [
    ["Ketchup, 450g", "Vegetable", False, "Plastic", "processed, sauce", 1.25],
    ["Ketchup, 380g", "Vegetable", True, "Plastic", "processed, sauce", 1.7],
    ["Ketchup, 550g", "Vegetable", True, "Plastic", "processed, sauce", 1.31 ],
    ["Ketchup, 480g", "Vegetable", True, "Glas", "processed, sauce", 1.78]
    ]

ketchup = pd.DataFrame(columns=["Product", "Type", 
                           "Organic", "Type of Packaging", "Processed", 
                           "CO2_Equivalent_per_Kilo"],data=ketchup_data)
ketchup["Source"] = "Wohner et al., 2020"


#Creating a DataFrame for Carbonated Softdrinks from the following source:
    #Amienyo, David, et al.,The International Journal of Life Cycle Assessment 18.1 (2013): 77-92.
drinks_data = [
    ["Cola, 0.33l", "Drinks", "Aluminium can", 5.7],
    ["Cola, 0.5l", "Drinks", "Plastic", 3.9],
    ["Cola, 2l", "Drinks", "Plastic", 2.5],
    ["Coca Cola, 0.33l", "Drinks", "Aluminium can", 5.15],
    ["Coca Cola, 2l", "Drinks", "Plastic", 2.5],
    ["Carbonated drink,ambient temp., 0.33l", "Drinks", "Aluminium can", 3.12],
    ["Carbonated drink,ambient temp., 0.5l", "Drinks", "Plastic", 2.93],
    ["Carbonated drink,ambient temp., 2l", "Drinks", "Plastic", 1.51],
    ["Carbonated drink,chilled, 0.33l", "Drinks", "Aluminium can", 4.67],
    ["Carbonated drink,chilled, 0.5l", "Drinks", "Plastic", 3.88],
    ]
drinks = pd.DataFrame(columns=["Product", "Type", 
                           "Type of Packaging", 
                           "CO2_Equivalent_per_Kilo"],data=drinks_data)
drinks["Source"] = "Amienyo et al., 2013"


#Add Data from https://www.statista.com/statistics/947969/greenhouse-gas-emissions-agricultural-production-worldwide-by-food-product/
#NOTE: Original data is in g CO2-eq per kcal!!!
statista_data = pd.DataFrame({"Product":["Beef/mutton", "Poultry", "Pork", "Eggs", "Dairy", "Fresh produce", "Rice", "Wheat", "Maize", "Pulses"],
                         "processing":[22.0, 3.7, 3.51, 2.1, 1.8, 0.8, 0.5, 0.2, 0.1, 0.1],
                         "Type":["Meat", "Meat", "Meat", "Eggs", "Dairy", "Vegetable", "Grains", "Grains", "Vegetable", "nan"]})
statista_data["Source"] = "https://www.statista.com/statistics/947969/greenhouse-gas-emissions-agricultural-production-worldwide-by-food-product/"

#conversion to kg CO2-eq per kg:
statista_data["kcals/100g"] = [277, 272, 242, 155, 46, 65, 130, 329, 99, 567]
statista_data["food_emissions_processing"] = statista_data["processing"] * statista_data["kcals/100g"]/10000
statista_data.drop(labels="processing", axis=1, inplace=True)
statista_data.drop(labels="kcals/100g", axis=1, inplace=True)
statista_data["Processed"]="unprocessed"


#Add Data from https://static.ewg.org/reports/2011/meateaters/pdf/methodology_ewg_meat_eaters_guide_to_health_and_climate_2011.pdf
#NOTE: Original data in kg CO2-eq per pound
#Data on Page 26 to 39
Meat_Eaters_Guide = pd.DataFrame({"Product":["Beef", "Lamb", "Pork", "Chicken", "Turkey", "Cheese", "Yoghurt", "Eggs", "Salmon", "Tuna"],
                         "food_emissions_processing":[22.4, 20.4, 4.6, 2.3, 3.4, 9.1, 0.8, 2.1, 4.1, 3.2],
                         "CO2_Equivalent_per_pound":[39.3, 39.3, 12.1, 6.9, 10.9, 13.5, 2.2, 4.8, 11.9, 6.1],
                         "Type":["Meat", "Meat", "Meat", "Meat", "Meat", "Dairy", "Dairy", "Eggs", "Fish", "Fish"]})
Meat_Eaters_Guide["Processed"]="unprocessed"
Meat_Eaters_Guide["Source"] = "https://static.ewg.org/reports/2011/meateaters/pdf/methodology_ewg_meat_eaters_guide_to_health_and_climate_2011.pdf"

#conversion to kg CO2-eq per kg:
Meat_Eaters_Guide["food_emissions_processing"] = Meat_Eaters_Guide["food_emissions_processing"]/0.4536
Meat_Eaters_Guide["CO2_Equivalent_per_Kilo"] = Meat_Eaters_Guide["CO2_Equivalent_per_pound"]/0.4536
Meat_Eaters_Guide.drop(labels="CO2_Equivalent_per_pound", axis=1, inplace=True)


#Add Data from https://www.fao.org/gleam/results/en/
fao_data = pd.DataFrame({"Product":["Beef", "Cattle Milk", "Small Ruminants Meat", "Small Ruminants Milk", "Buffalo Meat", "Buffalo Milk", "Pork", "Chicken Meat", "Chicken Eggs"],
                         "Type":["Meat", "Dairy", "Meat", "Dairy", "Meat", "Dairy", "Meat", "Meat", "Eggs"],
                         "emissions_kgCO2-eq per kg of protein":[295, 87, 201, 148, 404, 140, 55, 35, 31],
                         "g protein per 100g":[26, 3.4, 25, 6, 21.62, 3.9, 27, 27, 13]})
fao_data["Processed"] = "unprocessed"
fao_data["Source"] = "https://www.fao.org/gleam/results/en/"

#conversion to kg CO2-eq per kg:
fao_data["CO2_Equivalent_per_Kilo"] = fao_data["emissions_kgCO2-eq per kg of protein"]*fao_data["g protein per 100g"]/100

#Multiply total_emissions with 0.41 for animal feed (as feed accounts for 41% of total sector emissions)
fao_data["food_emissions_animal_feed"] = 0.41 * fao_data["CO2_Equivalent_per_Kilo"]
fao_data["food_emissions_animal_feed"] = fao_data["food_emissions_animal_feed"].round(decimals = 1)
fao_data.drop(labels="emissions_kgCO2-eq per kg of protein", axis=1, inplace=True)
fao_data.drop(labels="g protein per 100g", axis=1, inplace=True)

#---------------------------------------------------------------------------------------------------------------------------

#concatenating the datasets
concatenated = pd.concat([df_IFEU, tomatoes, df_Drewnowski, ketchup, drinks,
                          statista_data, Meat_Eaters_Guide, fao_data, df_OWID])
concatenated.replace("nan", np.nan, inplace=True)
concatenated.sort_values("Type", inplace=True)
concatenated.reset_index(drop=True, inplace=True)

#----------------------------------------------------------------------------------------------------
#savinf df_OWID as Excel
#df_OWID.sort_values("Type", inplace=True)
#df_OWID.to_excel("C:/Users/carol/Documents/TechLabs/df_OWID.xlsx")

#setting values for transport etc
Fruits = concatenated.iloc[62:78, :]
Fruits["CO2_Equivalent_per_Kilo"].fillna(Fruits["food_emissions_processing"]/2.5*10**(-17),inplace=True)
Fruits["food_emissions_land_use"].fillna(0.14*Fruits["CO2_Equivalent_per_Kilo"], inplace=True)
Fruits["food_emissions_farm"].fillna(0.31*Fruits["CO2_Equivalent_per_Kilo"], inplace=True)
Fruits["food_emissions_animal_feed"].fillna(0, inplace=True)
Fruits["food_emissions_processing"].fillna(2.5*10**(-17)*Fruits["CO2_Equivalent_per_Kilo"], inplace=True)
Fruits["food_emissions_transport"].fillna(0.124*Fruits["CO2_Equivalent_per_Kilo"], inplace=True)
Fruits["food_emissions_retail"].fillna(0, inplace=True)
Fruits["food_emissions_packaging"].fillna(6.1*10**(-17)*Fruits["CO2_Equivalent_per_Kilo"], inplace=True)
#Fruits.fillna(Fruits.mean(), inplace=True)

Dairy = concatenated.iloc[0:22, :]
Dairy["CO2_Equivalent_per_Kilo"].fillna(Dairy["food_emissions_processing"]/0.03, inplace=True)
Dairy["food_emissions_land_use"].fillna(0.21*Dairy["CO2_Equivalent_per_Kilo"], inplace=True)
Dairy["food_emissions_farm"].fillna(0.61*Dairy["CO2_Equivalent_per_Kilo"], inplace=True)
Dairy["food_emissions_animal_feed"].fillna(0.10*Dairy["CO2_Equivalent_per_Kilo"], inplace=True)
Dairy["food_emissions_processing"].fillna(0.03*Dairy["CO2_Equivalent_per_Kilo"], inplace=True)
Dairy["food_emissions_transport"].fillna(0.01*Dairy["CO2_Equivalent_per_Kilo"], inplace=True)
Dairy["food_emissions_retail"].fillna(0.03*Dairy["CO2_Equivalent_per_Kilo"], inplace=True)
Dairy["food_emissions_packaging"].fillna(0.01*Dairy["CO2_Equivalent_per_Kilo"], inplace=True)
#Dairy.fillna(Dairy.mean(), inplace=True)
    
Drinks = concatenated.iloc[26:49, :]
Drinks["CO2_Equivalent_per_Kilo"].fillna(Drinks["food_emissions_processing"]/0.04, inplace=True)
Drinks["food_emissions_land_use"].fillna(0.20*Drinks["CO2_Equivalent_per_Kilo"], inplace=True)
Drinks["food_emissions_farm"].fillna(0.61*Drinks["CO2_Equivalent_per_Kilo"], inplace=True)
Drinks["food_emissions_animal_feed"].fillna(0*Drinks["CO2_Equivalent_per_Kilo"], inplace=True)
Drinks["food_emissions_processing"].fillna(0.04*Drinks["CO2_Equivalent_per_Kilo"], inplace=True)
Drinks["food_emissions_transport"].fillna(0.01*Drinks["CO2_Equivalent_per_Kilo"], inplace=True)
Drinks["food_emissions_retail"].fillna(0.01*Drinks["CO2_Equivalent_per_Kilo"], inplace=True)
Drinks["food_emissions_packaging"].fillna(0.13*Drinks["CO2_Equivalent_per_Kilo"], inplace=True)
#Drinks.fillna(Drinks.mean(), inplace=True)
    
Eggs = concatenated.iloc[49:54, :]
Eggs["CO2_Equivalent_per_Kilo"].fillna(Eggs["CO2_Equivalent_per_Kilo"].mean(), inplace=True)
Eggs["food_emissions_land_use"].fillna(0.16*Eggs["CO2_Equivalent_per_Kilo"], inplace=True)
Eggs["food_emissions_farm"].fillna(0.29*Eggs["CO2_Equivalent_per_Kilo"], inplace=True)
Eggs["food_emissions_animal_feed"].fillna(0.49*Eggs["CO2_Equivalent_per_Kilo"], inplace=True)
Eggs["food_emissions_processing"].fillna(0*Eggs["CO2_Equivalent_per_Kilo"], inplace=True)
Eggs["food_emissions_transport"].fillna(0.02*Eggs["CO2_Equivalent_per_Kilo"], inplace=True)
Eggs["food_emissions_retail"].fillna(0*Eggs["CO2_Equivalent_per_Kilo"], inplace=True)
Eggs["food_emissions_packaging"].fillna(0.04*Eggs["CO2_Equivalent_per_Kilo"], inplace=True)
#Eggs.fillna(Eggs.mean(), inplace=True)
    
Fish = concatenated.iloc[54:62, :]
Fish["food_emissions_land_use"].fillna(0.04*Fish["CO2_Equivalent_per_Kilo"], inplace=True)
Fish["food_emissions_farm"].fillna(0.71*Fish["CO2_Equivalent_per_Kilo"], inplace=True)
Fish["food_emissions_animal_feed"].fillna(0.20*Fish["CO2_Equivalent_per_Kilo"], inplace=True)
Fish["food_emissions_processing"].fillna(0*Fish["CO2_Equivalent_per_Kilo"], inplace=True)
Fish["food_emissions_transport"].fillna(0.02*Fish["CO2_Equivalent_per_Kilo"], inplace=True)
Fish["food_emissions_retail"].fillna(0.01*Fish["CO2_Equivalent_per_Kilo"], inplace=True)
Fish["food_emissions_packaging"].fillna(0.02*Fish["CO2_Equivalent_per_Kilo"], inplace=True)
#Fish.fillna(Fish.mean(), inplace=True)
    
Grains = concatenated.iloc[78:86, :]
Grains["CO2_Equivalent_per_Kilo"].fillna(Grains["food_emissions_processing"]/0.05, inplace=True)
Grains["food_emissions_land_use"].fillna(0.01*Grains["CO2_Equivalent_per_Kilo"], inplace=True)
Grains["food_emissions_farm"].fillna(0.74*Grains["CO2_Equivalent_per_Kilo"], inplace=True)
Grains["food_emissions_animal_feed"].fillna(0*Grains["CO2_Equivalent_per_Kilo"], inplace=True)
Grains["food_emissions_processing"].fillna(0.05*Grains["CO2_Equivalent_per_Kilo"], inplace=True)
Grains["food_emissions_transport"].fillna(0.04*Grains["CO2_Equivalent_per_Kilo"], inplace=True)
Grains["food_emissions_retail"].fillna(0.06*Grains["CO2_Equivalent_per_Kilo"], inplace=True)
Grains["food_emissions_packaging"].fillna(0.10*Grains["CO2_Equivalent_per_Kilo"], inplace=True)
#Grains.fillna(Grains.mean(), inplace=True)
    
Ingredients = concatenated.iloc[86:98, :]
Ingredients["food_emissions_land_use"].fillna(0.15*Ingredients["CO2_Equivalent_per_Kilo"], inplace=True)
Ingredients["food_emissions_farm"].fillna(0.54*Ingredients["CO2_Equivalent_per_Kilo"], inplace=True)
Ingredients["food_emissions_animal_feed"].fillna(0*Ingredients["CO2_Equivalent_per_Kilo"], inplace=True)
Ingredients["food_emissions_processing"].fillna(0.11*Ingredients["CO2_Equivalent_per_Kilo"], inplace=True)
Ingredients["food_emissions_transport"].fillna(0.05*Ingredients["CO2_Equivalent_per_Kilo"], inplace=True)
Ingredients["food_emissions_retail"].fillna(0*Ingredients["CO2_Equivalent_per_Kilo"], inplace=True)
Ingredients["food_emissions_packaging"].fillna(0.15*Ingredients["CO2_Equivalent_per_Kilo"], inplace=True)
#Ingredients.fillna(Ingredients.mean(), inplace=True)   
 
Meat = concatenated.iloc[98:124, :]
Meat["CO2_Equivalent_per_Kilo"].fillna(Meat["food_emissions_processing"]/0.04, inplace=True)
Meat["food_emissions_land_use"].fillna(0.18*Meat["CO2_Equivalent_per_Kilo"], inplace=True)
Meat["food_emissions_farm"].fillna(0.65*Meat["CO2_Equivalent_per_Kilo"], inplace=True)
Meat["food_emissions_animal_feed"].fillna(0.10*Meat["CO2_Equivalent_per_Kilo"], inplace=True)
Meat["food_emissions_processing"].fillna(0.04*Meat["CO2_Equivalent_per_Kilo"], inplace=True)
Meat["food_emissions_transport"].fillna(0.02*Meat["CO2_Equivalent_per_Kilo"], inplace=True)
Meat["food_emissions_retail"].fillna(0.01*Meat["CO2_Equivalent_per_Kilo"], inplace=True)
Meat["food_emissions_packaging"].fillna(0.01*Meat["CO2_Equivalent_per_Kilo"], inplace=True)
#Meat.fillna(Meat.mean(), inplace=True)
    
Substitute = concatenated.iloc[131:139, :]
Substitute["food_emissions_land_use"].fillna(0.3*Substitute["CO2_Equivalent_per_Kilo"], inplace=True)
Substitute["food_emissions_farm"].fillna(0.15*Substitute["CO2_Equivalent_per_Kilo"], inplace=True)
Substitute["food_emissions_animal_feed"].fillna(0*Substitute["CO2_Equivalent_per_Kilo"], inplace=True)
Substitute["food_emissions_processing"].fillna(0.25*Substitute["CO2_Equivalent_per_Kilo"], inplace=True)
Substitute["food_emissions_transport"].fillna(0.08*Substitute["CO2_Equivalent_per_Kilo"], inplace=True)
Substitute["food_emissions_retail"].fillna(0.15*Substitute["CO2_Equivalent_per_Kilo"], inplace=True)
Substitute["food_emissions_packaging"].fillna(0.08*Substitute["CO2_Equivalent_per_Kilo"], inplace=True)
#Substitute.fillna(Substitute.mean(), inplace=True)  
  
Vegetables = concatenated.iloc[148:181, :]
Vegetables["CO2_Equivalent_per_Kilo"].fillna(Vegetables["food_emissions_processing"]/0.03, inplace=True)
Vegetables["food_emissions_land_use"].fillna(0.22*Vegetables["CO2_Equivalent_per_Kilo"], inplace=True)
Vegetables["food_emissions_farm"].fillna(0.53*Vegetables["CO2_Equivalent_per_Kilo"], inplace=True)
Vegetables["food_emissions_animal_feed"].fillna(0*Vegetables["CO2_Equivalent_per_Kilo"], inplace=True)
Vegetables["food_emissions_processing"].fillna(0.03*Vegetables["CO2_Equivalent_per_Kilo"], inplace=True)
Vegetables["food_emissions_transport"].fillna(0.18*Vegetables["CO2_Equivalent_per_Kilo"], inplace=True)
Vegetables["food_emissions_retail"].fillna(0*Vegetables["CO2_Equivalent_per_Kilo"], inplace=True)
Vegetables["food_emissions_packaging"].fillna(0.03*Vegetables["CO2_Equivalent_per_Kilo"], inplace=True)
#Vegetables.fillna(Vegetables.mean(), inplace=True)

#average percentual values for step in food supply chain (from https://ourworldindata.org/environmental-impacts-of-food)
Dish = concatenated.iloc[22:26,:]
Pastries = concatenated.iloc[124:131, :]
Sweets = concatenated.iloc[139:148, :]
none = concatenated.iloc[182:,:]
others = pd.concat([Dish, Pastries, Sweets, none])
others["CO2_Equivalent_per_Kilo"].fillna(1.6, inplace=True)
others["food_emissions_land_use"].fillna(0.24*others["CO2_Equivalent_per_Kilo"], inplace=True)
others["food_emissions_farm"].fillna(0.27*others["CO2_Equivalent_per_Kilo"], inplace=True)
others["food_emissions_animal_feed"].fillna(0.31*others["CO2_Equivalent_per_Kilo"], inplace=True)
others["food_emissions_processing"].fillna(0.04*others["CO2_Equivalent_per_Kilo"], inplace=True)
others["food_emissions_transport"].fillna(0.06*others["CO2_Equivalent_per_Kilo"], inplace=True)
others["food_emissions_retail"].fillna(0.03*others["CO2_Equivalent_per_Kilo"], inplace=True)
others["food_emissions_packaging"].fillna(0.05*others["CO2_Equivalent_per_Kilo"], inplace=True)

#concatenate evrything including df_OWID and fao_data
final = pd.concat([Dairy, Drinks, Eggs, Fish, Fruits, Grains, Ingredients, Meat,
                   Substitute, Vegetables, others])
final.replace("nan", np.nan, inplace=True)
final.sort_values("Product", inplace=True)
final.reset_index(drop=True, inplace=True)

#--------------------------------------------------------------------------------------------------------------------------

#saving the data
filename = "C:/Users/carol/Documents/TechLabs/group-5-carbon-food-print/complete dataset.csv"
final.to_csv(filename)
