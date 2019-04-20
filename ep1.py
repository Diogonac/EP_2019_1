# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Diogo Cintra, diogonac@al.insper.edu.br
# - aluno B: Alexandre Strutz, alexandrebs4@al.insper.edu.br

from random import randint


def sorteia_monstro():
    level = randint(0,5)
    if level > 3:
        print("HAHAHAHAHA")
        print("Por essa você não esperava")
        
        
    
    
def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao de entrada no prédio 1",
            "descricao": "Voce esta no saguao de entrada do insper ansioso para fazer o vestibular.Neste momento você esta indeciso para onde ir",
            "opcoes": {
                "elevador": "passar pela catraca e ir ao elevador A",
                "escada": "passar pela catraca e ir para a escada da casa do pão de queijo",
                "saida": "Você vai para fora do prédio respirar um pouco"
            }
        },
        "andar da sua sala": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala da sua prova",
            "opcoes": {
                "fugir": "Ixiiii... não estou bem vou dar o vazante",
                "sentar": "Achar sua sala e sua carteira com seu nome e sentar"
            }
        },
        "prova": {
            "titulo": "Até a morte tem medo",
            "descricao": "Voce senta em sua carteira e começa a pensar o que esta fazendo ali e reflete sobre a vida",
            "opcoes": {"vamo que vamo": "decide começar a prova",
                       "vish vou dar um migue": "vai para o banheiro e fica mexendo no celular"  
                    }
        },
        "aula desoft":{
                "titulo": "Inicio do EP1",
                "descricao": "Nosso deus vivo Raul começa a nos introduzir sobre o EP1.",
                },
        "Cenario1":{
                "titulo": "Fase 1: Testando suas abilidades de combate",
                "descricao": "Olá, bem vindo ao meu jogo. Nesta primeira fase vamos introduzir suas possiveis ações."
                },
        "Cenario2":{
                "titulo": "Fase 2: Conhecendo o inimigo",
                "descricao": "Nesse momento você se depara com um grupo de alunos da GV e outro da ESPM"
                }
        
    }
        
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

perguntas = {"pergunta1":"Você precisa soltar aquele barroso, mas gosta de extrema privacidade nessas horas. Em qual banheiro você vai?",
                 "opcoes1":{
                         "segundo andar",
                         "decimo primeiro andar"
                         },
                 "pergunta2": "Acabou aquela aula infinita de GDE e você está morrendo de fome. Qual o horario ideal para ir almoçar?",
                 "opcoes2":{"12:00",
                           "13:30"
                         },
                 "pergunta3": "Chegaram as semanas de provas, você fica na duivida café ou energetico. Como consegir café de graça?",
                 "opcoes3":{"puxar o saco de alguem do multi insper",
                           "marcar reunião com o marcos lisboa e tomar café na sala dele"
                           },
                 "pergunta4": "Você foi no momento insper a algum tempo e se perguntou: Quem é esse cara que fica indo de um lado pro outro?",
                 "opcoes4":{"presidente do insper",
                           "professor de engenharia"
                         },
                 "pergunta5":"Se você tivesse a opcao de ter comecado o ep1 semanas antes, começaria?",
                 "opcoes5":{"sim",
                           "não"
                         }
            }
                

         
def incremento_jogo():
    incremento = {"jogo1":{"1":"Poder da invisibilidade",
                  "2":"Empunhar sua espada e lutar",
                  "3":"Correr para sala das entidades buscar reforços",
                  "4":"Granada"
            }
                  }
    habilidade = "1"
    return incremento, habilidade

def incremento2_jogo():
    incremento2 = {"jogo2":{
            "1":"Ir guerriar com os grupos",
            "2":"Declarar paz"}
            }
    desicao = "1"
    return incremento2, desicao

def inventario():
    mochila={"a":"Espada da morte",
             "b":"Granada da aniquilação",
             "c":"Poder da invisibilidade"
            }
    item = "Espada da morte"
    return mochila, item
                 
