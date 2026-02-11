import os
import asyncio
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent

load_dotenv()

GROQ_API = os.getenv("GroqAPI")

async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "url":"http://127.0.0.1:8001/mcp",
                "transport":"streamable_http"
            },
            
            "weather":{
                "url":"http://127.0.0.1:8000/mcp",
                "transport":"streamable_http"
            }
        }
    )

    tools = await client.get_tools()
    model = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API)
    agent = create_agent(model, tools=tools)
    
    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What's 5 plus 5?"}]}
    )
    print("Math response:", math_response["messages"][-1].content)

    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What's the weather in Paris?"}]}
    )
    print("Weather response:", weather_response["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())
