# Switch case in python

def switch_case(n):
    switcher = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return switcher.get(n,"Type correct number")


flag = True
while flag:
    n = int(input("Enter a number from 1-7 : "))
    print(switch_case(n))
    if n == 0:
        flag = False
        print("program has stopped.")
