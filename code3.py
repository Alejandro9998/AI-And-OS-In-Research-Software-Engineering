import pandas as pd
import matplotlib.pyplot as plt

csv_file = "output.csv"

df = pd.read_csv(csv_file)

figure_counts = [len(str(figures).split(",")) for figures in df['figures']]

plt.hist(figure_counts, bins=max(figure_counts))
plt.title('Distribution of Figure Counts')
plt.xlabel('Number of Figures')
plt.ylabel('Frequency')
plt.show()