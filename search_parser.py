def parse_search_result(tool_result: dict) -> str:
    """
    Parses the search tool's result dictionary and returns a nicely formatted string summary.
    
    Expected tool_result structure:
    {
        'query': str,
        'follow_up_questions': Optional,
        'answer': Optional,
        'images': List,
        'results': List[{
            'title': str,
            'url': str,
            'content': str,
            ...
        }],
        ...
    }
    """
    if not tool_result or 'results' not in tool_result:
        return "No search results found."

    results = tool_result['results']
    if not results:
        return "No search results found."

    summary_lines = []

    # Show top 3 results with title, url, and a short snippet
    for i, item in enumerate(results, 1):
        title = item.get('title', 'No title')
        url = item.get('url', 'No url')
        content = item.get('content', '')

        summary_lines.append(f"{i}. {content}")

    return summary_lines
