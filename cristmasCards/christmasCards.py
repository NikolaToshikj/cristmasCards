import os

file=open('employees.txt', 'r')
names = file.read().splitlines()

file=open('template.txt', 'r')
template = file.read()

# Create christmasCards directory if it doesn't exist
os.makedirs('christmasCards', exist_ok=True)

# Generate cards for each employee
for name in names:
    
    card_content = template.replace('NAME', name)

    
    card_path = os.path.join('christmasCards', f'{name}.txt')
    with open(card_path, 'w') as file:
        file.write(card_content)

    print(f'Created card for {name} at {card_path}')
