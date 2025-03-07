import tts
from tts import Speech2text
## OOP Object Oriented Programming 객체지향 프로그램
if __name__ == "__main__": #메인에서 시작
    processor = Speech2text(language='ko-KR') #speech2text 클래스 선언
    processor.run() # 클래스.메서드 run메서드 실행행 
