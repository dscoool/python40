## command prompt 에서 실행
## 브라우저에서 http://localhost 로 접속.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Backend Web Server!!"

def main():
    app.run(debug=True,port=80)
    
if __name__== '__main__':
    main()