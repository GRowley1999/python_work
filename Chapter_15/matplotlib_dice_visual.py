import matplotlib.pyplot as plt
from die import Die

# Create a D6 die.
die = Die()

# Make some rolls and store the results in a list.
results = [die.roll() for roll_num in range(1000)]

# Analyse the results.
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]

# Visualize the results.
x_values = list(range(1, 7))
plt.scatter(x_values, frequencies, c=frequencies, cmap=plt.cm.Blues, 
    edgecolors='none', s=40)

# Set the chart title and label axes.
plt.title("Dice Frequency Visualization", fontsize=24)
plt.xlabel("Result", fontsize=14)
plt.ylabel("Result frequency", fontsize=14)

plt.show()