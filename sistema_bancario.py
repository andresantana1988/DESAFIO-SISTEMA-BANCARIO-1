menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


numero_saques = 0
saldo_conta =  0 
extrato = [] # cada item dessa lista será uma das operações
valor_maximo_saque = 500
LIMITE_SAQUES = 3
frase_operacao = ""
numero_operacoes_realizadas = 0


def validar_valor(valor:str) ->float:
    try:
        valor_formatado = float(valor)
        if valor_formatado <=0:
            print("Informe valores positivos")
            valor_formatado = 0    
    except:
        raise ValueError("Informe um valor numérico !")    
   
    return valor_formatado


while True:
    opcao = input(menu)
    print(opcao)
    
    if opcao.lower() =="d":
        valor = input("Informe o valor para o depósito: ")
        try:
            valor_depositado = validar_valor(valor)
            if valor_depositado > 0:
                saldo_conta += valor_depositado
                frase_operacao = 'Depósito:' + f'R$ {valor_depositado :.2f}'.rjust(31,' ')
                extrato.append(frase_operacao)
                numero_operacoes_realizadas += 1
        except ValueError as e:
            print (e)
          
    elif opcao.lower() =="s":
        valor = input("Informe o valor para o Saque:")
        try:
            valor_do_saque = validar_valor(valor)
            if valor_do_saque > 0:
                if valor_do_saque > 500:
                    print(f'O valor máximo de saque é de R$ {valor_maximo_saque :.2f} ')
                elif numero_saques >= LIMITE_SAQUES:
                    print(f'Limite de {LIMITE_SAQUES} saques diários exceditos!')
                else:
                    if saldo_conta < valor_do_saque:
                        print('Saldo insuficiente!')
                    else:
                        saldo_conta -= valor_do_saque
                        frase_operacao = 'Saque:'  + f'R$ {valor_do_saque :.2f}'.rjust(34,' ')
                        extrato.append(frase_operacao)
                        numero_saques += 1
                        numero_operacoes_realizadas += 1
        except ValueError as e:
            print (e)
    elif opcao.lower() =="e":
        if numero_operacoes_realizadas == 0:
            print('Ainda não foram realizados movimentações na conta')
        else :
            print('='*15,'EXTRATO','='*17)
            for operacao in extrato:
                print(operacao,'\n')
            print('SALDO' ,f'R$ {saldo_conta:.2f}'.rjust(34,' '))
            print('='*40)
            
    elif opcao.lower =="q":
        break
    else:
        print("Opção inválida")
