# Working with CSV Files
import numpy as np

# Create random 5x4 data
data = np.random.random((5, 4))

# Save to CSV with header
np.savetxt("main.csv", data, fmt="%.2f", delimiter=",", header="H1,H2,H3,H4", comments='')

# Read CSV back (skip header row)
reading_csv = np.loadtxt("main.csv", delimiter=",", skiprows=1)

# Show first 3 rows
print(reading_csv[:3, :])