def jogo():
    vida = 100
    cenarios, nome_cenario_atual = carregar_cenarios()
    cenario_atual = cenarios["Cenario1"]
    print(cenario_atual["titulo"])
    print('-'*len(cenario_atual["titulo"]))
    print(cenario_atual["descricao"])
    
    incremento, habilidade = incremento_jogo()
    
    for k,v in incremento["jogo1"].items():
        print(k,v)
        
    print("Sua vida atual é: {0}".format(vida))
    print()     
    cenario_atual = cenarios["Cenario2"]
    print(cenario_atual["titulo"])
    print('-'*len(cenario_atual["titulo"]))
    print(cenario_atual["descricao"])
    print("Seu inventario: ")
    mochila, item = inventario()
    for j,m in mochila.items():
        print(j,m)
    
    acao=input("Digite o numero da ação que deseja realizar: ")
    if acao == '1':
        print("Com o poder da invisibilidade você consegue ir no meio dos dois grupos e continua a estuda-los.")
        print("Não é permitido ativar o item 1")
        acao=input("Digite o numero da ação que deseja realizar: ")
        if acao == '2':
            print("Essa não, pessima escolha")
            game_over = True
        elif acao == '3':
            print("Você saiu correndo e sem querer deixou o poder da invisibilidade cair")
            print("Agora você não pode mais acessa-lo")
            print("Mas ok! Você chegou na sala das entidades")
            print()
            print("Você conseguiu mais quatro guerreiros")
            incremento2, desicao = incremento2_jogo()
            for f,c in incremento2["jogo2"].items:
                print(f,c)
            acao=input("Digite o numero da ação que deseja realizar: ")
            if acao == '1':
                print("Você e seu grupo causaram 350 de dano nos outrou grupos")
                
            elif acao == '2':
                print("Nossa, paz com esse pessoal da GV e ESPM? Um completo absurdo")
                print("Devido sua pessima escolha estou te banindo do meu ilustre jogo")
                game_over = True
            
        elif acao == '4':
            print("Ao jogar a granada você eliminou os grupos, mas...também perderu sua vida!")
            print("Você se sacrificou em nome de um bem maior")
            game_over == True
        
    elif acao == '2':
        print("Você decidiu empunhar sua espada e eliminar os grupos")
        print("Mas você estava em desvantagem numérica")
        print("Agora você tem {0}".format(vida-50))
        print("Você está muito fraco para lutar e correr, só restão as opções: 1 e 4")
        acao=input("Digite o numero da ação que deseja realizar: ")
        if acao == "4":
            print("Uau... você eliminou os grupos porém não conseguiu sobreviver")
            game_over = True
        elif acao == '1':
            print("Você está invisivel, poranto indetectável pelos grupos adversários")
            print("Você acaba de ganhar o elixir da vida")
            print("Agora você tem {0}".format(vida+25))
            print("Suas ações podem ser 2, 3 e 4")
            acao=input("Digite o numero da ação que deseja realizar: ")
            if acao == '2':
                print("Adimiro sua persistência, mas você não é forte o suficiente")
                game_over = True
            elif acao == '3':
                print("Você conseguiu mais quatro guerreiros")
                
            elif acao == '4':
                print("Respeito sua decisão, mas você não é importal!")
                game_over = True
                
                
        
    elif acao == '3':
        incremento2, desicao = incremento2_jogo()
        print("Excelente decisão, você conseguiu mais quatro guerreiros")
        for f,c in incremento2["jogo2"].items:
            print(f,c)
        acao=input("Digite o numero da ação que deseja realizar: ")
        if acao == '1':
            print("Boa guerreiro! Você e seu grupo causaram 100% de dano e eliminaram os inimigos!")
            
        elif acao == '2':
            print("Nossa, paz com esse pessoal da GV e ESPM? Um completo absurdo")
            print("Devido sua pessima escolha estou te banindo do meu ilustre jogo")
            game_over = True
            

        
        
    elif acao == '4':
        print("Você empunhou a granada e jogou no meio dos dois grupos")
        print("Conseguiu causar 100 de dados")
        print("Porém como você esta em desvantagem numerica, os grupos vão em sua direção")
        acao=input("Digite o numero da ação que deseja realizar: ")
        if acao == '1':
            print("Você ativou o poder da invisibilidade!")
            print("Por pouco você não é aniquilado")
            acao=input("Digite o numero da ação que deseja realizar: ")
        elif acao == '2':
            print("Brvo, bravo!!!")
            print("Você lutou como um espartano sedento por sangue")
            acao=input("Digite o numero da ação que deseja realizar: ")
        elif acao == '3':
            print("Neste momento os grupos estão atras de você")
            print("Quando você chega a sala  das entidades não encontra ninguém")
            acao=input("Digite o numero da ação que deseja realizar: ")
def primeiro_semestre():
    
    
    cenarios, nome_cenario_atual = carregar_cenarios()
    
    print("Neste momento você já comemorou sua aprovação e já começaram as aulas")
    print("Já começaram as aps, quizz, relatoris de instrumed e até já foram as PI's")
    print("Mas como nada é facil, os ep's também estão vindo com tudo")
    print()
    print("Agora você está na querida aula de de Design de Software")
    print()
    cenario_atual = cenarios["aula desoft"]
    print(cenario_atual["titulo"])
    print('-'*len(cenario_atual["titulo"]))
    print(cenario_atual["descricao"])
    print("Felizmente você já esta manjando de python e como EP1 decide fazer um joguinho simples, simples bem entre aspas")
    print()
    print("Já se passaram duas semanas e você finalizou o EP1")
    print()
    print("Neste momento chegou a vez do Raul ver esse tal joguinho")
    print("Usuário saia dai e deixe o Raul jogar!")
    print('-'*len("Usuário saia dai e deixe o Raul jogar!"))
    print()
    jogo()

