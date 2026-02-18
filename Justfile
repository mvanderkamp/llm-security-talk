# Indirect Prompt Injection Demo
# Usage: just --list

model := "llama3.2:3b"

# Show available commands
default:
    @just --list

# Start Ollama, pull the model, and drop into the agent shell
run: up pull
    docker compose run --rm agent bash -c "\
        pip install --quiet requests && \
        echo '✅ Ready. Run: python exploit_agent.py documents' && \
        exec bash"

# Start Ollama in the background and wait for it to be healthy
up:
    docker compose up -d ollama
    @echo "⏳ Waiting for Ollama to be ready..."
    @until docker compose exec ollama ollama list > /dev/null 2>&1; do \
        sleep 1; \
    done
    @echo "🟢 Ollama is ready."

# Pull the model (skips if already present)
pull:
    @if docker compose exec ollama ollama list | grep -q "{{ model }}"; then \
        echo "✅ Model {{ model }} already pulled."; \
    else \
        echo "⬇️  Pulling {{ model }}..."; \
        docker compose exec ollama ollama pull {{ model }}; \
    fi

# Run the demo directly (no interactive shell)
demo: up pull
    docker compose run --rm agent bash -c "\
        pip install --quiet requests && \
        python exploit_agent.py documents"

# Stop all containers
down:
    docker compose down

# Stop all containers and delete the model cache
clean:
    docker compose down -v
    @echo "🗑️  Removed containers and Ollama model cache."

# Tail Ollama server logs
logs:
    docker compose logs -f ollama
