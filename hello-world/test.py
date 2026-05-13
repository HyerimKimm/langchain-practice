class CustopmException(Exception):
	def __init__(self):
		super().__init__()
		print("CustopmException 예외가 발생했습니다.")

raise CustopmException()