from django.utils import timezone
from chat.ai.tools.web_tool import (
    get_function_internet_search,
    get_tool_internet_search,
)
from chat.ai.tools.bananatok_tool import (
    get_function_description_bananatok,
    get_tool_description_bananatok,
)
from .common import query_base_agent


def query_quiz_agent(query):
    functions = {
        "get_tool_internet_search": get_tool_internet_search,
        "get_tool_description_bananatok": get_tool_description_bananatok,
    }
    messages = [
        {
            "role": "system",
            "content": f"Today's date is {timezone.localtime().strftime('%Y-%m-%d')}.",
        },
        {
            "role": "system",
            "content": "You are a bot that generates a new quiz every day. Please return it in the following JSON format: {quiz: question, choices: [option1, option2, option3, option4], answer: the zero-based index of the correct answer}. The quiz must be presented in this format. There must always be one correct answer, and ensure that the quiz content is not duplicated.",
        },
        {
            "role": "user",
            "content": query,
        },
    ]
    tools = [get_function_internet_search(), get_function_description_bananatok()]
    return query_base_agent(messages, tools, functions)
