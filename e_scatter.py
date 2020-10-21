import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.scatter(2, 4)
ax.scatter(x_values, y_values, s=200)

# region Chart Title, Label, Tick, ...
ax.set_title("Square Numbers", fontsize=22)
ax.set_xlabel("Value", fontsize=16)
ax.set_ylabel("Square of Value", fontsize=16)
ax.tick_params(axis='both', labelsize=12)
# endregion

plt.show()