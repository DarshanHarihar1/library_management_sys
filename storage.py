import csv
from book import Book

def save_file(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for item in data:
            writer.writerow(item)


def load_file(filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            data = []
            for row in reader:
                data.append(row)
            return data
    except FileNotFoundError:
        return []
