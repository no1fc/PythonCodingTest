#자동차 class를 작성
class Car:
    #생성자 메서드를 사용하기 위해 __init__ 모듈을 작성
    def __init__(self, make, model, year):
        #인스턴스 초기화 변수를 작성
        self.make = make
        self.model = model
        self.year = year

    #변수가 실제로 초기화 되었는지 확인하기 위해 출력
    def get_car_name(self):
        print(f"Car: {self.year} {self.make} {self.model}")

# 인스턴스 초기화 값을 작성
my_car = Car("Toyota", "Corolla", 2020)

# 각 변수(속성)을 호출
print(my_car.year) # 2020
print(my_car.make) # Toyota
print(my_car.model)# Corolla

# 메서드 호출
my_car.get_car_name()
# Car: 2020 Toyota Corolla