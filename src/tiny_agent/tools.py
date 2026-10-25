from typing import Callable

class Tools:
    """Tool repository for the agent."""

    def __init__(self, requires_approval: list[str] = []):
        self.registry = {}
        self.requires_approval = requires_approval

    def add_tool(self, name: str, func: Callable, description: str = "") -> None:
        """Register a tool in the repository.
        
        Args:
            name (str): The name of the tool.
            func (Callable): The function implementing the tool.
            description (str, optional): A brief description of the tool. Defaults to "".
        """
        self.registry[name] = {"func": func, "description": description}

    # def get_tool(self, name: str) -> Callable | None:
    #     """Get a tool by name"""
    #     return self.registry.get(name)

    @property
    def schemas(self) -> None:
        """Used only for native tool calling."""
        return None