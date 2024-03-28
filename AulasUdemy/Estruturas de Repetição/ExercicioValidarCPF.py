cpf = '74682489070'
cpf_9dig = cpf[:9]
cpf_10dig = cpf[:10]
contador1 = 10
contador2 = 11
pDigito = 0
sDigito = 0
for n in cpf_9dig:
    pDigito += int(n) * contador1
    contador1 -= 1
pDigito = (pDigito * 10) % 11
pDigito= pDigito if pDigito <= 9 else 0
for n in cpf_10dig:
    sDigito += int(n) * contador2
    contador2 -= 1
sDigito = (sDigito * 10) % 11
sDigito = sDigito if sDigito <= 9 else 0
novo_cpf = f'{cpf_9dig}{pDigito}{sDigito}'
if cpf == novo_cpf:
    print('CPF Válido')
else:
    print('CPF Inválido')