import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from typing import Any
from agent.state import State
from IPython.display import Image, display

load_dotenv(dotenv_path=".env")

open_ai_api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=open_ai_api_key)

def load_emails(state: State) -> State:
    # This node assumes 'emails' are already passed in
    return state

def extract_entities(state: State) -> State:
    prompt = f"""
    From the following emails or meeting notes, extract:
    - Names of people involved
    - Tasks or responsibilities assigned
    - Any deadlines or dates mentioned
    Return it in JSON format.
    \n\n{state['emails']}
    """
    response = llm.invoke(prompt)
    state["entities"] = response.content
    return state

def summarize_meetings(state: State) -> State:
    previous_context = "There is no previous context right now"
    if "memory" in state and state["memory"]:
        previous_context = "this is the previous saved summaries:" + "\n".join(state["memory"])
    prompt = f"""
    Summarize the overall discussion in a few sentences in simple language and mention key updates and also look at the 
    previous memory to understand the whole context:
    \n\n{state['emails']}
    \n{previous_context}
    """
    response = llm.invoke(prompt)
    state["summary"] = response.content
    return state

def update_memory(state: State) -> State:
    if "memory" not in state:
        state["memory"] = []
    state["memory"].append(state["summary"])
    return state
