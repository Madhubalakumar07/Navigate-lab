import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"D:\Navigate lab\Datasets\weight-height.csv")

# prepare data
print(df.head())
print(df['Height'].describe())
print(df['Weight'].describe())

# Calculate IQR
Q1_height = df['Height'].quantile(0.25)
Q3_height = df['Height'].quantile(0.75)
IQR_height = Q3_height - Q1_height
print(f"IQR (Height): {IQR_height}")
Q1_weight = df['Weight'].quantile(0.25)
Q3_weight = df['Weight'].quantile(0.75)
IQR_weight = Q3_weight - Q1_weight
print(f"IQR (Weight): {IQR_weight}")

# Define outlier thresholds
lower_bound_height = Q1_height - 1.5 * IQR_height
upper_bound_height = Q3_height + 1.5 * IQR_height
print(f"Lower Bound (Height): {lower_bound_height}")
print(f"Upper Bound (Height): {upper_bound_height}")
lower_bound_weight = Q1_weight - 1.5 * IQR_weight
upper_bound_weight = Q3_weight + 1.5 * IQR_weight
print(f"Lower Bound (Weight): {lower_bound_weight}")
print(f"Upper Bound (Weight): {upper_bound_weight}")
# Filter out outliers
filtered_df_height = df[(df['Height'] >= lower_bound_height) & (df['Height'] <= upper_bound_height)]
filtered_df_weight = df[(df['Weight'] >= lower_bound_weight) & (df['Weight'] <= upper_bound_weight)]

# Plotting histograms before and after outlier removal
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(df['Height'], bins=30, color='blue', alpha=0.7)
plt.title('Height Distribution (Before Outlier Removal)')   
plt.subplot(1, 2, 2)
plt.hist(filtered_df_height['Height'], bins=30, color='green', alpha=0.7)
plt.title('Height Distribution (After Outlier Removal)')
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(df['Weight'], bins=30, color='blue', alpha=0.7)
plt.title('Weight Distribution (Before Outlier Removal)')
plt.subplot(1, 2, 2)
plt.hist(filtered_df_weight['Weight'], bins=30, color='green', alpha=0.7)
plt.title('Weight Distribution (After Outlier Removal)')
plt.show()