import matplotlib.pyplot as plt

points = [0, 1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(points, linewidth=3)
ax.set_title("Square Numbers", fontsize=22)
ax.set_xlabel("Value", fontsize=16)
ax.set_ylabel("Square of Value", fontsize=16)
ax.tick_params(axis='both', labelsize=12)

plt.show()