class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):   # 저장하지 않고 필요할 때 계산한다
        return self.celsius * 9 / 5 + 32


t = Temperature(25)
print(t.celsius, t.fahrenheit)

t.celsius = 30              # 섭씨를 바꾸면 화씨도 따라 바뀐다
print(t.celsius, t.fahrenheit)
