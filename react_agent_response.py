import os
from google.genai.types import GenerateContentConfig

def react_agent_response(llm_client, query, tools):
    """
    Function to handle the ReAct.
    
    Args:
        llm: The language model instance.
        query: The user query to process.
        tools: A dictionary of tools available for the agent to use.
        
    Returns:
        The response from the AI agent.
    """


    tools_str = "\n".join(f"- {name}: {info['description']}" for name, info in tools.items())

    react_prompt = f"""
    You are an intelligent AI agent that solves user questions by reasoning step-by-step and using tools when needed.

    You have access to the following tools:
    {tools_str}

    For each step select exactly one tool to use.

    When given a question, follow this format exactly. Your full output must be a single JSON object like this:

    {{
        "question": "restate the user's question",
        "reasoning": "explain your thought process step-by-step",
        "action": {{
            "tool": "tool name or null",
            "input": "tool input or null"
        }}
    }}

    Examples:

    Input:
    What is the capital of France?

    Output:
    {{
        "question": "What is the capital of France?",
        "reasoning": "France is a country in Europe and I know its capital is Paris.",
        "action": {{
            "tool": null,
            "input": null
        }}
    }}

    Input:
    What is the weather in New York City today?

    Output:
    {{
        "question": "What is the weather in New York City today?",
        "reasoning": "I do not have real-time information, so I will use the search tool to look it up.",
        "action": {{
            "tool": "search",
            "input": "What is the weather in New York City today?"
        }}
    }}

    Now answer this:

    Input:
    {query}
    """
    
    response = llm_client.models.generate_content(
        model="gemini-2.0-flash",
        contents=react_prompt,
        config=GenerateContentConfig(
            system_instruction=["You are a helpful AI assistant who reasons step by step and uses tools when appropriate."],
            max_output_tokens=250,
            temperature=0.5
        ),
    )

    return response.candidates[0].content.parts[0].text
