nome = str(input('Digite uma frase: '))
new = nome.upper()

print(f'A letrar A aparece: {new.count('A')} vezes')
print(f'A primeira vez que a letra A aparece é: {new.find('A')}')
print(f'A última vez que a letra A aparece é: {new.rfind('A')}')