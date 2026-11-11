from functools import wraps


def retry(times):
    """실패하면 times번까지 다시 시도하게 만드는 데코레이터를 돌려준다."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except ConnectionError as e:
                    print(f"  {attempt}번째 시도 실패: {e}")
            raise ConnectionError(f"{times}번 모두 실패했다")

        return wrapper

    return decorator


attempts = 0


@retry(3)
def fetch():
    """두 번 실패한 뒤 세 번째에 성공하는 척하는 함수."""
    global attempts
    attempts += 1
    if attempts < 3:
        raise ConnectionError("서버가 응답하지 않는다")
    return "응답 본문"


print(fetch())
