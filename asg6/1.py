numbers = []
while True:
    value = input("Enter a number (empty to quit): ")
    if value == "":
        break
    numbers.append(float(value))
numbers.sort(reverse=True)
print("Five greatest numbers:")
for num in numbers[:5]:
    print(num)