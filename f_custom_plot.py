import matplotlib.pyplot as plt

x_values = range(1, 501, 10)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

# ax.scatter(x_values, y_values, s=10, c=(1, 0, 0.5))
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Reds)
ax.axis([0, 600, 0, 250000])

# region Chart Title, Label, Tick, ...
ax.set_title("Square Numbers", fontsize=22)
ax.set_xlabel("Value", fontsize=16)
ax.set_ylabel("Square of Value", fontsize=16)
ax.tick_params(axis='both', labelsize=12)
# endregion

plt.show()