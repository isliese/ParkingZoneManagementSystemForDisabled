from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '오픈소스 웹페이지'

if __name__ == '__main__':
    app.run(debug=True)
