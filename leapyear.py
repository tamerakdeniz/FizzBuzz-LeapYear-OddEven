def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    try:
        year = int(input("Enter a year to check if it's a leap year: "))
        if is_leap(year):
            print(f"{year} is a leap year!")
        else:
            print(f"{year} is not a leap year.")
    except ValueError:
        print("Please enter a valid year (integer number).")

if __name__ == "__main__":
    main()