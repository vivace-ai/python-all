print(issubclass(FileNotFoundError, OSError))
print(issubclass(KeyError, LookupError))
print(issubclass(ZeroDivisionError, Exception))
print(issubclass(KeyboardInterrupt, Exception))

try:
    {}["없는 키"]
except LookupError as e:    # KeyError는 LookupError의 한 종류다
    print("잡았다:", type(e).__name__)
