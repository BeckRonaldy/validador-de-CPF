import random

def gerador():
    # Gera os nove primeiros dígitos do CPF
    numeros_cpf = [random.randint(0, 9) for _ in range(9)]

    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += numeros_cpf[i] * (10 - i)
    resto = soma % 11
    if resto < 2:
        numeros_cpf.append(0)
    else:
        numeros_cpf.append(11 - resto)

    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += numeros_cpf[i] * (11 - i)
    resto = soma % 11
    if resto < 2:
        numeros_cpf.append(0)
    else:
        numeros_cpf.append(11 - resto)

    # Formata o CPF
    cpf = ''.join(map(str, numeros_cpf))
    cpf_formatado = f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    return cpf_formatado
