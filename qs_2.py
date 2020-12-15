#Leap year is defined as year which is exactly divisible by 4 except for century year i.e years ending with 00. 
#Century year is a year which is divisible by 400

year = int(input("Enter a leap year:"))
if (year%4 == 0 and year%100 !=0 or year%400==0  ):
    print("The year is a leap year")

else:
    print("The year is not a leap year")
