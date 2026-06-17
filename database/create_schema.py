from langfuse import observe

@observe(name="get_schema")
def get_schema(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type='table'
            AND name NOT LIKE 'sqlite_%'
            ORDER BY name
        """)

        tables = cursor.fetchall()
        schema_parts = []

        for (table_name,) in tables:
            schema_parts.append(f"\nTABLE {table_name}")
            cursor.execute(
                f"PRAGMA table_info('{table_name}')"
            )
            columns = cursor.fetchall()

            for col in columns:
                column_name = col[1]
                datatype = col[2]
                schema_parts.append(
                    f"  {column_name} {datatype}"
                )

            cursor.execute(
                f"PRAGMA foreign_key_list('{table_name}')"
            )
            foreign_keys = cursor.fetchall()

            if foreign_keys:
                schema_parts.append("  FOREIGN KEYS:")
                
                for fk in foreign_keys:
                    schema_parts.append(
                        f"    {fk[3]} -> {fk[2]}.{fk[4]}"
                    )

        return "\n".join(schema_parts)

    except Exception as e:
        raise RuntimeError(
            f"Failed to load schema: {str(e)}"
        )