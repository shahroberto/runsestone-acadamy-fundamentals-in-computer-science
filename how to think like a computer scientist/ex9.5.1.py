person = raw_input('Your Name: ')
print('Hello {}!'.format(person))

origPrice = float(raw_input('Enter the original price: $'))
discount = float(raw_input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${:.2f} discounted by {}% is ${:.2f}.'.format(origPrice, discount, newPrice)
print(calculation)
