import numpy as np
import matplotlib.pyplot as plt

# Beispiel-Dictionary
data = {
    '2023-11-20': np.random.rand(4, 15, 3),
    '2023-11-21': np.random.rand(4, 15, 3),
    # ... weitere Einträge
}

# Vergleich der Mittelwerte
means = {}
for date, matrix in data.items():
    means[date] = np.mean(matrix)

# Visualisierung einer Heatmap
plt.imshow(data['2023-11-20'][:, :, 0], cmap='hot', interpolation='nearest')
plt.colorbar()
plt.show()
