import matplotlib.pyplot as plt
import os

os.makedirs("reports/figures", exist_ok=True)

names = ["A", "B", "C", "D", "E"]
marks = [70, 80, 65, 90, 85]
hours = [2, 3, 1, 5, 4]

color = "steelblue"

# 1. Bar chart
plt.figure()
plt.bar(names, marks, color=color)
plt.title("Marks of Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.savefig("reports/figures/bar_chart.png")
plt.show()
plt.close()

# 2. Histogram
plt.figure()
plt.hist(marks, bins=5, color=color, edgecolor="black")
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.savefig("reports/figures/histogram.png")
plt.show()
plt.close()

# 3. Scatter plot
plt.figure()
plt.scatter(hours, marks, color=color)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.savefig("reports/figures/scatter_plot.png")
plt.show()
plt.close()

# 4. Line chart
plt.figure()
plt.plot(names, marks, marker="o", color=color)
plt.title("Marks Across Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.savefig("reports/figures/line_chart.png")
plt.show()
plt.close()

print("All four charts created successfully!")