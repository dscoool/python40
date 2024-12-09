## flask 네이버 클라우드 서버로 배포
## https://daco2020.tistory.com/802
## http://localhost/map

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "Backend Web Server using Flask."

@app.route('/map')
def map():
    return render_template("uni_map.html")

def main():
    app.run(debug=True,port=80)
    
if __name__== '__main__':
    main()