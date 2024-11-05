import numpy as np

# Contoh data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Hitung rata-rata x dan y
x_mean = np.mean(x)
y_mean = np.mean(y)

# Hitung koefisien regresi b
b = sum((x - x_mean) * (y - y_mean)) / sum((x - x_mean) ** 2)

# Hitung intersep a
a = y_mean - b * x_mean

# Persamaan regresi linear
print("Persamaan regresi linear: y = {} + {}x".format(a, b))