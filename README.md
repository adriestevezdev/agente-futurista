# Agente Futurista

A modern AI agent that searches through your documents to provide accurate, document-based answers.

## Features

- **Document-based answers**: Gets information directly from your uploaded documents
- **Vector search**: Uses OpenAI's vector store for efficient semantic search
- **Futuristic UI**: Clean, responsive chat interface
- **Easy setup**: Simple configuration process

## Setup Instructions

### Prerequisites

- Python 3.7+
- OpenAI API key
- OpenAI Vector Store with your documents uploaded

### Step 1: Create Your Vector Store

1. Go to the [OpenAI platform](https://platform.openai.com/)
2. Navigate to "Vector stores" in the left sidebar
3. Click "Create vector store"
4. Name your vector store (e.g., "MyDocuments")
5. Upload your documents (PDF, DOCX, TXT, etc.)
6. Wait for the files to be processed
7. Once created, copy the vector store ID for use in the setup

### Step 2: Install and Configure

1. Clone or download this repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the setup script:
   ```
   python setup.py
   ```
5. Enter your OpenAI API key and Vector Store ID when prompted

### Step 3: Run the Application

1. Start the application:
   ```
   python app.py
   ```
2. Open your browser and go to `http://127.0.0.1:5000`
3. Start chatting with Agente Futurista!

## How to Use

Simply ask questions about the content in your documents. For example:
- "What are the key points in the quarterly report?"
- "Summarize the information about project timelines"
- "Find all mentions of budget constraints in my documents"

The agent will search through your documents and provide relevant answers based on what it finds.

## Troubleshooting

- **API Key Error**: Make sure your OpenAI API key is correct and has access to the necessary APIs
- **Vector Store Error**: Verify your Vector Store ID is correct and that your documents are properly uploaded
- **Missing Documents**: If the agent can't find information, ensure your documents are processed in the vector store

## Customization

You can customize the agent's behavior by modifying the instructions in `app.py`:

```python
agent = Agent(
    name="Agente Futurista",
    instructions="""
    Your custom instructions here...
    """,
    # Other settings...
)
```

## License

This project is open source and available under the MIT License.
