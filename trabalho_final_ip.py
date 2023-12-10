# Inicialização das variáveis
fruta_em_estoque = ""  # Variável para armazenar o nome da fruta em estoque
quantidade_em_estoque = 0  # Variável para armazenar a quantidade da fruta em estoque

# Loop principal
while True:
    # Menu de opções
    print("\n===== Controle de Estoque de Frutas =====")
    print("1. Registrar Entrada de Frutas")
    print("2. Verificar Estoque")
    print("3. Registrar Venda de Frutas")
    print("4. Sair")

    # Obter a escolha do usuário
    escolha = input("Escolha uma opção (1/2/3/4): ")

    # Opção 1: Registrar Entrada de Frutas
    if escolha == "1":
        if fruta_em_estoque == "":  # Verificar se já foi registrada uma fruta em estoque
            fruta_em_estoque = input("Digite o nome da fruta que chegou: ")
        
        quantidade_entrada = int(input("Digite a quantidade de frutas recebidas: "))
        
        # Atualizar o estoque
        quantidade_em_estoque += quantidade_entrada

        print(f"{quantidade_entrada} {fruta_em_estoque}(s) foram adicionados ao estoque.")

    # Opção 2: Verificar Estoque
    elif escolha == "2":
        if fruta_em_estoque == "":  # Verificar se há uma fruta registrada em estoque
            print("Nenhuma fruta em estoque.")
        else:
            print(f"O estoque atual de {fruta_em_estoque} é de {quantidade_em_estoque} unidades.")

    # Opção 3: Registrar Venda de Frutas
    elif escolha == "3":
        if fruta_em_estoque == "":  # Verificar se há uma fruta registrada em estoque para vender
            print("Nenhuma fruta em estoque para vender.")
        else:
            quantidade_venda = int(input(f"Digite a quantidade de {fruta_em_estoque}(s) vendida(s): "))
            
            # Verificar se há estoque suficiente
            if quantidade_venda <= quantidade_em_estoque:
                quantidade_em_estoque -= quantidade_venda
                print(f"{quantidade_venda} {fruta_em_estoque}(s) foram vendidos.")
            else:
                print("Quantidade insuficiente em estoque. Venda não realizada.")

    # Opção 4: Sair do Programa
    elif escolha == "4":
        print("Saindo do programa. Até mais!")
        break

    # Opção inválida
    else:
        print("Opção inválida. Tente novamente.")