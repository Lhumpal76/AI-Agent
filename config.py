import os
import getpass

def load_secrets(filepath="secrets.txt"):
    secrets = {}
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, value = line.split("=", 1)
            secrets[key.strip()] = value.strip()
    return secrets

secrets = load_secrets()

os.environ["LANGSMITH_TRACING"] = "true"

# if "LANGSMITH_API_KEY" not in os.environ:
#     os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your Langsmith API key: ")

# used for gemini 
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = secrets.get("GOOGLE_API_KEY")
    if not os.environ["GOOGLE_API_KEY"]:
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")

#used for LLM search engine
if "TAVILY_API_KEY" not in os.environ:
    os.environ["TAVILY_API_KEY"] = secrets.get("TAVILY_API_KEY")
    if not os.environ["TAVILY_API_KEY"]:
        os.environ["TAVILY_API_KEY"] = getpass.getpass("Enter your Tavily API key: ")