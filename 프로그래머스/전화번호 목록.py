def solution(phone_book):
    answer = True
    phone_book.sort()
    pre=phone_book[0]

    for number in phone_book[1:]:
        if pre==number[:len(pre)]:
            return False
        else:
            pre=number

    return answer

print(solution(["119", "97674223", "1195524421"]))


def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True