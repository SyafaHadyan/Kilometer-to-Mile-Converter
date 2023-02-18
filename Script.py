user_input = input("KM:")
KM = user_input

if user_input.isdigit():
    Mile = float(KM) / 1.609344
    print(f"Mile: {Mile}")

else:
    print("Invalid KM value, please insert a valid number")