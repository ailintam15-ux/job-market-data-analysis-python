import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("job_market_dataset.csv")

# Preview data
print(df.head())

# Dataset information
print(df.info())

# Check missing values
print(df.isnull().sum())

# Top job roles
top_jobs = df['job_title'].value_counts().head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_jobs.values, y=top_jobs.index)

plt.title("Top 10 Most In-Demand Job Roles")
plt.xlabel("Number of Listings")
plt.ylabel("Job Role")

plt.show()

# Salary distribution
plt.figure(figsize=(8,5))
sns.histplot(df['salary'], bins=30, kde=True)

plt.title("Salary Distribution")

plt.show()
