from tools.web_tool import (
    get_function_internet_search,
    get_tool_internet_search,
)
from tools.bananatok_tool import (
    get_function_description_bananatok,
    get_tool_description_bananatok,
)
from .common import query_base_agent


def query_bot_agent(query):
    functions = {
        "get_tool_internet_search": get_tool_internet_search,
        "get_tool_description_bananatok": get_tool_description_bananatok,
    }
    messages = [
        {
            "role": "system",
            "content": "You are a bot that provides answers to questions. Please respond to questions within 500 characters.",
        },
        {"role": "user", "content": query},
    ]
    tools = [get_function_internet_search(), get_function_description_bananatok()]
    return query_base_agent(messages, tools, functions)
