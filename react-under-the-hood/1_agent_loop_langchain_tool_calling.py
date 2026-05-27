from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langsmith import traceable

MAX_ITERATIONS = 10
MODEL = "qwen3:1.7b"

@tool
def get_product_price(product: str) -> float:
    """제품 이름을 입력받아서 제품의 가격을 리턴하는 함수"""
    prices = { "laptop": 1299.99, "headphones": 149.95, "keyboard": 89.50 }
    print(f"     >> get_product_price(product={product})를 실행중입니다.")
    return prices.get(product, 0)

@tool
def apply_discount(price: float, discount_tier: str) -> float:
    """
가격에 할인 등급을 적용하고, 최종 가격을 return한다.
티어 정보 : bronze, silver, gold.
	"""
    print(f"    >> apply_discount(price={price}, discount_tier={discount_tier})를 실행중입니다.")
    discount_percentages =  {"bronze": 5, "silver": 12, "gold": 23}
    discount = discount_percentages.get(discount_tier, 0)
    return round(price * (1 - discount / 100), 2)

# --- Agent Loop ---
@traceable(name="LangChain Agent Loop")
def run_agent(question: str) -> None:
    tools = [get_product_price, apply_discount]
    tools_dict = {t.name: t for t in tools}

    llm = init_chat_model(f"ollama: {MODEL}", temperature=0)

    llm_with_tools = llm.bind_tools(tools)

    print(f"Question: {question}")
    print("-" * 50)

    messages = [
        SystemMessage(content="""
당신은 쇼핑 도우미입니다. 
당신은 제품 목록을 확인하는 tool과 할인 적용 tool을 사용할 수 있습니다. 
[엄격한 규칙] - 당신은 이 규칙을 정확히 따라야만 합니다. 
1. 제품의 가격을 추측하거나 가정하지 말것
2. 실제로 가격을 얻으려면 당신은 반드시 get_product_price Tool을 호출해야 합니다. 
3. 할인 적용된 가격을 계산하기 위해 직접 수학계산 하지 말고, apply_discount Tool을 호출하여 얻어야 합니다.
4. 사용자의 할인 등급이 없는 경우, 어떤 할인 등급을 적용할 것인지 사용자에게 물어봐야 합니다. 절대 추측하지 마세요.
"""),
    HumanMessage(content=question),
    ]

    for iteration in range(1, MAX_ITERATIONS + 1):
        print(f"반복문 {iteration} 시작")

        ai_message = llm_with_tools.invoke(messages)

        tool_calls = ai_message.tool_calls

        if not tool_calls: 
            print(f"최종 답변 : ${ai_message.content}")


if __name__ == "__main__":
    print("Hello Langchain Agent (.bind_tools)!")
    print()
    result = run_agent("노트북 살건데, 내 할인 등급이 gold이면 할인 적용된 금액이 얼마야?")