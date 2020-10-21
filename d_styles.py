import matplotlib.pyplot as plt

values = [1, 2, 3, 4, 5]
square_values = [1, 4, 9, 16, 25]
# print(plt.style.available)
plt.style.use("seaborn")
fig, ax = plt.subplots()

ax.plot(values, square_values, linewidth=3)

# region Chart Title, Label, Tick, ...
ax.set_title("Square Numbers", fontsize=22)
ax.set_xlabel("Value", fontsize=16)
ax.set_ylabel("Square of Value", fontsize=16)
ax.tick_params(axis='both', labelsize=12)
# endregion

plt.show()