def resolvendo_prova():
    acertos = 0
    erros = 0
    
    print()
    print("Está na hora de começar!")
    print()
    print("Pergunta 1")
    print(perguntas["pergunta1"])
    print('-'*len(perguntas["pergunta1"]))
    print()
    for e in perguntas['opcoes1']:
        print(e)
    print()
    escolha = input('Digite sua resposta: ')
    
    if escolha == 'decimo primeiro andar':
        acertos+=1
    else:
        erros=+1
    print()    
    print("Pergunta 2")
    print(perguntas["pergunta2"])
    print('-'*len(perguntas["pergunta2"]))
    print()
    for e in perguntas['opcoes2']:
        print(e)
    print()
    escolha = input('Digite sua resposta: ')
    
    if escolha == '12:00':
        acertos+=1
    else:
        erros=+1
    print()
    print("Pergunta 3")
    print(perguntas["pergunta3"])
    print('-'*len(perguntas["pergunta3"]))
    print()
    for e in perguntas['opcoes3']:
        print(e)
    print()
    escolha = input('Digite sua resposta: ')
    
    if escolha == 'puxar o saco de alguem do multi insper':
        acertos+=1
    else:
        erros=+1
    print()    
    print("Pergunta 4")
    print(perguntas["pergunta4"])
    print('-'*len(perguntas["pergunta4"]))
    print()
    for e in perguntas['opcoes4']:
        print(e)
    print()
    escolha = input('Digite sua resposta: ')
    
    if escolha == 'presidente do insper':
        acertos+=1
    else:
        erros=+1
    print()    
    print("Pergunta 5")
    print(perguntas["pergunta5"])
    print('-'*len(perguntas["pergunta5"]))
    print()
    for e in perguntas['opcoes5']:
        print(e)
    print()
    escolha = input('Digite sua resposta: ')
    if escolha == 'sim':
        acertos+=1
    else:
        erros=+1
    print()  
    
    if acertos>=3:
        print("Parabéns você foi aprovado na primeira fase do vertibular do Insper 2020.1")
        print("Sua potuação foi de: {0}".format(acertos))
        primeiro_semestre()
    else:
        print("Sua pontuação foi inferior a 3. Você foi REPROVADO!!!")
        game_over = True
    
def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    

    tempo = 0
    
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]


        print(cenario_atual["titulo"])
        print('-'*len(cenario_atual["titulo"]))
        print(cenario_atual["descricao"])
        
        opcoes = cenario_atual['opcoes']
        
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            print()
            for k,v in cenario_atual['opcoes'].items():
                print('{0}: {1}'.format(k,v))
            print()

            escolha = input('O que você quer fazer?')
#Opção saida
            if escolha == 'saida':
                print("Escolha errada meu caro, tenha mais coragem!")
                game_over = True
#Opção elevador                
            if escolha == 'elevador':
                print("Aguarde o elevador chegar")
                while tempo<1e8:
                    tempo+=1
                print("Plinn plinn... Porta abrindo")
                print("Neste momento você entrou no elevador e  chegou no seu andar")
                
                cenario_atual = cenarios["andar da sua sala"]
                print(cenario_atual["titulo"])
                print('-'*len(cenario_atual["titulo"]))
                print(cenario_atual["descricao"])
                
                print()
                for a,b in cenario_atual['opcoes'].items():
                    print('{0}: {1}'.format(a,b))
                    print()
            
                escolha = input("O que você quer fazer?")
                if escolha == 'fugir':
                    game_over = True
                    print("Seja mais forte da próxima vez")
                    
                if escolha == 'sentar':          
                    cenario_atual = cenarios["prova"]
                    print(cenario_atual["titulo"])
                    print('-'*len(cenario_atual["titulo"]))
                    print(cenario_atual["descricao"])
                    print()
                    for c,d in cenario_atual['opcoes'].items():
                        print('{0}: {1}'.format(c,d))
                        print()  
                    escolha = input("O que você quer fazer?")
                    
                    if escolha == 'vamo que vamo':
                        resolvendo_prova()
                    if escolha == 'vish vou dar um migue':
                        game_over = True
                        
#Opção escada
            if escolha == 'escada':
                print("Neste momento você está subindo a escada")
                print("Aguarde...")
                while tempo<1e7:
                    tempo+=1
                cenario_atual = cenarios["andar da sua sala"]
                print(cenario_atual["titulo"])
                print('-'*len(cenario_atual["titulo"]))
                print(cenario_atual["descricao"])
                
                print()
                for a,b in cenario_atual['opcoes'].items():
                    print('{0}: {1}'.format(a,b))
                    print()
            
                escolha = input("O que você quer fazer?")
                if escolha == 'fugir':
                    game_over = True
                    print("Seja mais forte da próxima vez")
                    
                if escolha == 'sentar':          
                    cenario_atual = cenarios["prova"]
                    print(cenario_atual["titulo"])
                    print('-'*len(cenario_atual["titulo"]))
                    print(cenario_atual["descricao"])
                    print()
                    for c,d in cenario_atual['opcoes'].items():
                        print('{0}: {1}'.format(c,d))
                        print()  
                    escolha = input("O que você quer fazer?")
                    
                    if escolha == 'vamo que vamo':
                        resolvendo_prova()
                    if escolha == 'vish vou dar um migue':
                        game_over = True


            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Game Over!")


# Programa principal.
if __name__ == "__main__":
    main()
