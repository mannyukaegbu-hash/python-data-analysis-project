import pandas as pd

# Sample data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Score": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

print("Data:")
print(df)

print("\nAverage Score:", df["Score"].mean())
print("Highest Score:", df["Score"].max())
print("Lowest Score:", df["Score"].min())
