import requests

DATA_URL = "https://raw.githubusercontent.com/bnatok/bananatok-chatgpt/main/data.txt"


def get_tool_description_bananatok():
    """문서 내용 반환"""
    print("Tool description bananatok...")
    response = requests.get(DATA_URL)
    return response.text


def get_function_description_bananatok():
    return {
        "type": "function",
        "function": {
            "name": "get_tool_description_bananatok",
            "description": "Answers to questions about 바나나톡(Bananatok, BNA). For example, Please explain about Bananatok.",
            "parameters": {
                "type": "object",
                "properties": {},
            },
        },
    }
