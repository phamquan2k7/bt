def middle_char(text):
    length = len(text)
    mid = length // 2

    if length % 2 == 0:
        return text[mid - 1:mid + 1]
    else:
        return text[mid]
user_text = input("Nhập một chuỗi: ")
result = middle_char(user_text)

print("Ký tự ở giữa là:", result)
