escolha = int(input('Informe um numero'))
    
        if escolha % 2 == 0:  
            print('Par')
        else:
            print('Impar')


    idade = int(input('Digite sua idade'))
        
        if idade > 0 and idade <= 12: 
            print('CRIANÇA')
        elif idade > 12 and idade < 18: 
            print('ADOLESCENTE')
        else: 
            print('ADULTO')



lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in lista_de_numeros: 
    print(numero)

soma_impares = 0 
    
    for i in range(1,11,2)
        soma_impares += i
    print(soma_impares)

numero_tabuada = int(input('Digite um numero para a tabuada'))
    for i in range(1,11)
    resultado = numero_tabuada * i
    print(f'{numero_tabuada} x {i} = {resultado}')




maças_vendidas = input('Informe a quantidade de maças vendidas: ')
bananas_vendidas = input('Informe a quantidade de bananas vendidas: ')

    if maças_vendidas > bananas_vendidas: 
        print('Vendemos mais maças.')
    elif maças_vendidas < bananas_vendidas: 
        print('Vendemos mais bananas.')
    else: 
        print('Empate de vendas.')

def total_de_dias():
    dias_para_atividadeA + dias_para_atividadeB + dias_para_atividadeC


dias_para_atividadeA = input('Informe quantos dias para a atividade A: ')
dias_para_atividadeB = input('Informe quantos dias para a atividade B: ')
dias_para_atividadeC = input('Informe quantos dias para a atividade C: ')

    if dias_para_atividadeA or dias_para_atividadeB or dias_para_atividadeC < 0: 
        print('Nao é tolerado numero negativo')
    else: 
        total_de_dias()


def contar_caracteres(palavra):
    return len(palavra)

texto = input('Informe uma palavra desejada: ')
    print(f'A palavra tem {contar_caracteres(texto)} caracteres. ')