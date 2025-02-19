# functions in python

def total_tax_calculator(total_sales):
   calcCounty = total_sales * 0.02  # calculate county tax
   calcState = total_sales * 0.04  # calculate sate tax
   return calcCounty,calcState


def main():

   total_sales = float(input("Enter Your Monthly Sales: ")) # get user input on monthly sales

   # call the return function and assign it to the function header
   calcCounty,calcState = total_tax_calculator(total_sales)

   # calculate for the total sales
   total_sales = calcCounty + calcState

  # print the output on county tax, state tax and the total sales tax

   print(f"The county tax is: $ {calcCounty:.2f}")
   print(f"The state tax is: $ {calcState:.2f}")
   print(f"The total sales is: $ {total_sales:.2f}")

main()

total_sales = float(input("Enter Your Monthly Sales: "))

# calculate the calcCounty and calcState
calcCounty = total_sales * 0.02
calcState = total_sales * 0.04
total_sales = calcState + calcCounty

# print the output

print(f"The county tax is:${calcCounty:.2f}")
print(f"The state tax is: ${calcState:.2f}")
print(f"The total sales is: ${total_sales:.2f}")


def calcTotal(totalTax):
  calcState = totalTax * 0.04
  calcCounty = totalTax * 0.02
  return calcCounty,calcState

def main():
  totaltax = float(input("enter the total sales for the month: "))

  calcCounty,calcState = calcTotal(totaltax)

  totaltax = calcState + calcCounty

  print(f"the county tax is ${calcCounty:.2f}")
  print(f"the state tax is ${calcState:.2f}")
  print(f"the total tax is ${totaltax:.2f}")

main()

# monthly sales calculator
from masses.main import calcCounty, calcState


def monthly_sales(total_sales):
    calcCounty = total_sales * 0.025
    calcState = total_sales * 0.05
    return calcCounty,calcState

# define the main and request for user input
def main():
    total_sales = float(input("Enter the total sales for the month: "))

# call the return function and assign it to the function header

    calcCounty,calcState = monthly_sales(total_sales)

# formula for calculating the total sales

    total_sales = calcCounty + calcState

# print the output of monthly sales for the month, calcState tax and the
# calcCounty tax

    print(f"The county sales tax is:$ {calcCounty:.2f}")
    print(f"The state sales tax is:$ {calcState:.2f}")
    print(f"The total sales tax for the month is:$ {total_sales:,.2f}")

main()

