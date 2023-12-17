import re

with open('hw_10_test.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

items_expenses = {}
family_expenses = {}
user_total_purchases = 0
user_total_amount = 0

user_member = input('Family member: ')

for line in lines:
   parts = re.split(r'\s+', line.strip())

   items = parts[-1]
   amount = float(parts[-2][:-1])

   if items in items_expenses:
       items_expenses[items] += amount
   else:
       items_expenses[items] = amount

   member = " ".join(parts[1:-2])
   if member in family_expenses:
       family_expenses[member] += amount
   else:
       family_expenses[member] = amount

   if member == user_member:
       user_total_purchases += 1
       user_total_amount += amount

print('\n1. Total expenses in each product category:')
for category, total in items_expenses.items():
    print(f'{category}: ${total:.2f}')

print('\n2. Amount spent by each family member:')
for member, total in family_expenses.items():
    print(f'{member}: ${total:.2f}')

print(f'\n3. Information about expenses for {user_member}:')
print(f'Total number of purchases: {user_total_purchases}')
print(f'Total amount spent: ${user_total_amount:.2f}')