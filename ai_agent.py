from dotenv import load_dotenv
load_dotenv()
#Step 1: Setup API keys for GROQ and Tavily
import os
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY=os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")

#Step 2: Setup LLMs and Tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults


openai_llm=ChatOpenAI(model="gpt-4o-mini")
groq_llm=ChatGroq(model="llama-3.3-70b-versatile")

search_tool=TavilySearchResults(max_results=2)


#Step 3: Setup AI agent with search tool functionality
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

system_prompt="Act as an AI chatbot who is smart and friendly"

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider=="Groq":
        llm=ChatGroq(model=llm_id)
    elif provider=="OpenAI":
        llm=ChatOpenAI(model=llm_id)

    tools=[TavilySearchResults(max_results=2)] if allow_search else []
    agent=create_react_agent(
        model=llm,
        tools=tools
    )
    state = {
        "messages": [SystemMessage(content=system_prompt)] + query
    }
    
    response = agent.invoke(state)

    # Extract AI messages
    messages = response.get("messages", [])
    ai_messages = [m.content for m in messages if isinstance(m, AIMessage)]

    return ai_messages[-1] if ai_messages else "⚠️ No AI message found."
    

    #response=agent.invoke(state)
    #messages=response.get("messages",[])
    #ai_messages=[message.content for message in messages if isinstance(message, AIMessage)]
    #return ai_messages[-1] if ai_messages else "No AI response found."
    #for msg in reversed(messages):
        #if hasattr(msg, "content"):
           # return msg.content.strip()
   # return "No response found."
   

  