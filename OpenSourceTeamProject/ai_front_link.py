import random
from detect_carnum import detect_carnum  # 감지 함수 import

# 등록된 장애인 차량 목록
registered_disabled_cars = ['58우 2917', '63두 9655', '42구 9833', '67도 5104', '232다 2461']
# 차량 데이터셋 중 장애인 차량으로 등록되지 않은 일반 주차 차량 목록
nonregistered_cars = ['57너 3333', '25누 1409', '08러 4934', '18도 2764', '25더 2661', '59주 4274']

# 고유 번호에 따라 장애인 및 비장애인 사진을 결정하는 함수
def determine_car_photos(isDisabled):
    if isDisabled in ['1', '2', '3']:
        # 장애인 차량 이미지를 생성하거나 경로를 반환
        print(isDisabled)
        car_number = random.randint(1, 6)
        print(car_number)
        img_path = 'C:/Users/afrom/car_image/car_num{}.jpg'.format(car_number)  # 실제 로직에 따라 업데이트 필요
        print(img_path)
    elif isDisabled in ['4', '5', '6']:
        print(isDisabled)
        # 비장애인 차량 이미지를 생성하거나 경로를 반환
        car_number = random.randint(6, 12)
        img_path = 'C:/Users/afrom/car_image/car_num{}.jpg'.format(car_number)  # 실제 로직에 따라 업데이트 필요
    return img_path

# 감지된 차량 번호가 등록된 장애인 차량인지 확인하는 함수
def check_disabled_car(img_path):
    detected_carnum = detect_carnum(img_path)
    if detected_carnum in registered_disabled_cars:
        return detected_carnum, 1
    else:
        return detected_carnum, 2

def main(isDisabled):
    img_path = determine_car_photos(isDisabled)
    car_register_result = check_disabled_car(img_path)
    print(car_register_result)
    return car_register_result  # 프론트에 전달해주기
