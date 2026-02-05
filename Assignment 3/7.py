def acronym(phrase):
    words = phrase.split()
    result = ""

    for word in words:
        result += word[0].upper()

    return result

user_phrase = input("Nhập một cụm từ: ")
print("Acronym:", acronym(user_phrase))

