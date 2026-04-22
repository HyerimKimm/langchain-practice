number = input("정수입력> ")

# 마지막 자리 숫자 추출
last_character = number[-1]

last_number = int(last_character)

#짝수 확인
if last_number % 2 == 0:
		print("짝수입니다")