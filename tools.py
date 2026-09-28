# from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
# from langchain_community.utilities import WikipediaAPIWrapper
# from langchain.tools import Tool
# from datetime import datetime

# def save_to_txt(data: str, filename: str = "research_output.txt"):
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

#     with open(filename, "a", encoding="utf-8") as f:
#         f.write(formatted_text)
    
#     return f"Data successfully saved to {filename}"

# save_tool = Tool(
#     name="save_text_to_file",
#     func=save_to_txt,
#     description="Saves structured research data to a text file.",
# )

# search = DuckDuckGoSearchRun()
# search_tool = Tool(
#     name="search",
#     func=search.run,
#     description="Search the web for information",
# )

# api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
# wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

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

    Use this tool when the user wants the research results
    saved to a file.
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


# WEB SEARCH TOOL

search = DuckDuckGoSearchRun()


@tool
def search_web(query: str) -> str:
    """
    Search the internet for current or general information.

    Use this tool when the user asks about a topic that requires
    web research or information that may not be available from
    the model's existing knowledge.
    """

    return search.run(query)



# WIKIPEDIA TOOL

api_wrapper = WikipediaAPIWrapper(
    top_k_results=1,
    doc_content_chars_max=2000,
)

wiki = WikipediaQueryRun(
    api_wrapper=api_wrapper
)


# Export the Wikipedia tool directly because it is already
# a LangChain tool.
wiki_tool = wiki


# TOOL LIST

tools = [
    search_web,
    wiki_tool,
    save_to_txt,
]


