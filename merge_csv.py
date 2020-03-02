import pandas as pd

a = pd.read_csv("C:/Users/James/Desktop/Excel Files/S_10/S10_T3.csv")
b = pd.read_csv("C:/Users/James/Desktop/Excel Files/S_10/S10_T3_m.csv")
merged = pd.concat([a, b], axis=1)

merged.to_csv('C:/Users/James/Desktop/Excel Files/S_10/S10_T3_f.csv',index=False)