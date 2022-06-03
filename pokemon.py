lizard = ['lizard', 10, 2]
squirtle = ['squirtle', 6, 1]


def jogo():

    print("Bem vindo ao jogo de pokemon battle!\n")

    pokemon = input ("qual será sua escolha, \n lizard = l \n squirtle = s \n")

    def escolher(pokemon):
        if pokemon == 's' :
            pokemonEscolha = squirtle
            print("sua escolha foi :", pokemonEscolha[0] ,"\n")
            print ("seu pokemon possui", pokemonEscolha[1],"hp," , pokemonEscolha[2], "pontos de poder" "\n")
            
        elif pokemon == 'l' :
            pokemonEscolha = lizard
            print("sua escolha foi :", pokemonEscolha[0], "\n" )
            print ("seu pokemon possui", pokemonEscolha[1],"hp," , pokemonEscolha[2], "pontos de poder" "\n")

        else : 
            print("errou" "\n")
            jogo()

        return pokemonEscolha

    uai = escolher(pokemon)

    def contra(uai):
        if uai == lizard:
            contra = squirtle

        if uai == squirtle:
            contra = lizard
        return contra

    contra = contra(uai)

    print("contra", contra[0], ", hp", contra[1], ", pontos de poder", contra[2], "\n")

    def battle(uai, contra):

        
        atk = input("deseja utilizar qual ataque: \n info s/ s = stun \n info a/ a = atk \n")

        if atk == 'info s':
            print("stun : causa stun por 2 rounds" "\n")
        
        if atk == 'info a':
            print("atk : causa dano igual ao seus pontos de poder" "\n")

        if atk == 'a':
            contra[1] = contra[1] - uai[2]
            print("vida : ", contra[1], "de ", contra[0], "\n")

        if atk == 's':
            stun = [4]
            if stun[0] > 0:
                stun[0] = stun[0] - 1
                print("pokemon stunado : ", contra[0] , "\n")
        elif atk != 's':
            stun = [0]
            

        vida = [contra[1], uai[1], stun[0]]
        return vida
            
    def atkC(contra, stun):
            if stun <=0:
                uai[1] = uai[1] - contra[2]
                print("vida : ", uai[1], "de ", uai[0], "\n")



    while True:
        vida = battle(uai, contra)
        if 0 >= vida[1]:
            print("perdeu")
            break

        elif 0 >= vida[0]:
            print("ganhou")
            break

        elif 0  == vida [2]:
            stun = vida[2]
            atkC(contra, stun)

        else :
            battle(uai, contra)

jogo()

restar = input("Deseja jogar novamente? s ou n \n")

if restar == 's':
    jogo()


