from agents import Agent, FileSearchTool

def create_agent(vector_store_id):
    """Create the Agente Futurista that searches through documents."""
    
    # Create the agent with specific instructions
    agent = Agent(
        name="Agente Futurista",
        instructions="""
        You are 'Agente Futurista', an advanced AI assistant specialized in retrieving and analyzing information 
        from the user's documents. 
        
        When responding to queries:
        1. Use the file search tool to find relevant information in the user's documents
        2. Provide clear, accurate answers based on the document content
        3. If information is not found in the documents, politely indicate this
        4. Always cite the source document when providing information
        5. Respond in a friendly, helpful tone
        
        Your goal is to be the user's knowledgeable companion for navigating their document repository.
        """,
        tools=[
            FileSearchTool(
                vector_store_ids=[vector_store_id],
                max_num_results=3,
                description="Search through user documents to find relevant information",
            )
        ],
    )
    
    return agent
