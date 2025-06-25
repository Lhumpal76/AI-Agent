import os
import langchain
import langsmith
import getpass
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chat_models import init_chat_model
from rich import print
from rich.pretty import Pretty
from langgraph.prebuilt import create_react_agent
import langchain
langchain.debug = True

import config
from tools import tools

"""AI agents utilize LLMs to perform tasks autonomously. The LLM is the core component that reasons"""

# search_results = tools["search"].invoke("What is the weather in SF")
# print(Pretty(search_results))

model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

print("\n[bold green]Registered Tools:[/bold green]")
for tool in tools:
    print(f"[cyan]{tool.name}[/cyan]: {tool.description}")
    
agent_executor = create_react_agent(model, tools)

input_message = {"role": "user", "content": "Hi!"}
response = agent_executor.invoke({"messages": [input_message]})

input_message = {"role": "user", "content": "Search for the weather in Catawissa Missouri"}
response = agent_executor.invoke({"messages": [input_message]})

for message in response["messages"]:
    message.pretty_print()