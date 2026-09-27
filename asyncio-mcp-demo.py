import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import openai  # Using OpenAI-compatible client for Ollama

# 1. Configure the Ollama client for Llama 3
llm = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # Required but ignored by Ollama
)

# 2. Define the MCP Server parameters (e.g., using a free SQLite server)
server_params = StdioServerParameters(
    command="npx",
    args=["-y", "@modelcontextprotocol/server-sqlite", "--db-path", "./my_database.db"],
    env=None
)

async def main():
    # 3. Establish the connection to the MCP Server
    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            # 4. List available tools from the server
            response = await session.list_tools()
            tools = response.tools
            print(f"Available MCP Tools: {[t.name for t in tools]}\n")

            # 5. Format tools for Llama 3's tool-calling capability
            # (Converts MCP tool schemas into OpenAI/Ollama tool definitions)
            llm_tools = [
                {
                    "type": "function",
                    "function": {
                        "name": tool.name,
                        "description": tool.description,
                        "parameters": tool.inputSchema
                    }
                } for tool in tools
            ]

            # 6. Ask Llama 3 a question that requires the tool
            prompt = "Create a table named users with id and name columns."
            print(f"Prompt: {prompt}")
            
            response = llm.chat.completions.create(
                model="llama3",
                messages=[{"role": "user", "content": prompt}],
                tools=llm_tools
            )

            # 7. Check if Llama 3 wants to call the MCP tool
            tool_calls = response.choices[0].message.tool_calls
            if tool_calls:
                for tool_call in tool_calls:
                    print(f"Llama 3 selected tool: {tool_call.function.name}")
                    
                    # Execute the tool via the MCP server session
                    import json
                    tool_args = json.loads(tool_call.function.arguments)
                    result = await session.call_tool(tool_call.function.name, arguments=tool_args)
                    print(f"MCP Server Execution Result: {result.content}")

if __name__ == "__main__":
    asyncio.run(main())