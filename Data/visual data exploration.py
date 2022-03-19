# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 10:23:18 2022

@author: carol
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://drive.google.com/file/d/1RgVDovPm_AuNKmGIikFyHeS0vZDBMlww/view?usp=sharing"
url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]
df = pd.read_csv(url)

#Visualization of counts per food type
sns.countplot(x="Type", data=df)
plt.xticks(rotation=45)
plt.title("Counts per Food Type")
plt.xlabel("Food Type")
plt.ylabel("Counts")
