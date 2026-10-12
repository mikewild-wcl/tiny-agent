# main.py
from .tiny_agent import TinyAgent
from .llm import LLM
from dotenv import load_dotenv
from os import getenv

def main() -> None:
    load_dotenv()
    model_name = getenv("REASONING_MODEL", "gemma4:e4b")

    llm = LLM(model=model_name)
    agent = TinyAgent(llm)
    result = agent.run("What is 2 + 2?")
    print(result)

if __name__ == "__main__":
    main()