import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml

data = fetch_openml(name='wine', version=1, as_frame=True)

df = data.frame

df.sample(6)

df.describe()

df.dtypes

features = df.columns
features

selected_features = [features[1], features[9], features[7], features[10], features[5]]
selected_features

features = list(df.columns)
print("Available features:", features)
selected_features = [features[1], features[9], features[7], features[10], features[5]]
print("Selected features: ", selected_features)

fig, axs  = plt.subplots(1, len(selected_features), figsize = (20,3))

for ax, f in zip(axs, selected_features):
    ax.hist(df[f], bins=5, color='skyblue', edgecolor='black')
    ax.set_xlabel(f)

selected_features = [features[1], features[9], features[7], features[10], features[5]]
selected_features

reference_feature = selected_features[0]
y = df[reference_feature]

fig, axs  = plt.subplots(1, len(selected_features), figsize = (20,3))

for ax, f in zip(axs, selected_features):
  ax.scatter(df[f], y)
  ax.set_xlabel(f)

plt.show()


reference_feature = selected_features[0]  # The reference feature
comparison_feature = selected_features[3]  # A feature to compare to

# Create a scatter plot for the selected pair
plt.figure(figsize=(8, 6))
plt.scatter(df[reference_feature], df[comparison_feature], alpha=0.6 ,c='red')
plt.xlabel(reference_feature)
plt.ylabel(comparison_feature)

# Save the plot as an image file
plt.savefig('correlation_plot.png')

plt.show()















