last=2500
start=1800
year=int(input("Enter a year between 1800-2500: "))
if(year>start and year<last):

    if(year%4==0):
        print("This is a leap year")
    else:
        print("This is not a leap year")
else:
    print("Not a valid input")
    print("**********Restart the program**********")        