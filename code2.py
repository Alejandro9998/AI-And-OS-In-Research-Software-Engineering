import pandas as pd
from wordcloud import WordCloud

csv_file = "output.csv"

df = pd.read_csv(csv_file)

abstracts = df['abstract']

text = " ".join(abstracts)

wordcloud = WordCloud(width=800, height=800, background_color='white', max_words=50, colormap='inferno').generate(text)

import matplotlib.pyplot as plt
plt.figure(figsize=(8,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
