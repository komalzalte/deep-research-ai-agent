"""
Configuration Module

This module contains configuration parameters for the Deep Research AI Agentic System.
"""

# Real website crawling configuration
TAVILY_TARGET_WEBSITES = [
    "https://www.bbc.com/news/technology",
    "https://techcrunch.com",
    "https://www.analyticsvidhya.com/blog/"
]

TAVILY_CRAWL_DEPTH = 1  # Depth of crawling for demonstration

# LangChain configuration
import os
LANGCHAIN_MODEL_NAME = "gpt-4"  # Model to use for answer drafting
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Set your OpenAI API key in environment variables

# LangGraph configuration
LANGGRAPH_API_KEY = os.getenv("LANGGRAPH_API_KEY")  # Set your LangGraph API key in environment variables

# Other configurations
DATA_STORAGE_PATH = "data/"
LOGGING_LEVEL = "INFO"
