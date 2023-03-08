import os
import glob
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

nltk.download('punkt')
nltk.download('stopwords')

pdf_path = "D:\Users\alemo\Desktop\Ingeniería Informática\Asignaturas22-23\2o cuatri\Sw científico IA\PDFs\"

pdf_files = glob.glob(pdf_path)

articles = []

for pdf_file in pdf_files:
    with open(pdf_file, 'rb') as f:
        soup = BeautifulSoup(f, 'lxml')
        text = soup.get_text()
        articles.append(text)

words = []

for article in articles:
    sentences = nltk.sent_tokenize(article)
    summary = sentences[0]
    tokens = word_tokenize(summary)
    words += [word.lower() for word in tokens]

stop_words = set(stopwords.words('english'))
words = [word for word in words if word not in stop_words]

freq_dist = FreqDist(words)
wordcloud = WordCloud(width=800, height=800, background_color='white').generate_from_frequencies(freq_dist)
plt.figure(figsize=(8,8))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

fig_counts = []
for article in articles:
    fig_counts.append(len(re.findall(r"Figura", article)))

plt.bar(range(len(fig_counts)), fig_counts)
plt.xlabel('Artículo')
plt.ylabel('Número de figuras')
plt.show()

links = []
for article in articles:
    soup = BeautifulSoup(article, 'lxml')
    for link in soup.find_all('a'):
        links.append(link.get('href'))

print(links)
