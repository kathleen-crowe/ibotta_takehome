import csv

class CSVLoader:
    def load(self, file_path: str, model):
        records = []
        with open(file_path, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                records.append(model(**row))
        return records
    