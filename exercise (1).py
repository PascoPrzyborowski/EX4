# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn



#Task 1
# print()
# print("Task1")
# print()

# for i in range (2):
#     print("Give me two Numbers to compare:")
#     print()
#     num1= int(input("Give me  number 1 :"))
#     print()
#     num2= int(input("Give me  number 2 :"))
#     #print(num1, num2)
#     print("Your first Number is:",num1)
#     print("Your second Number is:",num2)
#     if num1 == num2:
#         print("Numbers are equal!")
#     elif num1 != num2:
#         print("Numbers are not equal!")
#     if num1 > num2:
#         print("Fist number is greater than the second Number!")
#     elif num1 < num2:
#         print("Fist number is smaller than the second Number!")
#     if num2 > num1:
#         print("Second number is greater than the first Number!")
#     elif num2 < num1:
#         print("Second number is smaller than the first Number!")
#     if num1 >= num2:
#         print("Fist number is greater than or equal to the second Number!")
#     elif num1 <= num2:
#         print("Fist number is smaller than or equal to the second Number!")
#     if num2 >= num1:
#         print("Second number is greater than or equal to the first Number!")
#     elif num2 <= num1:
#         print("Second number is smaller than or equal to the first Number!")
#     if num1 > 100 and num2 > 100:
#         print("Both numbers are big!")
#     elif num1 < 100 and num2 < 100:
#         print("Both numbers are small")
#     if num1 > 100 and num2 > 100:
#         big_num = True
#         print("The big_num is set to: ", big_num)
#     elif num1 < 100 and num2 < 100:
#         big_num = False
#         print("The big_num is set to: ", big_num)


    

#Task 2

import time
import calendar

print()
print("Task2")
print()
print("Here is a Calendar List for You: ")
print()
time.sleep(1)
month = list(calendar.month_name)
print("List of month: ", month)
print()
for i in range(2):
    nameofmonth = input("Input the name of the month: ")
    print()
    print("Your choosen month is: ", nameofmonth)
    x = month.index(nameofmonth) 
#print((calendar.monthrange(2022, 3,)))
    _, num_days = calendar.monthrange(2022, x)
    last_day = (num_days)
    print("The Month", nameofmonth, "has this amount of Days: ", last_day)
#print(last_day)