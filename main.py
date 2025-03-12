import os
import asyncio
from dotenv import load_dotenv
from agents import Runner, set_default_openai_key
from agent import create_agent

# Load environment variables
load_dotenv()

# Set OpenAI API key
set_default_openai_key(os.getenv("OPENAI_API_KEY"))

async def main():
    # Create agent with the vector store ID from environment variable
    vector_store_id = os.getenv("VECTOR_STORE_ID")
    if not vector_store_id:
        raise ValueError("VECTOR_STORE_ID environment variable not set")
    
    agent = create_agent(vector_store_id)
    
    print("🤖 Agente Futurista is ready! Type 'exit' to quit.")
    
    # Simple command-line chat loop
    while True:
        user_input = input("\n👤 You: ")
        if user_input.lower() == "exit":
            break
        
        # Run the agent with the user's query
        result = await Runner.run(agent, user_input)
        
        print(f"\n🤖 Agente Futurista: {result.final_output}")

if __name__ == "__main__":
    asyncio.run(main())
