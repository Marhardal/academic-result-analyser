import pandas as pd
# File Location
file = "./Analyser.xlsx"
# Loading the file in pandas
load = pd.read_excel(file)
# Loading the file content in a dataframe 
# df = pd.DataFrame(load)
# showing the first 5 rows
# print(df[0:5])
# print(load.head())
# Getting rows and columns count. Display the column names and data types.
# print(df.info())
# print(df.describe())
# Average score across all students and all subjects.
listscore = load["Score"]
average = listscore.sum()/listscore.count()
# print(average)
print(listscore.mean())

df = pd.DataFrame(load)
# Filter stodents who passed
student_p = df[df["Passed"] == True]

# print(student_p)
# Filter Maths Result
Maths_rst = df[df["Subject"] == "Math"]

print(Maths_rst)


