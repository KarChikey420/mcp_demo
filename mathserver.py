import os

from mcp.server.fastmcp import FastMCP

port = int(os.getenv("PORT", "8000"))
mcp = FastMCP("math-server", port=port)

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return a * b

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
