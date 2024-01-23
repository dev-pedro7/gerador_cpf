import random

def formatar_cpf(cpf):
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

for _ in range(1):
    nine_digit =''
    for i in range(9):
        nine_digit += str(random.randint(0, 9))

    contagem_multiplicacao = 10
    resultado = 0
    for digit in nine_digit:
        resultado += int(digit) * contagem_multiplicacao
        contagem_multiplicacao -= 1
    result_1 = (resultado* 10) %11
    result_1 = result_1 if result_1 <= 9  else 0

    #O segundo dígito do CPF 
    ten_digit = nine_digit + str(result_1)
    contagem_multiplicacao = 11
    resultado = 0
    for digit in ten_digit:
        resultado += int(digit) * contagem_multiplicacao
        contagem_multiplicacao -= 1
    result_2 = (resultado* 10) %11
    result_2 = result_2 if result_2 <= 9  else 0

    cpf_gerado_pelo_calculo = f'{nine_digit}{result_1}{result_2}'
    cpf_formatado =formatar_cpf(cpf_gerado_pelo_calculo)
    print('Gerando CPF valido...')
    print(f'CPF: {cpf_formatado}')
   