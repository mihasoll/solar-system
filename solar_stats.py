import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('stats.csv')
print(df.head)

figure, axis = plt.subplots(2, 2, figsize=(12, 7))
axis[0, 0].plot(df['t'], df['v'])
axis[0, 0].set_title("v(t)")
axis[0, 0].set_ylim([0, axis[0, 0].get_ylim()[1] * 1.1])

axis[0, 1].plot(df['t'], df['r'])
axis[0, 1].set_title("r(t)")
axis[0, 1].set_ylim([0, axis[0, 1].get_ylim()[1] * 1.1])

axis[1, 0].plot(df['r'], df['v'])
axis[1, 0].set_title("v(r)")
axis[1, 0].set_xlim([0, axis[1, 0].get_xlim()[1] * 1.1])
axis[1, 0].set_ylim([0, axis[1, 0].get_ylim()[1] * 1.1])

figure.delaxes(axis[1, 1])

plt.show()
