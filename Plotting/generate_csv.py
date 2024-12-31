import numpy as np
import pandas as pd

def damped_sine(x, A, B, C, D, E):
    """
    f(x) = A * exp(-B*x) * sin(C*x + D) + E
    """
    return A * np.exp(-B * x) * np.sin(C * x + D) + E

# Choose "true" parameters for a smaller-amplitude damped sinusoid
A_true = 1.5   # amplitude (smaller than 2.5)
B_true = 0.3   # decay rate
C_true = 2.0   # frequency
D_true = 0.5   # phase shift
E_true = 1.0   # vertical offset

# Generate x-values
np.random.seed(42)
x_data = np.linspace(0, 10, 25)

# Generate the corresponding y-values with random noise
y_clean = damped_sine(x_data, A_true, B_true, C_true, D_true, E_true)
noise = 0.25 * np.random.normal(size=len(x_data))  # smaller noise
y_data = y_clean + noise

# Save to CSV
df = pd.DataFrame({'x': x_data, 'y': y_data})
df.to_csv("mydata.csv", index=False)
print("Generated 'mydata.csv' with a smaller-amplitude damped sine wave.")