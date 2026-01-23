def check_zander_size():
    size = float(input("Enter the length of the zander (cm): "))
    limit = 42

    if size < limit:
        print("Release the fish back into the lake.")
        print(f"It is {limit - size:.1f} cm below the size limit.")
    else:
        print("The zander meets the size limit.")
check_zander_size()