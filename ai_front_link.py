from detect_carnum import detect_carnum

# 등록된 장애인 차량 목록
registered_disabled_cars = ['58우 2917', '63두 9655', '42구 9833', '67도 5104', '232다 2461']

# 고유 번호에 따라 장애인 및 비장애인 사진을 결정하는 함수
def determine_photos(isDisabled):
    if isDisabled:
        # 장애인 차량 이미지를 생성하거나 경로를 반환
        img_path = 'C:\\car_image\\car_num1.jpg'  # 실제 로직에 따라 업데이트 필요
    else:
        # 비장애인 차량 이미지를 생성하거나 경로를 반환
        img_path = 'C:\\car_image\\car_num2.jpg'  # 실제 로직에 따라 업데이트 필요
    return img_path

# 감지된 차량 번호가 등록된 장애인 차량인지 확인하는 함수
def check_disabled_vehicle(detected_carnum):
    if detected_carnum in registered_disabled_cars:
        return 'Disabled', 1
    else:
        return 'Non_Disabled', 2

# 차량 번호를 분류하고 결과를 반환하는 메인 함수
def classify_car_number(img_path):
    car_number = random.randint(1, 12)
    img_path = 'C:/car_image/car_num{}.jpg'.format(car_number)
    detected_number = detect_carnum(img_path)  # 차량 번호 인식 함수 호출
    classification, return_value = check_disabled_vehicle(detected_number)  # 장애인 차량 여부 확인
    car_register_result = {'car_number': detected_number, 'classification': classification, 'return_value': return_value}  # 결과 생성
    return car_register_result

