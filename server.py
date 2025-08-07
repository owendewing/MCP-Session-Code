from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from tavily import TavilyClient
import os
from dice_roller import DiceRoller
from weather_tool import get_weather

load_dotenv()

mcp = FastMCP("mcp-server")
client = TavilyClient(os.getenv("TAVILY_API_KEY"))

@mcp.tool()
def web_search(query: str) -> str:
    """Search the web for information about the given query"""
    search_results = client.get_search_context(query=query)
    return search_results

@mcp.tool()
def roll_dice(notation: str, num_rolls: int = 1) -> str:
    """Roll the dice with the given notation"""
    roller = DiceRoller(notation, num_rolls)
    return str(roller)

@mcp.tool()
def get_current_weather(city: str, country_code: str = "") -> str:
    """Get current weather information for a city
    
    Args:
        city: City name (e.g., "London", "New York", "Tokyo")
        country_code: Optional country code (e.g., "US", "GB", "JP")
    """
    return get_weather(city, country_code)

if __name__ == "__main__":
    mcp.run(transport="stdio")