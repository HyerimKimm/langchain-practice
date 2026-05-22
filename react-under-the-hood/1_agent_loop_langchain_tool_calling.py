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
    pass

if __name__ == "__main__":
    print("Hello Langchain Agent (.bind_tools)!")
    print()
    result = run_agent("노트북 살건데, 내 할인 등급이 gold이면 할인 적용된 금액이 얼마야?")