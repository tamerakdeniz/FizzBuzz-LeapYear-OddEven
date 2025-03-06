def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."

def main():
    try:
        number = int(input("Enter a number to check if it's odd or even: "))
        result = odd_or_even(number)
        print(result)
    except ValueError:
        print("Please enter a valid integer number.")

if __name__ == "__main__":
    main()
