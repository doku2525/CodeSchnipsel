import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Beispiel-DataFrame
data = {'A': [1, 2, 3], 'B': [2, 4, 5], 'C': [3, 2, 1]}
df = pd.DataFrame(data)

# Korrelationsmatrix berechnen
corr_matrix = df.corr()
print(corr_matrix)
# Heatmap mit matplotlib erstellen
plt.imshow(corr_matrix, cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.xticks(ticks=range(len(corr_matrix.columns)), labels=corr_matrix.columns)
plt.yticks(ticks=range(len(corr_matrix.columns)), labels=corr_matrix.columns)
plt.title('Korrelationsmatrix')
plt.show()