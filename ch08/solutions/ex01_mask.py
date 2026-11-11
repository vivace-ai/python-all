phone = input("전화번호: ")

masked = phone[:-4] + "****"    # 뒤 네 자리를 뺀 나머지에 별표를 붙인다
print(masked)
