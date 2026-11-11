def convert(text):
    try:
        number = int(text)
    except ValueError:
        print("  except: 숫자가 아니다")
    else:
        print("  else: 변환했다 ->", number)
    finally:
        print("  finally: 언제나 실행된다")


print("convert('42')")
convert("42")
print("convert('사십이')")
convert("사십이")
