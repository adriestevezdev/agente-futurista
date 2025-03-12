#!/usr/bin/env python
import os
import sys

def setup():
    print("\n" + "="*50)
    print("  AGENTE FUTURISTA SETUP")
    print("="*50 + "\n")
    
    # Get OpenAI API key
    api_key = input("Enter your OpenAI API key: ").strip()
    if not api_key:
        print("Error: API key is required.")
        sys.exit(1)
    
    # Get Vector Store ID
    vector_store_id = input("Enter your OpenAI Vector Store ID: ").strip()
    if not vector_store_id:
        print("Error: Vector Store ID is required.")
        sys.exit(1)
    
    # Create .env file
    with open('.env', 'w') as f:
        f.write(f"OPENAI_API_KEY={api_key}\n")
        f.write(f"VECTOR_STORE_ID={vector_store_id}\n")
    
    print("\n✅ Setup complete!\n")
    print("To start the application, run:")
    print("  python app.py\n")
    print("Then open your browser at: http://127.0.0.1:5000")
    print("="*50 + "\n")

if __name__ == "__main__":
    setup()
