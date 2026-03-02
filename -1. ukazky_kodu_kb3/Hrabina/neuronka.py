import csv
from sklearn.neural_network import MLPClassifier

x = []
y = []

with open ("merc.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        model = hash row 
