import time
saldo = 0
produtos_lista = []
cadastros = []
print('-'*10,'Menu do produto', '-'*10)
cores = {
    "limpa":"\033[m",
    "amarelo":"\033[33m",
    "vermelho":"\033[31m",
    "verde":"\033[32m",
}
taxas = {
    'm': 0.12,  
    'e': 0.08,  
    'n': 0.05   
}

opcao = """
Função:
1 - Gerente
2 - Cliente
3 - Sair
"""
opcaoGerente = """
Gerente:
1 - Cadastrar Produto
2 - Cadastrar Cliente
3 - Sair
"""

menuProduto = """
Menu dos produtos:
1 - Cadastrar produto 
2 - Listar produtos cadastrados
3 - Atualizar produto (digite o codigo)
4 - Excluir produto
5 - Sair
"""
menu_cadastro_cliente = """
Menu do cadastro cliente:
1 - Cadastrar Cliente
2 - Listar clientes
3 - Atualizar perfil do cliente (digite o cpf)
4 - excluir cliente
5 - Sair
"""
menu_do_cliente = """
Menu do cliente:
0 - Fazer login (Caso já tenha)
1 - Colocar no carrinho
2 - Listar Carrinho
3 - Retirar do Carrinho (digite o codigo)
4 - Comprar
5 - Sair
"""

i = 0

estoque_cheio = False

