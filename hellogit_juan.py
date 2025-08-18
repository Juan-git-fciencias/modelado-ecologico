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
# Import pandas
import pandas as  pd
# Import dataset 
df = pd.read_csv("Terminos_lagoon_TA_DIC_2023_RawData.csv")
print(df.head(5))
print(df.tail(5))
print(df.info())



