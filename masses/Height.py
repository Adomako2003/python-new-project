#Males and Females percentage

males = int(input("please enter the number of males"))

females = int(input("please enter the number of females"))

sumOfallStudents= males + females

male_percentage= (males/sumOfallStudents)*100

female_percentage= (females/sumOfallStudents)*100

print(f"Males, {male_percentage}%")

print(f"female, {female_percentage}%")
