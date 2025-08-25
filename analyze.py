import numpy as np
import pandas as pd

# Generate random data
data = np.random.rand(10)

# Print stats
print("Mean:", data.mean())
print("Max:", data.max())
print("Min:", data.min())

# Save CSV
df = pd.DataFrame(data, columns=["Values"])
df.to_csv("data.csv", index=False)
