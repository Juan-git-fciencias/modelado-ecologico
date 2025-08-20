## Week 1
# Printing Hello world
print("Hello, World!")
# Simple Arithmetic Operations
a = 37323
b = 39373
# Adittion
print(a+b)
# Substraction
print(b-a)
# Multiplication
print(a*b)
# Division
print(a/b)
# Absolute value of a number
def valor_absoluto(x):
    return x if x >= 0 else -x 

print(valor_absoluto(-13))

## Week 2
# Import packages
import numpy as np
import pandas as  pd
# Import dataset 
df = pd.read_csv("Terminos_lagoon_TA_DIC_2023_RawData.csv")
print(df.head(5))
print(df.tail(5))
print(df.info())
# New column "TA_DIC_ratio"
df["TA_DIC_ratio"] = df["ta_micromol_kg"]/df["dic_micromol_kg"]
print(df.head(6))
# Mean of "TA_DIC_ratio" per season 
print(df["season"].head())
season_mean = df.groupby("season")["TA_DIC_ratio"].mean()
print(season_mean)
# Mean of "TA_DIC_ratio"per area
area_mean = df.groupby("area")["TA_DIC_ratio"].mean()
print(area_mean)
# Std of "TA_DIC_ratio" per season and area
season_std = df.groupby("season")["TA_DIC_ratio"].std()
print(season_std)
area_std = df.groupby("area")["TA_DIC_ratio"].std()
print(area_std)
# Create dataframe with objects
TA_DIC_Season_Areas = pd.DataFrame({
    "season_mean": season_mean,
    "area_mean": area_mean, 
    "season_std": season_std,
    "area_std": area_std,
})
print(np.transpose(TA_DIC_Season_Areas))
# Crearte excel with results 
TA_DIC_Season_Areas.to_excel("TA_DIC_Season_Area.xlsx", sheet_name="Hoja 1", index=True)


