import requests
import csv
import io
import nltk
from nltk.corpus import stopwords
from pdfminer.high_level import extract_text

nltk.download('punkt')
nltk.download('stopwords')

pdf_dir = "D:/Users/alemo/Desktop/Ingeniería Informática/MIERDA A APROBAR 2022-2023/2o cuatri/Sw científico IA/PDFs/"

output_csv = "output.csv"
fields = ["title", "abstract", "references"]
data = []


stopwords_es = set(stopwords.words('spanish'))

# Loop a través de cada archivo PDF en el directorio
for i in range(1, 11):
    pdf_path = pdf_dir + "PDF{}.pdf".format(i)

    pdf_text = extract_text(pdf_path)

    pdf_text = " ".join([word for word in nltk.word_tokenize(pdf_text) if word.lower() not in stopwords_es and word.isalpha()])

    title = pdf_text.split("\n")[0].strip()

    abstract = pdf_text.split("\n\n")[0].replace(title, "").strip()

    references = []
    for line in pdf_text.split("\n"):
        if "Referencias" in line or "Bibliografía" in line:
            for reference in line.split(";"):
                references.append(reference.strip())

    row = {"title": title, "abstract": abstract, "references": references}

    data.append(row)

with io.open(output_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)