def hemoglobin_check():
    while True:
        sex = input("Enter biological sex (male/female): ").lower()
        if sex == "male" or sex == "female":
            break
        else:
            print("Invalid input. Please enter 'male' or 'female'.")
    while True:
        try:
            hb = float(input("Enter hemoglobin value (g/l): "))
            break
        except ValueError:
            print("Hemoglobin value must be a number.")

    if sex == "female":
        if hb < 117:
            print("Hemoglobin level is low.")
        elif hb > 155:
            print("Hemoglobin level is high.")
        else:
            print("Hemoglobin level is normal.")
    else:  # male
        if hb < 134:
            print("Hemoglobin level is low.")
        elif hb > 167:
            print("Hemoglobin level is high.")
        else:
            print("Hemoglobin level is normal.")
hemoglobin_check()