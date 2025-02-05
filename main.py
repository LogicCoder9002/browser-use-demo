import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from pydantic import SecretStr
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
print("Loaded API Key:", api_key)

# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))

# Create agent with the model
agent = Agent(
    task="Search for 'latest AI trends 2024' on Google and summarize the top result.",
    llm=llm
)

# Run the agent asynchronously using asyncio.run
result = asyncio.run(agent.run())
print("Agent Result:", result)
