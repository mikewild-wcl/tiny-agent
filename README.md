# tiny-agent

Implementation of TinyAgent from An Illustrated Guide to AI Agents. Book code is [here](https://github.com/HandsOnLLM/An-Illustrated-Guide-To-AI-Agents).

## Setup

This requires uv and ollama.

If uv is not installed:
```
winget install astral-sh.uv
```

If Ollama is not installed:
```
winget install --id=Ollama.Ollama -e
```

Initialise the workspace - you can use the -p option to specify the Python version, e.g. 3.14:
```
uv init -p 3.14
```

In the initial version there was no need to add packages, but to set up the virtual environment just run
```
uv sync
```

You can then open in VS Code.
```
code .
```

Make sure the Python support extension is installed. Select the python interpreter - ctrl-shift-P -> Python:Select interpreter, and select the virtual environment matching .venv.

### Ollama models

Download models:
```
ollama pull gemma4:e4b
ollama pull gemma3:12b
```

### Running

Make sure that uv is up to date and that the packages are synchronized (make sure the correct path is used in the cd command):
```
cd c:\dev\ai\tiny-agent
uv sync
```

Run the agent by calling:
```
uv run python -m tiny_agent.main
```
