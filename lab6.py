# Matthew Khan
def encode(sequence):
    encoded_sequence = ""
    for digit in str(sequence):
        encoded_digit = str((int(digit) + 3) % 10)  # Ensure the result stays a single digit (0-9)
        encoded_sequence += encoded_digit
    return int(encoded_sequence)

# Caleb Karimov
def decode(encoded_sequence):
    output = ""
    for number in encoded_sequence:
        add_to_output = int(number)
        add_to_output -= 3
        if add_to_output < 0:
            add_to_output += 10
        output += str(add_to_output)
    return output

def main():
    while True:
        print("Menu\n-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")
        choice = input("Please enter an option: ")

        if choice == '1':
            original_password = int(input("Please enter your password to encode: "))
            encoded_password = encode(original_password)
            print("Your password has been encoded and stored!")
            print("")

        elif choice == '2':
                print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.")
                print("")
        elif choice == '3':
            break

if __name__ == "__main__":
    main()
