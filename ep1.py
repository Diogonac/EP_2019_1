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
                "Saida": "Você vai para fora do prédio respirar um pouco"
            }
        },
        "andar da sua sala": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala da sua prova",
            "opcoes": {
                "inicio": "Desistir do vestibular e ir embora",
                "sentar": "Achar a carteira com seu nome e sentar"
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

def carregar_perguntas():
    perguntas = {"pergunta1":"Você precisa soltar aquele barroso, mas gosta de extrema privacidade nessas horas. Em qual banheiro você vai?",
                 "opcoes":{
                         "segundo andar",
                         "decimo primeiro andar"
                         },
                 "pergunta2": "Acabou aquela aula infinita de GDE e você está morrendo de fome. Qual o horario ideal para ir almoçar?",
                 "opcoes":{"12:00",
                           "13:30"
                         }
            
            
            
            
            
            
            
            
            
            
            
            }
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

            escolha = input('O que voce quer fazer?')


            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
