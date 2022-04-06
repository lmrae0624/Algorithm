answer=''

# 양 끝단의 불필요한 문자열을 삭제
text = "......Hello World,,,,,,,," 
text.strip("."",")
#'Hello World'

text = "ababHello Worldabca" 
text.strip("a""b""c")
#'Hello World'


# 왼쪽 끝단의 불필요한 문자를 삭제
text = "aaaaaHello Worldaaaaaa" 
text.lstrip("a")
#'Hello Worldaaaaaa'


# 오른쪽 끝단의 불필요한 문자를 삭제
text = "aaaaaHello Worldaaaaaa" 
text.rstrip("a")
#'aaaaaaHello World'