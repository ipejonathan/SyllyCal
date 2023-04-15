import pandas as pd
import json

example_data_json_file = "structuredData 3.json"

with open('structuredData 3.json', 'r') as f:
    data = json.loads(f.read())

example_json = pd.json_normalize(data, record_path=['elements'])

print(example_json.head())