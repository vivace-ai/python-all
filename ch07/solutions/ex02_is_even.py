def is_even(number):
    return number % 2 == 0  # 비교의 결과를 그대로 돌려준다


print(is_even(10), is_even(7))

if is_even(42):
    print("42는 짝수입니다.")
