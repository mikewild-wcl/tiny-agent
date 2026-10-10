# main.py
from TinyAgent import TinyAgent

def main() -> None:
    agent = TinyAgent()
    result = agent.run("What is 2 + 2?")
    print(result)

if __name__ == "__main__":
    main()