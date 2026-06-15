from pathlib import Path
import pandas as pd
from .connection import get_connection

# when there are multiple csv files in database
def load_all_csvs(data_folder="data"):
    conn = get_connection()
    tables = {}

    for file in Path(data_folder).glob("*.csv"):
        table_name = file.stem
        df = pd.read_csv(file)
        df.to_sql(
            table_name,
            conn,
            if_exists="replace",
            index=False
        )
        tables[table_name] = list(df.columns)

    return tables