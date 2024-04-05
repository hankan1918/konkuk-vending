from base_parser import BaseParser

'''
모드
    올바른 입력이 아닙니다.
'''

class ModeParser(BaseParser):
    
    def parse(self, input: str) -> tuple[bool, any]:
        command = self.parse_command(input)
        if command in [0, 1, 2]:
            return True, command
        else: 
            return False, "오류: 올바른 입력이 아닙니다."

# 테스트
if __name__ == "__main__":
    parser = ModeParser()
    test_input = "   \t\f\v3 \t \n\n"
    t = parser.parse(test_input)
    print(t)