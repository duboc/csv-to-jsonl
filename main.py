import csv
import json

def csv_to_jsonl(csv_file_path, jsonl_file_path):
  """
  Converts a CSV file to JSONL format.

  Args:
    csv_file_path: Path to the CSV file.
    jsonl_file_path: Path to the output JSONL file.
  """
  with open(csv_file_path, 'r', encoding='utf-8') as csv_file, \
       open(jsonl_file_path, 'w', encoding='utf-8') as jsonl_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
      jsonl_file.write(json.dumps(row) + '\n')

# Replace these paths with your actual file paths
csv_file_path = './file.csv'
jsonl_file_path = './file.jsonl'

csv_to_jsonl(csv_file_path, jsonl_file_path)

print(f"CSV converted to JSONL. Output file: {jsonl_file_path}")