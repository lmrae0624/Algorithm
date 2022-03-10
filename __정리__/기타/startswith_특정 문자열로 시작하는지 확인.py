# str.startswith(str or tuple) / list나 dict는 안됨 ! 조심 !

string = "hello startswith"
print(string.startswith("hello"))
# True

string = "hello startswith"
tuple_string = ("hello", "bye")
print(string.startswith(tuple_string))
# True