def remove_odd(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result
def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    new_list = remove_odd(numbers)
    print("Original list:", numbers)
    print("Without odd numbers:", new_list)
main()