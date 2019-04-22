# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Diogo Cintra, diogonac@al.insper.edu.br
# - aluno B: Alexandre Strutz, alexandrebs4@al.insper.edu.br

from random import randint

tempo = 10


raul = {"1": "O El Raul é obrigado a fazer o EP1!",
        "2": "Abaixar a guarda e econtrar deus mais cedo",
        }

def luta_raul():
    print("Agora você está diante do ser mais temido de todo universo! O El Raul")
    for d,x in raul.items():
        print(d,x)
    e = input("Digite o numero correspondente a sua escolha: ")
    if e == '1':
        print("Boa escolha")
        print("Como o Raul está sozinho, se torna impossivel fazer o ep1")
        print("E então ele fica muito distraido e você consegue elimina-lo")
        
    else:
        print("Desistir foi uma péssima escolha!")
        game_over = True
    
        
    
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
                "teleporte":{
                        "titulo": "Esta é a sua chance de ser Raposa o quanto antes",
                        "descrição": "Se acertar a resposta da pergunta X, poderá ingressar ao curso do insper de maneira mais rapida sem ter que passar por todas as fases",
                        "opcoes":{"opçao A",
                                  "opcao B",
                                  "opcao C",
                                  "opcao D"
                                  }
                        },
                                  
        "Cenario1":{
                "titulo": "Fase 1: Testando suas abilidades de combate",
                "descricao": "Olá, bem vindo ao meu jogo. Nesta primeira fase vamos introduzir suas possiveis ações."
                },
        "Cenario2":{
                "titulo": "Fase 2: Conhecendo e lutando com o inimigo",
                "descricao": "Nesse momento você se depara com um grupo de alunos da GV e outro da ESPM"
                },
        "Cenario3":{
                "titulo": "Fase 3: Mostrando conhecimento",
                "descricao": "Agora é a sua hora, você vai mostrar se esta preparado para se tornar um INSPERINO, vamos la: O que significa Private Equity?"
                },
        
    }
        
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual
 
    
perguntas = {"pergunta1":"Você precisa soltar aquele barro, mas gosta de extrema privacidade nessas horas. Em qual banheiro você vai?",
                 "opcoes1":{
                         "segundo andar",
                         "quinto andar",
                         "decimo primeiro andar"
                         },
                 "pergunta2": "Acabou aquela aula infinita de GDE e você está morrendo de fome. Qual o horario ideal para ir almoçar?",
                 "opcoes2":{"11:45",
                           "13:30"
                         },
                 "pergunta3": "Chegaram as semanas de provas, você fica na duivida café ou energetico. Como consegir café de graça?",
                 "opcoes3":{"puxar o saco de alguem do multi insper",
                           "marcar reunião com o marcos lisboa e tomar café na sala dele",
                           "comprar a capsula e tomar na sala das entidades"
                           },
                 "pergunta4": "Você foi no momento insper a algum tempo e se perguntou: Quem é esse cara que fica indo de um lado pro outro?",
                 "opcoes4":{"presidente do insper",
                           "professor de engenharia"
                         },
                 "pergunta5":"Se você tivesse a opcao de ter comecado o ep1 semanas antes, começaria?",
                 "opcoes5":{"sim",
                           "não"
                         },
                 "pergunta6": "Tem piscina em qual andar no insper?",
                 "opcoes6":{"quinto andar",
                            "rooftop predio novo",
                            "nao tem piscina no insper"
                         },
                 "pergunta7": "Qual o melhor time da atletica do insper?",
                 "opcoes7":{"futebol de campo",
                            "handebol masculino",
                            "handebol feminino"
                         },
                 "pergunta8": "O Insper antigamente tinha qual nome?",
                 "opcoes8":{"IBMEC",
                            "Puc SP",
                            "Fundacao Escola de Comercio Alvares Penteado"
                         },
                 "pergunta9": "Qual universidade tem parceria com o Insper?",
                 "opcoes9":{"Universidade de British Columbia",
                            "Harvard",
                            "UCLA"
                         },
                 "pergunta10": "Existe sala de dormir, sala de netflix ou sala para jogar play station no insper?",
                 "opcoes10":{"sala de dormir",
                             "sala de netflix",
                             "sala para play station",
                         },
                            
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
    decisao = "1"
    return incremento2, decisao

def inventario():
    mochila={"a":"Espada da morte",
             "b":"Granada da aniquilação",
             "c":"Poder da invisibilidade"
            }
    item = "a"
    return mochila, item
    

def teleporte_ultima_sala():
    entrar_insper = {"1":"PE é uma modalidade de investimento em que um fundo levanta capital para adquirir participação em empresas já desenvolvidas e obter lucro a médio ou longo prazo com a venda",
                     "2": "PE são transações nas quais a propriedade de empresas, outras organizações empresariais ou suas unidades operacionais são transferidas ou consolidadas com outras entidades",
                     "3": "PE é qualquer tipo de investimento que possui regras de remuneração definidas no momento da aplicação no título",
                     }
    resposta = "1"
    return entrar_insper, resposta
              
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
    
    print("Sua vida atual é: {0}".format(vida))
    print()     
    entrar_insper, resposta = teleporte_ultima_sala()

        
    acao=input("Digite o numero da ação que deseja realizar: ")
    if acao == '1':
        print("Com o poder da invisibilidade você consegue ir no meio dos dois grupos e continua a estuda-los.")
        print("Não é permitido ativar o item 1 novamente")
        acao=input("Digite o numero da ação que deseja realizar: ")
        if acao == '2':
            print("Essa não, pessima escolha, você está fora.")
            game_over = True
        elif acao == '3':
            print("Você saiu correndo e sem querer deixou o poder da invisibilidade cair")
            print("Agora você não pode mais acessa-lo")
            print("Mas ok! Você chegou na sala das entidades")
            print()
            print("Você conseguiu mais quatro guerreiros para ajuda-lo nesta luta")
            
            incremento2, decisao = incremento2_jogo()
            for f,c in incremento2["jogo2"].items():
                print(f,c)
            acao=input("Digite o numero da ação que deseja realizar: ")
            
            if acao == '1':
                print("Você e seu grupo causaram 350 de dano nos outrou grupos")
                cenario_atual = cenarios["Cenario3"]
                print(cenario_atual["titulo"])
                print('-'*len(cenario_atual["titulo"]))
                print(cenario_atual["descricao"])
                for n,o in entrar_insper.items():
                    print(n,o)
                acao=input("Digite o numero da ação que deseja realizar: ")
                if acao == '1':
                    level = randint(0,5)
                    if level>3:
                        print("Parabéns, você ganhou o jogo")
                    else:
                        print("HAHAHAHAHA")
                        print("Por essa você não esperava... Vai ter que lutar com o chefão, o grande El Raul")
                        luta_raul()
                else:
                    print("Não foi desta vez!")
                    game_over = True
                    
            elif acao == '2':
                print("Nossa, paz com esse pessoal da GV e ESPM? Um completo absurdo, não esperamos uma atitude dessa de um aluno nosso")
                print("Devido sua pessima escolha estou te banindo do meu ilustre jogo")
                game_over = True
            
        elif acao == '4':
            print("Ao jogar a granada você eliminou os grupos, mas...também perdeu sua vida! Diga adeus para este jogo.")
            print("Você se sacrificou em nome de um bem maior")
            game_over == True
        
    elif acao == '2':
        print("Você decidiu empunhar sua espada e eliminar os grupos")
        print("Mas você estava em desvantagem numérica")
        print("Agora você tem {0}".format(vida-50))
        print("Você está muito fraco para lutar e correr, só restão as opções: 1 e 4")
        acao=input("Digite o numero da ação que deseja realizar: (1 ou 4) ")
        if acao == "4":
            print("Uau... você eliminou os grupos porém não conseguiu sobreviver, se machucou muito, fim de jogo para você.")
            game_over = True
        elif acao == '1':
            print("Você está invisivel, portanto indetectável pelos grupos adversários")
            print("Você acaba de ganhar o elixir da vida")
            print("Agora você tem {0}".format(vida+25))
            print("Suas ações podem ser 2, 3 e 4")
            acao=input("Digite o numero da ação que deseja realizar: (2,3 ou 4) ")
            if acao == '2':
                print("Adimiro sua persistência, mas você não é forte o suficiente, tchau.")
                game_over = True
            elif acao == '3':
                print("Você conseguiu mais quatro loucos pela raposa para te ajudar.")
                print("Você e seu grupo lutam bravamente com o inimigo e consegue extermina-los")
                cenario_atual = cenarios["Cenario3"]
                print(cenario_atual["titulo"])
                print('-'*len(cenario_atual["titulo"]))
                print(cenario_atual["descricao"])
                for n,o in entrar_insper.items():
                    print(n,o)
                acao=input("Digite o numero da ação que deseja realizar: ")
                if acao == '1':
                    level = randint(0,5)
                    if level<3:
                        print("Parabéns, você ganhou o jogo")
                    else:
                        print("HAHAHAHAHA")
                        print("Por essa você não esperava... Vai ter que lutar com o chefão, o grande El Raul")
                        luta_raul()
                else:
                    print("Não foi desta vez!")
                    game_over = True
            elif acao == '4':
                print("Respeito sua decisão, mas você não é imortal!")
                game_over = True
                
                
        
    elif acao == '3':
        incremento2, decisao = incremento2_jogo()
        print("Excelente decisão, você conseguiu mais quatro guerreiros")
        for f,c in incremento2["jogo2"].items:
            print(f,c)
        acao=input("Digite o numero da ação que deseja realizar: ")
        if acao == '1':
            print("Boa guerreiro! Você e seu grupo causaram 100% de dano e eliminaram os inimigos!")
            cenario_atual = cenarios["Cenario3"]
            print(cenario_atual["titulo"])
            print('-'*len(cenario_atual["titulo"]))
            print(cenario_atual["descricao"])
            for n,o in entrar_insper.items():
                print(n,o)
            acao=input("Digite o numero da ação que deseja realizar: ")
            if acao == '1':
                level = randint(0,5)
                if level<3:
                    print("Parabéns, você ganhou o jogo")
                else:
                    print("HAHAHAHAHA")
                    print("Por essa você não esperava... Vai ter que lutar com o chefão, o grande El Raul")
                    luta_raul()
            else:
                print("Não foi desta vez!")
                game_over = True
            
        elif acao == '2':
            print("Nossa, paz com esse pessoal da GV e ESPM? Um completo absurdo")
            print("Devido sua pessima escolha estou te banindo do meu ilustre jogo pra sempre, você nao merece estar aqui")
            game_over = True
            

        
        
    elif acao == '4':
        print("Você empunhou a granada e jogou no meio dos dois grupos")
        print("Conseguiu causar 100% de dano e assim elimina os grupos")
        cenario_atual = cenarios["Cenario3"]
        print(cenario_atual["titulo"])
        print('-'*len(cenario_atual["titulo"]))
        print(cenario_atual["descricao"])
        for n,o in entrar_insper.items():
            print(n,o)
            acao=input("Digite o numero da ação que deseja realizar: ")
            if acao == '1':
                level = randint(0,5)
                if level<3:
                    print("Parabéns, você ganhou o jogo")
                else:
                    print("HAHAHAHAHA")
                    print("Por essa você não esperava... Vai ter que lutar com o chefão, o grande El Raul")
                    luta_raul()
            else:
                print("Não foi desta vez!")
                game_over = True




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
    print("Pergunta 6")
    print(perguntas["pergunta6"])
    print('-'*len(perguntas["pergunta6"]))
    print()
    for e in perguntas['opcoes6']:
        print(e)
    print()
    escolha = input('Digite sua resposta: ')
    if escolha == 'nao tem piscina no insper':
        acertos += 1
    else:
        erros+=1

    
    print()    
    print("Pergunta 7")
    print(perguntas["pergunta7"])
    print('-'*len(perguntas["pergunta7"]))
    print()
    for e in perguntas['opcoes7']:
        print(e)
    print()
    escolha = input('Digite sua resposta: ')
    if escolha == 'futebol de campo':
        acertos+=1
    else:
        erros+=1
    
    
    print()    
    print("Pergunta8")
    print(perguntas["pergunta8"])
    print('-'*len(perguntas["pergunta8"]))
    print()
    for e in perguntas['opcoes8']:
        print(e)
    print()
    escolha = input('Digite sua resposta: ')
    if escolha == 'IBMEC':
        acertos +=1
    else:
        erros+=1
    
    
    print()    
    print("Pergunta 9")
    print(perguntas["pergunta9"])
    print('-'*len(perguntas["pergunta9"]))
    print()
    for e in perguntas['opcoes9']:
        print(e)
    print()
    escolha = input('Digite sua resposta: ')
    if escolha == 'universidade de British Columbia':
        acertos+=1
    else:
        erros +=1
    
    
    print()    
    print("Pergunta 10")
    print(perguntas["pergunta10"])
    print('-'*len(perguntas["pergunta10"]))
    print()
    for e in perguntas['opcoes10']:
        print(e)
    print()
    escolha = input('Digite sua resposta: ')
    if escolha == 'sala para dormir':
        acertos+=1
    else:
        erros+=1
    print()
    if acertos>=5:
        print("Parabéns você foi aprovado na primeira fase do vertibular do Insper 2020.1")
        print("Sua potuação foi de: {0}".format(acertos))
        primeiro_semestre()
    elif acertos<5:
        print("Sua nota não foi das melhoras, porem a faculdade acredita no seu potencial, você tem uma ultima chance para entrar no Insper.")
        print("Suas opções são:")
        print("Instituto de pesquisa")
        print("Inspirar e Pertencer")
        Y=input("O que significa INSPER?")
                
        if Y == 'Inspirar e Pertencer':
            print("Você passou de fase como esperavamos, agora você vai para a sala do Marcos Lisboa ter uma conversa para ele definir seu potencial")
            conversa_com_Marquinhos()
        else:
            print("Sua pontuação foi inferior a 5. Você foi REPROVADO, vai pra GV!!!")    
            game_over = True
            
                   
        
def conversa_com_Marquinhos():
    
    print("Você tem uma oportunidade de ouro, conversar com um dos economistas mais famosos do pais")
    Z = input("Ele tem uma pergunta para você, quer uma resposta de sim ou não sobre o salario minimo, você acha que ele deve levar em conta o ajuste real todo ano?")
    if Z == 'sim':
        print("Você ganhou o direito de ingressar na faculdade em 2020.1")
        primeiro_semestre()
    else:
        print("Você não merece ser raposa, você esta eliminado do processo seletivo, tente proximo semestre")
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
                        if resolvendo_prova() == 5:
                            conversa_com_Marquinhos()
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
