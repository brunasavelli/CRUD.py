'''
FEITO -- Implementar a opção 2 (procurar contato) da seguinte forma:
Ficar pedindo para digitar um nome até digitar um nome que existe;
mostrar então na tela TODOS os demais dados daquela pessoa, cujo
nome foi digitado.

Implementar a opção 3 (atualizar contato) da seguinte forma:
Ficar mostrando um menu oferecendo as opções de atualizar aniversário, ou
endereco, ou telefone, ou celular, ou email, ou finalizar as
atualizações; ficar pedindo para digitar a opção até digitar uma
opção válida; realizar a atulização solicitada; até ser escolhida a
opção de finalizar as atualizações.

FEITO -- Implementar a opção 4 (listar contato) da seguinte forma:
Mostrar na tela os TODOS os dados de CADA um dos contatos presentes
na lista chamada agenda (eventualmente chamada de agd).

Implemenar nas novas opções, BEM COMO nas já implementadas, todas as
validações cabíveis.

Entregar em aula prática ou dia 25 ou dia 26 ou dia 27, conforme seja
seu dia de aula, na forma de demonstração para o professor.
'''
def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Bruna Nascimento Savelli e Rafaela Lorena da Luz Antunes    |')
    print('|                                                             |')
    print('| Versão 1.0 de 25/05/2026                                 |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

def umTexto (solicitacao, mensagem, valido):
    digitouDireito=False
    while not digitouDireito:
        txt=input(solicitacao)

        if txt not in valido:
            print(mensagem,'- Favor redigitar...')
        else:
            digitouDireito=True

    return txt

def opcaoEscolhida (mnu):
    print ()

    opcoesValidas=[]
    posicao=0
    while posicao<len(mnu):
        print (posicao+1,') ',mnu[posicao],sep='')
        opcoesValidas.append(str(posicao+1))
        posicao+=1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)

'''
procura nom em agd e, se achou, retorna:
uma lista contendo True e a posicao onde achou;
MAS, se não achou, retorna:
uma lista contendo False e a posição onde inserir,
aquilo que foi buscado, mas nao foi encontrado,
mantendo a ordenação da lista.
'''
def ondeEsta (nom,agd):
    inicio=0
    final =len(agd)-1
    
    while inicio<=final:
        meio=(inicio+final)//2
        
        if nom.upper()==agd[meio][0].upper():
            return [True,meio]
        elif nom.upper()<agd[meio][0].upper():
            final=meio-1
        else: # nom.upper()>agd[meio][0].upper()
            inicio=meio+1
            
    return [False,inicio]

def cadastrar (agd):
    chave_para_digitar_ate_acertar_ligada=True
    while chave_para_digitar_ate_acertar_ligada:
        nome=input('\nNome.......: ')

        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]

        if achou:
            print ('Pessoa já cadastrada; tente novamente!')
        else:
            chave_para_digitar_ate_acertar_ligada=False
            
    aniversario=input('Aniversário: ')
    endereco   =input('Endereço...: ')
    telefone   =input('Telefone...: ')
    celular    =input('Celular....: ')
    email      =input('e-mail.....: ')
    
    contato=[nome,aniversario,endereco,telefone,celular,email]
    
    agd.insert(posicao,contato)
    print('Cadastro realizado com sucesso!')

def procurar (agd):
    chave_para_digitar_ate_acertar_ligada = True
    while chave_para_digitar_ate_acertar_ligada:
        nome = input("\nProcure um contato pelo nome: ")

        resposta = ondeEsta(nome,agd)
        achou = resposta[0]
        posicao = resposta[1]

        if not achou:
            print('Esse contato não está na sua lista. Tente novamente!')
        else:
            chave_para_digitar_ate_acertar_ligada=False
            print('Contato encontrado com sucesso!')
            print('-----------------------------')
            print('Nome.......: ',agd[posicao][0])
            print('Aniversário: ',agd[posicao][1])
            print('Endereço...: ',agd[posicao][2])
            print('Telefone...: ',agd[posicao][3])
            print('Celular....: ',agd[posicao][4])
            print('e-mail.....: ',agd[posicao][5])
            print('-----------------------------')

def atualizar (agd): 
    if len(agd) == 0:
        print('Agenda vazia!')
    else:
        nome = input('\nDigite o nome do contato que deseja atualizar: ')

        resposta = ondeEsta(nome, agd)
        achou = resposta[0]
        posicao = resposta[1]

        if not achou:
            print('Esse contato não está na sua lista!')
        else:
            submenu = [
                'Atualizar aniversário',
                'Atualizar endereço',
                'Atualizar telefone',
                'Atualizar celular',
                'Atualizar e-mail',
                'Finalizar atualizações'
            ]

            finalizar = False

            while not finalizar:
                opcao = int(opcaoEscolhida(submenu))

                if opcao == 1:
                    agd[posicao][1] = input('Novo aniversário: ')
                    print('Aniversário atualizado com sucesso!')

                elif opcao == 2:
                    agd[posicao][2] = input('Novo endereço: ')
                    print('Endereço atualizado com sucesso!')

                elif opcao == 3:
                    agd[posicao][3] = input('Novo telefone: ')
                    print('Telefone atualizado com sucesso!')

                elif opcao == 4:
                    agd[posicao][4] = input('Novo celular: ')
                    print('Celular atualizado com sucesso!')

                elif opcao == 5:
                    agd[posicao][5] = input('Novo e-mail: ')
                    print('E-mail atualizado com sucesso!')

                else:
                    finalizar = True
                    print('Atualizações finalizadas!')

def listar (agd):
    if len(agd)==0:
        print("Agenda vazia!")
    else:
        posicao=0
        while posicao<len(agd):
            print('-----------------------------')
            print('Nome.......: ',agd[posicao][0])
            print('Aniversário: ',agd[posicao][1])
            print('Endereço...: ',agd[posicao][2])
            print('Telefone...: ',agd[posicao][3])
            print('Celular....: ',agd[posicao][4])
            print('e-mail.....: ',agd[posicao][5])
            posicao+=1
        print('-----------------------------')

def excluir (agd): 
    if len(agd) == 0:
        print('Agenda vazia!')
    else:
        nome = input('\nDigite o nome do contato que deseja excluir: ')

        resposta = ondeEsta(nome, agd)
        achou = resposta[0]
        posicao = resposta[1]

        if not achou:
            print('Esse contato não está cadastrado!')
        else:
            confirmacao = umTexto(
                'Confirma a exclusão? Digite S para sim ou N para não: ',
                'Confirmação inválida',
                ['S', 'N', 's', 'n']
            )

            if confirmacao.upper() == 'S':
                agd.pop(posicao)
                print('Exclusão realizada com sucesso!')
            else:
                print('Exclusão não realizada!')

apresenteSe()

agenda=[]

menu=['Cadastrar Contato',\
        'Procurar Contato',\
        'Atualizar Contato',\
        'Listar Contatos',\
        'Excluir Contato',\
        'Sair do Programa']

chave_para_executar_opcoes_ate_escolher_sair_ligada=True
while chave_para_executar_opcoes_ate_escolher_sair_ligada:
    opcao = int(opcaoEscolhida(menu))

    if opcao==1:
        cadastrar(agenda)
    elif opcao==2:
        procurar(agenda)
    elif opcao==3:
        atualizar(agenda)
    elif opcao==4:
        listar(agenda)
    elif opcao==5:
        excluir(agenda)
    else: # opcao==6
        chave_para_executar_opcoes_ate_escolher_sair_ligada=False
        
print('PROGRAMA ENCERRADO COM SUCESSO!')