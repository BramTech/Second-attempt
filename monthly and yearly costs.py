
#find expenses
def show_cost(loan, insurance, gas, oil, tires, maintenance, month,):
    monthly_cost = (loan + insurance + gas + oil + tires + maintenance)
    per_annum = (monthly_cost * 12)
    year_to_date_cost = (monthly_cost * x)
    remaining_months = (12 - x)
    remaining_cost = (monthly_cost * remaining_months)
    print ("your monthly costs are: ", monthly_cost)
    print ("your yearly costs are: ", per_annum,)
    print ("your current expenses so far this year are: ", year_to_date_cost)
    print ("your costs for the remainder of this year are:", remaining_cost)

loan = int(input("Enter the cost of the loan payment: "))
insurance = int(input("Enter the cost of insurance: "))
gas = int(input("Enter the cost of gas: "))
oil = int(input("Enter the cost of oil: "))
tires = int(input("Enter the cost of tires: "))
maintenance = int(input("Enter the cost of maintenance: "))
month = str(input("What month is it now? "))
#monthly expenses
if (month) == ("january") or (month) == ("January"):
    x = 1
elif (month) == ("february") or (month) == ("February") :
    x = 2
elif (month) == ("march") or (month) == ("March"):
    x = 3
elif (month) == ("april") or (month) == ("Aril"):
    x = 4
elif (month) == ("may") or (month) == ("May"):
    x = 5
elif (month) == ("june") or (month) == ("June"):
    x = 6
elif (month) == ("july") or (month) == ("July"):
    x = 7
elif (month) == ("august") or (month) == ("August"):
    x = 8
elif (month) == ("september") or (month) == ("September"):
    x = 9
elif (month) == ("october") or (month) == ("October") :
    x = 10
elif (month) == ("november") or (month) == ("November"):
    x = 11
elif (month) == ("december") or (month) == ("December"):
    x = 12
else:
    x = 0
    print ("Invalid value")
show_cost(loan, insurance, gas, oil, tires, maintenance, month)
