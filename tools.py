
from datetime import datetime

from langchain.tools import tool
from langchain_community.tools import (
    DuckDuckGoSearchRun,
    WikipediaQueryRun,
)
from langchain_community.utilities import WikipediaAPIWrapper


# SAVE RESEARCH TO FILE

@tool
def save_to_txt(data: str, filename: str = "research_output.txt") -> str:
    """
    Save research results to a text file.

    Use this tool when the user asks to save research results.
    """

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    formatted_text = (
        "--- Research Output ---\n"
        f"Timestamp: {timestamp}\n\n"
        f"{data}\n\n"
    )

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Research successfully saved to {filename}"


# WEB SEARCH

search = DuckDuckGoSearchRun()


@tool
def search_web(query: str) -> str:
    """
    Search the internet for information.

    Use this tool when current information or external
    research is required.
    """

    try:
        return search.run(query)

    except Exception as e:
        return (
            f"Web search failed. Error: {str(e)}"
        )


# WIKIPEDIA

api_wrapper = WikipediaAPIWrapper(
    top_k_results=1,
    doc_content_chars_max=2000,
)

wiki = WikipediaQueryRun(
    api_wrapper=api_wrapper
)


@tool
def search_wikipedia(query: str) -> str:
    """
    Search Wikipedia for background information.

    Use this tool when Wikipedia is useful for researching
    a topic.
    """

    try:
        return wiki.run(query)

    except Exception as e:
        return (
            f"Wikipedia search failed. "
            f"Please use the web search tool instead. "
            f"Error: {str(e)}"
        )

# AVAILABLE TOOLS

tools = [
    search_web,
    search_wikipedia,
    save_to_txt,
]
