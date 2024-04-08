'''
프로그램 전체에서 사용될 전역변수와 전역상수가 필요하면 Config 클래스 내 필요한 변수를 선언 및 정의
가져오기: from config import config (as c)
'''

class Config:
    _instance = None

    # 파일 경로
    seller_file_path : str = 'seller.txt'
    cash_file_path : str = 'cash.txt'
    drinks_file_path : str = 'drinks.txt'
    
    AdminList = [] #관리자 클래스 리스트 생성
    CurrencyList = [] #권종 클래스 리스트 생성
    
    @staticmethod
    def get_instance():
        if Config._instance is None:
            Config._instance = Config()
        return Config._instance
    
config = Config.get_instance()

