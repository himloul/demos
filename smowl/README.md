# Smowl 🦉

Smowl is a lightweight, on-device chatbot using SmolLM2-1.7B-Instruct model, designed to run efficiently on CPU.

## Features

- Starts Function calling with SmolLM2-1.7B-Instruct model.
- Runs entirely on-device, using only CPU
- No Python dependencies required (only `requests`)
- Uses only llama.cpp binaries
- Quick start with a single command

## Quick start

To set up and run the CLI chatbot, use the following command:

```shell
make run-all
```

This command will: Set up the llama.cpp binaries, Download the model from HuggingFace, Start the server, then launch the CLI chatbot

The chatbot interacts with user queries using a set of predefined tools specified in the [functions.json](./src/functions.json) file.

### System requirements

- CPU-only setup (no GPU required)
- Sufficient RAM to run the 1.7B parameter model

**Aknowledgments**

This project was made possible thanks to the outstanding work of the llama.cpp project, and HuggingFace for releasing the SmolLM2 models.

## Todo

- [] Validate the output when using function calling.
