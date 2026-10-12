from .models import Response, Step, Trajectory
from .llm import LLM

class TinyAgent:
    """A minimal agent framework,"""

    def __init__(self, llm: LLM):
        self.llm = llm
        self.memory = None
        self.tools = None
        self.planner = None
        self.trajectory = Trajectory()

    def run(self, task: str):
        """Run the agent on a task."""
        self.trajectory.initialize(task)
        print(f"Running task: {task}")
        return self._step(task)

    def _step(self, task: str):
        """Perform a single step."""
        messages = [{"role": "user", "content": task}]
        response = self.llm.generate(messages)
        self.trajectory.add(response)
        return response.content

    def _execute_action(self, action: str) -> str | None:
        """Perform a tool action."""
        return f"Executed action: {action}"
