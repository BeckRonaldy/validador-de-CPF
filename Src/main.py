from validadorCPF import validador
from geradorCPF import gerador

# Menu inicial
if __name__ == '__main__':
    while(True):
        opc = int(input("Informe uma opção:\n1 - Validador de CPF\n2 - Gerador de CPF\n3 - Sair\n> "))
        if(opc == 1):
            cpf = input("Digite o CPF (formato: 000.000.000-00): ")
            print(validador(cpf) + "\n")
        elif(opc == 2):
            print("CPF gerado:", gerador() + "\n")
        else: break
    