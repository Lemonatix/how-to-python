import numpy as np
import pandas as pd

def damped_sine(x, A, B, C, D, E):
    return A * np.exp(-B * x) * np.sin(C * x + D) + E

# True parameters
A_true = 2.5
B_true = 0.3
C_true = 2.0
D_true = 0.5
E_true = 1.0

# Generate x values
np.random.seed(42)
x_data = np.linspace(0, 10, 25)

# Generate noisy y data
y_clean = damped_sine(x_data, A_true, B_true, C_true, D_true, E_true)
noise = 0.3 * np.random.normal(size=len(x_data))
y_data = y_clean + noise

# Create a DataFrame and save to CSV
df = pd.DataFrame({'x': x_data, 'y': y_data})
df.to_csv("mydata.csv", index=False)
print("mydata.csv has been generated!")