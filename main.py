import json
import csv

# Define the JSON file path and the output CSV file path
json_file = 'data.json'  # Your JSON file with each row being a JSON object
csv_file = 'output.csv'  # The CSV file to write to

# Define the desired columns
columns = ['Тегло', 'Каталожен номер', 'Размер на опаковката', 'URL', 'PRICE', 'Марка']

# Open the input JSON file and the output CSV file
with open(json_file, 'r', encoding='utf-8') as infile, open(csv_file, 'w', newline='', encoding='utf-8') as outfile:
    # Initialize the CSV writer
    csv_writer = csv.DictWriter(outfile, fieldnames=columns)
    csv_writer.writeheader()  # Write the CSV header

    # Process each line (each line is a JSON object)
    for line in infile:
        # Parse the JSON object
        json_obj = json.loads(line)

        # Extract only the desired columns (handle missing keys)
        filtered_row = {
            'Тегло': json_obj.get('Тегло'),
            'Каталожен номер': json_obj.get('Каталожен номер'),
            'Размер на опаковката': json_obj.get('Размер на опаковката'),
            'URL': json_obj.get('URL'),
            'PRICE': json_obj.get('PRICE'),
            'Марка': json_obj.get('Марка')
        }

        # Write the extracted data to the CSV
        csv_writer.writerow(filtered_row)

print(f"Data extraction complete. Check '{csv_file}' for results.")
