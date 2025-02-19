SALARY = 30000.0
YEARS_ON_LOAN = 2

# get the user input

customer_salary = float(input("Enter your salary:$ "))
years_on_job = int(input("Enter the number of years on job: "))

# check whether the customer qualifies

if customer_salary >= SALARY:
    if years_on_job >= YEARS_ON_LOAN:
         print("You qualify for the loan")

    else:

         print("You must have been on your current job")

else:
    print(f"You must earn at least {SALARY}"
          f"per year to qualify")



