expenses=[2200,2350,2600,2130,2190]

extra_expenses_in_faburary_compare_to_janury=expenses[1]-expenses[0]
print(extra_expenses_in_faburary_compare_to_janury)
totale_expenses_in_first_three_month=sum(expenses[0:3])
print(totale_expenses_in_first_three_month)
for i in expenses:
    if i==2000:
        print("2000 is found")
        break
    else:
        print("2000 is not found")
        break

print(2000 in expenses)
expenses.append(1980)
print(expenses)
new_exp=expenses[3] - 200
expenses[3]=new_exp
print(expenses)
