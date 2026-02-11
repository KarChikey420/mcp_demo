import os

from mcp.server.fastmcp import FastMCP

port = int(os.getenv("PORT", "8000"))
mcp = FastMCP("weather-server", port=port)

@mcp.tool()
def weather(city: str) -> str:
    """Get the weather for a city."""
    return f"The weather is sunny."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
