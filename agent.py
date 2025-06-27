import os
import langchain
import langsmith
import getpass
import os
from google import genai
from colorama import Fore, Style, init


import config
from tools import tools
from react_agent_response import react_agent_response
from response_parser import parse
from search_parser import parse_search_result

# query = input("User: ")
query = "What is the weather like in Catawissa Missouri right now?"

llm_client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])


# ask agent to ReaAct to the query
# and return a JSON object with the question, reasoning, and action
# if json is invalid, retry up to 3 times
# if action is to invoke a tool, invoke the tool and return the result 
max_retries = 3
attempt = 0

while attempt < max_retries:
    response = react_agent_response(llm_client, query, tools)
    try:
        parsed_output = parse(response)
        # Successfully parsed the response
        print(f"{Fore.BLUE}Reasoning: {parsed_output.reasoning}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Action: {parsed_output.action}{Style.RESET_ALL}")
        break 
    except ValueError as e:
        attempt += 1
else:
    # all attempts failed
    raise RuntimeError(f"Failed to parse response after {max_retries} attempts.")



#3. invoke tools
if parsed_output.action.tool is not None:
    tool_name = parsed_output.action.tool
    tool_input = parsed_output.action.input

    if tool_name in tools:
        tool_func = tools[tool_name]["func"]
        tool_result = tool_func.invoke(tool_input)

        summary = parse_search_result(tool_result)
        print(f"{Fore.YELLOW}{summary}{Style.RESET_ALL}")
    else:
        raise ValueError(f"Tool '{tool_name}' not found in available tools.")
    
#5. invoke llm with tool results

#6. return llm response