while True:

    print(opcao)
    informacaOpcao = int(input('Qual função você è:'))

    sair_gerente = False

    if informacaOpcao == 1:
        while not sair_gerente:
            print(opcaoGerente)
            gerente = int(input('Escolha a opção desejada:'))
            if gerente == 1:
                    while True:
                        print(menuProduto)
                        try:
                            informacaoDoMenu = int(input('digite o valor:'))
                            if informacaoDoMenu == 1:
                                sair_cadastro_produto = False
                                while not sair_cadastro_produto:
                                    print("="*10,'CADASTRO DO PRODUTO','='*10)
                                    try:    
                                        produto = {
                                            'codigo' : int(input('Digite o codigo do produto: ')),
                                            'nome' : input('Digite o nome do produto: '),
                                            'preco' : float(input('Digite o preço do produto: R$')),
                                            'estoque' : int(input('Digite a quantidade que deseja: ')),
                                        }

                                        codigo_existe = False

                                        for p in produtos_lista:
                                            if p['codigo'] == produto['codigo']:
                                                codigo_existe = True
                                                break

                                        if codigo_existe:
                                            print(f"{cores['vermelho']}Já existe um produto com esse código.{cores['limpa']}")
                                            continue

                                        while True:
                                            imposto = input("Digite o imposto (m-municipal | e-estadual | n-nacional): ").lower()
                                            if imposto in ['m','n','e']:
                                                break
                                            else:
                                                print(f"{cores["vermelho"]}Erro: Digite apenas 'n', 'e' ou 'm'.{cores["limpa"]}")

                                        produto['imposto'] = imposto
                                        produtos_lista.append(produto)
                                        estoque_cheio = True

                                        sair = int(input('deseja sair (1- sim | 2 - não): '))

                                        if sair == 1:
                                            print(f"{cores['verde']}Produto cadastrado...{cores['limpa']}")
                                            print(f"{cores['verde']}Saiu do cadastro{cores['limpa']}")
                                            sair_cadastro_produto = True
                                        elif sair == 2: 
                                            print(f"{cores["verde"]}Produto cadastrado...{cores["limpa"]}")
                                            

                                    except ValueError:
                                        print(f"{cores['vermelho']}ERROR...{cores['limpa']}")
                                        continue


                            
                            if informacaoDoMenu == 2:
                                    print('-'*10,'Lista de produtos cadastrados','-'*10)
                                    for p in produtos_lista:
                                        print(f"Nome: {p['nome']} \t|\t codigo{p['codigo']} \t|\t Estoque: {p['estoque']}")
                                    print('='*49)

                            if informacaoDoMenu == 3:
                                print('-'*10,'Atualizar produtos','-'*10,'\n')

                                time.sleep(1)
                                
                                for p in produtos_lista:
                                    print(f"Nome: {p['nome']} \t|\t codigo: {p['codigo']} \t|\t Estoque: {p['estoque']}")
                                
                                resposta = int(input('Digite o codigo do produto que dejesa atualizar: '))
                                verificacaoCodigo = False
                                
                                for p in produtos_lista:
                                
                                    if p['codigo'] == resposta:
                                        print(f'{cores["verde"]}PRODUTO ENCONTRADO COM SUCESSO{cores["limpa"]}')
                                        p['estoque'] = int(input('Digite a quantidade no estoque: '))
                                        p['nome'] = input('Digite o novo nome: ')
                                        p['preco'] = float(input('Digite o preço: R$'))
                                        verificacaoCodigo = True
                                        break
                                    
                                    if not verificacaoCodigo:
                                        print(f'{cores['vermelho']}Codigo não foi encontrado{cores["limpa"]}')
                                
                                print('-'*40)

                            if informacaoDoMenu == 4:
                                print('-'*10,'Excluir produtos','-'*10)
                                
                                for p in produtos_lista:
                                    print(f"Produto: {p['nome']} \t|\t Codigo: {p['codigo']}")
                                
                                resposta = input('Deseja excluir produto (s/n):').lower()
                                
                                if resposta == "s":
                                    try:
                                        excluir = int(input('Insira o codigo do produto para excluir: '))
                                    except ValueError:
                                        print(f'{cores["vermelho"]}Insira apenas numeros...{cores["limpa"]}')       
                                    produto_encontrado = False
                                
                                    for p in produtos_lista: 
                                            if p['codigo'] == excluir:
                                                produtos_lista.remove(p)
                                                print(f'{cores["verde"]}PRODUTO REMOVIDO COM SUCESSO{cores["limpa"]}')
                                                produto_encontrado = True
                                                break
                                            elif not produto_encontrado:
                                                print(f'{cores["vermelho"]}Produto não encontrado...{cores["limpa"]}')

                                if resposta == "n":
                                    print('voltando para o menu...')
                                    time.sleep(2)
                                else:
                                    print(f'{cores["vermelho"]} Valor digitado errado {cores["limpa"]}')
                                
                                print('='*36)

                            if informacaoDoMenu == 5:
                                print("Voce saiu")
                                break
                        
                        except KeyError:
                            print()

            elif gerente == 2:
                    while True:
                        print(menu_cadastro_cliente)
                        informaCliente = int(input('qual opção deseja: '))
                
                        if informaCliente == 1:
                            while True:
                
                                pessoa = {
                                    "cpf": input('Digite seu cpf: '),
                                    "nome": input('Digite seu nome: '),
                                    "email": input('Digite seu email: '),
                                    "fone": input('Digite teu telefone: '),
                                    "cidade": input('Digite sua Cidade: '),
                                    "senha" : input('Digite sua Senha: ')
                                }
                                print(f'{cores["verde"]}pessoa cadastrada..{cores["limpa"]}')
                                cpf_existe = False
                                for p in cadastros:
                
                                    if p['cpf'] == pessoa['cpf']:
                                        cpf_existe = True
                                        continue
                                    if cpf_existe:
                                        print(f'{cores["vermelho"]}Erro.. Cpf já inserido {cores['limpa']}')
                                    else:
                                        cadastros.append(pessoa)

                                sair = input('Deseja sair (s/n): ').lower()
                
                                if sair == 's':
                                    print(f'{cores["verde"]}Saiu do cadastro...{cores["limpa"]}')
                                    break
                
                                else:
                                    print(f'{cores["verde"]}Informações cadastradas{cores["limpa"]}')
                                    time.sleep(2)
                                    print(f'{cores["verde"]}Novo cadastro{cores["limpa"]}')

                        if informaCliente == 2:
                            print('='*10,'Lista dos Clientes', '='*10)
                
                            for gerente in cadastros:
                                print(f'NOME: {gerente['nome']} \t| EMAIL: {gerente['email']} \t| FONE: {gerente['fone']} \t| CIDADE: {gerente['cidade']}')    

                        if informaCliente == 3:
                            print('='*10,'Atualizar informações do Cliente','='*10)

                            time.sleep(1)

                            for gerente in cadastros:
                                print(f'NOME: {gerente['nome']} \t| EMAIL: {gerente['email']} \t| FONE: {gerente['fone']} \t| CPF: {gerente['cpf']}')    


                            atualizar_Cliente = input('Digite Cliente que queira excluir pelo cpf: ')

                            for c in cadastros:
                                if c['cpf'] == atualizar_Cliente:
                                    c['nome'] = input('Nome: ')
                                    c['cpf'] = input('Cpf: ')
                                    c['fone'] = input('Fone: ')
                                    c['email'] = input('Email: ')

                        if informaCliente == 4:
                            print("="*10,'Excluir cadastro',"="*10)
                
                            for gerente in cadastros:
                                print(f'NOME: {gerente['nome']} \t| CPF: {gerente['cpf']}')    


                            resposta = input('Deseja excluir cadastro (s/n):').lower()
                            
                            if resposta == "s":
                
                                try:
                                    excluir = int(input('Insira o CPF do produto para excluir: '))
                
                                except ValueError:
                                    print(f'{cores["vermelho"]}Insira apenas numeros...{cores["limpa"]}')       
                                produto_encontrado = False
                            
                                for p in cadastros: 
                
                                        if p['cpf'] == excluir:
                                            cadastros.remove(p)
                                            print(f'{cores["verde"]}CLIENTE REMOVIDO COM SUCESSO{cores["limpa"]}')
                                            produto_encontrado = True
                                            break
                
                                        elif not produto_encontrado:
                                            print(f'{cores["vermelho"]}Cliente não encontrado...{cores["limpa"]}')

                            if resposta == "n":
                                print('voltando para o menu...')
                                time.sleep(2)
                
                            else:
                                print(f'{cores["vermelho"]} Valor digitado errado {cores["limpa"]}')
                            
                            print('='*36)

                        if informaCliente == 5:
                            print("Voce saiu")
                            break
            
            elif gerente == 3:
                print('Saiu')
                sair_gerente = True

    if informacaOpcao == 2:
            saldo = int(input('Quanto voce tem na carteira: R$'))
            carrinho = []

            if estoque_cheio == False:
                print('Antes tem que cadastrar os produtos')
            else:
                print('Estoque liberado')
                while estoque_cheio:
                    print(menu_do_cliente)
                    
                    caixa = int(input('Escolha a ação desejada: '))
                    cliente_logado = {"nome": "Não informado", "email": "Não informado"}

                    if caixa == 0:

                        email_login = input('Email:')
                        senha_login = input('Senha:')
                        for c in cadastros:
                            if c['email'] == email_login and c['senha'] == senha_login:
                                cliente_logado = c
                                print(f"{cores['verde']}Login realizado!{cores['limpa']}")
                                break
                    
                    if caixa == 1:
                    
                        for p in produtos_lista:
                            print(f'Produto: {p['nome']} \t| Preco: {p['preco']} \t| Codigo: {p['codigo']}')
                        cod_escolha = int(input('Digite o codigo do produto: '))
                        try:
                            for c in produtos_lista:
                                if c['codigo'] == cod_escolha:
                                    qtd = int(input('Digite a quantidade: '))
                                    if qtd <= c['estoque']:
                                        c['estoque'] -= qtd
                                        item_carrinho = {
                                        'codigo': c['codigo'], 'nome': c['nome'],
                                        'preco': c['preco'], 'quantidade': qtd,
                                        'subtotal': c['preco'] * qtd,
                                        'imposto_tipo': c['imposto']
                                    }
                                        carrinho.append(item_carrinho)
                                        print(f'{cores["verde"]}Produto adicionado!{cores["limpa"]}')
                                    
                                    else:
                                        print(f'{cores["vermelho"]}Estoque insuficiente!{cores["limpa"]}')
                                        break

                        except:
                            print(f'{cores["vermelho"]} Apenas nomes {cores["limpa"]}')
                    
                    if caixa == 2:
                    
                        print('-'*10,'Lista de produtos cadastrados','-'*10)
                    
                        for p in produtos_lista:
                            print(f"Nome: {p['nome']} \t|\t codigo{p['codigo']} \t|\t Estoque: {p['estoque']}")
                        print('='*49)
                    
                    if caixa == 3:
                        print('-'*10,'Retirar Do Carrinho','-'*10)
                                
                        for p in produtos_lista:
                            print(f"Produto: {p['nome']} \t|\t Codigo: {p['codigo']}")
                        
                        resposta_cliente = input('Deseja retirar produto do carrinho (s/n):').lower()
                        
                        if resposta_cliente == "s":
                            try:
                                excluir = int(input('Insira o codigo do produto para excluir: '))
                    
                            except ValueError:
                                print(f'{cores["vermelho"]}Insira apenas numeros...{cores["limpa"]}')       
                            produto_encontrado = False

                            quantidade_retirada = 0
                            
                            for p in carrinho: 
                                if p['codigo'] == excluir:
                                    quantidade_retirada = p['codigo']
                                    
                                    for prod in carrinho:
                                        if prod['codigo'] == prod['codigo']:
                                            prod['estoque'] += quantidade_retirada
                                            break

                                        carrinho.remove(p)
                                        print(f'{cores["verde"]}PRODUTO REMOVIDO COM SUCESSO{cores["limpa"]}')
                                        produto_encontrado = True
                                        break

                                elif not produto_encontrado:
                                    print(f'{cores["vermelho"]}Produto não encontrado...{cores["limpa"]}')

                        if resposta_cliente == "n":
                            print('voltando para o menu...')
                            time.sleep(2)
                    
                        else:
                            print(f'{cores["vermelho"]} Valor digitado errado {cores["limpa"]}')
                        
                        print('='*36)
                    if caixa == 4:
                        print('='*10,'CUPOM FISCAL','='*10)
                        print(f'\n Nome: {cliente_logado['nome']} | Email: {cliente_logado['email']}')

                        print("\nProdutos:")
                        total_compra = 0
                        for i in carrinho:
                            print(f'Nome: {i['nome']} | Preço: R${i['preco']} | SubTotal: R${i['subtotal']} | Quantidade: {i['quantidade']}')
                            total_compra += i['subtotal']
                        
                        total_compra = 0
                        total_impostos = 0
                        
                        print("-" * 45)
                        for item in carrinho:
                            
                            taxa_aplicada = taxas[item['imposto_tipo']]
                            valor_imposto_item = item['subtotal'] * taxa_aplicada
                            
                            total_compra += item['subtotal']
                            total_impostos += valor_imposto_item
                            
                            print(f"{item['nome']} (x{item['quantidade']})")
                            print(f"   Subtotal: R${item['subtotal']:.2f} | Imposto ({item['imposto_tipo']}): R${valor_imposto_item:.2f}")
                        
                        print("-" * 45)
                        print(f"SUBTOTAL PRODUTOS: R${total_compra:.2f}")
                        print(f"TOTAL IMPOSTOS:    R${total_impostos:.2f}")
                        print(f"{cores['verde']}TOTAL GERAL:       R${total_compra + total_impostos:.2f}{cores['limpa']}")
                        print("="*45)

                        carrinho = []

                    if caixa == 5:
                        print('saiu')
                        break
        
    if informacaOpcao == 3:
        print('saiu de tudo fiii')
        break


