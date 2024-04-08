import re

def save_currencies(cash_file_path, CurrencyList, Currency): #잔돈 파일 생성/저장
	"""
	저장하는 과정에서 저장에 대한 에러는 무시하는지 정해진 것으로 아는데 맞는지 확인 필요함
	"""
	with open(cash_file_path, 'w') as file:
		for Currency in CurrencyList:
			file.write(f"{Currency.value} {Currency.quantity}\n") #공백으로 권종, 개수 분리

def load_currencies(cash_file_path, CurrencyList, Currency): #잔돈 파일 로드
	"""
	잔돈 파일에서 100원, 500원, 1000원, 5000원, 10000원, 50000원 외에 
	다른 권종 있는지 로드하면서 판별하는 과정 필요 -> 무결점 검사에서 추가바람

	또한 권종 개수 이후 다른 문자에 대한 예외 처리 혹은 에러 처리가 필요함
	"""
	with open(cash_file_path, 'r') as file:
		for line in file:
			parts = re.split(r'\s+', line.strip()) #횡공백류열1 기준으로 분리
			try:
				value, quantity = parts[0], parts[1]
			except IndexError:
				return "error message"
			CurrencyList.append(Currency(int(value), int(quantity))) #인스턴스 생성 (리스트)

def change_currency(CurrencyList, Currency, Currency_Value, Currency_Amount):
	for Currency in CurrencyList:
		if Currency.value == Currency_Value:
			if (Currency.quantity + Currency_Amount < 100) & (Currency.quantity + Currency_Amount >= 0) :
				Currency.quantity += Currency_Amount
				break
			else:
				return "error message"