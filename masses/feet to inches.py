# feet to inches

def feet_to_inches(no_of_feet):
    number_of_inches = no_of_feet * 12
    return number_of_inches


def main():
    no_of_feet= float(input("enter the number of feet "))

    number_of_inches = feet_to_inches(no_of_feet)

    print(number_of_inches)

main()

week_day = int(input("enter the number of days ? "))

if week_day == 1:
    print("monday")

elif week_day == 2:
    print("tuesday")

elif week_day == 3:
    print("wednesday")

elif week_day == 4:
    print("thursday")

elif week_day == 5:
    print("friday")

elif week_day == 6:
    print("saturday")

else:
    print("sunday")



