hora = input('Digite APENAS a hora atual: ')

if int(hora) >= 0 and int(hora) <= 11:
    print('Bom Dia')
elif int(hora) >= 12 and int(hora) <= 17:
    print('Boa Tarde')
else:
    print('Boa Noite')