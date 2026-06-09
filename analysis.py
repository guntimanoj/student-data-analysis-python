import pandas as pd
import matplotlib.pyplot as plt

# Student dataset
data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Math": [78, 85, 60, 90, 88],
    "CS": [82, 79, 70, 95, 86],
    "Physics": [75, 80, 65, 88, 90]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate total and average marks
df["Total"] = df["Math"] + df["CS"] + df["Physics"]
df["Average"] = df["Total"] / 3

print("Student Performance Data")
print(df)

print("\nSubject-wise Average Marks")
print(df[["Math", "CS", "Physics"]].mean())

# Bar chart for subject averages
df[["Math", "CS", "Physics"]].mean().plot(kind="bar")
plt.title("Subject-wise Average Marks")
plt.ylabel("Marks")
plt.show()

# Bar chart for total marks
df.plot(x="Student", y="Total", kind="bar")
plt.title("Student Total Marks")
plt.ylabel("Marks")
plt.show()