from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit

def create_sql_tools(db, llm):
    toolkit = SQLDatabaseToolkit(
        db=db,
        llm=llm
    )

    return {
        tool.name: tool
        for tool in toolkit.get_tools()
    }