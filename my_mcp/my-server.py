from mcp.server.fastmcp import FastMCP

# MCP server instance
mcp = FastMCP("Math")

# Registers a function as an available tool on the MCP server
@mcp.tool()
def add(a: int, b: int) -> int:
    """Adds two numbers together"""
    return a + b

@mcp.tool()
def muliply(a: int, b: int) -> int:
    """Multiplies two numbers together"""
    return a * b


# Run the server
if __name__ == "__main__":
    mcp.run()
