import matplotlib.pyplot as plt

x_values = list(range(0, 5001))
y_values = [x ** 3 for x in x_values]

plt.scatter(x_values, y_values, c='blue', edgecolor='none', s=40)

# Set the chart title and label axes.
plt.title("Cubes_2", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Cubes of Values", fontsize=14)

plt.axis([0, 5100, 0, 135_000_000_000])

plt.show()