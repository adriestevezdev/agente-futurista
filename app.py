from agents import Agent, Runner, FileSearchTool
from flask import Flask, request, jsonify, render_template
import os
import asyncio
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get configuration from environment
api_key = os.getenv("OPENAI_API_KEY")
vector_store_id = os.getenv("VECTOR_STORE_ID")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables")
if not vector_store_id:
    raise ValueError("VECTOR_STORE_ID not found in environment variables")

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = api_key

# Create the agent with file search capability
agent = Agent(
    name="Agente Futurista",
    instructions="""
    You are Agente Futurista, an AI assistant that specializes in searching through documents and providing accurate answers.
    Always respond in a helpful, knowledgeable and slightly futuristic tone.
    Base your answers on the documents you can search through, and if you don't find relevant information, acknowledge that clearly.
    When appropriate, cite the specific document or section where you found the information.
    """,
    model="gpt-4o", # Using a capable model for better document understanding
    tools=[
        FileSearchTool(
            max_num_results=5,  # Return up to 5 relevant chunks
            vector_store_ids=[vector_store_id],
        )
    ],
)

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    
    # Create and set a new event loop for this thread
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        # Run the agent with the user's input
        result = Runner.run_sync(agent, user_input)
        
        return jsonify({
            'response': result.final_output
        })
    finally:
        # Clean up the event loop
        loop.close()

if __name__ == '__main__':
    app.run(debug=True)
