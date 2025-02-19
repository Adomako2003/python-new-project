# feet to inches

def feet_to_inches(feet):
    number_of_inches = feet * 12
    return number_of_inches

def main():
    feet = float(input("Enter the number of feet: "))

    number_of_inches = feet_to_inches(feet)

    print(f"The number of inches:{number_of_inches}")


main()


# falling objects

def falling_distance(distance,g,t):
     distance = 0.5*g*t**2
     return distance

def main():
     d = float



