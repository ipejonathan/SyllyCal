import pandas as pd
import json

def create_df_from_json(path):

    with open(path, 'r') as f:
        data = json.loads(f.read())

    df = pd.json_normalize(data, record_path=['elements'])

    return df