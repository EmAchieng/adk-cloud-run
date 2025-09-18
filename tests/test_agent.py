import datetime
from multi_tool_agent import agent

def test_get_weather_new_york():
    result = agent.get_weather("New York")
    assert result["status"] == "success"
    assert "sunny" in result["report"]

def test_get_weather_unknown_city():
    result = agent.get_weather("London")
    assert result["status"] == "error"
    assert "not available" in result["error_message"]

def test_get_current_time_new_york():
    result = agent.get_current_time("New York")
    assert result["status"] == "success"
    assert "The current time in New York is" in result["report"]

def test_get_current_time_unknown_city():
    result = agent.get_current_time("London")
    assert result["status"] == "error"
    assert "don't have timezone information" in result["error_message"]