import json
import csv

keywords = ["html", "div", "meta", "title", "link", "script", "style", "h1", "h2", "ul", "a", "class", "br", "button", "img"]

def extract_values(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results

def read_json(file_name):
    """Read each JSON file and parse compressed data into CSV file"""
    with open(file_name, "r") as file:
        data = json.load(file, strict=False)

    df = []

    print("PARSING DATA FROM " + file_name)
    for i in range(len(keywords)):
        freq = len(extract_values(data, keywords[i]))
        df.append(freq)

    df = dict(zip(keywords, df))

    with open('training_data.csv', mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keywords)
        writer.writeheader()
        writer.writerow(df)

for i in range(1, 7):
    read_json(str(i)+".json")
