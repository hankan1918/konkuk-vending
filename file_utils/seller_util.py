import re

"""
아이디 비밀번호 변경 함수 추가할지 논의 필요함
"""

def load_admin(seller_file_path, AdminList, Admin): #관리자 파일 로드
	"""
	아이디 비밀번호 이후 다른 문자에 대한 예외 처리 혹은 에러 처리가 필요함
	"""
	try:
		with open(seller_file_path, 'r') as file:
			for line in file:
				parts = re.split(r'\s+', line.strip()) #횡공백류열1 기준으로 분리
				try:
					name, password = parts[0], parts[1]
				except IndexError:
					pass
				AdminList.append(Admin(name, password)) #인스턴스 생성 (리스트)
	except FileNotFoundError:
		return "error message" #에러 코드로 리턴할지 문자열로 리턴할지는 논의 필요함

def save_admin(seller_file_path, AdminList, Admin): #관리자 파일 생성/저장
	"""
	저장하는 과정에서 저장에 대한 에러는 무시하는것으로 하는것이 맞는지 확인 필요함
	"""
	with open(seller_file_path, 'w') as file:
		for Admin in AdminList:
			file.write(f"{Admin.name} {Admin.password}\n") #공백으로 아이디, 비밀번호 분리