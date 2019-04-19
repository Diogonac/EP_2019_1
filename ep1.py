# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Diogo Cintra, diogonac@al.insper.edu.br
# - aluno B: Alexandre Strutz, alexandrebs4@al.insper.edu.br

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
                 "opcoes3":{"puxar o saco de alguém do multi insper",
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
                
def resolvendo_prova():
    acertos = 0
    erros = 0
    
    print()
    print("Está na hora de começar!")
    
    print("Pergunta 1")
    print(perguntas["pergunta1"])
    print('-'*len(perguntas["pergunta1"]))
    print()
    for e in perguntas['opcoes1']:
        print(e)
    print()
    escolha = input('O que você quer fazer?')
    
    if escolha == 'decimo primeiro andar':
        acertos+=1
    else:
        erros=+1


        

    
    
                
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
                        #resolvendo_prova()
                        print("chama a função")
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
