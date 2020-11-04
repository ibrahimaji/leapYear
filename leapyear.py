print('Program to check leap year')
print('0 will finish the program')

while True:
    year=int(input('Put year to check if it leap or not : '))
    if year==0:
        break
    if year % 4==0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year}. is leap year.")
            else:
                print(f"{year}. is not leap and have 365 days.")
        else:
            print(f"{year}. is leap year.")
    else:
        print(f"{year}. is not leap and have 365 days")