import re

# remove code block markers
def clean_sql(sql: str) -> str:
    sql = re.sub(r"```sql", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"```", "", sql)
    return sql.strip()

# check for forbidden SQL keywords
FORBIDDEN = {
    "DROP",
    "DELETE",
    "UPDATE",
    "INSERT",
    "ALTER",
    "TRUNCATE",
    "CREATE",
    "REPLACE",
}
def validate_safe_sql(sql: str):
    sql_upper = sql.upper()
    for keyword in FORBIDDEN:
        if keyword in sql_upper:
            raise ValueError(
                f"Forbidden SQL keyword detected: {keyword}"
            )
    return True

# Parse the schema to get tables and columns 
def parse_schema(schema_text: str):
    tables = {}
    current_table = None
    for line in schema_text.splitlines():
        line = line.strip()
        if line.startswith("TABLE"):
            current_table = line.split()[1]
            tables[current_table] = set()
        elif current_table and line and not line.startswith("FOREIGN"):
            parts = line.split()
            if len(parts) >= 2:
                tables[current_table].add(parts[0])
    return tables

# Extract table names from query and validate them
def extract_tables(sql: str):
    pattern = r"(?:FROM|JOIN)\s+([a-zA-Z_][a-zA-Z0-9_]*)"
    return set(
        re.findall(
            pattern,
            sql,
            flags=re.IGNORECASE
        )
    )
def validate_tables(sql, schema_dict):
    sql_tables = extract_tables(sql)
    valid_tables = set(schema_dict.keys())
    invalid = sql_tables - valid_tables
    if invalid:
        raise ValueError(
            f"Invalid tables found: {invalid}"
        )
    return True

# Extract column names from query and validate them
def extract_columns(sql: str):
    match = re.search(
        r"SELECT(.*?)FROM",
        sql,
        re.IGNORECASE | re.DOTALL
    )
    if not match:
        return []
    cols = match.group(1)
    columns = []
    for col in cols.split(","):
        col = col.strip()
        if "." in col:
            col = col.split(".")[-1]
        col = col.split()[0]
        if "(" not in col:
            columns.append(col)
    return columns
def validate_columns(sql, schema_dict):
    all_columns = set()
    for cols in schema_dict.values():
        all_columns.update(cols)
    sql_columns = extract_columns(sql)
    invalid = []
    for col in sql_columns:
        if col != "*" and col not in all_columns:
            invalid.append(col)
    if invalid:
        raise ValueError(
            f"Invalid columns found: {invalid}"
        )
    return True