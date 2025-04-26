import subprocess
import sys
import os

def run_script(script_path):
    print(f"Running {script_path}...")
    # Set working directory to deep_research_ai_agent for imports to work
    cwd = os.path.join(os.getcwd(), "deep_research_ai_agent")
    result = subprocess.run([sys.executable, script_path], capture_output=True, text=True, cwd=cwd)
    print(result.stdout)
    if result.stderr:
        print("Errors:")
        print(result.stderr)

def main():
    # Run research agent to crawl and collect data
    run_script("research_agent.py")

    # Run langgraph integration to add data to knowledge graph
    run_script("langgraph_integration.py")

    # Run answer drafter agent to generate answers
    run_script("answer_drafter_agent.py")

if __name__ == "__main__":
    main()
