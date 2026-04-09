from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

from thrid_parties.linkedin import scrape_linkedin_profile

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
    # llm = ChatOllama(model="mistral")

    # | 는 앞 결과를 뒤로 넘기는 연산자임
    chain = summary_prompt_template | llm | StrOutputParser()
    linked_data = scrape_linkedin_profile(linkedin_profile_url="https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json")

    res = chain.invoke(input={"information": linked_data})
    print(res)