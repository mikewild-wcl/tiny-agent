from .models import Response, Step, Trajectory
from .llm import LLM
from .memory import Memory
from .tools import Tools

class TinyAgent:
    """A minimal agent framework,"""

    def __init__(self, llm: LLM, memory: Memory | None = None, tools: Tools | None = None):
        print("Initializing TinyAgent")
        self.llm = llm
        self.memory = memory
        self.tools = tools
        self.planner = None
        self.trajectory = Trajectory()

    def run(self, task: str):
        """Run the agent on a task."""
        if self.memory:
            self.memory.add("user", task)
        self.trajectory.initialize(task)
        print(f"Running task: {task}")
        #print(f"Memory state: {self.memory.get_messages()}")
        return self._step(task)

    def _step(self, task: str):
        """Perform a single step."""
        if self.memory:
            response = self.llm.generate(self.memory.get_messages())
            self.memory.add("assistant", response.content)
        else:
            # Allow momory-free operation using code from the original version of TinyAgent
            response = self.llm.generate( [{"role": "user", "content": task}])

        self.trajectory.add(response)
        return response.content

    def _execute_action(self, action: str) -> str | None:
        """Perform a tool action."""
        return f"Executed action: {action}"
