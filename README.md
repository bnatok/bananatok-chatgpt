# bananatok-chatgpt
This repository contains Python code for generating quizzes and answering questions with ChatGPT.
Python 3.9 or higher is recommended.

## Description
- This code integrates the [ChatGPT API](https://platform.openai.com/docs/introduction) and Tool.
- Based on the requirement, it reads content from a web browser using [SERP API](https://serpapi.com/) or fetches specific documents (data.txt).
- Subsequently, it generates answers derived from that content.
- Examples are implemented in `main.py` and consist of a bot that automatically generates quizzes in JSON format and responds to Bananatok-related questions.

## Usage
1. Install the required packages:
```bash
$ pip install -r requirements.txt
```

2. Set environment variables in `main.py`:
```python
os.environ["OPENAI_API_KEY"] = "<Your-OpenAI-API-Key>"
os.environ["SERPAPI_API_KEY"] = "<Your-SERPAPI-API-Key>"
```

3. Execute the example code:
```bash
$ python main.py
```
