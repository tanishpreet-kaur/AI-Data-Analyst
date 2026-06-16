import re

# remove code block markers
def clean_sql(sql: str) -> str:
    sql = re.sub(r"```sql", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"```", "", sql)
    return sql.strip()

# check for forbidden SQL keywords
FORBIDDEN = [
    "DROP",
    "DELETE",
    "UPDATE",
    "INSERT",
    "ALTER",
    "TRUNCATE"
]
def validate_sql(sql):
    sql_upper = sql.upper()
    for keyword in FORBIDDEN:
        if keyword in sql_upper:
            raise ValueError(
                f"Forbidden SQL detected: {keyword}"
            )
    return True