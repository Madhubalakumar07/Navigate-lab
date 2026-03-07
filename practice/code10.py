import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
height = np.round(np.random.uniform(50, 100, 100), 2)
weight = np.round((0.5 * height + np.random.normal(0, 5, 100)),2)
species = np.random.choice(["Empror Penguin", "Adelie Penguin", "King Penguin", "Gentoo Penguin"], 100)
penguins = pd.DataFrame({"Height": height, "Weight": weight, "Species": species})
print(penguins.to_string())
group = penguins.groupby("Species")
print(np.round(group["Weight"].mean(), 2))
plt.scatter(group["Height"].mean(), group["Weight"].mean())
plt.xlabel('Average Height')
plt.ylabel('Average Weight')
plt.title('Average Weight vs Average Height by Species')
plt.show()