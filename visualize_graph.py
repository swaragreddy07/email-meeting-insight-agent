# visualize_graph.py
from agent.workflow import create_workflow

# 1. Create your workflow
app = create_workflow()

# 2. Generate the PNG bytes of the LangGraph structure
graph_bytes = app.get_graph().draw_mermaid_png()

# 3. Save it locally
output_path = "workflow_diagram.png"
with open(output_path, "wb") as f:
    f.write(graph_bytes)

print(f"✅ Workflow diagram saved as: {output_path}")
