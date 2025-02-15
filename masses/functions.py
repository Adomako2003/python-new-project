# A program to calculate the average number of wins over the past  5 years

year_1 = float(input("Enter the number of wins in year 1: "))
year_2 = float(input("Enter the number of wins in year 2: "))
year_3 = float(input("Enter the number of wins in year 3: "))
year_4 = float(input("Enter the number of wins in year 4: "))

year_5 = float(input("Enter the number of wins in year 5: "))

total_no_of_wins_in_5years = year_1 + year_2 + year_3 + year_4 + year_5

no_of_years = 5

average_number = total_no_of_wins_in_5years/no_of_years

print(f"The average number of wins of over 5 years: {average_number:.2f}")
print(f"The average number of wins of over 5 years: {average_number:,.4f}")














