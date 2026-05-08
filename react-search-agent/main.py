from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

tavily = TavilyClient();

@tool
def search(query: str) -> str: 
    """
    인터넷 검색을 하는 툴
    파라미터: 
        query: 검색할 질문
    Returns:
        검색 결과
    """
    print(f"{query}을 검색합니다.")
    return tavily.search(query=query)

llm = ChatOpenAI('gpt-5')
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from react-search-agent!")
    result = agent.invoke({"messages": HumanMessage(content="서울 날씨는 어때?")})
    print(result)

if __name__ == "__main__":
    main()
