import time, os
os.system("cls")

print('''
      Você é um explorador corajoso em busca de tesouros lendários na
misteriosa Ilha Maluca. Rumores dizem que um grande tesouro está
escondido em algum lugar na ilha, mas para encontrá-lo, você
precisa decifrar uma série de enigmas. Ao chegar na ilha, você se depara com uma placa estranha com
inscrições antigas. As inscrições dizem o seguinte:
''')
time.sleep(5)
os.system("cls")
print('''
"Para desbloquear o tesouro escondido, você deve provar sua destreza. Resolva os
desafios a seguir e siga as instruções para encontrar o caminho certo."
''')
time.sleep(5)
os.system("cls")
os.system("color 3")

print('''
      Desafio 1: O Guardião da Porta

     Você se depara com uma porta enorme guardada por um gigante adormecido. Para passar
pela porta e continuar sua jornada, você precisa responder a seguinte questão:
      
"Quantos cocos o macaco tem se eu pegar metade dos cocos que ele tem, mais dois cocos,
e depois subtrair três cocos?"
''')

cocos = int(input("Quantos cocos o macaco tem?: "))
resposta1 = float(input("Com quantos cocos ele ficou?: "))
conta1 = cocos/2 + 2 - 3 
if conta1 == resposta1:
    print("Resposta correta, pode seguir em frente!")
else:
    print("Resposta incorreta, tente novamente.")
    quit()

os.system("color 5")
print('''
      Desafio 2: O Labirinto dos Crocodilos
Após passar pela porta, você entra em um labirinto infestado de 
crocodilos famintos. Para escapar deles, você precisa resolver o seguinte 
problema:
      
"Se eu tenho uma corda de 12 metros e preciso atravessar um rio de 7 metros de largura, 
quantos metros de corda a mais eu tenho para amarrar nas árvores e atravessar com 
segurança?"
      ''')

corda = int(input("Quantos metros de corda a mais você tem?: "))
conta2 = 12 - 7
if corda == conta2:
    print("Resposta correta, siga em frente!")
else:
    print("Resposta incorreta, tente novamente.")
    quit()

os.system("color 4")
print('''
    Desafio 3: O Enigma Final
Finalmente, você chega à câmara do tesouro, mas para abri-la, você precisa resolver um 
enigma final:
      
"Se o número de tesouros enterrados na ilha é igual ao dobro do número de palmeiras, 
e o número de palmeiras é igual a três vezes o número de periquitos na ilha, e o número 
total de periquitos é 42, quantos tesouros tem na ilha?"
''')

periquitos = int(input("Qual é o total de periquitos?: "))
palmeiras = periquitos * 3
tesouros = palmeiras * 2
tesourosjogador = int(input("Quantos tesouros tem na ilha?: "))
if tesourosjogador == tesouros:
    print("Parabéns você encontrou o tesouro!!")
else:
    print("Game Over! Você não passou pelo guardião da porta.")
    quit()