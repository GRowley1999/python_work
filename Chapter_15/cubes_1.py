import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]

plt.plot(x_values, y_values, linewidth=5)

# Set the chart title and label the axes.
plt.title("Cubes_1", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Cubes of Values", fontsize=14)

plt.axis([0, 6, 0, 130])

plt.show()