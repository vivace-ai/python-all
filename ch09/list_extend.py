morning = ["메일", "회의"]
afternoon = ["보고서"]

today = morning + afternoon     # 두 리스트를 이은 새 리스트
print(today)

morning.extend(afternoon)       # morning 자체에 이어 붙인다
print(morning)

print([0] * 5)                  # 같은 값을 되풀이한 리스트
