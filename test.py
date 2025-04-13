print("Rodando...")

import csv
from tabulate import tabulate

with open("Developer Ecosystem Survey 2024_ Raw data sharing/2024_sharing_data_outside.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for _, row in zip(range(2), reader)]  # Read first 2 rows, 5 columns

    output = tabulate(rows, tablefmt="grid")

    with open("saida.txt", "w", encoding='utf-8') as f:
        print(output, file=f)