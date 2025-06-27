import os
import langchain
import langsmith
import getpass
import os
from google import genai

import config
from tools import tools
from react_agent_response import react_agent_response

# query = input("User: ")
query = "What is the total if I add the current temeperature in SF to 1000?"

# search_results = tools["search"].invoke("What is the weather in SF")
# print(search_results)

llm_client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

response = react_agent_response(llm_client, query, tools)

#1. parse response for tools
#2. iterate for correct json
#3. invoke tools
#4. parse tool results
#5. invoke llm with tool results

#6. return llm response