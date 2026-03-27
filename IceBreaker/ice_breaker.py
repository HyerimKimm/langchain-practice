from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

information = """
미국의 기업인이자 행정가.
남아공에서 태어나 캐나다를 거쳐 미국에 정착했으며, 현재 미국 텍사스 주 오스틴에 거주하고 있다.
테슬라, 스페이스X, 스타링크, 뉴럴링크, xAI 홀딩스 등 다수의 첨단 기업을 설립, 보유 및 운영하면서 인류 역사상 최고의 부호로 등극했다. 
혁신 중심적인 경영과 미래 지향적 비전이 그의 특징으로 평가받고 있다.
현재 세계 최고의 부자이자 인류 역사상 최고의 부자로, 개인 순자산이 8,000억 달러(한화 약 1,202조원)를 돌파한 인류 역사상 최초의 인물이다. 
일론 머스크가 설립한 우주 기업 스페이스X의 기업 가치 상승도 재산 증가에 크게 기여했다. 
포브스는 일론 머스크의 순자산이 최근 기준으로 8,570억 달러, 한화 약 1,288조원에 이른다고 추산했다. 
테슬라의 경영 미션을 완료할 시 일론 머스크는 인류 역사상 최초로 1조 달러, 한화 약 1,502조원 가량의 수익을 얻게 된다.
"""

if __name__ == '__main__':
    load_dotenv()
    print("hello langChain")

    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": information})
    print(res)