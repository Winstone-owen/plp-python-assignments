
pip install pandas
pip install matplotlib
pip install seaborn
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set Seaborn style
sns.set(style="whitegrid")

# Load the Iris dataset
iris_data = load_iris()
iris_df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
iris_df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)

# Display the first few rows
print("First 5 rows of the dataset:")
print(iris_df.head())

# Check for missing values
print("\nMissing values in each column:")
print(iris_df.isnull().sum())

# Dataset info
print("\nDataset Info:")
print(iris_df.info())

# Clean the dataset (no missing values to drop here, but included for completeness)
iris_df.dropna(inplace=True)

# Descriptive statistics
print("\nDescriptive statistics:")
print(iris_df.describe())

# Group by species and compute mean
print("\nMean values grouped by species:")
print(iris_df.groupby('species').mean())

# Create visualizations
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# 1. Line chart (simulated time-series using index)
axs[0, 0].plot(iris_df.index, iris_df['sepal length (cm)'], label='Sepal Length')
axs[0, 0].set_title('Simulated Time-Series of Sepal Length')
axs[0, 0].set_xlabel('Index (Simulated Time)')
axs[0, 0].set_ylabel('Sepal Length (cm)')
axs[0, 0].legend()

# 2. Bar chart: Average petal length per species
avg_petal_length = iris_df.groupby('species')['petal length (cm)'].mean()
axs[0, 1].bar(avg_petal_length.index, avg_petal_length.values, color=['green', 'blue', 'orange'])
axs[0, 1].set_title('Average Petal Length per Species')
axs[0, 1].set_ylabel('Petal Length (cm)')

# 3. Histogram: Sepal Width
axs[1, 0].hist(iris_df['sepal width (cm)'], bins=15, color='purple')
axs[1, 0].set_title('Distribution of Sepal Width')
axs[1, 0].set_xlabel('Sepal Width (cm)')
axs[1, 0].set_ylabel('Frequency')

# 4. Scatter plot: Sepal Length vs Petal Length
axs[1, 1].scatter(iris_df['sepal length (cm)'], iris_df['petal length (cm)'], 
                  c=iris_data.target, cmap='viridis')
axs[1, 1].set_title('Sepal Length vs. Petal Length')
axs[1, 1].set_xlabel('Sepal Length (cm)')
axs[1, 1].set_ylabel('Petal Length (cm)')

plt.tight_layout()
plt.show()
