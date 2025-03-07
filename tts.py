import speech_recognition as sr

class Speech2text: #객체 생성 class, 객체, object
    #초기화 메서드 method init(ilization)
    def __init__(self, language='ko-KR'): # function 함수수
        self.recognizer = sr.Recognizer() #self로 선언된 변수는 
        self.language = language          # Speechto2Text Class내에서 사용가능
    #메서드
    def process_audio(self): # 음성 입력, 텍스트로 변환
        try:
            #음성입력
            with sr.Microphone() as source: #오디오 입력
                print("음성을 입력하세요.")
                audio = self.recognizer.listen(source) #소리 저장
            # text변환 #음성 텍스트로 변환, 출력 / 구글이용
            stt = self.recognizer.recognize_google(audio, 
                                language=self.language) #language option
            print("음성변환: " + stt)
            self.handle_keywords(stt) #handle_keyword() 메서드 호출
                                    #정해진 키워드에 반응응
        except sr.UnknownValueError:
            print("오디오를 이해할 수 없습니다.")
        except sr.RequestError as e:
            print(f"에러가 발생했습니다. 에러원인: {e}")
    #메서드
    def handle_keywords(self, text): # 특정 키워드에 반응
        if "안녕" in text:
            print("네 안녕하세요.")
        elif "날씨" in text:
            print("정말 날씨가 좋네요.")
        # 필요한 다른 키워드 처리 추가
    #메서드
    def run(self):     #processor.run() 을 하였을 경우 실행되는 부분
        """음성 인식 프로세스를 계속 실행합니다."""
        try:
            while True: #무한루프
                self.process_audio() #process_audio 메서드 반복 호출
        except KeyboardInterrupt: # CTRL+C --> 종료
            print("\n프로그램을 종료합니다.")
