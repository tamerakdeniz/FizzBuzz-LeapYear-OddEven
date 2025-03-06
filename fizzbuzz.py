# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

def main():
    try:
        request = int(input("Enter a number to count up to: "))
        if request <= 0:
            print("Please enter a positive number.")
            return
        fizz_buzz(request)
    except ValueError:
        print("Please enter a valid integer number.")

if __name__ == "__main__":
    main()