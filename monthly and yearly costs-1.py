def show_expenses(loan, insurance, gas, oil, tires, maintenance):
    monthly_cost = (loan + insurance + gas + oil + tires + maintenance)
    print ("your monthly costs are: ", monthly_cost)
    annual_cost = monthly_cost * 12
    print ("your yearly cost is: ", annual_cost)
#display outcomes

#find expenses


loan = float(input("Enter the cost of the loan payment: "))
insurance = float(input("Enter the cost of insurance: "))
gas = float(input("Enter the cost of gas: "))
oil = float(input("Enter the cost of oil: "))
tires = float(input("Enter the cost of tires: "))
maintenance = float(input("Enter the cost of maintenance: "))
#monthly expenses

show_expenses(loan, insurance, gas, oil, tires, maintenance)

