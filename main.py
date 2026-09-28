from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_ollama import ChatOllama

from tools import tools


# LOAD ENVIRONMENT VARIABLES

load_dotenv()

# OLLAMA MODEL

llm = ChatOllama(
    model="qwen3:4b",
    temperature=0.7,
    num_predict=2000,
)


# SYSTEM PROMPT

system_prompt = """
You are a research assistant.

Your job is to help the user research a topic and provide
accurate, useful and well-organized information.

You have access to the following tools:

1. search_web
   - Searches the internet.
   - Use it when current information or web research is needed.

2. wikipedia
   - Searches Wikipedia.
   - Use it when general background information is useful.

3. save_to_txt
   - Saves research results to a text file.
   - Use it when the user asks you to save the research.

Research process:

1. Understand the user's question.
2. Decide whether external research is necessary.
3. Use the appropriate tools.
4. Review the information returned by the tools.
5. Produce a clear and useful answer.
6. If the user asks you to save the research, use save_to_txt.

Do not use tools unnecessarily.
"""


# CREATE AGENT

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=system_prompt,
)

# USER INPUT

query = input("\nWhat can I help you research? ")


# RUN AGENT

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": query,
            }
        ]
    }
)


# DISPLAY RESPONSE

print("\n" + "=" * 60)
print("RESEARCH RESULT")
print("=" * 60)


final_message = result["messages"][-1]

print(final_message.content)

print("=" * 60)

