from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

# 전역 변수로 차량 번호 저장
selected_car_number = None

@app.route('/')
def index():
    return render_template('Home.html')

@app.route('/Disabled')
def disabled():
    return render_template('Disabled.html')

@app.route('/Login')
def login():
    return render_template('Login.html')

@app.route('/LoginSuccess')
def loginsuccess():
    return render_template('LoginSuccess.html')

@app.route('/NoDisabled')
def nodisabled():
    return render_template('NoDisabled.html')

@app.route('/ParkingLot')
def parkinglot():
    return render_template('ParkingLot.html')

@app.route('/ParkingStateManaging')
def parkingstatemanaging():
    return render_template('ParkingStateManaging.html')

@app.route('/SignUp')
def signup():
    return render_template('SignUp.html')

@app.route('/SignUpSuccess')
def signupsuccess():
    return render_template('SignUpSuccess.html')

@app.route('/Report')
def report():
    return render_template('Report.html')

# 변수 받아오는 부분
# POST 요청을 처리하는 새로운 라우트 추가
@app.route('/setCarNumber', methods=['POST'])
def set_car_number():
    global selected_car_number
    data = request.get_json()
    if 'carNumber' in data:
        selected_car_number = data['carNumber']
        # 선택된 차량 번호를 터미널에 출력
        print(f'Selected car number: {selected_car_number}')
        
        # 외부 명령어 실행 (예: 'echo' 명령어)
        try:
            result = subprocess.run(['echo', str(selected_car_number)], capture_output=True, text=True, shell=True)
            return jsonify(success=True, output=result.stdout)
        except subprocess.CalledProcessError as e:
            return jsonify(success=False, error=str(e))
    return jsonify(success=False)

if __name__ == '__main__':
    app.run(debug=True)