import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load CSV files (local path)
# -----------------------------
titles = pd.read_csv("titles.csv")
ratings = pd.read_csv("ratings.csv")

# -----------------------------
# 2. Clean and merge
# -----------------------------
# Ensure numeric fields are clean
titles["runtime_minutes"] = pd.to_numeric(titles["runtime_minutes"], errors="coerce")
titles["start_year"] = pd.to_numeric(titles["start_year"], errors="coerce")
ratings["average_rating"] = pd.to_numeric(ratings["average_rating"], errors="coerce")
ratings["num_votes"] = pd.to_numeric(ratings["num_votes"], errors="coerce")

# Merge datasets
df = pd.merge(titles, ratings, on="tconst", how="inner")
df_clean = df.dropna(subset=["runtime_minutes", "average_rating", "num_votes", "start_year"])

# -----------------------------
# 3. NumPy statistical analysis
# -----------------------------
runtimes = df_clean["runtime_minutes"].to_numpy()
ratings_np = df_clean["average_rating"].to_numpy()
votes = df_clean["num_votes"].to_numpy()
years = df_clean["start_year"].to_numpy()

print("\n📊 Runtime Stats")
print("Mean:", np.mean(runtimes))
print("Median:", np.median(runtimes))
print("Std Dev:", np.std(runtimes))
print("Min:", np.min(runtimes))
print("Max:", np.max(runtimes))

print("\n⭐ Rating Stats")
print("Mean:", np.mean(ratings_np))
print("Median:", np.median(ratings_np))
print("Std Dev:", np.std(ratings_np))
print("Min:", np.min(ratings_np))
print("Max:", np.max(ratings_np))

print("\n🗳️ Vote Stats")
print("Mean:", np.mean(votes))
print("Median:", np.median(votes))
print("Std Dev:", np.std(votes))
print("Min:", np.min(votes))
print("Max:", np.max(votes))

# Titles per year
titles_per_year = df_clean.groupby("start_year").size()

# -----------------------------
# 4. Visualizations
# -----------------------------

# Runtime distribution
plt.figure(figsize=(10, 6))
plt.hist(runtimes, bins=30, color="skyblue", edgecolor="black")
plt.title("Runtime Distribution")
plt.xlabel("Runtime (minutes)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Rating distribution
plt.figure(figsize=(10, 6))
plt.hist(ratings_np, bins=20, color="salmon", edgecolor="black")
plt.title("Average Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()

# Titles released per year
plt.figure(figsize=(12, 6))
titles_per_year.plot(kind="line", marker="o", color="green")
plt.title("Titles Released Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.tight_layout()
plt.show()

# Number of votes distribution (log scale)
plt.figure(figsize=(10, 6))
plt.hist(votes, bins=30, color="orange", edgecolor="black", log=True)
plt.title("Distribution of Number of Votes (Log Scale)")
plt.xlabel("Number of Votes")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
