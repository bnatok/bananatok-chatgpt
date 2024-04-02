import os
from agents.quiz_agent import query_quiz_agent
from agents.bot_agent import query_bot_agent

os.environ["OPENAI_API_KEY"] = ""
os.environ["GOOGLE_CSE_ID"] = ""
os.environ["GOOGLE_API_KEY"] = ""

if __name__ == "__main__":
    # Quiz AI with internet access
    result_str = query_quiz_agent(
        "Create a quiz related to the most recent blockchain issue"
    )
    result_str = result_str.replace("```json\n", "", 1).strip("`")
    print(f"[QUIZ]: {result_str}")
    # Bot AI using data.txt
    result_str = query_bot_agent("Tell me about bananatok")
    # Bot AI with stock price api
    result_str = query_bot_agent("What is the stock price of Tesla?")
    print(f"[BOT]: {result_str}")
