def cadastrar(pessoas):
    cpf = input("Digite seu cpf: ")
    nome = input("Digite seu nome: ")
    idade = int(input("digite sua idade: "))
    pessoas.append((cpf, nome, idade))

def listar(pessoas):
    for pessoa in pessoas:
        cpf, nome, idade = pessoa
        print(f"""
                Nome: {nome}
                CPF: {cpf}
                Idade: {idade}
                """)

def exibirMenu():
    print("""
    
    1 - Cadastrar Pessoa
    2 - Listar Pessoa
    3 - Sair
            """)

def main():
    pessoas = []
    flag = True

    while flag:
        exibirMenu()

        try:
            opcao = int(input("Digite uma opção: "))
            if opcao == 1:
                cadastrar(pessoas)
            elif opcao == 2:
                listar(pessoas)
            elif opcao == 3:
                flag = False
            else:
                print("Digite apenas as opções indicadas.")
        except ValueError:
            print("Digite apenas números.")



main()