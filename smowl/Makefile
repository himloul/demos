# Makefile for llama.cpp setup and execution

# Variables
REPO_URL = https://github.com/ggerganov/llama.cpp.git
MODEL_URL = https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct-GGUF/resolve/main/smollm2-1.7b-instruct-q4_k_m.gguf
MODEL_FILE = smollm2-1.7b-instruct-q4_k_m.gguf
LLAMA_DIR = llama.cpp
SERVER_BINARY = $(LLAMA_DIR)/llama-server

.PHONY: all clean setup build download run run-cli run-all help

all: setup build download

# Clone the repository if it doesn't exist
setup:
	@if [ ! -d "$(LLAMA_DIR)" ]; then \
		echo "Cloning llama.cpp repository..."; \
		git clone $(REPO_URL) $(LLAMA_DIR); \
		echo "Repository cloned successfully."; \
	else \
		echo "llama.cpp repository already exists. Skipping clone."; \
	fi

# Build the server if the binary doesn't exist
build: setup
	@if [ ! -f "$(SERVER_BINARY)" ]; then \
		echo "Building llama-server..."; \
		$(MAKE) -C $(LLAMA_DIR) llama-server; \
		echo "llama-server built successfully."; \
	else \
		echo "llama-server binary already exists. Skipping build."; \
	fi

# Download the model if it doesn't exist
download: setup
	@if [ ! -f "$(LLAMA_DIR)/models/$(MODEL_FILE)" ]; then \
		echo "Downloading the model..."; \
		wget $(MODEL_URL) -O $(LLAMA_DIR)/models/$(MODEL_FILE) --no-check-certificate; \
		echo "Model downloaded successfully."; \
	else \
		echo "Model file already exists. Skipping download."; \
	fi

# Run the server
run: build download
	@echo "Starting llama-server..."
	cd $(LLAMA_DIR) && ./llama-server -m models/$(MODEL_FILE) -c 2048 --path ./examples/server/public_legacy

run-background: build download
	@echo "Starting llama-server in the background..."
	@cd $(LLAMA_DIR) && ./llama-server -m models/$(MODEL_FILE) -c 2048 --path ./examples/server/public_legacy > server.log 2>&1 &
	@echo "Server started in background. Log file: $(LLAMA_DIR)/server.log"

# Run the CLI chatbot
run-cli: build download
	@echo "Starting CLI chatbot..."
	python app.py

# Target to run both server and CLI
run-all: run-background
	@echo "Waiting for server to start..."
	@sleep 10  # Adjust this delay as needed
	@$(MAKE) run-cli

# Stop the background server
stop-server:
	@echo "Stopping llama-server..."
	@-pkill -f llama-server
	@echo "Server stopped."

# Clean up
clean:
	@echo "Cleaning up..."
	rm -rf $(LLAMA_DIR)
	rm -f $(MODEL_FILE)
	@echo "Cleanup complete."

help:
	@echo "Available targets:"
	@echo "all       - Setup, build, and download (does not run anything)"
	@echo "  setup     - Clone the llama.cpp repository (if not exists)"
	@echo "  build     - Build the llama-server (if not built)"
	@echo "  download  - Download the model (if not exists)"
	@echo "  run       - Run the llama-server"
	@echo "  run-cli   - Run the CLI chatbot"
	@echo "  run-all   - Run both llama-server and CLI chatbot"
	@echo "  clean     - Remove llama.cpp directory and downloaded model"
	@echo "  help      - Show this help message"
