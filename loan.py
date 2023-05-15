import matplotlib.pyplot as plt

name = input("Type the name of the loan here: ")
loan_size = float(input("Type the size of the loan here: "))
monthly_payment = float(input("Type the amount you would like to pay every month: "))
yearly_interrest = float(input("Type in the yearly interrest here: "))

total = loan_size
total_paid = 0

loan_arr = []
year_arr = []

year = 0
print(name + ": " + str(round(loan_size)))
year_arr.append(year)
loan_arr.append(loan_size)
while loan_size > 0:
    # Payment
    payment = monthly_payment * 12
    loan_size = loan_size - payment

    # Interrest rate
    interrest = loan_size * (yearly_interrest / 100)
    loan_size = loan_size + interrest

    # Total
    total_paid += payment
    if loan_size < 0:
        total_paid += loan_size

    # Year
    year += 1
    year_arr.append(year)
    loan_arr.append(loan_size)
    print("Year: " + str(year))
    print("Remaining loan: " + str(round(loan_size)))
    print("Total paid: " + str(round(total_paid)))

# Generate graph
x=year_arr
y=loan_arr
plt.plot(x,y)
plt.xlabel('Year')
plt.ylabel('Remaning loan')
plt.title(name)
plt.show()
