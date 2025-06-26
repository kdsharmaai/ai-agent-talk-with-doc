from langgraph.graph import StateGraph, START, END
from state import State
from nodes import ingest_pdf, answer_question

graph_builder = StateGraph(State)
graph_builder.add_node("ingest_pdf", ingest_pdf)
graph_builder.add_node("answer_question", answer_question)

# Edges
graph_builder.add_edge(START, "ingest_pdf")
graph_builder.add_edge("ingest_pdf", "answer_question")
graph_builder.add_edge("answer_question", END)

graph = graph_builder.compile()
# graph.get_graph().draw_mermaid_png(output_file_path="graph.png")