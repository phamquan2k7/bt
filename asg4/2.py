def is_valid_hex_color(color):
    if len(color) != 7:
        return False  
    if color[0] != '#':
        return False    
    for ch in color[1:]:
        if not (ch.isdigit() or 'A' <= ch <= 'F' or 'a' <= ch <= 'f'):
            return False
    return True
color = input("Enter hex color: ")
print(is_valid_hex_color(color))