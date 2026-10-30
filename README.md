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

The default models for the application are `gemma4:e4b` and `gemma3:12b`. For machines with less than 16Gb of VRAM, `gemma4:e2b` can be used. Some of the notebooks use `gemma4:e2b`by default.

**Download models:**
```
ollama pull gemma4:e2b
ollama pull gemma4:e4b
ollama pull gemma3:12b
```

### Running

Make sure that uv is up to date and that the packages are synchronized (make sure the correct path is used in the cd command):
```
cd c:\dev\ai\tiny-agent
uv sync
```

If you don't want to use the default models (`gemma4:e4b` and `gemma3:12b`), copy `.env.example` to `.env` and set the models there.

Run the agent by calling:
```
uv run python -m tiny_agent.main
```
