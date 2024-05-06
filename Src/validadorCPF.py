def is_digit(c):
    return c.isdigit()

def calcula_digito(cpf, inicio, fim):
    soma = 0
    for i in range(inicio, fim + 1):
        soma += int(cpf[i]) * (fim + 2 - i)
    resto = soma % 11
    if resto < 2:
        return 0
    else:
        return 11 - resto

def validador(cpf):
    # Verifica se o CPF tem o formato correto
    for i in range(len(cpf)):
        if i == 3 or i == 7:
            if cpf[i] != '.':
                return False
        elif i == 11:
            if cpf[i] != '-':
                return False
        elif not is_digit(cpf[i]):
            return False
    
    # Remove os pontos e o traços do CPF
    numeros_cpf = ''.join(filter(str.isdigit, cpf))

    # Calcula os dígitos verificadores
    first_digit = calcula_digito(numeros_cpf, 0, 8)
    second_digit = calcula_digito(numeros_cpf, 0, 9)

    # Verifica se os dígitos verificadores estão corretos
    if int(numeros_cpf[9]) == first_digit and int(numeros_cpf[10]) == second_digit:
        return str("CPF válido.")
    else:
        return str("CPF inválido.")
