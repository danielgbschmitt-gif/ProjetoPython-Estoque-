nomes = []
precos = []
quantidades = []

while True:

    print ("\n=== SUPERMERCADO ===")
    print ("1 - Cadastrar Produtos")
    print ("2 - Listar Produtos")
    print ("3 - Buscar Produtos")
    print ("4- Produto mais caro")
    print ("5 - Valor total do estoque")
    print ("6 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Digite o nome do protuto: ")
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade do produto: "))

        nomes.append (nome)
        precos.append (preco)
        quantidades.append (quantidade)

        print ("Produto cadastrado com sucesso!")
    
    elif opcao == 2:
        for i in range(len(nomes)):
            print ("\nProduto ", i + 1)
            print ("Nome:", nomes[i])
            print ("Preço:", precos[i])
            print ("Quantidade:", quantidades[i])

    elif opcao == 3:
        busca = input("\nDigite o nome do produto:")

        if busca.lower() in nomes.lower():
            i = nomes.index(busca)

            print ("Nome:", nomes[i])
            print ("Preço:", precos[i])
            print ("Quantidade:", quantidades[i])
        else:
            print ("Produto não encontrado.")

    elif opcao == 4:
        if len(precos) > 0:
            mscaro = precos[0]
            pos = 0

            for i in range(1, len(precos)):
                if precos[i] > mscaro:
                    mscaro = precos[i]
                    pos = i

            print(f"O produto mais caro é um(a) {nomes[pos]} e custa R$ {precos[pos]:.2f}")
        else:
            print("Nenhum produto cadastrado.")

    elif opcao == 5:
        if(len(precos)):
            total = 0

        for i in range(len(precos)):
            total = total + (precos[i] * quantidades[i])

        print(f"O valor total do estoque é R$ {total:.2f}")

    elif opcao == 6:
        print("Saindo...")
        break
