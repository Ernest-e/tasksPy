from pathlib import Path

import json
import csv
import pickle


def get_directory_info(directory_path):
    directory = Path(directory_path)
    result = []

    for item in directory.iterdir():
        item_info = {
            'name': item.name,
            'type': 'file' if item.is_file() else 'directory',
            'parent': directory_path,
        }

        if item.is_file():
            item_info['size'] = item.stat().st_size
        else:
            item_info['size'] = sum(f.stat().st_size for f in item.rglob('*') if f.is_file())

        result.append(item_info)

        if item.is_dir():
            result.extend(get_directory_info(item))

    return result

def save_to_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=2)

def save_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as csv_file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def save_to_pickle(data, output_file):
    with open(output_file, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)

if __name__ == "__main__":
    directory_path = "/path/to/your/directory"  # Замените путь к вашей директории

    directory_info = get_directory_info(directory_path)

    json_output_file = "directory_info.json"
    csv_output_file = "directory_info.csv"
    pickle_output_file = "directory_info.pkl"

    save_to_json(directory_info, json_output_file)
    save_to_csv(directory_info, csv_output_file)
    save_to_pickle(directory_info, pickle_output_file)
    
    
    
    
    
    
    