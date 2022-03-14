# 유클리드 호제법: 숫자 a, b가 있을 때, a를 b로 나눈 나머지와 b 의최대 공약수 는 a 와 b 의 최대 공약수 가 같다는 것을 의미한다.
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


# 최소공배수
# 최소공배수는 a, b의 곱을 a, b의 최대 공약수로 나누면 나오게 된다.
def lcm(a, b):
    return a * b / gcd(a, b)