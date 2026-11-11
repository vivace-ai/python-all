def invert(mapping):
    result = {}
    for key, value in mapping.items():
        result[value] = key     # 값과 키의 자리를 바꾼다
    return result


codes = {"KR": "한국", "JP": "일본", "FR": "프랑스"}
print(invert(codes))
