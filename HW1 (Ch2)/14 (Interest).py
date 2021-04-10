print("This program calculates the balance of an account after a specific number of years\n")

principal = float(input("Enter the amount of principal originally deposited into the account: "))

annualRate = float(input("Enter the annual interest rate paid by the account: "))

timesPerYear = float(input("Enter the number of times per year that the interest is compounded: "))

yearsLeft = float(input("Enter the number of years the account will be left to earn interest: "))

#A = P(1+rn)^nt
#P = principal, r = annualRate, n = timesPerYear, t = yearsLeft

moneyAmount = principal * ((1 + (annualRate * timesPerYear)) ** (timesPerYear * yearsLeft))

print("\nThe amount of money that will be in the account after",format(yearsLeft, '.2f'), "years is $",format(moneyAmount, '.2f'))
