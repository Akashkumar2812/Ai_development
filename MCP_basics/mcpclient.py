from fastmcp import Client
from pathlib import Path
 #connect to the server and return the client object
async def connect():

    """
    Connect to the MCP Server.
    """

    client = Client(Path("mcpserver.py"))
    #connect to the server using the context manager
    await client.__aenter__()

    print("Connected to MCP Server.")

    return client

#disconnect from the server and close the connection
async def disconnect(client):

    """
    Close the MCP connection.
    """

    await client.__aexit__(
        None,
        None,
        None
    )
# 3. discove the tools available on the server and return a list of tool names
async def discover_tools(client):
    
    """
    Retrieve all tools from the server.
    """
#tools-> [{"name": "roll_dice", "description": "Roll a six-sided dice."}, {"name": "current_date_time", "description": "Return the current date and time"}]
    tools = await client.list_tools()

    return tools

#4. execute a tool on the server and return the result

async def execute_tool(
    client,
    tool_name,
    arguments=None
):

    """
    Execute a tool.
    """

    if arguments is None:

        arguments = {}

    result = await client.call_tool(

        tool_name,
        arguments
    )

    return result