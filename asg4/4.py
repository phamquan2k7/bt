def redact_phone_numbers(text):
    result = ""
    i = 0
    n = len(text)
    
    while i < n:
        if text[i:i+3] == "+84":
            j = i + 3
            while j < n and text[j].isdigit():
                j += 1
            result += "[REDACTED]"
            i = j
        
        elif i + 10 <= n and text[i:i+10].isdigit():
            result += "[REDACTED]"
            i += 10
        
        else:
            result += text[i]
            i += 1
    
    return result


text = input("Enter text: ")
print(redact_phone_numbers(text))