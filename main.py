import model
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition
from tools import tools
from database import engine, Base, get_db
from model import Report

db = get_db()

load_dotenv()

Base.metadata.create_all(bind=engine)

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant"
)

llm_with_tools = llm.bind_tools(tools)

tool_nodes = ToolNode(tools)

def call_llm(state: MessagesState):
    messages = state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

graph_builder = StateGraph(MessagesState)
graph_builder.add_node("call_llm", call_llm)
graph_builder.add_node("tools", tool_nodes)
graph_builder.add_edge(START, "call_llm")
graph_builder.add_conditional_edges("call_llm", tools_condition)
graph_builder.add_edge("tools", "call_llm")

graph = graph_builder.compile()

result = graph.invoke({
    "messages": [
        ("system", """You are a research assistant. When the user gives you a topic:
1. Search the web for information about it using search_web
2. Write a clean structured summary based on the results
3. Collect all URLs from the search results as sources
4. Save the report using save_report with the topic, summary, and sources

Always search first before writing anything."""),
        ("human", "who is abiy ahmed?")
    ]
})

final_message = result["messages"][-1].content
print(final_message)
report = db.query(Report).order_by(Report.id.desc()).first()
print(report.summary)
print("SOURCES:")
print(report.source)