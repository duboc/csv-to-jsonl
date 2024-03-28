## How to use the CSV to JSONL converter
This app converts a CSV file to JSONL format. JSONL is a line-delimited JSON format, where each line is a valid JSON object.  

### Prerequisites
You will need the following:

A CSV file
Python 3 or later
The csv and json Python modules
#### Installation
To install the app, clone the repository and install the dependencies:

```
git clone https://github.com/duboc/csv-to-jsonl.git
cd csv-to-jsonl
pip install -r requirements.txt
```

Usage
To use the app, run the following command:

```
python main.py csv_file_path jsonl_file_path
```

where:

csv_file_path is the path to the CSV file
jsonl_file_path is the path to the output JSONL file
For example, to convert the file file.csv to file.jsonl, run the following command:

```
python main.py file.csv file.jsonl
```

Output
The output JSONL file will be created in the specified directory. Each line of the file will be a valid JSON object.

Example
The following is an example of a CSV file:

name,age
John,30
Jane,25
The following is the corresponding JSONL file:
```
{"name": "John", "age": 30}
{"name": "Jane", "age": 25}
```