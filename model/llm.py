from dotenv import load_dotenv
load_dotenv()

from decouple import config
OPENROUTER_API_KEY = config("OPENROUTER_API_KEY")

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
    model_name="openai/gpt-oss-120b:free"
)