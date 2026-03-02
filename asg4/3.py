def sum_numbers_in_text(text):
    total = 0
    current_number = ""
    for ch in text:
        if ch.isdigit():
            current_number += ch
        else:
            if current_number != "":
                total += int(current_number)
                current_number = ""
    if current_number != "":
        total += int(current_number) 
    return total
text = input("Enter paragraph: ")
print(sum_numbers_in_text(text))