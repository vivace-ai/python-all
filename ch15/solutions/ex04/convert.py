"""길이 단위를 바꾸는 함수 모음."""

KM_PER_MILE = 1.609344


def km_to_mile(km):
    return km / KM_PER_MILE


def mile_to_km(mile):
    return mile * KM_PER_MILE


if __name__ == "__main__":
    print(f"{km_to_mile(10):.2f}")
    print(f"{mile_to_km(26.2):.2f}")
