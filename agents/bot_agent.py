import os
from openai import OpenAI
from chat.ai.tools.web_tool import (
    get_function_internet_search,
    get_tool_internet_search,
)
from .common import query_base_agent

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def query_bot_agent(query):
    functions = {"get_tool_internet_search": get_tool_internet_search}
    messages = [
        {
            "role": "system",
            "content": "You are a bot that provides answers to questions. Please respond to questions within 500 characters.",
        },
        {"role": "user", "content": query},
    ]
    tools = [get_function_internet_search()]
    return query_base_agent(messages, tools, functions)
