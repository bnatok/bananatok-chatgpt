import logging
from langchain_community.utilities import SerpAPIWrapper

logger = logging.getLogger("logger")


def get_tool_internet_search(query):
    """인터넷 검색결과 반환"""
    try:
        logger.info("Tool Internet search: {}".format(query[:10]))
        params = {"engine": "google", "gl": "kr"}
        search = SerpAPIWrapper(params=params)
        return search.run(query)
    except:
        return ""


def get_function_internet_search():
    return {
        "type": "function",
        "function": {
            "name": "get_tool_internet_search",
            "description": "Get information on recent events from the web.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query to use. For example: 'Latest news on Nvidia stock performance'",
                    },
                },
                "required": ["query"],
            },
        },
    }
