# Deep Research AI Agentic System - Implementation Explanation

## Overview

This project implements a Deep Research AI Agentic System designed to fulfill the qualifying assignment requirements. The system is composed of multiple agents and integrates LangGraph and LangChain frameworks to effectively gather, organize, and utilize online information.

## System Architecture

### 1. Research Agent

- Crawls websites using Tavily, a web crawling tool.
- Collects raw data and metadata from target websites specified in the configuration.
- Saves the collected data locally in JSON format for further processing.
- This agent focuses on research and data collection.

### 2. LangGraph Integration

- Initializes a knowledge graph using LangGraph.
- Organizes and manages the collected data by adding it to the knowledge graph.
- Structures the gathered information to enable efficient querying and relationship mapping.

### 3. Answer Drafter Agent

- Loads the collected data from storage.
- Uses LangChain, a language model framework, to process the data and generate answers based on user queries.
- Functions as the answer drafting agent.

## Configuration

- The system is configurable via the `config.py` file.
- Target websites, crawl depth, LangChain model, LangGraph API key, and data storage paths are defined here.

## Usage Workflow

1. Run the Research Agent to crawl and collect data:

   ```bash
   python deep_research_ai_agent/research_agent.py
   ```

2. Run the LangGraph integration to organize the collected data:

   ```bash
   python deep_research_ai_agent/langgraph_integration.py
   ```

3. Run the Answer Drafter Agent to generate answers from the data:

   ```bash
   python deep_research_ai_agent/answer_drafter_agent.py
   ```

## Design Considerations

- Modular design with clear separation of concerns.
- Placeholder logic is used for crawling, graph management, and answer generation to allow easy extension.
- The system is designed to be extensible and adaptable to real API integrations.
- The README.md file provides detailed instructions and project overview.

## Submission Notes

- This implementation meets the assignment requirements for a dual-agent system using Tavily, LangGraph, and LangChain.
- The project is structured for easy deployment and further development.
- Contact: contact@kairon.co.in

## Next Steps

- Replace placeholder logic with actual API calls and business logic.
- Enhance error handling and logging.
- Add unit tests and integration tests.
- Prepare a GitHub repository with this code and documentation.

---

Prepared for the qualifying assignment submission due by 26 April 2025.
