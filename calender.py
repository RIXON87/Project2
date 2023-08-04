import calendar

year=int(input("Enter the year: "))
# month=int(input("Enter ther month(in numbers): "))
print("Mon\tTue\tWed\tThu\tFri\tSat\tSun")
for i in range(1,13):
    a = calendar.monthcalendar(year,i)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if(j%7==0):
                print("\n")        
            print(a[i][j], end="\t")
    print("\n")
    print("-----------------------------------")
    

# print("Su\tmo\ttu\twe\tth\tfr\tst")
# for i in range(1,32):
#     print(i, end="\t")
#     if(i%7==0):
#         print("\n")
# calender.