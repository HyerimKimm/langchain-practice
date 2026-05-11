from typing import List

from pydantic import BaseModel, Field

from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

class Source(BaseModel):
    """Agent가 사용할 source를 저장하는 스키마(Schema) 입니다."""

llm = ChatOpenAI(model="gpt-5")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from react-search-agent!")
    result = agent.invoke({"messages": HumanMessage(content="LinkedIn에서 서울/경기 지역의 AI Engineer 채용 공고 3개를 검색하고 상세 정보를 나열해줘.")})
    print(result)

if __name__ == "__main__":
    main()
