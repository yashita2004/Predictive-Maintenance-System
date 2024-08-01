import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
data_path = "C:\\Users\\yuvi\\Desktop\\predictive_maintenance.csv"
data = pd.read_csv(data_path)
n = data.shape[0]
# First checks
print('Features non-null values and data type:')
data.info()
print('Check for duplicate values:',
      data['Product ID'].unique().shape[0]!=n)
data['Tool wear'] = data['Tool wear'].astype('float64')
data['Rotational speed '] = data['Rotational speed'].astype('float64')
# Rename features
data.rename(mapper={'Air temperature': 'Air temperature',
                    'Process temperature': 'Process temperature',
                    'Rotational speed ': 'Rotational speed',
                    'Torque ': 'Torque',
                    'Tool wear': 'Tool wear'}, axis=1, inplace=True)
# Remove first character and set to numeric dtype
data['Product ID'] = data['Product ID'].apply(lambda x: x[1:])
data['Product ID'] = pd.to_numeric(data['Product ID'])

# Histogram of ProductID
sns.histplot(data=data, x='Product ID', hue='Type')
plt.show()
# Drop ID columns
df = data.copy()
df.drop(columns=['UID','Product ID'], inplace=True)
# Pie chart of Type percentage
value = data['Type'].value_counts()
Type_percentage = 100*value/data.Type.shape[0]
labels = Type_percentage.index.array
x = Type_percentage.array
plt.pie(x, labels = labels, colors=sns.color_palette('tab10')[0:3], autopct='%.0f%%')
plt.title('Machine Type percentage')
plt.show()
df.describe()