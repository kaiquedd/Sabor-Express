import os

restaurantes = [{'nome':'Mamamia' , 'categoria':'Pizza', 'ativo':True} , 
                {'nome':'lunchLife' , 'categoria':'Italiana', 'ativo':False} , 
                {'nome':'HojeTem' , 'categoria':'Self-Service' , 'ativo':False}]
                

def exibir_programa():
    print(' Sabor Express\n')

def exibir_opçoes():
    print('1- Cadastrar Restaurantes')
    print('2- Listar Restaurantes')
    print('3- Ativar Restaurantes')
    print('4- Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app...'); 

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal:')
    main()

def opcao_invalida():
    print('Opçao Invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(text): 
    os.system('cls')
    print(text)
    print()    

def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite um nome de restaurante que deseja incluir:')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante) 
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurante():
    exibir_subtitulo('Listando restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}') 
    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    exibir_subtitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
        
    voltar_ao_menu_principal()


def escolher_opçao():
        try:
            opçao_escolhida = int(input('Escolha uma opçao: '))

            if opçao_escolhida == 1:
                cadastrar_restaurante()
            elif opçao_escolhida == 2:
                listar_restaurante()
            elif opçao_escolhida == 3:
                alternar_estado_restaurante()
                voltar_ao_menu_principal()
            elif opçao_escolhida == 4:
                finalizar_app()
        except:
            opcao_invalida()
    

def main():
    os.system('cls') 
    exibir_programa()
    exibir_opçoes()
    escolher_opçao()

if __name__ == '__main__': 
    main()
 