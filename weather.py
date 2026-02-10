from mcp.server.fastmcp import FastMCP

mcp = FastMCP("math-server")

@mcp.tool()
def weather(city: str) -> str:
    """Get the weather for a city."""
    return f"The weather is sunny."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")