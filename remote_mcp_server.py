from fastmcp import FastMCP

mcp = FastMCP("practice_mcp_server")

@mcp.tool(description= "Prints hello world")
def printHelloWorld() -> None:
    """This function prints hello world"""
    print("Hello World!")
    return None

@mcp.tool(description="Adds two numbers 2 and 3 and prints the results")
def addNumbers() -> None:
    """This function adds the numbers 2 + 3 together"""
    print(2+3)
    return None

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000) 

