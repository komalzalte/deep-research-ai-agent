# Deep Research AI Agentic System

## Overview

This project implements a Deep Research AI Agentic System designed to crawl websites, collect data, organize it in a knowledge graph, and generate answers based on the collected information. The system consists of three main components:

1. **Research Agent**: Crawls websites using Tavily to gather online information.
2. **LangGraph Integration**: Organizes and manages the collected data in a knowledge graph.
3. **Answer Drafter Agent**: Uses LangChain to process the collected data and generate answers.

## Components

### Research Agent

- Crawls target websites defined in the configuration using Tavily.
- Collects raw data and metadata.
- Saves collected data to a JSON file for further processing.

### LangGraph Integration

- Initializes the LangGraph knowledge graph.
- Adds collected data to the graph to create structured relationships.

### Answer Drafter Agent

- Loads collected data.
- Uses LangChain with a specified model to generate answers based on user queries.

## Configuration

Configuration parameters are defined in `config.py`, including:

- Target websites and crawl depth for Tavily.
- LangChain model name.
- LangGraph API key.
- Data storage path and logging level.

## Usage

1. Run the Research Agent to crawl and collect data:

```bash
python deep_research_ai_agent/research_agent.py
```

2. Run the LangGraph integration to organize data:

```bash
python deep_research_ai_agent/langgraph_integration.py
```

3. Run the Answer Drafter Agent to generate answers:

```bash
python deep_research_ai_agent/answer_drafter_agent.py
```

## Dependencies

Dependencies are listed in `requirements.txt`. Install them using:

```bash
pip install -r deep_research_ai_agent/requirements.txt
```

## Notes

- The current implementation contains placeholder logic for Tavily crawling, LangGraph integration, and LangChain answer generation.
- Replace placeholder code with actual API calls and logic as needed.
- Ensure API keys and configurations are set correctly in `config.py`.

## Contact

For questions or contributions, please contact: contact@kairon.co.in

## Submission

This project is prepared as a qualifying assignment for the Deep Research AI Agentic System.

Submission deadline: 26 April 2025
