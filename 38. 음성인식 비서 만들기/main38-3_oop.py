import speech_recognition as sr

class Speech2text:
    def __init__(self, language='ko-KR'): #초기화, 옵션변수가 들어오는 곳
        self.recognizer = sr.Recognizer() #self로 선언된 변수는 
        self.language = language          # SpeechtoTextProcessor Class내에서 사용가능

    def process_audio(self): # 음성 입력, 텍스트로 변환
        try:
            #음성입력
            with sr.Microphone() as source:
                print("음성을 입력하세요.")
                audio = self.recognizer.listen(source)
            # text변환
            stt = self.recognizer.recognize_google(audio, 
                                language=self.language)
            print("음성변환: " + stt)
            self.handle_keywords(stt)

        except sr.UnknownValueError:
            print("오디오를 이해할 수 없습니다.")
        except sr.RequestError as e:
            print(f"에러가 발생했습니다. 에러원인: {e}")

    def handle_keywords(self, text): # 특정 키워드에 반응
        if "안녕" in text:
            print("네 안녕하세요.")
        elif "날씨" in text:
            print("정말 날씨가 좋네요.")
        # 필요한 다른 키워드 처리 추가

    def run(self):     #processor.run() 을 하였을 경우 실행되는 부분
        """음성 인식 프로세스를 계속 실행합니다."""
        try:
            while True: #무한루프
                self.process_audio()
        except KeyboardInterrupt:
            print("\n프로그램을 종료합니다.")

if __name__ == "__main__":
    processor = Speech2text(language='ko-KR')
    processor.run()