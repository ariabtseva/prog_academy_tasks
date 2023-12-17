# Task 1

text = input('text = ')
res = {}

for word in text.split():
    word = word.strip('.,!?()[]{}"\'')
    res[word] = text.count(word)

print(res)

#or 
res = {word: text.count(word) for word in text}
#or
for word in text.split():
    if word not in res:
        res[word] = text.count(word)

# Task 2

translations = {
    'hello': 'привіт',
    'goodbye': 'до побачення',
    'cat': 'кіт',
    'dog': 'собака'
}

translations_reverse = {value: key for key, value in translations.items}

word = input('Word: ').strip().lower()
if word in translations:
    translation = translations.get(word, 'Word not found')
    print(f'{word} - {translation}')
else:
    print(translations_reverse.get(word, 'No translation'))
    keys, values = tuple(translations.keys()), tuple(translations.values())
    if word in values:
        value_index = values.index(word)
        print(keys[value_index])
    else:
        print('No translations')

# Task 3

contacts = {}

while True:
    option = input('Add/Delete/Get contact: ')

    if option == 'Add':
        name = input('name = ')
        number = (input('number = '))
        contacts[name] = number
        print('Contact saved')
    
    elif option == 'Delete':
        remove_name = input('Delete contact: ')
        if remove_name in contacts:
            contacts.pop(remove_name, None)
            print(f'{remove_name} was deleted successfully')  
        else:
            print('Contact not found')

    elif option == 'Get':
        find_name = input('Enter name: ')
        print(f'{find_name}: {contacts.get(find_name, "Contact not found")}')

    else:
        print('Error')
    
    break

# Task 4

money = float(input('Enter amount:'))
conv_from = (input('Converting from (UAH, USD, EUR, GBP, JPY):')).upper()
conv_to = (input('Converting to (UAH, USD, EUR, GBP, JPY):')).upper()

exchange_rates = {
    'UAH': 1.0,
    'USD': 36.26,
    'EUR': 39.72,
    'GBP': 45.79,
    'JPY': 0.24
}

converted = money * exchange_rates[conv_from] / exchange_rates[conv_to]

print(f'Equals {converted:.2f} {conv_to}')