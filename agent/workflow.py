from langgraph.graph import StateGraph, END
from agent.state import State
from agent.nodes import load_emails, extract_entities, summarize_meetings, update_memory

def create_workflow():
    workflow = StateGraph(State)
    workflow.add_node("load_emails", load_emails)
    workflow.add_node("extract_entities", extract_entities)
    workflow.add_node("summarize_meetings", summarize_meetings)
    workflow.add_node("update_memory", update_memory)

    workflow.add_edge("load_emails", "extract_entities")
    workflow.add_edge("extract_entities", "summarize_meetings")
    workflow.add_edge("summarize_meetings", "update_memory")
    workflow.add_edge("update_memory", END)

    workflow.set_entry_point("load_emails")

    return workflow.compile()
