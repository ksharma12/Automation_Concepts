import pandas as pd
import numpy as np

# # 1. Creating a DataFrame from a Dictionary
# dict = {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
# df = pd.DataFrame(dict)
# print(type(df))
# print(df)

# 2. DataFrame with Specified Index Labels
# Write a Pandas program to create and display a DataFrame from a specified dictionary data
# which has the index labels.

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# Sample Python dictionary data and list labels:
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
# 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
# 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
# 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, labels)
# print(df)

# 3. DataFrame Basic Summary Information
# print(df.info())

# 4. Selecting the First 3 Rows
# print(df.iloc[:3, :])

# 5. Selecting 'name' and 'score' Columns
# print(df.loc[:,'name':'score'])
# print(df[['name', 'score']])

# 6. Selecting Specific Columns and Rows
# Select 'name' and 'score' columns in rows 1, 3, 5, 6 from the following data frame.
# print(df.iloc[[1, 3, 5, 6], [0, 1]])

# 7. Selecting Rows Where Attempts > 2
# print(df[df['attempts'] > 2])

# 8. Counting Rows and Columns
# print("Rows : ", df.shape[0])
# print("Columns : ", df.shape[1])
# print("Rows : ", len(df.axes[0]))
# print("Columns : ", len(df.axes[1]))

# 9. Selecting Rows with Missing Score
# print(df[df['score'].isna()])
# print(df[df['score'].isnull()])

# 10. Selecting Rows Where Score is Between 15 and 20
# print(df[(df['score'] >= 15) & (df['score'] <= 20)])
# print(df[df['score'].between(15, 20)])

# 11. Selecting Rows with Attempts < 2 and Score > 15
# print(df[(df['score'] > 15) & (df['attempts'] < 2)])

# 12. Changing the Score in a Specific Row
# df.loc['d', 'score'] = 11.5
# print(df.loc['d', 'score'])

# 13. Summing Examination Attempts
# print(df['attempts'].sum())

# 14. Calculating the Mean of Scores
# print(df['score'].mean())

# 15. Appending and Deleting a New Row
# name : "Suresh", score: 15.5, attempts: 1, qualify: "yes", label: "k"
# df.loc['k'] = ['Suresh', 15.5, 1, 'yes']
# print(df)
# df = df.drop('k')
# print(df)

# 16. Sorting the DataFrame by Multiple Columns
# first by 'name' in descending order, then by 'score' in ascending order.
# df = df.sort_values(by=['name', 'score'], ascending=[False, True])
# print(df)

# # 17. Replacing Column Values (qualify)
# df['qualify'] = df['qualify'].map({'yes': True, 'no': False})
# print(df)

# 18. Changing a Specific Name Value
# change the name 'James' to 'Suresh' in name column of the DataFrame.
# df['name'] = df['name'].replace('James', 'Suresh')
# print(df)

# 19. Deleting a Column from the DataFrame
# df = df.drop('attempts', axis=1)
# df.pop('attempts')
# print(df)

# 20. Inserting a New Column
# color = ['Red','Blue','Orange','Red','White','White','Blue','Green','Green','Red']
# df['color'] = color
# print(df)

# 21. Iterating Over DataFrame Rows
