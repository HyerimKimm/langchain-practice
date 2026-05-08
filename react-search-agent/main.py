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

llm = ChatOpenAI(model="gpt-5")
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from react-search-agent!")
    result = agent.invoke({"messages": HumanMessage(content="LinkedIn에서 서울/경기 지역의 AI Engineer 채용 공고 3개를 검색하고 상세 정보를 나열해줘.")})
    print(result)

if __name__ == "__main__":
    main()
