# ollama_web

Minimal Flask web interface for chatting with Ollama models installed on your server. The app shows the latest model response and lets you select a model manually or enable auto-selection.

## Features
- Simple web UI with a form input and on-screen response display.
- Model selection by name or automatic selection of the first available model.
- Direct integration with Ollama via `python-ollama`.

## Requirements
- Python 3.9+
- Ollama running on the same server where the app is hosted
- Python dependencies:
  - `flask`
  - `ollama`

## Installation
1. Clone the project.
2. Move to the cloned project ```cd ollama-web```
3. Move to the buil directory ``` cd build ```
4. Build the package ``` makepkg -si ```
5. After the installation use the ``` ollama-web``` to run the programm

## Usage
1. Open your browser at `http://localhost:5000`.
2. Enter the model name (e.g., `llama3`) or enable **Auto choose model** to use the first available model.
3. Enter your prompt and click **Send**.
4. The model response will appear in the **Chat** section.

## Main endpoints
- `GET /` renders the home page.
- `POST /input` sends a prompt to the model and updates the displayed response.

## Error codes
If the app cannot select a valid model, the backend returns an error message:
- **401**: unable to retrieve any model from Ollama.
- **402**: requested model not found among available models.

## Notes
- Make sure Ollama is running and at least one model has been pulled.

## To-DO
- [ ] Improve UI
- [x] Chat history
- [ ] Multi media file support
- [ ] Save Old Chat
- [ ] Transform this project in an AUR packet
