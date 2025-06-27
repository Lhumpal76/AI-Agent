from langchain_tavily import TavilySearch
tools = {}

class ToolEntry:
    def __init__(self, name, description, func):
        self.name = name
        self.description = description
        self.func = func


search = TavilySearch(
    max_results=5,
    topic="general",
    # include_answer=False,
    # include_raw_content=False,
    # include_images=False,
    # include_image_descriptions=False,
    # search_depth="basic",
    # time_range="day",
    # include_domains=None,
    # exclude_domains=None
)

def calculator(expression: str) -> str:
    """
    Toy calculator: evaluates basic math expressions like '2 + 3 * 4'.
    Only supports +, -, *, /, and parentheses.
    """
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

# Add a new tool called "search"
tools["search"] = {
    "description": "Useful for finding current information.",
    "func": search,
}

# Add a new tool called "search"
tools["calculator"] = {
    "description": "Useful for performing calculations.",
    "func": calculator,
}