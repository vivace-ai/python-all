def to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


print(f"섭씨 26.5도 = 화씨 {to_fahrenheit(26.5):.1f}도")
print(f"화씨 79.7도 = 섭씨 {to_celsius(79.7):.1f}도")
print(f"왕복 확인: {to_celsius(to_fahrenheit(26.5)):.1f}")
