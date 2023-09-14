import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {'X': [1, 2, 3, 4, 5],
        'Y': [2, 4, 5, 4, 6]}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate the correlation
correlation = df['X'].corr(df['Y'])
print(f"Correlation between X and Y: {correlation}")

# Create a scatter plot
plt.scatter(df['X'], df['Y'], alpha=0.5)
plt.title('Scatter Plot of X vs. Y')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
