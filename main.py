import os
from agents.quiz_agent import query_quiz_agent
from agents.bot_agent import query_bot_agent

os.environ["OPENAI_API_KEY"] = ""
os.environ["SERPAPI_API_KEY"] = ""

if __name__ == "__main__":
    # Quiz AI with internet access
    result_str = query_quiz_agent(
        "Create a quiz related to the most recent blockchain issue"
    )
    result_str = result_str.replace("```json\n", "", 1).strip("`")
    print(f"[QUIZ]: {result_str}")
    # Bot AI using data.txt
    result_str = query_bot_agent("Tell me about bananatok")
    print(f"[BOT]: {result_str}")
