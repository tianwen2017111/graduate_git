import numpy as np
import matplotlib.pyplot as plt

item = 4
x = np.arange(item)
precision = [0.9537, 0.7975, 0.92, 0.9081]
recall = [0.906, 0.5, 0.8642, 0.8719]
F_measure = [0.9209, 0.443, 0.8781, 0.8689]

total_width, n = 0.8, 3
width = total_width / n
x = x - (total_width - width) / 2
print x

plt.bar(x, precision, width=width, label='precision', color='steelblue')
plt.bar(x + width, recall, width=width, label='recall', color='darkseagreen')
plt.bar(x + 2*width, F_measure, width=width, label='F-measure', color='salmon')

plt.legend()
plt.show()