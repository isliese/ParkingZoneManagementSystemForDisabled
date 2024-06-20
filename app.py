from flask import Flask, render_template, request, jsonify
from ai_front_link import classify_car_number, determine_photos
import os  # os 모듈을 추가하여 이미지 경로 유효성 검사

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

# POST 요청을 처리하는 새로운 라우트 추가
@app.route('/setCarNumber', methods=['POST'])
def set_car_number():
    global selected_car_number
    data = request.get_json()
    if 'carNumber' in data:
        selected_car_number = data['carNumber']
        # 선택된 차량 번호를 터미널에 출력
        print(f"Received car number: {selected_car_number}")
        return jsonify(success=True, receivedCarNumber=selected_car_number)
    return jsonify(success=False)

# POST 요청을 처리하여 차량 번호를 받아와 분류하고 결과 반환
@app.route('/detectAndClassify', methods=['POST'])
def detect_and_classify():
    # 요청 JSON 데이터에 'isDisabled'가 포함되어 있는지 확인
    if 'isDisabled' not in request.json:
        return jsonify(success=False, message="isDisabled not provided")
    
    isDisabled = request.json['isDisabled']
    img_path = determine_photos(isDisabled)
    
    # 이미지 경로가 유효한지 확인
    if not img_path or not os.path.exists(img_path):
        return jsonify(success=False, message="Image path is invalid or image not found")
    
    result = classify_car_number(img_path)
    # 분류 결과를 터미널에 출력
    print(f"Classification result: {result}")
    return jsonify(success=True, result=result)

if __name__ == '__main__':
    app.run(debug=True)
