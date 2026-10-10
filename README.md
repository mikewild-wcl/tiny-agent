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

Initialise the workspace - you can use the -p option to specify the Python version, e.g. 3.13:
```
uv init -p 3.15
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

