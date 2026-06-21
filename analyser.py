import pandas as pd
# File Location
file = "./Analyser.xlsx"
# Loading the file in pandas
load = pd.read_excel(file)
# Loading the file content in a dataframe 
df = pd.DataFrame(load)
# showing the first 5 rows
# print(df[0:5])
# Getting rows and columns
print(df.info())
