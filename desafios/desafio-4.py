tipo = input('Digite algo: ')
print(type(tipo))

# verifica se eh alfanumerico e retorna False ou True
print('Alfanumérico? {}'.format(tipo.isalnum()))

# verifica se eh numerico
print('Numérico? {}'.format(tipo.isnumeric()))

# verifica se eh alfabetico
print('Alfabético? {}'.format(tipo.isalpha()))

# verifica se tudo escrito eh minusculo
print('Minúsculo? {}'.format(tipo.islower()))

# verifica se tudo escrito eh maiusculo
print('Maiúsculo? {}'.format(tipo.isupper()))
